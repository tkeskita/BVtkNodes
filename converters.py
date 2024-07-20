from .core import l  # Import logging
from .core import *
from .cache import BVTKCache
import bmesh
from vtk.util import numpy_support

try:
    import pyopenvdb

    with_pyopenvdb = True
except ImportError:
    l.warning("pyopenvdb was not found (this is normal)")
    with_pyopenvdb = False

# -----------------------------------------------------------------------------
# Converters from VTK to Blender
# -----------------------------------------------------------------------------
# Mesh Converters
# -----------------------------------------------------------------------------


class BVTK_Node_VTKToBlender(Node, BVTK_Node):
    """Legacy node for converting output from VTK Node to Blender Mesh Object.
    Note: Not upgraded to new core.py. Superceded by VTK To Blender Mesh Node.
    """

    bl_idname = "BVTK_Node_VTKToBlenderType"  # type name
    bl_label = "VTK To Blender"  # label for nice name display

    m_Name: bpy.props.StringProperty(name="Name", default="mesh")
    smooth: bpy.props.BoolProperty(name="Smooth", default=False)
    generate_material: bpy.props.BoolProperty(name="Generate Material", default=False)

    def start_scan(self, context):
        if context:
            if self.auto_update:
                bpy.ops.node.bvtk_auto_update_scan(
                    node_name=self.name, tree_name=context.space_data.node_tree.name
                )

    auto_update: bpy.props.BoolProperty(default=False, update=start_scan)

    def m_properties(self):
        return ["m_Name", "smooth", "generate_material"]

    def m_connections(self):
        return (["input"], [], [], [])

    def draw_buttons(self, context, layout):
        layout.prop(self, "m_Name")
        layout.prop(self, "auto_update", text="Auto update")
        layout.prop(self, "smooth", text="Smooth")
        layout.prop(self, "generate_material")
        layout.separator()
        layout.operator("node.bvtk_node_update", text="update").node_path = node_path(
            self
        )

    def update_cb(self):
        """Update node color bar and update Blender object"""
        input_node, vtkobj = self.get_input_node("input")
        color_mapper = None
        if input_node and input_node.bl_idname == "BVTK_Node_ColorMapperType":
            color_mapper = input_node
            color_mapper.update()  # setting auto range
            input_node, vtkobj = input_node.get_input_node("input")
        if vtkobj:
            vtkobj = resolve_algorithm_output(vtkobj)
            vtkdata_to_blender(
                vtkobj, self.m_Name, color_mapper, self.smooth, self.generate_material
            )
            update_3d_view()

    def apply_properties(self, vtkobj):
        pass


def unwrap_and_color_the_mesh(
    ob, vtk_obj, name, color_mapper, bm, generate_material, vimap
):
    """Create UV unwrap corresponding to a generated color image to color
    the mesh. Also generates material if needed.
    """

    # Set colors and color legend
    if color_mapper and color_mapper.color_by:
        texture = color_mapper.get_texture()
        # Color Ramp texture_type is 'IMAGE'
        image_width = 1000
        img = image_from_ramp(texture.color_ramp, texture.name, image_width)

        # Color legend
        vrange = (color_mapper.min, color_mapper.max)
        if color_mapper.lut:
            create_lut(name, vrange, 6, texture, h=color_mapper.height)

        # Generate UV maps to get coloring either by points or faces
        bm.verts.index_update()
        bm.faces.index_update()
        if len(color_mapper.color_by) < 3:
            return error_text
        type_letter = color_mapper.color_by[0]
        array_name = color_mapper.color_by[2:]
        if type_letter == "P" or type_letter == "p":
            bm, val = point_unwrap(bm, vtk_obj, array_name, vrange, vimap)
            if val:
                return val
        elif type_letter == "C" or type_letter == "c":
            bm, val = face_unwrap(bm, vtk_obj, array_name, vrange)
            if val:
                return val
        else:
            return error_text

    # Generate default material if wanted
    if generate_material and color_mapper and color_mapper.color_by:
        create_material(ob, texture.name)
    elif generate_material:
        create_material(ob, None)


def vtkdata_to_blender(
    data, name, color_mapper=None, smooth=False, generate_material=False
):
    """Convert VTK data to Blender mesh object, using optionally
    given color mapper and normal smoothing. Optionally generates default
    material, which includes also color information if color_mapper is given.

    Note: This is the original implementation and does not consider
    VTK cell types (vertex semantics) in conversion, so it works best
    with polygon generators like vtkGeometryFilter.
    """
    if not data:
        l.error("no data!")
        return
    if issubclass(data.__class__, vtk.vtkImageData):
        imgdata_to_blender(data, name)
        return
    me, ob = mesh_and_object(name)
    if me.is_editmode:
        bpy.ops.object.mode_set(mode="OBJECT", toggle=False)
    err = 0  # Number of errors encountered
    bm = bmesh.new()
    # bm.from_mesh(me) # fill it in from a Mesh

    # Get vertices
    data_p = data.GetPoints()
    verts = [bm.verts.new(data_p.GetPoint(i)) for i in range(data.GetNumberOfPoints())]

    # Loop over cells to create edges and faces
    for i in range(data.GetNumberOfCells()):
        data_pi = data.GetCell(i).GetPointIds()
        # Error is raised if a face already exists. Count errors.
        try:
            face_verts = [
                verts[data_pi.GetId(x)] for x in range(data_pi.GetNumberOfIds())
            ]

            # Remove last vert if it is same as first vert
            if face_verts[-1] == face_verts[0]:
                face_verts = face_verts[0:-1]

            if len(face_verts) == 2:
                e = bm.edges.new(face_verts)
            else:
                f = bm.faces.new(face_verts)
                f.smooth = smooth
        except:
            err += 1
    if err:
        l.error("number of errors: " + str(err))

    # Set normals
    point_normals = data.GetPointData().GetNormals()
    cell_normals = data.GetCellData().GetNormals()
    if cell_normals:
        bm.faces.ensure_lookup_table()
        for i in range(len(bm.faces)):
            bm.faces[i].normal = cell_normals.GetTuple(i)
    if point_normals:
        for i in range(len(verts)):
            verts[i].normal = point_normals.GetTuple(i)

    # Set colors and color legend
    unwrap_and_color_the_mesh(ob, data, name, color_mapper, bm, generate_material)
    bm.to_mesh(me)  # store bmesh to mesh
    l.info("conversion successful, verts = " + str(len(verts)))


