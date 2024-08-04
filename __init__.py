# <pep8 compliant>

# ---------------------------------------------------------------------------------
# ADDON HEADER SECTION
# ---------------------------------------------------------------------------------

bl_info = {
    "name": "BVTKNodes, Blender VTK Nodes",
    "author": "BVTKNodes Developers",
    "version": (0, 11),
    "blender": (3, 3, 0),
    "location": "BVTK Node Tree Editor > New",
    "description": "Create and execute VTK pipelines in Blender Node Editor",
    "warning": "Experimental",
    "wiki_url": "https://github.com/tkeskita/BVtkNodes",
    "tracker_url": "https://github.com/tkeskita/BVtkNodes/issues",
    "support": "COMMUNITY",
    "category": "Node",
}

# Nomenclature
# ============
# (BVTK) node = a Blender node object in BVTK node tree
# generated node = VTK node which has been automatically generated
# custom node = customized version of a generated node
# VTK node = a generated or a custom node which implements a VTK class
# special node = all other nodes in BVTK node tree
# socket = Blender socket in a node
# VTK object = instance of vtkObject class
# VTK connection = instance of vtkAlgorithmOutput class

# Note: See core.py on how to set up Python Logging to see debug messages

# IDEAS FOR FUTURE DEVELOPMENT
# - Pass on VTK errors to node.ui_message. How to get VTK error texts?
# - Upgrade vtkSphere to support getting location and scale from
#   Blender Sphere Empty object (similar implementation as for
#   vtkPlane).
# - Add version number to JSON exports and check minimum version number
#   for compatibility before import.
# - Modify core to support multiple inputs, e.g. for
#   vtkAppendFilter.
# - Time Selector to give error for time unaware readers if file does not exist.
#   vtkThreshold to give error if attribute does not exist, and if user
#   provided range is out of data range.
# - Custom Filter should ideally support several inputs and
#   outputs. Also communicate errors to users via self.ui_message. More
#   general approach would be to use special functions specified in text
#   block like init_vtk(), apply_properties_special(),
#   get_vtk_output_object_special(), draw_buttons_special(), ...
# - Edit/Save Custom Code buttons in nodes should ideally work also
#   before running Update. Requires a direct way to get node to the
#   operator without cache information.
# - vtkOpenFOAMReader with Custom Code EnableAllPatchArrays() fails to
#   produce Patches block on first run.
# - Calculator Node: use vtkExpression evaluator?
# - Blender To VTK Node: A BVTK node which converts Blender mesh into
#   vtkPolyData. Alternatively add vtkBlendReader to VTK?
#   Or maybe vtkAlembicReader to VTK? https://www.alembic.io/
# - Support for several VTK versions in one add-on. Would require making
#   gen_VTK*.py, VTK*.py and b_properties dependent on specific VTK version
#   and easy switch between versions.
# - Time subranges for temporal averaged analysis?
# - generate/vtk_info_modified.py is not used, should it be deleted?
# - continue development of node_tree_from_py at some point?


# Import VTK Python module or exit immediately
try:
    import vtk
except:
    pass

try:
    dir(vtk)
except:
    message = """
    BVTKNodes add-on failed to access the VTK library. You must
    compile and install Python library corresponding to the Python
    library version used by Blender, and then compile and install
    VTK on top of it. Finally you must customize environment variables
    to use the compiled Python library before starting Blender.
    Please refer to BVTKNodes documentation for help.
    """
    raise Exception(message)

need_reloading = "bpy" in locals()

if need_reloading:
    import importlib

    importlib.reload(core)
    importlib.reload(b_properties)
    importlib.reload(showhide_properties)
    importlib.reload(tree)
    importlib.reload(b_inspect)
    importlib.reload(colormap)
    importlib.reload(customfilter)
    importlib.reload(info)
    importlib.reload(favorites_data)
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
    from bpy.app.handlers import persistent
    import nodeitems_utils
    from nodeitems_utils import NodeItem

    from . import core
    from . import b_properties
    from . import showhide_properties
    from . import b_inspect
    from . import favorites
    from . import tree
    from . import colormap
    from . import customfilter
    from . import info
    from . import converters

    from .custom_nodes import VTKSources
    from .custom_nodes import VTKReaders
    from .custom_nodes import VTKWriters
    from .custom_nodes import VTKFilters

    from .custom_nodes import VTKOthers

from .core import l  # Import logging

if need_reloading:
    l.debug("Reloaded modules")
else:
    l.debug("Initialized modules")

l.info("Loaded VTK version: " + vtk.vtkVersion().GetVTKVersion())
l.info("VTK base path: " + vtk.__file__)

