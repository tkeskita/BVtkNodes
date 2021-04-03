# <pep8 compliant>

#---------------------------------------------------------------------------------
# ADDON HEADER SECTION
#---------------------------------------------------------------------------------

bl_info = {
    "name": "BVTKNodes, Blender VTK Nodes",
    "author": "Silvano Imboden, Lorenzo Celli, Paul McManus, Tuomo Keskitalo",
    "version": (0, 6),
    "blender": (2, 83,  0),
    "location": "BVTK Node Tree Editor > New",
    "description": "Create and execute VTK pipelines in Blender Node Editor",
    "warning": "Experimental",
    "wiki_url": "https://github.com/tkeskita/BVtkNodes",
    "tracker_url": "https://github.com/tkeskita/BVtkNodes/issues",
    "support": 'COMMUNITY',
    "category": "Node",
    }

# Note: See core.py on how to set up Python Logging to see debug messages

# OPEN ISSUES
# - Currently it is not possible to use Blender 2.8 animation system
#   to animate BVTKNodes properties. This is due to bug in Blender,
#   and it has been previously reported at
#   https://developer.blender.org/T66392
# - generate/vtk_info_modified.py is not used, should it be deleted?
# - continue development of node_tree_from_py at some point?
# - cone.json example raises a lot of vtkInformation request errors on
#   first run, but still works, and later updates do not produce errors
# - Color Mapper color_by produces RNA warnings due to empty list
#   until input nodes generate the list
# - Generate Scalar Bar in Color Mapper is not working correctly.
#
# IDEAS FOR FUTURE DEVELOPMENT
#
# - Calculator Node: use vtkExpression evaluator
# - Blender To VTK Node: A BVTK node which converts Blender mesh into
#   vtkPolyData. Alternatively add vtkBlendReader to VTK?
#   Or maybe vtkAlembicReader to VTK? https://www.alembic.io/
# - Support for several VTK versions in one add-on. Would require making
#   gen_VTK*.py, VTK*.py and b_properties dependent on specific VTK version
#   and easy switch between versions.
# - Time subranges for temporal averaged analysis
# - Better access to OpenFOAM Reader settings, like selection of
#   regions and different data arrays


# Import VTK Python module or exit immediately
try:
    import vtk
except:
    pass

try:
    dir(vtk)
except:
    message = '''
    BVTKNodes add-on failed to access the VTK library. You must
    compile and install Python library corresponding to the Python
    library version used by Blender, and then compile and install
    VTK on top of it. Finally you must customize environment variables
    to use the compiled Python library before starting Blender.
    Please refer to BVTKNodes documentation for help.
    '''
    raise Exception(message)

need_reloading = "bpy" in locals()

if need_reloading:
    import importlib

    importlib.reload(update)
    importlib.reload(core)
    importlib.reload(cache)
    importlib.reload(b_properties)
    importlib.reload(showhide_properties)
    importlib.reload(tree)
    importlib.reload(b_inspect)
    importlib.reload(colormap)
    importlib.reload(customfilter)
    importlib.reload(info)
    # importlib.reload(favorites_data)
    importlib.reload(favorites)
    importlib.reload(converters)

    importlib.reload(generated_nodes.gen_VTKSources)
    importlib.reload(custom_nodes.VTKSources)

    importlib.reload(generated_nodes.gen_VTKReaders)
    importlib.reload(custom_nodes.VTKReaders)

    importlib.reload(generated_nodes.gen_VTKWriters)
    importlib.reload(custom_nodes.VTKWriters)
    
    importlib.reload(generated_nodes.gen_VTKFilters1)
    importlib.reload(generated_nodes.gen_VTKFilters2)
    importlib.reload(generated_nodes.gen_VTKFilters)
    importlib.reload(custom_nodes.VTKFilters)

    importlib.reload(generated_nodes.gen_VTKTransform)
    importlib.reload(generated_nodes.gen_VTKImplicitFunc)
    importlib.reload(generated_nodes.gen_VTKParametricFunc)
    importlib.reload(generated_nodes.gen_VTKIntegrator)

    importlib.reload(custom_nodes.VTKOthers)