class BVTK_Node_VTKToBlenderMesh(Node, BVTK_Node):
    """New surface mesh coverter node. Convert output from a VTK Node to a
    Blender Mesh Object. Converts linear VTK cell types into a boundary mesh.
    """

    bl_idname = "BVTK_Node_VTKToBlenderMeshType"  # type name
    bl_label = "VTK To Blender Mesh"  # label for nice name display

    m_Name: bpy.props.StringProperty(
        name="Name", default="mesh", update=BVTK_Node.outdate_vtk_status
    )
    create_all_verts: bpy.props.BoolProperty(
        name="Create All Verts", default=False, update=BVTK_Node.outdate_vtk_status
    )
    create_edges: bpy.props.BoolProperty(
        name="Create Edges", default=True, update=BVTK_Node.outdate_vtk_status
    )
    create_faces: bpy.props.BoolProperty(
        name="Create Faces", default=True, update=BVTK_Node.outdate_vtk_status
    )
    smooth: bpy.props.BoolProperty(
        name="Smooth", default=False, update=BVTK_Node.outdate_vtk_status
    )
    recalc_norms: bpy.props.BoolProperty(
        name="Recalculate Normals", default=False, update=BVTK_Node.outdate_vtk_status
    )
    generate_material: bpy.props.BoolProperty(
        name="Generate Material", default=False, update=BVTK_Node.outdate_vtk_status
    )
    motion_blur: bpy.props.BoolProperty(
        name="Motion Blur", default=False, update=BVTK_Node.outdate_vtk_status
    )
    motion_blur_by: bpy.props.StringProperty(
        default="", name="Motion Blur By", update=BVTK_Node.outdate_vtk_status
    )
    motion_blur_time_step: bpy.props.FloatProperty(
        default=1.0,name="Time Step for Motion Blur",update=BVTK_Node.outdate_vtk_status
    )

    def motion_blur_by_enum_generator(self, context=None):
        """Enum list generator for motion_blur property.
        Generate array items available for coloring.
        """

        items = [("None", "Empty (clear value)", "Empty (clear value)", ENUM_ICON, 0)]

        (
            input_node,
            vtk_output_obj,
            vtk_connection,
        ) = self.get_input_node_and_output_vtk_objects()
        if vtk_output_obj:
            if hasattr(vtk_output_obj, "GetPointData"):
                p_data = vtk_output_obj.GetPointData()
                p_descr = "Color by point data using "
                for i in range(p_data.GetNumberOfArrays()):
                    arr_name = str(p_data.GetArrayName(i))
                    if p_data.GetArray(i).GetNumberOfComponents() != 3:
                        continue
                    items.append(
                        (
                            "P_" + arr_name,
                            arr_name,
                            p_descr + arr_name + " array",
                            "VERTEXSEL",
                            len(items),
                        )
                    )
        return items

    def motion_blur_set_value(self, context=None):
        """Set value of motion_blur_set_value using value from EnumProperty"""
        if self.motion_blur_property_list == "None":
            self.motion_blur_by = ""
        else:
            self.motion_blur_by = str(self.motion_blur_property_list)

    motion_blur_property_list: bpy.props.EnumProperty(
        items=motion_blur_by_enum_generator, update=motion_blur_set_value, name="Choices"
    )

    def m_properties(self):
        return [
            "m_Name",
            "create_all_verts",
            "create_edges",
            "create_faces",
            "smooth",
            "recalc_norms",
            "generate_material",
            "motion_blur",
            "motion_blur_by",
            "motion_blur_time_step",
        ]

    def m_connections(self):
        return (["input"], [], [], [])

    def draw_buttons_special(self, context, layout):
        """Custom draw buttons function, to show force update button. Force
        update is sometimes necessary for e.g. vtkPlane when using
        Blender object for specifying the plane. Changing Blender
        object properties does not trigger property outdating for
        nodes, so user must have an option for force updating the
        upstream pipeline.
        """
        layout.prop(self, "m_Name")
        layout.prop(self, "create_all_verts")
        layout.prop(self, "create_edges")
        layout.prop(self, "create_faces")
        layout.prop(self, "smooth")
        layout.prop(self, "recalc_norms")
        layout.prop(self, "generate_material")
        layout.prop(self, "motion_blur")
        if self.motion_blur:
            row = layout.row(align=True)
            row.prop(self, "motion_blur_by")
            row.prop(self, "motion_blur_property_list", icon_only=True)
            layout.prop(self,"motion_blur_time_step")
        layout.operator("node.bvtk_node_force_update_upstream").node_path = node_path(
            self
        )

    def apply_properties_special(self):
        """Generate Blender mesh object from VTK object"""
        (
            input_node,
            vtk_output_obj,
            vtk_connection,
        ) = self.get_input_node_and_output_vtk_objects()
        color_mapper = None
        if input_node and input_node.bl_idname == "BVTK_Node_ColorMapperType":
            color_mapper = input_node
        val = vtkdata_to_blender_mesh(
            vtk_output_obj,
            self.m_Name,
            smooth=self.smooth,
            create_all_verts=self.create_all_verts,
            create_edges=self.create_edges,
            create_faces=self.create_faces,
            recalc_norms=self.recalc_norms,
            generate_material=self.generate_material,
            color_mapper=color_mapper,
            motion_blur=self.motion_blur,
            motion_blur_array_name = self.motion_blur_by,
            motion_blur_time_step = self.motion_blur_time_step,
        )
        if val:
            self.ui_message = val
            return "error"
        update_3d_view()
        return "up-to-date"

    def init_vtk(self):
        self.set_vtk_status("out-of-date")
        return None


def map_elements(vals, slist):
    """Create list of elements (possibly recursing into embedded lists)
    with same structure as index list slist, where each element has
    been mapped to a value in vals.
    """
    dlist = []
    for elem in slist:
        if isinstance(elem, list):
            dlist.append(map_elements(vals, elem))
        else:
            dlist.append(vals[elem])
    return dlist


def add_verts_to_facelist(verts, facelist):
    """Help function to check and add verts to facelist"""
    if len(set(verts)) > 2:
        facelist.append(verts)
    else:
        l.debug("Skipping face, not enough unique verts: " + str(verts))
    return facelist


def vtk_cell_to_edges_and_faces(cell_type, vis, polyfacelist):
    """Create lists of edge vertices and face vertices from argument VTK
    cell type and VTK vertex ids. Polyfacelist is face stream for polyhedrons.
    """

    # List of VTK cell types:
    # https://vtk.org/doc/nightly/html/vtkCellType_8h_source.html
    # https://lorensen.github.io/VTKExamples/site/VTKFileFormats/

    def get_polyhedron_fis(polyfacelist):
        """Generate face vertex indices (fis) from argument polyhedron face
        stream list
        """
        # https://vtk.org/Wiki/VTK/Polyhedron_Support
        next_number_is_vertex_count = True
        fis = []  # list of vertex index lists, to be generated here
        for n in polyfacelist[1:]:
            if next_number_is_vertex_count:
                numVerts = n
                next_number_is_vertex_count = False
                vertlist = []
            else:
                vertlist.append(n)
            if len(vertlist) == numVerts:
                fis.append(vertlist)
                next_number_is_vertex_count = True
        return fis

    # Generate edge vertex lists and face vertex lists for each cell type
    if cell_type < 3:  # VTK_VERTEX or VTK_POLY_VERTEX are ignored here
        return [None], [None]

    elif cell_type == 3:  # VTK_LINE
        return [vis], [None]

    elif cell_type == 4:  # VTK_POLY_LINE
        edgelist = [[vis[i], vis[i + 1]] for i in range(len(vis) - 1)]
        return edgelist, [None]

    elif cell_type == 5:  # VTK_TRIANGLE
        return [None], [vis]

    elif cell_type == 6:  # VTK_TRIANGLE_STRIP
        facelist = []
        from math import floor

        # Pairwise triangle generation to get correct normal directions
        for i in range(0, floor(len(vis) / 2), 2):
            verts = [vis[i], vis[i + 1], vis[i + 2]]
            facelist = add_verts_to_facelist(verts, facelist)
            verts = [vis[i + 1], vis[i + 3], vis[i + 2]]
            facelist = add_verts_to_facelist(verts, facelist)
        # Last odd triangle
        if len(vis) % 2 == 1:
            verts = [vis[-3], vis[-2], vis[-1]]
            facelist = add_verts_to_facelist(verts, facelist)
        return [None], facelist

    elif cell_type == 7:  # VTK_POLYGON
        return [None], [vis]

    elif cell_type == 8:  # VTK_PIXEL
        return [None], [[vis[0], vis[1], vis[3], vis[2]]]

    elif cell_type == 9:  # VTK_QUAD
        return [None], [vis]

    elif cell_type == 10:  # VTK_TETRA
        fis = [[0, 2, 1], [0, 1, 3], [1, 2, 3], [0, 3, 2]]
        facelist = map_elements(vis, fis)
        return [None], facelist

    elif cell_type == 11:  # VTK_VOXEL
        fis = [
            [0, 1, 5, 4],
            [0, 4, 6, 2],
            [4, 5, 7, 6],
            [1, 3, 7, 5],
            [0, 2, 3, 1],
            [6, 7, 3, 2],
        ]
        facelist = map_elements(vis, fis)
        return [None], facelist

    elif cell_type == 12:  # VTK_HEXAHEDRON
        fis = [
            [0, 3, 2, 1],
            [0, 1, 5, 4],
            [1, 2, 6, 5],
            [2, 3, 7, 6],
            [3, 0, 4, 7],
            [7, 4, 5, 6],
        ]
        facelist = map_elements(vis, fis)
        return [None], facelist

    elif cell_type == 13:  # VTK_WEDGE (=prism)
        fis = [[0, 1, 2], [0, 3, 4, 1], [1, 4, 5, 2], [2, 5, 3, 0], [3, 5, 4]]
        facelist = map_elements(vis, fis)
        return [None], facelist

    elif cell_type == 14:  # VTK_PYRAMID
        fis = [[0, 3, 2, 1], [0, 4, 3], [3, 4, 2], [2, 4, 1], [1, 4, 0]]
        facelist = map_elements(vis, fis)
        return [None], facelist

    elif cell_type == 15:  # VTK_PENTAGONAL_PRISM
        fis = [
            [0, 1, 2, 3, 4],
            [0, 5, 6, 1],
            [1, 6, 7, 2],
            [2, 7, 8, 3],
            [3, 8, 9, 4],
            [4, 9, 5, 0],
            [9, 8, 7, 6, 5],
        ]
        facelist = map_elements(vis, fis)
        return [None], facelist

    elif cell_type == 16:  # VTK_HEXAGONAL_PRISM
        fis = [
            [0, 1, 2, 3, 4, 5],
            [0, 6, 7, 1],
            [1, 7, 8, 2],
            [2, 8, 9, 3],
            [3, 9, 10, 4],
            [4, 10, 11, 5],
            [5, 11, 6, 0],
            [11, 10, 9, 8, 7, 6],
        ]
        facelist = map_elements(vis, fis)
        return [None], facelist

    elif cell_type == 42:  # VTK_POLYHEDRON
        facelist = get_polyhedron_fis(polyfacelist)
        return [None], facelist

    else:
        raise ValueError("Unsupported VTK cell type %d" % cell_type)


