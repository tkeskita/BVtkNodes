from .core import l # Import logging
from .core import *

class BVTK_Node_Info(Node, BVTK_Node):
    '''BVTK Info Node'''
    bl_idname = 'BVTK_Node_InfoType'
    bl_label  = 'Info'

    arr_string = '{k} [{i}] ({data_type_name}{n_comps}): \'{name}\': {range_text}'

    def m_properties(self):
        return []

    def m_connections(self):
        return (['input'],[],[],['output'])

    def update_cb(self):
        l.debug('tree updated')

    def update(self):
        # Make info node wider to show all text
        self.width = 300

    def draw_buttons(self, context, layout):
        fs="{:.5g}" # Format string
        in_node, vtkobj = self.get_input_node('input')
        if not in_node:
            layout.label(text='Connect a node')
        elif not vtkobj:
            layout.label(text='Input has not vtkobj (try updating)')
        else:
            vtkobj = resolve_algorithm_output(vtkobj)
            if not vtkobj:
                return

            layout.label(text='Type: ' + vtkobj.__class__.__name__)

            layout.label(text='Points: ' + str(vtkobj.GetNumberOfPoints()))
            if hasattr(vtkobj, 'GetNumberOfCells'):
                layout.label(text='Cells: ' + str(vtkobj.GetNumberOfCells()))
            if hasattr(vtkobj, 'GetBounds'):
                layout.label(text='X range: ' + fs.format(vtkobj.GetBounds()[0]) + \
                             ' - ' + fs.format(vtkobj.GetBounds()[1]))
                layout.label(text='Y range: ' + fs.format(vtkobj.GetBounds()[2]) + \
                             ' - ' + fs.format(vtkobj.GetBounds()[3]))
                layout.label(text='Z range: ' + fs.format(vtkobj.GetBounds()[4]) + \
                             ' - ' + fs.format(vtkobj.GetBounds()[5]))
            data = {}
            if hasattr(vtkobj, 'GetPointData'):
                data['Point data'] = vtkobj.GetPointData()
            if hasattr(vtkobj, 'GetCellData'):
                data['Cell data'] = vtkobj.GetCellData()
            if hasattr(vtkobj, 'GetFieldData'):
                data['Field data'] = vtkobj.GetFieldData()
            for k in data:
                d = data[k]
                for i in range(d.GetNumberOfArrays()):
                    arr = d.GetArray(i)
                    data_type_name = arr.GetDataTypeAsString()
                    n_comps = arr.GetNumberOfComponents()
                    name = arr.GetName()

                    if name is None or data_type_name is None or n_comps is None:
                        l.warning("Invalid array encountered...")
                        #continue

                    range_text = ''
                    for n in range(n_comps):
                        r = arr.GetRange(n)
                        range_text += '[' + fs.format(r[0]) +', ' + fs.format(r[1]) + ']  '
                    row = layout.row()
                    row.label(text = arr_string.format(k, i, data_type_name, n_comps, name, range_text))

        layout.separator()
        row = layout.row()
        row.separator()
        row.separator()
        row.separator()
        row.separator()
        row.operator("node.bvtk_node_update", text="update").node_path = node_path(self)
        row.separator()
        row.separator()
        row.separator()
        row.separator()

    def apply_properties(self, vtkobj):
        pass

    def get_output(self, socketname):
        return self.get_input_node('input')[1]

TYPENAMES = []
add_class(BVTK_Node_Info)
TYPENAMES.append('BVTK_Node_InfoType')

menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(BVTK_NodeCategory("Debug", "Debug", items=menu_items))
