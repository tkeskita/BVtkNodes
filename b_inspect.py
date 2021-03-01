import bpy
import bpy.utils.previews
from .core import *

# -----------------------------------------------------------------------------
# Debug panel and node documentation panel (information about
# active node's vtk object)
# -----------------------------------------------------------------------------
class BVTK_PT_Inspect(bpy.types.Panel):
    '''Panel for operators which printing information about active node's
    VTK object
    '''
    bl_label = 'Inspect'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Inspect'

    @classmethod
    def poll(cls, context):
        return context.active_node is not None and context.space_data.tree_type == 'BVTK_NodeTreeType'

    def draw(self, context):
        active_node = context.active_node
        layout = self.layout
        layout.label(text='VTK version: ' + vtk.vtkVersion().GetVTKVersion())
        vtkobj = active_node.get_vtkobj()
        layout.operator('node.bvtk_update_obj', text='Update Object')
        if vtkobj:
            column = layout.column(align=True)
            o = column.operator('node.bvtk_set_text_editor', text='Documentation')
            o.print = 0
            o = column.operator('node.bvtk_set_text_editor', text='Node Status')
            o.print = 1
            o = column.operator('node.bvtk_set_text_editor', text='Output Status')
            o.print = 2
            o = column.operator(
                'node.bvtk_open_website', text=' Online Documentation', icon='WORLD')
            o.href = 'https://www.vtk.org/doc/nightly/html/class{}.html'.format(active_node.bl_label)
        else:
            layout.label(text='Not a VTK node')

# -----------------------------------------------------------------------------
# Add button to console header
# -----------------------------------------------------------------------------
class BVTK_HT_Console(bpy.types.Header):
    '''BVTK Header Buttons in Python Console'''
    bl_space_type = 'CONSOLE'

    def draw(self, context):
        node_tree = None
        for area in context.screen.areas:
            if area.type == 'NODE_EDITOR':
                for space in area.spaces:
                    if space.type == 'NODE_EDITOR':
                        node_tree = space.node_tree.name

        if node_tree:
            self.layout.separator()
            row = self.layout.row(align=True)
            o = row.operator("console.insert", text="Get Node")
            o.text = "x=bpy.data.node_groups['" + node_tree + "'].nodes.active"
            o = row.operator("console.insert", text="Get VTK Object")
            o.text = "x=bpy.data.node_groups['" + node_tree + "'].nodes.active.get_vtkobj()"
            o = row.operator("console.insert", text="Get Node Output")
            o.text = "x=bpy.data.node_groups['" + node_tree + "'].nodes.active.get_vtkobj().GetOutput()"


# -----------------------------------------------------------------------------
# Operators
# -----------------------------------------------------------------------------
class BVTK_OT_SetTextEditor(bpy.types.Operator):
    '''Add node info to the text editor'''
    bl_idname = "node.bvtk_set_text_editor"
    bl_label = "Print info (BVTK in text editor)"

    # 0 to print doc, 1 to print node status, 2 to print outputs status
    print: bpy.props.IntProperty(default=0)

    def execute(self, context):
        active_node = context.active_node
        vtkobj = active_node.get_vtkobj()
        classname = vtkobj.__class__.__name__
        if self.print == 0:
            inner = self.text_block("DOCUMENTATION " + classname, str(vtkobj.__doc__))
        if self.print == 1:
            inner = self.text_block(classname, str(vtkobj))
        if self.print == 2:
            output_ports = active_node.m_connections()[1]
            inner = ''
            for o in output_ports:
                if o == 'output' or o == 'output 0':
                    inner += self.text_block('output', str(vtkobj.GetOutput(0)))
                if o == 'output 1':
                    inner += self.text_block('output 1', str(vtkobj.GetOutput(1)))
                # TODO: handle output 2,3,....

        text = self.get_text('BVTK', inner)
        flag = True
        areas = context.screen.areas
        for area in areas:
            if area.type == 'TEXT_EDITOR':
                for space in area.spaces:
                    if space.type == 'TEXT_EDITOR':
                        if flag:
                            space.text = text
                            space.top = 0
                            flag = False
        if flag:
            self.report({'INFO'}, "See 'BVTK' in the text editor")
        return {'FINISHED'}

    def get_text(self, name, inner):
        '''Get text object'''
        if name not in bpy.data.texts.keys():
            text = bpy.data.texts.new(name)
        else:
            text = bpy.data.texts[name]
        text.from_string(inner)
        return text

    def text_block(self, title, content):
        '''Pretty print text content with title'''
        s = '-'*50+'\n' + title + '\n' + '-'*50 + '\n' + content + '\n'
        if content == 'None':
            s += '\n\n'
        return s


class BVTK_OT_OpenWebsite(bpy.types.Operator):
    '''Open web site in web browser'''
    bl_idname = 'node.bvtk_open_website'
    bl_label = ''

    href: bpy.props.StringProperty()

    def execute(self, context):
        import webbrowser
        webbrowser.open(self.href)
        return {'FINISHED'}


class BVTK_OT_UpdateObj(bpy.types.Operator):
    '''Run update of this node's VTK Object'''
    bl_idname = "node.bvtk_update_obj"
    bl_label = "call update()"

    prop: bpy.props.StringProperty()

    def execute(self, context):
        check_cache()
        active_node = context.active_node
        vtkobj = active_node.get_vtkobj()
        log_check()
        active_node.apply_properties(vtkobj)
        if hasattr(vtkobj, 'Update'):
            vtkobj.Update()
        log_show()
        return {'FINISHED'}

# Register classes
add_ui_class(BVTK_PT_Inspect)
add_ui_class(BVTK_HT_Console)
add_ui_class(BVTK_OT_SetTextEditor)
add_ui_class(BVTK_OT_OpenWebsite)
add_ui_class(BVTK_OT_UpdateObj)