def process_cell_edge(edges, verts):
    """Add argument cell edge verts to edges dictionary"""

    key = str(sorted(verts))
    edges[key] = verts
    return edges


def process_cell_face(faces, verts):
    """Add (or remove) argument cell face verts to (from) faces dictionary"""

    # First make sure first vertex is not repeated at end
    if verts[0] == verts[-1]:
        verts = verts[0:-1]

    # Discard face if same vertices are used many times.
    # At least vtkContourFilter can produce such bad triangles.
    if not (sorted(verts) == sorted(set(verts))):
        l.debug("Discarding illegal face (verts %s)" % str(verts))
        return faces

    key = str(sorted(verts))
    if key not in faces:
        faces[key] = verts
    else:
        faces.pop(key)
    return faces


def edges_and_faces_to_bmesh(
    edges,
    faces,
    vcoords,
    smooth,
    bm,
    create_all_verts,
    create_edges,
    create_faces,
    recalc_norms,
):
    """Add argument verts, edges and faces using vertex coordinates
    vcoords to bmesh bm.
    """

    vertmap = {}  # dictionary to map from VTK vertex index to BMVert
    vimap = {}  # map from bmesh vertex index to VTK vertex index
    viset = set()  # set to store added VTK vertex indices for fast access

    def add_vert(vi, vertmap, vcoords, bm):
        """Add vertex index vi to bmesh if vertex is not there already"""
        if vi not in vertmap:
            v = bm.verts.new(vcoords[vi])
            vertmap[vi] = v

    def add_vi(vi, vimap, viset):
        """Add index of vertex to map from bmesh vertex index to VTK vertex index"""
        if vi in viset:
            return
        i = len(vimap)
        vimap[i] = vi
        viset.add(vi)

    # Create BMVerts
    if create_all_verts:
        for vi in range(len(vcoords)):
            add_vert(vi, vertmap, vcoords, bm)
            add_vi(vi, vimap, viset)

    # Create BMEdges
    if create_edges:
        for vi1, vi2 in edges.values():
            add_vert(vi1, vertmap, vcoords, bm)
            add_vert(vi2, vertmap, vcoords, bm)
            add_vi(vi1, vimap, viset)
            add_vi(vi2, vimap, viset)
            bm.edges.new([vertmap[vi1], vertmap[vi2]])

    # Create BMFaces
    for vis in faces.values():
        if len(set(vis)) < 3:
            l.debug("Skipping face with verts " + str(vis))
            continue
        for vi in vis:
            add_vert(vi, vertmap, vcoords, bm)
            add_vi(vi, vimap, viset)
        f = bm.faces.new(map_elements(vertmap, vis))
        f.smooth = smooth

    if not create_faces:
        bmesh.ops.delete(bm, geom=bm.faces, context="FACES_ONLY")
    if not create_edges and not create_faces:
        bmesh.ops.delete(bm, geom=bm.edges, context="EDGES_FACES")

    if recalc_norms:
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    else:
        # Force normal updates. Without normal updates use of smooth
        # option will result in surfaces being rendered as black.
        for f in bm.faces:
            f.normal_update()
        for v in bm.verts:
            v.normal_update()

    return vimap


def vtkdata_to_blender_mesh(
    vtk_obj,
    name,
    create_all_verts=False,
    create_edges=True,
    create_faces=True,
    color_mapper=None,
    smooth=False,
    recalc_norms=False,
    generate_material=False,
    motion_blur=False,
    motion_blur_array_name=None,
    motion_blur_time_step=1.0,
):
    """Convert linear and polyhedron VTK cells into a boundary Blender
    surface mesh object.
    """

    from mathutils import Vector
    if not vtk_obj:
        return "No VTK object on input"
    if issubclass(vtk_obj.__class__, vtk.vtkImageData):
        imgdata_to_blender(vtk_obj, name)
        return
    me, ob = mesh_and_object(name)

    if me.is_editmode:
        bpy.ops.object.mode_set(mode="OBJECT", toggle=False)

    # Initialize the Basis shape key for mesh motion blur
    if motion_blur and not ob.data.shape_keys:
        ob.shape_key_add(name="Basis", from_mix=False)

    # Get all VTK vertex coordinates
    data_p = vtk_obj.GetPoints()
    vcoords = [data_p.GetPoint(i) for i in range(vtk_obj.GetNumberOfPoints())]

    faces = {}  # dictionary of boundary face vertices to be created
    edges = {}  # dictionary of non-face edges to be created

    # Process all VTK cells
    for i in range(vtk_obj.GetNumberOfCells()):
        data_pi = vtk_obj.GetCell(i).GetPointIds()
        vert_ids = [data_pi.GetId(x) for x in range(data_pi.GetNumberOfIds())]
        cell_type = vtk_obj.GetCell(i).GetCellType()
        polyfacelist = []

        # Polyhedrons need additional polyfacelist (face stream in VTK terminology)
        # https://vtk.org/Wiki/VTK/Polyhedron_Support
        if cell_type == 42:
            fs = vtk.vtkIdList()
            vtk_obj.GetFaceStream(i, fs)
            polyfacelist = [fs.GetId(ind) for ind in range(fs.GetNumberOfIds())]

        edge_vis, face_vis = vtk_cell_to_edges_and_faces(
            cell_type, vert_ids, polyfacelist
        )

        # l.debug("cell %d: edge_vis: %s" % (i, str(edge_vis))
        #        + " face_vis: %s" % str(face_vis))

        for vis in edge_vis:
            if vis == None:
                continue
            edges = process_cell_edge(edges, vis)

        for vis in face_vis:
            if vis == None:
                continue
            faces = process_cell_face(faces, vis)

    # Create mesh from remaining faces
    bm = bmesh.new()
    vimap = edges_and_faces_to_bmesh(
        edges,
        faces,
        vcoords,
        smooth,
        bm,
        create_all_verts,
        create_edges,
        create_faces,
        recalc_norms,
    )
    val = unwrap_and_color_the_mesh(
        ob, vtk_obj, name, color_mapper, bm, generate_material, vimap
    )

    # Mesh motion blur
    if motion_blur:
        nFrame = bpy.context.scene.frame_current
        l.debug("Set up motion blur for frame %d" % nFrame)
        if ((not bm.verts.layers.shape.keys()) or \
            (not "key_blur" in bm.verts.layers.shape.keys())):
               key_shape = bm.verts.layers.shape.new("key_blur")
        else:
            key_shape = bm.verts.layers.shape["key_blur"]

        if len(motion_blur_array_name) < 3:
            return "Motion blur array name is wrong (minimum 3 letters)"
        array_data = get_vtk_array_data(vtk_obj, motion_blur_array_name[2:], array_type=motion_blur_array_name[0])
        if not array_data:
            return "Did not find point array %r" % motion_blur_array_name[2:]
        array_data = numpy_support.vtk_to_numpy(array_data)

        # Calculate shape key coordinates
        for i, bv in enumerate(bm.verts):
            bv[key_shape] = bv.co + motion_blur_time_step * Vector(array_data[i])

    bm.to_mesh(me)

    # Add keyframes to shape key Value parameter to animate motion blur
    if motion_blur:
        ob.data.shape_keys.animation_data_clear()
        kb = ob.data.shape_keys.key_blocks["key_blur"]
        kb.value = 1.0
        kb.keyframe_insert("value", frame=nFrame+1)
        kb.value = 0.0
        kb.keyframe_insert("value", frame=nFrame)
        # Set FCurve interpolation to linear (default is bezier).
        # Setting kb.interpolation="KEY_LINEAR" does not produce linear interpolation.
        ob.data.shape_keys.animation_data.action.fcurves[0].keyframe_points[0].interpolation='LINEAR'
        ob.data.shape_keys.animation_data.action.fcurves[0].keyframe_points[1].interpolation='LINEAR'
        bpy.context.scene.cycles.use_motion_blur = True
        bpy.context.scene.eevee.use_motion_blur = True
        # Must use "Start on Frame" Position for motion blur to avoid frame changes
        bpy.context.scene.cycles.motion_blur_position = "START"
        bpy.context.scene.eevee.motion_blur_position = "START"
        bpy.context.scene.view_layers.update()

    if val:
        start_info = "Coloring failed,"
    else:
        start_info = "Conversion successful,"

    l.info(
        start_info
        + " verts:%d" % len(bm.verts)
        + " edges:%d" % len(bm.edges)
        + " faces:%d" % len(bm.faces)
    )
    return val