else:
    import bpy
    from   bpy.app.handlers import persistent
    import nodeitems_utils
    from   nodeitems_utils import NodeItem

    from . import core
    from . import cache
    from . import b_properties
    from . import showhide_properties
    from . import b_inspect
    from . import favorites
    from . import tree
    from . import colormap
    from . import customfilter
    from . import info
    from . import update
    from . import converters

    from .custom_nodes import VTKSources
    from .custom_nodes import VTKReaders
    from .custom_nodes import VTKWriters
    from .custom_nodes import VTKFilters
    
    from .custom_nodes import VTKOthers

from .core import l # Import logging

if need_reloading:
    l.debug("Reloaded modules")
else:
    l.debug("Initialized modules")

l.info("Loaded VTK version: " + vtk.vtkVersion().GetVTKVersion())
l.info("VTK base path: " + vtk.__file__)


@persistent
def on_file_loaded(scene):
    '''Initialize cache after a blender file open'''
    cache.BVTKCache.init()

@persistent
def compareGeneratedAndCurrentVTKVersion():
    '''Check if the vtk version with which the files were generated is equal to the current vtk version and log a warning if not'''
    import re
    import os
    from .generated_nodes import gen_VTKFilters

    vtk_re = re.compile("^\# VTK version\: (\S*).*$")

    gen_vtk_path = os.path.abspath(gen_VTKFilters.__file__)
    gen_vtk_f = open(gen_vtk_path, 'r')
    lines = gen_vtk_f.readlines()
    vtk_version = vtk.vtkVersion().GetVTKVersion()
    gen_vtk_version = None

    # Strips the newline character
    for line in lines:
        matches = vtk_re.match(line)

        if matches is not None:
            gen_vtk_version = matches.group(1)
            break

    if gen_vtk_version is None:
        l.warning("Warning: Generated VTK file did not provide a VTK version")

    elif gen_vtk_version != vtk_version :
        l.warning("Warning: Generated VTK file has version %s, but blender's VTK version is %s" % (gen_vtk_version, vtk_version))

compareGeneratedAndCurrentVTKVersion()

converters_list = ['BVTK_Node_VTKToBlenderType', 'BVTK_Node_VTKToBlenderMeshType', 
        'BVTK_Node_VTKToBlenderVolumeType', 'BVTK_Node_VTKToBlenderParticlesType']

def backtrack_converter_nodes(root_node):
    '''Searches all converter nodes and returns a list of them
    '''
    all_outputs = root_node.outputs

    found_converter_nodes = []
    for output in all_outputs:
        links = output.links
        for link in links:
            output_node = link.to_socket.node
            if output_node.bl_idname in converters_list:
                found_converter_nodes += [output_node]
            else:
                found_converter_nodes += backtrack_converter_nodes(output_node)

    return found_converter_nodes

@persistent
def on_frame_change(scene, depsgraph):
    '''Updates done after frame (time step) changes'''

    nodes_2b_updated = set()

    # Update Time Selectors
    for node_group in bpy.data.node_groups:
        for node in node_group.nodes:
            # Set frame number directly from Blender timeline.
            # Note: This is a workaround to enable transient data traversal
            # while this issue remains: https://developer.blender.org/T66392
            if node.bl_idname == 'BVTK_Node_TimeSelectorType' and node.use_scene_time:
                node.time_step = scene.frame_current
                l.debug("TimeSelector time step %d" % node.time_step)
                connected_converter_nodes = backtrack_converter_nodes(node)
                #Append, ignoring duplicates
                nodes_2b_updated = nodes_2b_updated.union(set(connected_converter_nodes))

            elif node.bl_idname == 'BVTK_Node_GlobalTimeKeeperType':
                updated_nodes = node.set_new_time(scene.frame_current)
                connected_converter_nodes = [backtrack_converter_nodes(node) for node in updated_nodes]
                l.debug("Global Time Keeper time step %d" % node.global_time)

                #Append, ignoring duplicates
                for conv_nodes in connected_converter_nodes:
                    nodes_2b_updated = nodes_2b_updated.union(set(conv_nodes))

    # Update mesh objects
    for node in nodes_2b_updated:
        try:
            if node.bl_idname == 'BVTK_Node_VTKToBlenderType':
                l.debug("Animation: Updating VTKToBlender")
                update.no_queue_update(node, node.update_cb)
            elif node.bl_idname == 'BVTK_Node_VTKToBlenderMeshType':
                l.debug("Animation: Updating VTKToBlenderMesh")
                update.no_queue_update(node, node.update_cb)
            elif node.bl_idname == 'BVTK_Node_VTKToBlenderVolumeType':
                l.debug("Animation: Updating VTKToBlenderVolume")
                converters.delete_objects_startswith(node.ob_name)
                update.no_queue_update(node, node.update_cb)

            # Update particle objects
            elif node.bl_idname == 'BVTK_Node_VTKToBlenderParticlesType':
                l.debug("VTKToBlenderParticles")
                update.no_queue_update(node, node.update_cb)
                node.update_particle_system(depsgraph)
            
            else:
                l.warning("on_frame_change: Converter nodes " + str(node) + " was found during backtracking but was not updated")
        except Exception as ex:
            #An error message will be logged, but we can't display an error here in the UI
            err_str = "Animation: Update of %s failed with ex: %s" % (node, ex)
            l.error(err_str)