# Global add-on settings as a property group
class BVTKNodes_Settings(bpy.types.PropertyGroup):
    update_mode: bpy.props.EnumProperty(
        name="Update Mode",
        description="Update Mode for BVTK Node Tree",
        items={
            (
                "no-automatic-updates",
                "No Automatic Updates",
                "Nothing is automatically updated after node changes",
                0,
            ),
            (
                "update-current",
                "Update Current Automatically",
                "Update only the changed node automatically",
                1,
            ),
            (
                "update-all",
                "Update All Automatically",
                "Update changes to all nodes automatically",
                2,
            ),
        },
        default="update-current",
    )

    on_frame_change_is_running: bpy.props.BoolProperty(
        name="on_frame_change() is running",
        description="Internal boolean state to detect whether on_frame_change() is running",
        default=False,
    )

    on_depsgraph_update_is_running: bpy.props.BoolProperty(
        name="on_depsgraph_update() is running",
        description="Internal boolean state to detect whether on_depsgraph_update() is running",
        default=False,
    )

    volume_import_is_running: bpy.props.BoolProperty(
        name="Volume Import is running",
        description="Internal boolean state to detect whether volume import process is running",
        default=False,
    )


@persistent
def on_file_loaded(scene):
    """Initialize cache and VTK objects after Blender file has been opened"""
    l.debug("Triggered")

    # Force guard variable off
    bpy.context.scene.bvtknodes_settings.on_frame_change_is_running = False

    # Reset the node cache
    cache.BVTKCache.reset_cache()

    # Set all nodes out-of-date and remove input connection information
    # to force correct initialization upon first update.
    bvtk_nodes = core.get_all_bvtk_nodes()
    for node in bvtk_nodes:
        node.set_vtk_status("out-of-date")
        node.connected_input_names = ""
        # Update nodeMaxId
        if node.node_id > cache.nodeMaxId:
            cache.nodeMaxId = node.node_id

    # Update if needed
    update_mode = bpy.context.scene.bvtknodes_settings.update_mode
    if update_mode == "update-all":
        cache.BVTKCache.update_all()


@persistent
def compareGeneratedAndCurrentVTKVersion():
    """Check if the vtk version with which the files were generated is equal to the current vtk version and log a warning if not"""
    import re
    import os
    from .generated_nodes import gen_VTKFilters

    vtk_re = re.compile("^\# VTK version\: (\S*).*$")

    gen_vtk_path = os.path.abspath(gen_VTKFilters.__file__)
    gen_vtk_f = open(gen_vtk_path, "r")
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

    elif gen_vtk_version != vtk_version:
        l.warning(
            "Warning: Generated VTK file has version %s, but Blender's VTK version is %s"
            % (gen_vtk_version, vtk_version)
        )


compareGeneratedAndCurrentVTKVersion()


@persistent
def on_frame_change(scene, depsgraph):
    """Updates done after frame number (time step) changes"""

    l.debug(
        "Frame update was triggered at frame %d (Update Mode %r)"
        % (scene.frame_current, str(scene.bvtknodes_settings.update_mode))
    )

    # Do nothing if frame update has already been triggered
    if bpy.context.scene.bvtknodes_settings.on_frame_change_is_running:
        l.debug("-- Frame update canceled since it's already running")
        return None

    # Set internal guard state to avoid running this also from
    # on_depsgraph_update()
    bpy.context.scene.bvtknodes_settings.on_frame_change_is_running = True

    bvtk_nodes = core.get_all_bvtk_nodes()

    # Update always special converters requiring depsgraph
    for node in bvtk_nodes:
        if node.bl_idname == "BVTK_Node_VTKToBlenderParticlesType":
            node.update_particle_system(depsgraph)

    def time_changed(bvtk_nodes):
        """Return True if time point has changed"""
        for node in bvtk_nodes:
            if node.bl_idname == "BVTK_Node_TimeSelectorType" and node.use_scene_time:
                if node.time_index != scene.frame_current:
                    return True
            elif node.bl_idname == "BVTK_Node_GlobalTimeKeeperType":
                if node.global_time != scene.frame_current:
                    return True
        return False

    # This check is needed because this routine can be triggered also
    # from depsgraph update.
    if not time_changed(bvtk_nodes):
        l.debug("Time unchanged, exiting on_frame_change")
        bpy.context.scene.bvtknodes_settings.on_frame_change_is_running = False
        return None

    # Set no automatic updates to avoid triggering multiple updates
    update_mode = bpy.context.scene.bvtknodes_settings.update_mode
    bpy.context.scene.bvtknodes_settings.update_mode = "no-automatic-updates"

    # Update Time Selectors or Global Time Keeper
    for node in bvtk_nodes:
        # Outdate all nodes. Maybe it is possible to outdate only some
        # nodes, but using this simple approach for now.
        node.set_vtk_status("out-of-date")

        # Note: This is a workaround to enable transient data traversal
        # while this issue remains: https://developer.blender.org/T66392
        if node.bl_idname == "BVTK_Node_TimeSelectorType" and node.use_scene_time:
            node.time_index = scene.frame_current
            node.time_index_update()
            l.debug("Time Selector time step %d" % node.time_index)

        elif node.bl_idname == "BVTK_Node_GlobalTimeKeeperType":
            node.global_time = scene.frame_current
            node.update_time(bpy.context)
            l.debug("Global Time Keeper time step %d" % node.global_time)

    # Restore update_mode and update if needed
    bpy.context.scene.bvtknodes_settings.update_mode = update_mode
    if update_mode == "update-all":
        cache.BVTKCache.update_all()

    bpy.context.scene.bvtknodes_settings.on_frame_change_is_running = False
    l.debug("Frame %d update completed!" % scene.frame_current)