# -----------------------------------------------------------------------------
# Particle converter
# -----------------------------------------------------------------------------


class BVTK_OT_InitializeParticleSystem(bpy.types.Operator):
    """Operator to initialize Blender Particle system for VTK To Blender
    Particles node.
    """

    bl_idname = "node.bvtk_initialize_particle_system"
    bl_label = "Initialize Particles"

    def execute(self, context):
        nSystems = 0
        for node_group in bpy.data.node_groups:
            for node in node_group.nodes:
                if node.bl_idname == "BVTK_Node_VTKToBlenderParticlesType":
                    nSystems += 1
                    zero_particle_system(node)
        self.report({"INFO"}, "Initialized %d Particle Systems." % nSystems)
        return {"FINISHED"}


def zero_particle_system(node):
    """Reinitialize Blender Particle System for argument node"""

    obname = node.ob_name
    glyph_obname = node.glyph_name
    np = node.np

    # Delete existing any old object
    if obname in bpy.data.objects:
        bpy.context.view_layer.objects.active = bpy.data.objects[obname]
        mesh = bpy.data.objects[obname].data
        bpy.ops.object.mode_set(mode="OBJECT")
        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects[obname].select_set(True)
        bpy.ops.object.particle_system_remove()
        bpy.ops.object.parent_clear()
        bpy.ops.object.delete()
        bpy.data.meshes.remove(mesh)

    # Reset material on glyph object, get material
    matname = obname + "_material"
    if node.generate_material:
        glyph_ob = bpy.data.objects[node.glyph_name]
        mat = reset_particle_material(glyph_ob, matname)
    else:
        mat = bpy.data.materials[matname]

    mesh_data = bpy.data.meshes.new(obname)
    ob = bpy.data.objects.new(obname, mesh_data)
    bpy.context.scene.collection.objects.link(ob)
    bpy.context.view_layer.objects.active = bpy.data.objects[obname]
    ob.select_set(True)

    # Must have some geometry from where to emit particles
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.primitive_cube_add(size=1e-6)  # TODO: Improve
    bpy.ops.object.mode_set(mode="OBJECT")

    # Set glyph material to particles object
    bpy.ops.object.material_slot_add()
    ob.active_material = mat

    # Add and parent particle system
    bpy.ops.object.particle_system_add()
    bpy.ops.object.select_all(action="DESELECT")
    bpy.data.objects[glyph_obname].select_set(True)
    bpy.ops.object.parent_set()

    ob.particle_systems[0].settings.count = np
    ob.particle_systems[0].settings.frame_start = 0
    ob.particle_systems[0].settings.frame_end = 0
    ob.particle_systems[0].settings.lifetime = 1000000
    ob.particle_systems[0].settings.physics_type = "NO"
    ob.particle_systems[0].settings.render_type = "OBJECT"
    ob.particle_systems[0].settings.particle_size = 1.0
    ob.particle_systems[0].settings.instance_object = bpy.data.objects[glyph_obname]
    ob.particle_systems[0].settings.emit_from = "VERT"
    ob.particle_systems[0].settings.normal_factor = 0.0
    # ob.particle_systems[0].settings.object_align_factor[1] = 1.0

    ob.show_instancer_for_viewport = True


class BVTK_Node_VTKToBlenderParticles(Node, BVTK_Node):
    """Convert output from VTK Node to Blender Particle System"""

    bl_idname = "BVTK_Node_VTKToBlenderParticlesType"  # type name
    bl_label = "VTK To Blender Particles"  # label for nice name display

    ob_name: bpy.props.StringProperty(
        name="Name", default="particles", update=BVTK_Node.outdate_vtk_status
    )
    glyph_name: bpy.props.StringProperty(
        name="Glyph Name", default="glyph", update=BVTK_Node.outdate_vtk_status
    )
    vec_name: bpy.props.StringProperty(
        name="Direction Vector Array Name",
        default="",
        update=BVTK_Node.outdate_vtk_status,
    )
    scale_name: bpy.props.StringProperty(
        name="Scale Value or Name", default="", update=BVTK_Node.outdate_vtk_status
    )
    color_name: bpy.props.StringProperty(
        name="Color Value Array Name", default="", update=BVTK_Node.outdate_vtk_status
    )
    np: bpy.props.IntProperty(
        name="Particle Count", default=1000, min=1, update=BVTK_Node.outdate_vtk_status
    )
    generate_material: bpy.props.BoolProperty(
        name="Generate Material", default=True, update=BVTK_Node.outdate_vtk_status
    )

    # Data storage for point data from VTK
    from typing import List

    locs: List[float]
    scales: List[float]
    color_values: List[float]
    quats: List[float]
    nParticles: float

    def m_properties(self):
        return [
            "ob_name",
            "glyph_name",
            "vec_name",
            "scale_name",
            "color_name",
            "np",
            "generate_material",
        ]

    def m_connections(self):
        return (["input"], [], [], [])

    def draw_buttons_special(self, context, layout):
        layout.prop(self, "ob_name")
        layout.prop(self, "glyph_name")
        layout.prop(self, "vec_name")
        layout.prop(self, "scale_name")
        layout.prop(self, "color_name")
        layout.prop(self, "np")
        layout.prop(self, "generate_material")
        layout.operator("node.bvtk_initialize_particle_system", text="Initialize")

    def update_particle_system(self, depsgraph):
        """Updates Blender Particle System from point data in vtkPolyData"""
        (
            input_node,
            vtk_output_obj,
            vtk_connection,
        ) = self.get_input_node_and_output_vtk_objects()
        if not vtk_output_obj:
            return

        l.debug("Updating Particle System for Object %r" % self.ob_name)
        if not vtk_output_obj:
            l.error("No vtkdata!")
            return
        if not issubclass(vtk_output_obj.__class__, vtk.vtkPolyData):
            l.error("Data is not vtkPolyData!")
            return

        npoints = get_vtk_particle_data(self, vtk_output_obj)
        if npoints == 0:
            return
        vtkdata_to_blender_particles(self, depsgraph)
        update_3d_view()

    def apply_properties_special(self):
        warning_text = warn_if_not_exist_object(self.glyph_name)
        if warning_text:
            self.ui_message = warning_text
            return "error"
        # Note: update_particle_system is called from on_frame_change
        # and not here, because it requires depsgraph.
        return "up-to-date"

    def init_vtk(self):
        self.set_vtk_status("out-of-date")
        return None


def truncate_or_pad_list(slist, n):
    """Truncate or pad the argument list slist to contain exacly n entries"""

    # Truncate
    length = len(slist)
    if length >= n:
        return slist[0:n]

    # Pad
    if type(slist[0]) is list:
        element = [0.0 * i for i in slist[0]]
    elif type(slist[0]) is tuple:
        element = tuple([0.0 * i for i in slist[0]])
    else:
        element = 0.0
    newlist = list(slist)
    for i in range(n - length):
        newlist.append(element)
    return newlist


def get_array_data(pointdata, array_name):
    """Return vtkArray from VTK point data for given array name"""

    narrays = pointdata.GetNumberOfArrays()
    if narrays == 0:
        return None

    array_names = [pointdata.GetArrayName(i) for i in range(narrays)]
    if array_name not in array_names:
        return None
    arrdata = pointdata.GetArray(array_names.index(array_name))
    return arrdata


def color_scale(vals):
    """Scale list of values to 0.0 <= x <= 1.0"""
    minval = min(vals)
    maxval = max(vals)
    # Force a small difference to avoid div by zero
    if maxval <= minval:
        minval = 0.99999 * minval
        maxval = 1.00001 * minval
    return [(v - minval) / (maxval - minval) for v in vals]