@persistent
def on_depsgraph_update(scene, depsgraph):
    '''Updates done after depsgraph changes'''

    # Update particle objects
    for node_group in bpy.data.node_groups:
        for node in node_group.nodes:
            if node.bl_idname == 'BVTK_Node_VTKToBlenderParticlesType':
                l.debug("VTKToBlenderParticles")
                node.update_particle_system(depsgraph)



def custom_register_node_categories():
    '''Custom registering of node categories to prevent node categories to
    be shown on the tool-shelf
    '''

    identifier = "VTK_NODES"
    cat_list = core.CATEGORIES

    if identifier in nodeitems_utils._node_categories:
        raise KeyError("Node categories list '%s' already registered" % identifier)
        return

    def draw_node_item(self, context):
        layout = self.layout
        col = layout.column()
        for item in self.category.items(context):
            item.draw(item, col, context)

    def draw_add_menu(self, context):
        layout = self.layout
        for cat in cat_list:
            if cat.poll(context):
                layout.menu("NODE_MT_category_%s" % cat.identifier)

    menu_types = []
    for cat in cat_list:
        menu_type = type(\
            "NODE_MT_category_" + cat.identifier, (bpy.types.Menu,), {
                "bl_space_type": 'NODE_EDITOR',
                "bl_label": cat.name,
                "category": cat,
                "poll": cat.poll,
                "draw": draw_node_item,
            })
        menu_types.append(menu_type)
        bpy.utils.register_class(menu_type)

    nodeitems_utils._node_categories[identifier] = \
        (cat_list, draw_add_menu, menu_types, []) # , panel_types)


def register():
    '''Register function. CLASSES and CATEGORIES are defined in core.py and
    filled in all the gen_VTK*.py and VTK*.py files
    '''
    bpy.app.handlers.load_post.append(on_file_loaded)
    bpy.app.handlers.frame_change_post.append(on_frame_change)
    bpy.app.handlers.depsgraph_update_post.append(on_depsgraph_update)
    core.check_b_properties() # delayed to here to allow class overriding
    for c in core.UI_CLASSES:
        try:
            bpy.utils.register_class(c)
        except:
            l.critical('error registering ' + str(c))
    # TODO: May register priority queue
    for c in sorted(core.CLASSES.keys()):
        try:
            bpy.utils.register_class(core.CLASSES[c])
        except:
            l.critical('error registering ' + str(c))
    custom_register_node_categories()

def unregister():
    nodeitems_utils.unregister_node_categories("VTK_NODES")
    for c in reversed(sorted(core.CLASSES.keys())):
        bpy.utils.unregister_class(core.CLASSES[c])
    for c in reversed(core.UI_CLASSES):
        bpy.utils.unregister_class(c)
    bpy.app.handlers.load_post.remove(on_file_loaded)
    bpy.app.handlers.frame_change_post.remove(on_frame_change)
            