@persistent
def on_depsgraph_update(scene, depsgraph):
    """Updates done after depsgraph changes"""

    l.debug(
        "Depsgraph update was triggered at frame %d (Update Mode %r)"
        % (scene.frame_current, str(scene.bvtknodes_settings.update_mode))
    )

    # Do nothing if depsgraph update has already been triggered
    if bpy.context.scene.bvtknodes_settings.on_depsgraph_update_is_running:
        l.debug("-- on_depsgraph_update canceled since it's already running")
        return None

    # Do nothing if depsgraph update was triggered from volume_import()
    if bpy.context.scene.bvtknodes_settings.volume_import_is_running:
        l.debug("-- on_depsgraph_update canceled since volume import process is running")
        return None

    # Set internal guard state to avoid recursion loops
    bpy.context.scene.bvtknodes_settings.on_depsgraph_update_is_running = True

    # Call on_frame_change() only when it's not anymore running.
    import time
    i = 1
    while i > 0:
        if bpy.context.scene.bvtknodes_settings.on_frame_change_is_running:
            l.debug(
                "Depsgraph update, waiting for on_frame_change(), "
                + "(iteration %d)" % (i + 1)
            )
            time.sleep(0.5)
        else:
            break
        i += 1
        if i > 10000:
            raise Exception("Giving up, on_frame_change_is_running forever")

    l.debug("Depsgraph update, calling on_frame_change()")
    on_frame_change(scene, depsgraph)

    bpy.context.scene.bvtknodes_settings.on_depsgraph_update_is_running = False
    l.debug("Depsgraph update completed at frame %d!" % scene.frame_current)


def custom_register_node_categories():
    """Custom registering of node categories to prevent node categories to
    be shown on the tool-shelf
    """
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
        menu_type = type(
            "NODE_MT_category_" + cat.identifier,
            (bpy.types.Menu,),
            {
                "bl_space_type": "NODE_EDITOR",
                "bl_label": cat.name,
                "category": cat,
                "poll": cat.poll,
                "draw": draw_node_item,
            },
        )
        menu_types.append(menu_type)
        bpy.utils.register_class(menu_type)

    nodeitems_utils._node_categories[identifier] = (
        cat_list,
        draw_add_menu,
        menu_types,
        [],
    )  # , panel_types)


def register():
    """Register function. CLASSES and CATEGORIES are defined in core.py and
    filled in all the gen_VTK*.py and VTK*.py files
    """
    bpy.app.handlers.load_post.append(on_file_loaded)
    bpy.app.handlers.frame_change_post.append(on_frame_change)
    bpy.app.handlers.depsgraph_update_post.append(on_depsgraph_update)
    core.check_b_properties()  # delayed to here to allow class overriding
    for c in core.UI_CLASSES:
        try:
            bpy.utils.register_class(c)
        except:
            l.critical("error registering " + str(c))
    for c in sorted(core.CLASSES.keys()):
        try:
            bpy.utils.register_class(core.CLASSES[c])
        except:
            l.critical("error registering " + str(c))
    custom_register_node_categories()
    bpy.utils.register_class(BVTKNodes_Settings)
    bpy.types.Scene.bvtknodes_settings = bpy.props.PointerProperty(
        type=BVTKNodes_Settings
    )
    bpy.types.CONSOLE_HT_header.append(b_inspect.draw_console_header)

def unregister():
    bpy.types.CONSOLE_HT_header.remove(b_inspect.draw_console_header)
    nodeitems_utils.unregister_node_categories("VTK_NODES")
    for c in reversed(sorted(core.CLASSES.keys())):
        bpy.utils.unregister_class(core.CLASSES[c])
    for c in reversed(core.UI_CLASSES):
        bpy.utils.unregister_class(c)
    bpy.app.handlers.load_post.remove(on_file_loaded)
    bpy.app.handlers.frame_change_post.remove(on_frame_change)
    bpy.utils.unregister_class(BVTKNodes_Settings)
    del bpy.types.Scene.bvtknodes_settings