def get_vtk_particle_data(self, vtkdata):
    """Get lists of particle properties from vtkPolyData and store those
    to self storage variables.
    """
    n = vtkdata.GetNumberOfPoints()
    if n == 0:
        return 0

    # Vertex locations
    p = vtkdata.GetPoints()
    locs = [p.GetPoint(i) for i in range(n)]
    locs = truncate_or_pad_list(locs, self.np)
    # Flatten the list
    self.locs = [i for sublist in locs for i in sublist]

    pdata = vtkdata.GetPointData()

    # Direction vectors
    vecs_array = get_array_data(pdata, self.vec_name)
    if not vecs_array:
        vecs = n * [(1.0, 0.0, 0.0)]
    else:
        vecs = [vecs_array.GetTuple3(i) for i in range(n)]
    vecs = truncate_or_pad_list(vecs, self.np)

    # Quaternion coefficients for rotating glyphs towards direction vectors
    # https://stackoverflow.com/questions/1171849/finding-quaternion-representing-the-rotation-from-one-vector-to-another
    from mathutils import Vector
    from math import sqrt

    quats = []  # List where to append quaternion coefficients w, x, y and z

    # Assume glyph object points towards positive X axis
    v1 = Vector((0.0, -1.0, 0.0))

    for vec in vecs:
        v2 = Vector(vec).normalized()
        crossvec = v1.cross(v2)
        w = 1.0 + v1.dot(v2)
        quats.append(w)
        quats.append(crossvec[0])
        quats.append(crossvec[1])
        quats.append(crossvec[2])
    self.quats = quats

    # Scaling sizes
    scales_array = get_array_data(pdata, self.scale_name)
    if not scales_array:
        try:
            # Check if Scale Name is a float
            float_val = float(self.scale_name)
        except:
            float_val = 1.0
        scales = n * [float_val]
    else:
        scales = [scales_array.GetValue(i) for i in range(n)]
    scales = truncate_or_pad_list(scales, self.np)
    self.scales = scales

    # Color ramp values
    color_values_array = get_array_data(pdata, self.color_name)
    if not color_values_array:
        color_values = n * [0.5]
    else:
        color_values = [color_values_array.GetValue(i) for i in range(n)]
    color_values = color_scale(color_values)
    color_values = truncate_or_pad_list(color_values, self.np)
    self.color_values = color_values
    return n


def vtkdata_to_blender_particles(self, depsgraph):
    """Populate Blender Particle System with data"""

    obname = self.ob_name
    ob = bpy.data.objects[obname]

    particle_system = ob.evaluated_get(depsgraph).particle_systems[0]
    particles = particle_system.particles

    particles.foreach_set("location", self.locs)
    particles.foreach_set("size", self.scales)
    particles.foreach_set("rotation", self.quats)

    # Use particle lifetime slot for color ramp value. If there is a
    # better way to color Blender particles, please let me know.
    # Note: Coloring shows up currently only in Cycles!
    particles.foreach_set("lifetime", self.color_values)


def reset_particle_material(ob, matname):
    """Create default particle material setup for object"""

    if matname in bpy.data.materials:
        mat = bpy.data.materials[matname]
    else:
        mat = bpy.data.materials.new(name=matname)

    if not mat.use_nodes:
        mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Delete existing nodes
    for i in nodes:
        nodes.remove(i)

    node1 = nodes.new("ShaderNodeOutputMaterial")
    node1.location = (300, 300)

    node2 = nodes.new("ShaderNodeBsdfPrincipled")
    node2.location = (0, 300)
    links.new(node2.outputs["BSDF"], node1.inputs["Surface"])

    node3 = nodes.new("ShaderNodeValToRGB")
    node3.location = (-300, 300)
    links.new(node3.outputs["Color"], node2.inputs["Base Color"])

    # Create a blue-to-red rainbow color ramp as a default
    elems = node3.color_ramp.elements
    elems[0].color = (0.0, 0.0, 1.0, 1.0)
    elems[1].position = 0.25
    elems[1].color = (0.0, 1.0, 1.0, 1.0)
    a = elems.new(0.5)
    a.color = (0.0, 1.0, 0.0, 1.0)
    a = elems.new(0.75)
    a.color = (1.0, 1.0, 0.0, 1.0)
    a = elems.new(1.0)
    a.color = (1.0, 0.0, 0.0, 1.0)

    node4 = nodes.new("ShaderNodeParticleInfo")
    node4.location = (-500, 300)
    links.new(node4.outputs["Lifetime"], node3.inputs["Fac"])

    # Assign material
    if ob.data.materials:
        ob.data.materials[0] = mat
    else:
        ob.data.materials.append(mat)
    return mat


# -----------------------------------------------------------------------------
# Blender Volume (OpenVDB) converter
# -----------------------------------------------------------------------------


class BVTK_Node_VTKToBlenderVolume(Node, BVTK_Node):
    """Convert output from VTK Node to Blender Volume Object.
    Requires pyopenvdb, which is included in Blender 3.6 by default.
    """

    bl_idname = "BVTK_Node_VTKToBlenderVolumeType"
    bl_label = "VTK To Blender Volume"

    ob_name: bpy.props.StringProperty(name="Name", default="volume")
    density_name: bpy.props.StringProperty(name="Density Field Name", default="")
    color_name: bpy.props.StringProperty(name="Color Field Name", default="")
    flame_name: bpy.props.StringProperty(name="Flame Field Name", default="")
    temperature_name: bpy.props.StringProperty(
        name="Temperature Field Name", default=""
    )
    generate_material: bpy.props.BoolProperty(name="Generate Material", default=True)
    use_copy_from_array: bpy.props.BoolProperty(
        name="Use copyFromArray()", default=False
    )
    export_file_sequence: bpy.props.BoolProperty(
        name="Export File Sequence", default=False
    )

    def m_properties(self):
        return [
            "ob_name",
            "density_name",
            "color_name",
            "flame_name",
            "temperature_name",
            "generate_material",
            "use_copy_from_array",
            "export_file_sequence",
        ]

    def m_connections(self):
        return (["input"], [], [], [])

    def draw_buttons_special(self, context, layout):
        global with_pyopenvdb
        if not with_pyopenvdb:
            layout.label(text="Error: Missing pyopenvdb!")
            layout.label(text="Please read node docs for more info")
            return
        layout.prop(self, "ob_name")
        layout.prop(self, "density_name")
        layout.prop(self, "color_name")
        layout.prop(self, "flame_name")
        layout.prop(self, "temperature_name")
        # Do not expose use_copy_from_array - it's not working correctly. TODO: Why?
        # layout.prop(self, 'use_copy_from_array')
        layout.prop(self, "generate_material")
        layout.prop(self, "export_file_sequence")
        layout.operator("node.bvtk_node_force_update_upstream").node_path = node_path(
            self
        )

    def apply_properties_special(self):
        """Update Blender Volume data from vtkImageData"""
        (
            input_node,
            vtk_output_obj,
            vtk_connection,
        ) = self.get_input_node_and_output_vtk_objects()
        l.debug("Updating Volume Object %r" % self.ob_name)

        if not vtk_output_obj:
            self.ui_message = "Error: No VTK data on input!"
            return "error"

        if not issubclass(vtk_output_obj.__class__, vtk.vtkImageData):
            self.ui_message = "Error: Input is not vtkImageData!"
            return "error"

        vtk_image_data_to_volume_object(self, vtk_output_obj)
        update_3d_view()
        return "up-to-date"

    def init_vtk(self):
        self.set_vtk_status("out-of-date")
        return None


def create_grid_from_data_array(
    imgdata,
    data_name,
    grid_name,
    background_value,
    tolerance,
    use_copy_from_array=False,
    atype="scalar",
):
    """Return OpenVDB grid containing data copied from vtkImageData array"""

    import numpy
    from vtk.util import numpy_support

    vdb = pyopenvdb

    if data_name == "":
        return None

    dims = list(imgdata.GetDimensions())

    if atype == "scalar":
        data = imgdata.GetPointData().GetScalars(data_name)
        if not data:
            raise ValueError("Input data %r not found" % data_name)
        grid = vdb.FloatGrid(background_value)
    elif atype == "vector":
        data = imgdata.GetPointData().GetVectors(data_name)
        if not data:
            raise ValueError("Input data %r not found" % data_name)
        grid = vdb.Vec3SGrid()
        dims.append(3)
    else:
        raise TypeError("unknown type %s" % str(atype))

    grid.gridClass = vdb.GridClass.FOG_VOLUME
    grid.name = grid_name

    if use_copy_from_array:
        # Create grid from NumPy array
        # TODO: There's something strange going on in array shape or order..
        ndarray = numpy_support.vtk_to_numpy(data).reshape(list(reversed(dims)))
        grid.copyFromArray(ndarray, tolerance=tolerance)

    else:
        # Create grid by looping over points with accessor
        ndarray = numpy_support.vtk_to_numpy(data).reshape(dims)
        acc = grid.getAccessor()
        for i in range(dims[0]):
            for j in range(dims[1]):
                for k in range(dims[2]):
                    idx = i + j * dims[0] + k * dims[0] * dims[1]
                    if atype == "scalar":
                        value = data.GetTuple1(idx)
                        if value > background_value:
                            acc.setValueOn((i, j, k), value)
                    elif atype == "vector":
                        value = data.GetTuple3(idx)
                        acc.setValueOn((i, j, k), value)
    return grid


