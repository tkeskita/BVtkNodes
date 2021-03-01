from ..generated_nodes.gen_VTKFilters1 import *
from ..generated_nodes.gen_VTKFilters2 import *
from ..generated_nodes.gen_VTKFilters  import *
from ..core import show_custom_code, run_custom_code

class BVTK_PG_ValueSettings(bpy.types.PropertyGroup):
    '''Property Group for float array of variable size'''
    value: bpy.props.FloatProperty(default = 0)

add_ui_class(BVTK_PG_ValueSettings)

# -----------------------------------------------------------------------------

class BVTK_ContourHelper:
    '''Base class for filters which use variable number of discrete
    data values for input, similar to vtkCountourFilter.
    '''
    m_ContourValues: bpy.props.CollectionProperty(type=BVTK_PG_ValueSettings)

    @show_custom_code
    def draw_buttons(self, context, layout):
        m_properties = self.m_properties()
        for i in range(len(m_properties)):
            if self.b_properties[i]:
                prop = m_properties[i]
                if prop == 'm_ContourValues':
                    prop = getattr(self, prop)
                    prop_path = node_prop_path(self, 'm_ContourValues')
                    row = layout.row()
                    op = row.operator('node.bvtk_update_collection', text='', icon='ZOOM_IN')
                    op.prop_path = prop_path
                    op.add = True
                    row.label(text='Contour values')
                    for i, item in enumerate(self.m_ContourValues):
                        row = layout.row(align=True)
                        op = row.operator('node.bvtk_update_collection', text='', icon='ZOOM_OUT')
                        op.prop_path = prop_path
                        op.add = False
                        op.index = i
                        row.prop(item, 'value')
                else:
                    layout.prop(self, prop)

    @run_custom_code
    def apply_properties(self, vtkobj):
        m_properties = self.m_properties()
        for x in [m_properties[i] for i in range(len(m_properties)) if self.b_properties[i]]:
            if x == 'm_ContourValues':
                vtkobj.SetNumberOfContours(0)
                i = 0
                for item in self.m_ContourValues:
                    vtkobj.SetValue(i, item.value)
                    i += 1
            else:
                cmd = 'vtkobj.Set' + x[2:] + '(self.' + x + ')'
                exec(cmd, globals(), locals())

    def special_properties(self):
        return [x.value for x in self.m_ContourValues]

    def export_properties(self):
        '''Export properties'''
        return {'m_ContourValues':[x.value for x in self.m_ContourValues]}

    def import_properties(self, dict):
        '''Import properties'''
        values = dict['m_ContourValues']
        for i, val in enumerate(values):
            if i < len(self.m_ContourValues):
                self.m_ContourValues[i].value = val
            else:
                item = self.m_ContourValues.add()
                item.value = val


class BVTK_OT_UpdateCollection(bpy.types.Operator):
    '''Operator to update collection'''
    bl_idname = "node.bvtk_update_collection"
    bl_label = "Update"

    index: bpy.props.IntProperty(default = 0)
    value: bpy.props.FloatProperty()
    prop_path: bpy.props.StringProperty()
    add: bpy.props.BoolProperty(default=True)

    def execute(self, context):
        prop = eval(self.prop_path)
        if self.add:
            item = prop.add()
            item.value = self.value
        else:
            prop.remove(self.index)
        return {'FINISHED'}

add_ui_class(BVTK_OT_UpdateCollection)

# -----------------------------------------------------------------------------

class VTKContourFilter(BVTK_ContourHelper, Node, BVTK_Node):
    '''Manually modified version of VTK Contour Filter'''
    bl_idname = 'VTKContourFilterType'
    bl_label = 'vtkContourFilter'

    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True)
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True)
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True)
    m_GenerateTriangles: bpy.props.BoolProperty(name='GenerateTriangles', default=True)
    m_ArrayComponent: bpy.props.IntProperty(name='ArrayComponent', default=0)
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1)

    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_GenerateTriangles', 'm_ArrayComponent',
                'm_NumberOfContours', 'm_ContourValues']

    def m_connections(self):
        return (['input'], ['output'], [], [])

add_class(VTKContourFilter)

# -----------------------------------------------------------------------------

class VTKMarchingCubes(BVTK_ContourHelper, Node, BVTK_Node):
    '''Manually modified version of VTK Marching Cubes'''
    bl_idname = 'VTKMarchingCubesType'
    bl_label = 'vtkMarchingCubes'

    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True)
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True)
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True)
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1)

    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars',
                'm_NumberOfContours', 'm_ContourValues']

    def m_connections(self):
        return (['input'], ['output'], [], [])

add_class(VTKMarchingCubes)

# -----------------------------------------------------------------------------

class VTKAppendFilter(Node, BVTK_Node):
    '''Manually modified version of VTK Append Filter, to handle multiple
    inputs correctly
    '''
    bl_idname = 'VTKAppendFilterType'
    bl_label = 'vtkAppendFilter'

    m_MergePoints        : bpy.props.BoolProperty ( name='MergePoints',         default=True )
    m_ToleranceIsAbsolute: bpy.props.BoolProperty ( name='ToleranceIsAbsolute', default=True )
    m_Tolerance          : bpy.props.FloatProperty( name='Tolerance',           default=0.0 )

    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_MergePoints', 'm_ToleranceIsAbsolute', 'm_Tolerance']

    def m_connections(self):
        return (['input'], ['output'], [], [])

    def setup(self):
        self.inputs['input'].link_limit = 300

    def apply_inputs(self, vtkobj):
        added = [vtkobj.GetInputConnection(0, i) for i in range(vtkobj.GetNumberOfInputConnections(0))]
        toadd = []
        for node, in_obj in self.get_input_nodes('input'):
            toadd.append(in_obj)
            if in_obj not in added:
                vtkobj.AddInputConnection(in_obj)

        for obj in added:
            if obj not in toadd:
                vtkobj.RemoveInputConnection(0, obj)