def count_active_voxels(grids):
    """Counts the number of active voxels in list of OpenVDB grids"""
    n = 0
    for grid in grids:
        n += grid.activeVoxelCount()
    return n


def delete_objects_startswith(ob_name, export_file_sequence = False):
    """Deletes object(s) whose name starts with argument object name"""

    if export_file_sequence:
        objects = [ob for ob in bpy.data.objects if ob.name.startswith(ob_name)]
    else:
        ob = bpy.data.objects.get(ob_name)
        objects = [ob] if ob else []

    for ob in objects:
        l.debug("Deleting object %r" % ob.name)
        ob_data = ob.data

        bpy.context.collection.objects.unlink(ob)
        bpy.data.objects.remove(ob)

        if ob_data is None:
            continue
        if ob_data.users > 0:
            continue
        if isinstance(ob_data, bpy.types.Volume):
            bpy.data.volumes.remove(ob_data)
            

def import_volume_object(
    ob_name, filename, bounding_box=None, dims=None, generate_material=False, export_file_sequence = False
):
    """Import OpenVDB volume object from given file name into scene"""

    bpy.ops.object.volume_import(filepath=filename)
    if export_file_sequence:
        objects = [ob for ob in bpy.data.objects if ob.name.startswith(ob_name)]

        if len(objects) == 0:
            l.error("OpenVDB import failed for %r" % filename)
            return None
        elif len(objects) > 1:
            l.warning("Several objects name starts with %r, using last." % ob_name)

        ob = objects[-1]
    else:
        ob = bpy.data.objects.get(ob_name)
        if ob is None:
            l.error("OpenVDB import failed for %r" % filename)
            return None

    l.debug("Imported volume object: %s" % ob.name)

    # Final object transforms
    bbox = bounding_box
    if bbox:
        ob.location[0] = bbox[0]
        ob.location[1] = bbox[2]
        ob.location[2] = bbox[4]
    if bbox and dims:
        ob.scale[0] = (bbox[1] - bbox[0]) / dims[0]
        ob.scale[1] = (bbox[3] - bbox[2]) / dims[1]
        ob.scale[2] = (bbox[5] - bbox[4]) / dims[2]

    # Volume material
    matname = ob_name + "_material"
    if generate_material:
        reset_volume_material(ob, matname)
    elif matname in bpy.data.materials:
        mat = bpy.data.materials[matname]
        ob.data.materials.append(mat)
    return ob


def reset_volume_material(ob, matname):
    """Reset volume material to a default"""

    if matname in bpy.data.materials:
        mat = bpy.data.materials[matname]
    else:
        mat = bpy.data.materials.new(name=matname)

    if not mat.use_nodes:
        mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Delete existing nodes
    for i in nodes:
        nodes.remove(i)

    node1 = nodes.new("ShaderNodeOutputMaterial")
    node1.location = (300, 300)

    node2 = nodes.new("ShaderNodeVolumePrincipled")
    node2.location = (0, 300)
    links.new(node2.outputs["Volume"], node1.inputs["Volume"])

    node3 = nodes.new("ShaderNodeVolumeInfo")
    node3.location = (-300, 300)
    links.new(node3.outputs["Color"], node2.inputs["Color"])
    links.new(node3.outputs["Density"], node2.inputs["Density"])
    links.new(node3.outputs["Flame"], node2.inputs["Emission Strength"])

    # Assign material
    if ob.data.materials:
        ob.data.materials[0] = mat
    else:
        ob.data.materials.append(mat)
    return mat


def vtk_image_data_to_volume_object(node, imgdata):
    """Update Blender Volume data from vtkImageData"""

    vdb = pyopenvdb
    background_value = 0.0  # Zero value for OpenVDB grid
    tolerance = 1e-6  # Tolerance for value being zero

    density_grid = create_grid_from_data_array(
        imgdata,
        node.density_name,
        "density",
        background_value,
        tolerance,
        node.use_copy_from_array,
        "scalar",
    )
    color_grid = create_grid_from_data_array(
        imgdata,
        node.color_name,
        "color",
        background_value,
        tolerance,
        node.use_copy_from_array,
        "vector",
    )
    flame_grid = create_grid_from_data_array(
        imgdata,
        node.flame_name,
        "flame",
        background_value,
        tolerance,
        node.use_copy_from_array,
        "scalar",
    )
    temperature_grid = create_grid_from_data_array(
        imgdata,
        node.temperature_name,
        "temperature",
        background_value,
        tolerance,
        node.use_copy_from_array,
        "scalar",
    )

    if not node.export_file_sequence:
        basename = node.ob_name + ".vdb"
    else:
        seq = "_%05d" % bpy.context.scene.frame_current
        basename = node.ob_name + seq + ".vdb"

    filename = os.path.join(bpy.path.abspath("//"), basename)
    grids = [density_grid, color_grid, flame_grid, temperature_grid]
    grids = [g for g in grids if g is not None]
    nvoxels = count_active_voxels(grids)
    if nvoxels == 0:
        l.info("No voxel data found, no volume exports or imports done.")
        return
    vdb.write(filename, grids=grids)
    l.info("Saved %r (%d active voxels)" % (filename, nvoxels))

    bbox = imgdata.GetBounds()
    dims = imgdata.GetDimensions()
    delete_objects_startswith(node.ob_name, node.export_file_sequence)
    import_volume_object(node.ob_name, filename, bbox, dims, node.generate_material, node.export_file_sequence)


class BVTK_Node_VTKToOpenVDBExporter(Node, BVTK_Node):
    """Convert image data from VTK Node to OpenVDB Exporter JSON file"""

    bl_idname = "BVTK_Node_VTKToOpenVDBExporterType"
    bl_label = "VTK To OpenVDB Exporter"

    ob_name: bpy.props.StringProperty(
        name="Name", default="volume", update=BVTK_Node.outdate_vtk_status
    )
    density_name: bpy.props.StringProperty(
        name="Density Field Name", default="", update=BVTK_Node.outdate_vtk_status
    )
    color_name: bpy.props.StringProperty(
        name="Color Field Name", default="", update=BVTK_Node.outdate_vtk_status
    )
    flame_name: bpy.props.StringProperty(
        name="Flame Field Name", default="", update=BVTK_Node.outdate_vtk_status
    )
    temperature_name: bpy.props.StringProperty(
        name="Temperature Field Name", default="", update=BVTK_Node.outdate_vtk_status
    )

    def m_properties(self):
        return [
            "ob_name",
            "density_name",
            "color_name",
            "flame_name",
            "temperature_name",
        ]

    def m_connections(self):
        return (["input"], [], [], [])

    def apply_properties_special(self):
        """Export vtkImageData into OpenVDB Volume data"""
        (
            input_node,
            vtk_output_obj,
            vtk_connection,
        ) = self.get_input_node_and_output_vtk_objects()
        if not vtk_output_obj:
            self.ui_message = "Error: No VTK data on input!"
            return "error"

        if not issubclass(vtk_output_obj.__class__, vtk.vtkImageData):
            self.ui_message = "Error: Input is not vtkImageData!"
            return "error"
        dims = vtk_image_data_to_openvdb_export(self, vtk_output_obj)
        self.ui_message = "Exported dimensions: %s" % str(dims)
        update_3d_view()
        l.debug("Exported OpenVDB data for %r" % self.ob_name)
        return "up-to-date"

    def init_vtk(self):
        self.set_vtk_status("out-of-date")
        return None


def vtk_image_data_to_openvdb_export(node, imgdata):
    """Create text export files from vtkImageData for convert_to_vdb.py script"""

    background_value = 0.0  # Zero value for OpenVDB grid

    density_data = create_data_from_data_array(
        imgdata, node.density_name, background_value, "scalar"
    )
    color_data = create_data_from_data_array(
        imgdata, node.color_name, background_value, "vector"
    )
    flame_data = create_data_from_data_array(
        imgdata, node.flame_name, background_value, "scalar"
    )
    temperature_data = create_data_from_data_array(
        imgdata, node.temperature_name, background_value, "scalar"
    )

    seq = "_%05d" % bpy.context.scene.frame_current
    basename = node.ob_name + seq + ".json"
    filepath = os.path.join(bpy.path.abspath("//"), basename)
    dims = list(imgdata.GetDimensions())
    export_vdb_data(
        filepath,
        background_value,
        dims,
        density_data,
        color_data,
        flame_data,
        temperature_data,
    )
    l.info("Saved %r (dims %s)" % (filepath, str(dims)))
    return dims


def create_data_from_data_array(imgdata, data_name, background_value, atype):
    """Return array values from vtkImageData"""

    if data_name == "":
        return None

    dims = list(imgdata.GetDimensions())

    if atype == "scalar":
        data = imgdata.GetPointData().GetScalars(data_name)
        if not data:
            raise ValueError("Input data %r not found" % data_name)
    elif atype == "vector":
        data = imgdata.GetPointData().GetVectors(data_name)
        if not data:
            raise ValueError("Input data %r not found" % data_name)
    else:
        raise TypeError("unknown type %s" % str(atype))

    # Create grid by looping over points with accessor
    vals = []
    MAXVAL = 9.999999e37
    for idx in range(dims[0] * dims[1] * dims[2]):
        if atype == "scalar":
            value = data.GetTuple1(idx)
            if value > background_value and value < MAXVAL:
                vals.append(value)
            else:
                vals.append(None)
        elif atype == "vector":
            value = data.GetTuple3(idx)
            vals.append(value)
    return vals


def export_vdb_data(
    filepath,
    background_value,
    dims,
    density_data,
    color_data,
    flame_data,
    temperature_data,
):
    """Exports data objects to JSON file."""

    import json

    data = (
        background_value,
        dims,
        density_data,
        color_data,
        flame_data,
        temperature_data,
    )
    with open(filepath, "w") as outfile:
        json.dump(data, outfile)


# -----------------------------------------------------------------------------
# Help functions
# -----------------------------------------------------------------------------


def mesh_and_object(name):
    """Get mesh object and mesh"""
    me = get_item(bpy.data.meshes, name)
    ob = get_object(name, me)
    return me, ob


def get_item(data, *args):
    """Get or create item with key args[0] from data"""
    item = data.get(args[0])
    if not item:
        item = data.new(*args)
    return item


def set_link(data, item):
    """Link item to data"""
    if item.name not in data:
        data.link(item)


def get_object(name, data):
    """Initialize mesh object name with data into current scene"""
    ob = get_item(bpy.data.objects, name, data)
    ob.data = data
    set_link(bpy.context.collection.objects, ob)
    return ob


def warn_if_not_exist_object(name):
    """Return warning if argument object name does not exist"""
    if not name in bpy.data.objects:
        return "Object %r does not exist!" % name


def create_material(ob, texture_name=None):
    """Create default material for final output node mesh object.
    Add image coloring nodes if texture name is given.
    """

    if ob.name in bpy.data.materials:
        mat = bpy.data.materials[ob.name]
    else:
        mat = bpy.data.materials.new(name=ob.name)
    if not mat.use_nodes:
        mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Delete existing nodes
    for i in nodes:
        nodes.remove(i)

    node1 = nodes.new("ShaderNodeOutputMaterial")
    node1.location = (300, 300)

    node2 = nodes.new("ShaderNodeBsdfPrincipled")
    node2.location = (0, 300)
    links.new(node2.outputs["BSDF"], node1.inputs["Surface"])

    # Add UV related nodes for colored materials
    if texture_name:
        node3 = nodes.new("ShaderNodeTexImage")
        node3.image = bpy.data.images[texture_name]
        node3.location = (-300, 300)
        links.new(node3.outputs["Color"], node2.inputs["Base Color"])
        links.new(node3.outputs["Alpha"], node2.inputs["Alpha"])

        node4 = nodes.new("ShaderNodeMapping")
        node4.location = (-700, 300)
        links.new(node4.outputs["Vector"], node3.inputs["Vector"])

        node5 = nodes.new("ShaderNodeTexCoord")
        node5.location = (-900, 300)
        links.new(node5.outputs["UV"], node4.inputs["Vector"])

    # Assign material
    if ob.data.materials:
        ob.data.materials[0] = mat
    else:
        ob.data.materials.append(mat)


def image_from_ramp(ramp, name, length):
    """Create image (size 4 px) from color ramp"""
    # Blender requires minimum image dimension 3 px to correctly
    # show up images longer than 256 pixels. Bug is reported:
    # https://developer.blender.org/T65309
    # Use height 4 px to ease viewing color ramp in Image Editor
    height = 4
    img = get_item(bpy.data.images, name, length, height)
    for j in range(length):
        for i, val in enumerate(ramp.evaluate(j / length)):
            for k in range(height):
                img.pixels[height * k * length + height * j + i] = val
    # Pack color ramp image so it will be saved with blend file,
    # to show it correctly when blend file is reloaded
    img.pack()

    # TODO: Delete below
    # p.extend(ramp.evaluate(j/length))
    # img.pixels = p
    # return img


def face_unwrap(bm, vtk_obj, array_name, vrange):
    """Unwrap by cell data"""

    array_data = get_vtk_array_data(vtk_obj, array_name, array_type="C")
    num_comps = array_data.GetNumberOfComponents()
    minr, maxr = vrange
    uv_layer = bm.loops.layers.uv.verify()
    for face in bm.faces:
        for loop in face.loops:
            tup = array_data.GetTuple(face.index)
            v = 0.0
            # Get Euclidean norm (magnitude) of the data vector.
            # Leave scalars unchanged.
            if num_comps == 1:
                v = tup[0]
            else:
                for i in range(num_comps):
                    v += tup[i] ** 2
                v = v ** 0.5
            v = (v - minr) / (maxr - minr)
            v = min(0.999, max(0.001, v))  # Force value inside range
            loop[uv_layer].uv = (v, 0.5)
    return bm, None


def point_unwrap(bm, vtk_obj, array_name, vrange, vimap):
    """Unwrap by point data"""

    array_data = get_vtk_array_data(vtk_obj, array_name, array_type="P")
    num_comps = array_data.GetNumberOfComponents()
    minr, maxr = vrange
    uv_layer = bm.loops.layers.uv.verify()
    for face in bm.faces:
        for loop in face.loops:
            tup = array_data.GetTuple(vimap[loop.vert.index])
            v = 0.0
            # Get Euclidean norm (magnitude) of the data vector.
            # Leave scalars unchanged.
            if num_comps == 1:
                v = tup[0]
            else:
                for i in range(num_comps):
                    v += tup[i] ** 2
                v = v ** 0.5
            v = (v - minr) / (maxr - minr)
            v = min(0.999, max(0.001, v))  # Force value inside range
            loop[uv_layer].uv = (v, 0.5)
    return bm, None


def get_vtk_array_data(vtk_obj, array_name, array_type="P"):
    """Get VTK data array from data set with given name and type (point or
    cell data)
    """
    if not vtk_obj:
        return None
    if array_type in ("P", "p"):
        data = vtk_obj.GetPointData()
    elif array_type in ("C", "c"):
        data = vtk_obj.GetCellData()
    else:
        raise ValueError("Unknown array type %r" % array_type)

    for i in range(data.GetNumberOfArrays()):
        name = str(data.GetArrayName(i))
        if name == array_name:
            return data.GetArray(i)


# -----------------------------------------------------------------------------
# Color legend
# -----------------------------------------------------------------------------


def text(name, body):
    """Get a text data block"""
    font = get_item(bpy.data.curves, name, "FONT")
    ob = get_object(name, font)
    font.body = body
    return ob


def delete_texts(name):
    """Delete text data block"""
    for ob in bpy.data.objects:
        if ob.name.startswith(name):
            curve = ob.data
            bpy.data.objects.remove(ob)
            bpy.data.curves.remove(curve)