add_class(VTKAppendFilter)
TYPENAMES.append('VTKAppendFilterType')

# -----------------------------------------------------------------------------


class VTKThreshold(Node, BVTK_Node):
    '''Manually created node to provide vtkThreshold.
    Provides just the ThresholdBetween(value1,value2) mode.
    To do ThresholdByUpper set value1 to -inf.
    To do ThresholdByLower set value2 to +inf.
    User must specify the name and type (point or cell data)
    of the input attribute.
    '''
    bl_idname = 'VTKThresholdType'
    bl_label = 'vtkThreshold'

    e_AttrType_items=[ (x,x,x) for x in ['PointData', 'CellData']]

    m_Value1:     bpy.props.FloatProperty  (name='Low Value', default=float("-inf") )
    m_Value2:     bpy.props.FloatProperty  (name='High Value', default=float("inf") )
    m_AttrName:   bpy.props.StringProperty (name='Attribute Name', default='' )
    e_AttrType:   bpy.props.EnumProperty   (name='Attribute Type', default='PointData', items=e_AttrType_items )

    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Value1', 'm_Value2', 'm_AttrName', 'e_AttrType']

    def m_connections(self):
        return (['input'], ['output'], [], [])

    @run_custom_code
    def apply_properties(self, vtkobj):
        value1 = self.m_Value1
        value2 = self.m_Value2
        attr_name = self.m_AttrName
        attr_type = vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS
        if self.e_AttrType == 'CellData':
            attr_type = vtk.vtkDataObject.FIELD_ASSOCIATION_CELLS

        vtkobj.ThresholdBetween(value1, value2)

        # Previously in VTK, to get a threshold with respect to a given
        # attribute you needed to place it as the current scalars.
        # Nowadays user must indicate on which array the filter should operate.
        # This idiom is becoming more and more used in VTK.
        vtkobj.SetInputArrayToProcess(0, 0, 0, attr_type, attr_name)

add_class(VTKThreshold)
TYPENAMES.append('VTKThresholdType')


#--------------------------------------------------------------
class VTKBoxClipDataSet(Node, BVTK_Node):
    '''Manually modified version of vtkBoxClipDataSet.
    Exposes the BoxClip property.
    '''
    bl_idname = 'VTKBoxClipDataSetType'
    bl_label  = 'vtkBoxClipDataSet'
    
    m_GenerateClipScalars  : bpy.props.BoolProperty( name='GenerateClipScalars',   default=True )
    m_GenerateClippedOutput: bpy.props.BoolProperty( name='GenerateClippedOutput', default=True )
    m_Orientation          : bpy.props.IntProperty ( name='Orientation',           default=1 )
    m_BoxClip              : bpy.props.FloatVectorProperty ( name='BoxClip',          default=[0.,1.0,0.,1.0,0.0,1.0], size=6)

    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateClipScalars','m_GenerateClippedOutput','m_Orientation','m_BoxClip',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], [], []) 
    
    @run_custom_code
    def apply_properties(self, vtkobj):
        m_properties=self.m_properties()
        for x in [m_properties[i] for i in range(len(m_properties)) if self.b_properties[i]]:
            # Skip setting any empty values
            inputval = getattr(self, x)
            if len(str(inputval)) == 0:
                continue
            # SetX(*self.Y)
            if 'BoxClip' in x:
                cmd = 'vtkobj.Set'+x[2:]+'(*self.'+x+')'
            # SetX(self.Y)
            else:
                cmd = 'vtkobj.Set'+x[2:]+'(self.'+x+')'
            exec(cmd, globals(), locals())


add_class( VTKBoxClipDataSet )        
TYPENAMES.append('VTKBoxClipDataSetType' )


# --------------------------------------------------------------
class VTKTransformFilter(Node, BVTK_Node):
    bl_idname = 'VTKTransformFilterType'
    bl_label = 'vtkTransformFilter'

    #m_TransformAllInputVectors: bpy.props.BoolProperty(name='TransformAllInputVectors', default=False)

    #b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    m_Scale: bpy.props.FloatVectorProperty(name='Scale X/Y/Z', default=[1., 1., 1.], size=3)
    m_Rotation: bpy.props.FloatVectorProperty(name='Rotation X/Y/Z', default=[0., 0., 0.],
                                              min=0.,
                                              max=360., size=3)
    m_Translation: bpy.props.FloatVectorProperty(name='Translation X/Y/Z', default=[0., 0., 0.], size=3)
    # m_AttrName:   bpy.props.StringProperty (name='Attribute Name', default='' )
    # e_AttrType:   bpy.props.EnumProperty   (name='Attribute Type', default='PointData', items=e_AttrType_items )

    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Scale', 'm_Rotation', 'm_Translation']

    def m_connections(self):
        return (['input'], ['output'], [], [])

    @run_custom_code
    def apply_properties(self, vtkobj):
        self.vtk_transform = vtk.vtkTransform()
        self.vtk_transform.Scale(*self.m_Scale)
        self.vtk_transform.RotateX(self.m_Rotation[0])
        self.vtk_transform.RotateY(self.m_Rotation[1])
        self.vtk_transform.RotateZ(self.m_Rotation[2])
        self.vtk_transform.Translate(*self.m_Translation)


        vtkobj.SetTransform(self.vtk_transform)
        return
        #TODO: This crashes!
        if self.m_TransformAllInputVectors:
            vtkobj.TransformAllInputVectorsOn()
        else:
            vtkobj.TransformAllInputVectorsOff()


add_class(VTKTransformFilter)
TYPENAMES.append('VTKTransformFilterType')