def create_lut(
    name, vrange, n_div, texture, b=0.5, h=5.5, x=5, y=0, z=0, fontsize=0.35, roundto=2
):
    """Create value labels and color legends and add to current scene"""
    name = name + "_colormap"
    delete_texts(name + "_lab")  # Delete old labels

    # Create plane and UVs
    plane = bmesh.new()
    plane.faces.new(
        (
            plane.verts.new((0, 0, 0)),
            plane.verts.new((b, 0, 0)),
            plane.verts.new((b, 0, h)),
            plane.verts.new((0, 0, h)),
        )
    )
    uv_layer = plane.loops.layers.uv.verify()
    plane.faces.ensure_lookup_table()
    plane.faces[0].loops[0][uv_layer].uv = (0, 1)
    plane.faces[0].loops[1][uv_layer].uv = (0, 0)
    plane.faces[0].loops[2][uv_layer].uv = (1, 0)
    plane.faces[0].loops[3][uv_layer].uv = (1, 1)
    me, ob = mesh_and_object(name)
    plane.to_mesh(me)
    ob.location = x, y, z
    # texture_material(me, name, texture)

    # Calculate label interval
    min, max = vrange
    if min > max or h <= 0:
        l.error("vrange maximum greater than minimum")
        return
    import math

    idealspace = (max - min) / (h)
    exponent = math.floor(math.log10(idealspace))
    mantissa = idealspace / (10 ** exponent)
    if mantissa < 2.5:
        step = 10 ** exponent
    elif mantissa < 7.5:
        step = 5 * 10 ** exponent
    else:
        step = 10 * 10 ** exponent
    start = math.ceil(min / step) * step
    delta = max - min
    if step > delta:
        return
    starth = (h * (start - min)) / delta
    steph = (h * step) / delta

    # Add labels as texts
    for i in range(int(math.floor((max - start) / step)) + 1):
        t = text(name + "_lab" + str(i), "{:.15}".format(float(start + i * step)))
        t.data.size = fontsize
        t.rotation_mode = "XYZ"
        t.rotation_euler = (1.5707963705062866, 0.0, 0.0)
        t.location = b + b / 5, 0, starth + steph * i
        t.parent = ob


# -----------------------------------------------------------------------------
#  Image data conversion
# -----------------------------------------------------------------------------


class BVTK_Node_VTKToBlenderImage(Node, BVTK_Node):
    """Convert vtkImageData output into a Blender Image Texture.
    """

    bl_idname = "BVTK_Node_VTKToBlenderImageType"  # type name
    bl_label = "VTK To Blender Image"  # label for nice name display

    m_Name: bpy.props.StringProperty(
        name="Image Name", default="vtk_image", update=BVTK_Node.outdate_vtk_status
    )
    field_name: bpy.props.StringProperty(
        name="Field Name", default="", update=BVTK_Node.outdate_vtk_status
    )

    def m_properties(self):
        return ["m_Name", "field_name"]

    def m_connections(self):
        return (["input"], [], [], [])

    def draw_buttons_special(self, context, layout):
        """Custom draw buttons function, to show force update button.
        """
        layout.prop(self, "m_Name")
        layout.prop(self, "field_name")
        layout.operator("node.bvtk_node_force_update_upstream").node_path = node_path(
            self
        )

    def apply_properties_special(self):
        """Generate Blender image from VTK Image Data"""
        (
            input_node,
            vtk_output_obj,
            vtk_connection,
        ) = self.get_input_node_and_output_vtk_objects()
        val = image_data_to_blender(vtk_output_obj, self.m_Name, self.field_name)
        if val:
            self.ui_message = val
            return "error"
        update_3d_view()
        return "up-to-date"

    def init_vtk(self):
        self.set_vtk_status("out-of-date")
        return None


def image_data_to_blender(vtk_data, name, field_name):
    """Convert vtkImageData to a Blender Image"""

    if not vtk_data:
        return "No VTK object on input"
    if not issubclass(vtk_data.__class__, vtk.vtkImageData):
        return "Input type is not VTK Image Data"

    # Determine which axis indices produce a 2D image
    dim = vtk_data.GetDimensions()
    if sum(dim) < 4:
        return "Image data is missing resolution (sum(dim) was %d)" % sum(dim)
    if dim[0] == 1:
        dim1 = 1
        dim2 = 2
    elif dim[1] == 1:
        dim1 = 0
        dim2 = 2
    else:
        dim1 = 0
        dim2 = 1

    if name in bpy.data.images:
        bpy.data.images.remove(bpy.data.images[name])
    img = bpy.data.images.new(name, dim[dim1], dim[dim2])

    scalars = vtk_data.GetPointData().GetScalars(field_name)
    if not scalars:
        return "Did not find data in input point data"
    n_tuples = scalars.GetNumberOfTuples()
    pixels = []
    for j in range(n_tuples):
        vals = scalars.GetTuple(j)
        if len(vals) == 1:
            pixels.extend([vals[0], vals[0], vals[0], 1])
        else:
            alpha = 1 if len(vals) < 4 else vals[3]
            pixels.extend([vals[0], vals[1], vals[2], alpha])

    img.pixels = pixels


# Old image data converter for the original VTK To Blender node


def imgdata_to_blender(data, name):
    """Convert vtkImageData to a Blender image"""

    wm = bpy.context.window_manager
    scalars = data.GetPointData().GetScalars()

    # Generate image data to img
    dim = data.GetDimensions()
    z = 0
    wm.progress_begin(0, 100)
    if name in bpy.data.images:
        bpy.data.images.remove(bpy.data.images[name])
    img = bpy.data.images.new(name, dim[0], dim[1])
    n_tuples = scalars.GetNumberOfTuples()
    p = []
    prog = 0
    l_prog = 1
    for j in range(n_tuples):
        t = scalars.GetTuple(j)
        if len(t) == 1:
            p.extend([t[0] / 255, t[0] / 255, t[0] / 255, 1])
        else:
            alpha = 1 if len(t) < 4 else t[3] / 255
            p.extend([t[0] / 255, t[1] / 255, t[2] / 255, alpha])

        prog = int(j / n_tuples * 100)
        if prog != l_prog:
            l_prog = prog
            wm.progress_update(prog)
            l.debug("Converting to img: " + str(prog) + "%")
    img.pixels = p
    wm.progress_end()
    l.info("Image data conversion succesful, num pixels = " + str(n_tuples))

    # Create plane mesh with UVs to show the image
    spacing = data.GetSpacing()
    x = dim[0] * spacing[0]
    y = dim[1] * spacing[0]
    plane = bmesh.new()
    plane.faces.new(
        (
            plane.verts.new((0, 0, 0)),
            plane.verts.new((x, 0, 0)),
            plane.verts.new((x, y, 0)),
            plane.verts.new((0, y, 0)),
        )
    )
    uv_layer = plane.loops.layers.uv.verify()
    plane.faces.ensure_lookup_table()
    plane.faces[0].loops[0][uv_layer].uv = (0, 0)
    plane.faces[0].loops[1][uv_layer].uv = (1, 0)
    plane.faces[0].loops[2][uv_layer].uv = (1, 1)
    plane.faces[0].loops[3][uv_layer].uv = (0, 1)
    me, ob = mesh_and_object(name)
    ob.location = data.GetOrigin()
    plane.to_mesh(me)
    # tex, mat = texture_material(me, 'VTK' + name)
    # mat.use_shadeless = True
    # tex.image = img


# Add classes and menu items
TYPENAMES = []
# Disabled legacy mesh output node, it's not upgraded to new core.py.
# You can use VTK To Blender Mesh node instead.
# add_class(BVTK_Node_VTKToBlender)
# TYPENAMES.append('BVTK_Node_VTKToBlenderType')
add_class(BVTK_Node_VTKToBlenderMesh)
TYPENAMES.append("BVTK_Node_VTKToBlenderMeshType")
add_class(BVTK_OT_InitializeParticleSystem)
add_class(BVTK_Node_VTKToBlenderParticles)
TYPENAMES.append("BVTK_Node_VTKToBlenderParticlesType")
add_class(BVTK_Node_VTKToBlenderImage)
TYPENAMES.append("BVTK_Node_VTKToBlenderImageType")

add_class(BVTK_Node_VTKToBlenderVolume)
TYPENAMES.append('BVTK_Node_VTKToBlenderVolumeType')
add_class(BVTK_Node_VTKToOpenVDBExporter)
TYPENAMES.append("BVTK_Node_VTKToOpenVDBExporterType")
menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(BVTK_NodeCategory("Converters", "Converters", items=menu_items))
