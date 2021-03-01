# -----------------------------------------------------------------------------
# Color map nodes and functions
# -----------------------------------------------------------------------------

from .core import *
import json
import os
import numpy as np

current_dir = os.path.dirname(__file__)

with open(current_dir + '/colormaps/colormaps_hsv.json') as json_file:
    colormaps_hsv = json.load(json_file)

with open(current_dir + '/colormaps/colormaps_rgb.json') as json_file:
    colormaps_rgb = json.load(json_file)

def get_default_texture(name):
    '''Create and return a new color ramp BLEND type brush texture'''
    if name not in bpy.data.textures:
        tex = bpy.data.textures.new(name, 'BLEND')
    else:
        tex = bpy.data.textures[name]
    tex.use_color_ramp = True

    # Force saving of blend texture, so that ramp is correct when
    # blend file is loaded. TODO: Is there better way to fix this?
    tex.use_fake_user = True

    elements = tex.color_ramp.elements
    elements[0].color = (10 / 255, 10 / 255, 180 / 255, 1)
    elements[0].position = 0.05
    elements[1].color = (180 / 255, 10 / 255, 20 / 255, 1)
    elements[1].position = 0.95
    e = elements.new(0.425)
    e.color = (141 / 255, 176 / 255, 254 / 255, 1)
    e = elements.new(0.5)
    e.color = (221 / 255, 221 / 255, 221 / 255, 1)
    e = elements.new(0.575)
    e.color = (243 / 255, 148 / 255, 117 / 255, 1)
    return tex

def get_matplotlib_colormap(texture_name, cm_name, cm_nr_values):
    '''Create or modify a texture map according to the colormap given name'''
    if texture_name not in bpy.data.textures:
        tex = bpy.data.textures.new(texture_name, 'BLEND')
    else:
        tex = bpy.data.textures[texture_name]
    tex.use_color_ramp = True

    # Force saving of blend texture, so that ramp is correct when
    # blend file is loaded. TODO: Is there better way to fix this?
    tex.use_fake_user = True

    elements = tex.color_ramp.elements
    old_len = len(elements.items())

    #Fetch new colormap
    new_colors = np.array(colormaps_rgb[cm_name]).astype(np.float32)
    new_colors_nr = new_colors.shape[0]
    #Positions on the x-axis of the colors
    colors_cmap_x = np.linspace(0, 1, num=new_colors_nr)
    colors_x = np.linspace(0, 1, num=cm_nr_values+1)[:-1]
    real_colors_x = np.linspace(0, 1, num=cm_nr_values)
    #Interpolate to desired length
    new_colors_interp = np.stack([np.interp(real_colors_x, colors_cmap_x, new_colors[:, i]) for i in range(3)], axis=-1)
    new_colors_interp_w_alpha = np.concatenate([new_colors_interp, np.ones_like(new_colors_interp[:, :1])], axis=-1)

    #Delete old colors if too many
    [elements.remove(elements[0]) for i in range(old_len - cm_nr_values)]

    #Add new colors if too few
    [elements.new(colors_x[i]) for i in range(cm_nr_values - old_len)]

    elements.foreach_set('position', colors_x)
    elements.foreach_set('color', new_colors_interp_w_alpha.reshape([-1]))
    return tex


class BVTK_Node_ColorMapper(Node, BVTK_Node):
    '''BVTK Color Mapper Node'''
    bl_idname = 'BVTK_Node_ColorMapperType'
    bl_label  = 'Color Mapper'

    # Properties of ColorMapper
    texture_type: bpy.props.EnumProperty(
        name="texture type",
        items=[('IMAGE','IMAGE','IMAGE','FILE_IMAGE',1)],
        default='IMAGE'
    )
    default_texture: bpy.props.StringProperty(default="")
    last_color_by: bpy.props.StringProperty(default='')
    lut: bpy.props.BoolProperty(default=False) # Lookup table
    height: bpy.props.FloatProperty(default=5.5)
    max: bpy.props.FloatProperty(default=0)
    min: bpy.props.FloatProperty(default=0)

    def array_change(self, context):
        '''Determine coloring by either point or cell data'''
        vtkobj = self.get_input_node('input')[1]
        if self.color_by and vtkobj:
            vtkobj = resolve_algorithm_output(vtkobj)
            # Color by point data or cell data
            if self.color_by[0] == 'P':
                d = vtkobj.GetPointData()
            else:
                d = vtkobj.GetCellData()
            if d:
                range = d.GetArray(int(self.color_by[1:])).GetRange()
                self.max = range[1]
                self.min = range[0]

    def color_arrays(self, context):
        '''Generate array items available for coloring'''
        items = []
        vtkobj = self.get_input_node('input')[1]
        if vtkobj:
            vtkobj = resolve_algorithm_output(vtkobj)
            if hasattr(vtkobj, 'GetCellData'):
                c_data = vtkobj.GetCellData()
                p_data =  vtkobj.GetPointData()
                c_descr = 'Color by cell data using '
                p_descr = 'Color by point data using '
                for i in range(p_data.GetNumberOfArrays()):
                    arr_name = str(p_data.GetArrayName(i))
                    items.append(('P'+str(i), arr_name, p_descr+arr_name+' array', 'VERTEXSEL', len(items)))
                for i in range(c_data.GetNumberOfArrays()):
                    arr_name = str(c_data.GetArrayName(i))
                    items.append(('C'+str(i), arr_name, c_descr+arr_name+' array', 'FACESEL', len(items)))
        if not len(items):
            items.append(('', '', ''))
        return items

    # Must define these annotations here after function defs
    color_by: bpy.props.EnumProperty(items=color_arrays, name="color by", update=array_change)
    auto_range: bpy.props.BoolProperty(default=True, update=array_change)

    def m_properties(self):
        return ['color_by', 'texture_type', 'auto_range',
                'lut', 'min', 'max', 'height']

    def m_connections(self):
        return (['input'],[],[],['output'])

    def setup(self):
        self.inputs.new('BVTK_NodeSocketType', 'lookuptable')

    def update(self):
        if self.last_color_by != self.color_by or self.auto_range:
            self.last_color_by = self.color_by
            self.array_change(None)

    def get_texture(self):
        in_links = self.inputs['lookuptable'].links
        if len(in_links) > 0:
            return in_links[0].from_node.get_texture()
        if self.default_texture:
            if self.default_texture in bpy.data.textures:
                return bpy.data.textures[self.default_texture]
        new_texture = get_default_texture(self.name)
        self.default_texture = new_texture.name
        return new_texture

    def free(self):
        if self.default_texture:
            if self.default_texture in bpy.data.textures:
                bpy.data.texures.remove(bpy.data.textures[self.default_texture])
        node_deleted(self)

    def draw_buttons(self, context, layout):
        in_node, vtkobj = self.get_input_node('input')
        if not in_node:
            layout.label(text='Connect a node')
        elif not vtkobj:
            layout.label(text='Input has not vtkobj (try updating)')
        else:
            vtkobj = resolve_algorithm_output(vtkobj)
            if hasattr(vtkobj, 'GetPointData'):
                layout.prop(self, 'lut', text='Generate scalar bar')
                # layout.prop(self, 'texture_type')
                if self.lut:
                    layout.prop(self, 'height', text='scalar bar height')
                layout.prop(self, 'color_by', text='color by')
                layout.prop(self, 'auto_range', text='automatic range')
                row = layout.row(align=True)
                row.enabled = not self.auto_range
                row.prop(self, 'min')
                row.prop(self, 'max')
                layout.separator()
            else:
                layout.label(text='Input has no associated data (try updating)')



class BVTK_Node_ColorRamp(Node, BVTK_Node):
    '''BVTK Color Ramp Node'''
    bl_idname = 'BVTK_Node_ColorRampType'
    bl_label  = 'Color Ramp'

    texture_type: bpy.props.EnumProperty(
        name="texture type",
        items=[('IMAGE','IMAGE','IMAGE','FILE_IMAGE',1)],
        default='IMAGE'
    )
    my_texture: bpy.props.StringProperty()

    def preset_name_from_ind(self, ind):
        return self.cm_preset_items[ind][0]
    
    def update_colorbar_preset(self, context):
        if self.cm_preset == 'custom':
            return

        new_texture = get_matplotlib_colormap(self.name, self.cm_preset, self.cm_nr_values)
        self.my_texture = new_texture.name
        #return value

    def update_colorbar_nr(self, context):
        #Custom nodes will not be modified by the automatic helper
        if self.cm_preset == 'custom':
            return

        self.update_colorbar_preset(context)
        #self.cm_nr_values_ = value
        #return value

    cm_preset_items = [ (x,x,x) for x in ['custom'] + sorted(list(colormaps_rgb.keys()))] #['viridis', 'jet', 'coolwarm', 'custom']]
    cm_preset:   bpy.props.EnumProperty   (name='Preset', default='custom', items=cm_preset_items, update=update_colorbar_preset) #, set=update_colorbar_preset)
    cm_nr_values: bpy.props.IntProperty(name='Nr Color values', default=8, max=32, min=2, update=update_colorbar_nr) #, get=get_cm_nr_values)
    b_properties: bpy.props.BoolVectorProperty(name="", size=32, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['cm_preset', 'cm_nr_values']

    def m_connections(self):
        return ([],[],[],['lookupTable'])

    def copy_setup(self, node):
        new_texture = get_default_texture(self.name)
        self.my_texture = new_texture.name
        old_texture = node.get_texture()
        if old_texture:
            elements = new_texture.color_ramp.elements
            new_elements = old_texture.color_ramp.elements
            while len(elements) > len(new_elements):
                elements.remove(elements[0])
            for i, new_el in enumerate(new_elements):
                if i < len(elements):
                    elements[i].color = new_el.color
                    elements[i].position = new_el.position
                else:
                    e = elements.new(new_el.position)
                    e.color = new_el.color

    def setup(self):
        new_texture = get_default_texture(self.name)
        self.my_texture = new_texture.name


    def get_texture(self):
        if self.my_texture not in bpy.data.textures.keys():
            return None
        return bpy.data.textures[self.my_texture]

    def free(self):
        if self.my_texture in bpy.data.textures:
            bpy.data.textures.remove(bpy.data.textures[self.my_texture])
        node_deleted(self)

    def draw_buttons(self, context, layout):
        if self.my_texture in bpy.data.textures.keys():
            layout.template_color_ramp(bpy.data.textures[self.my_texture], "color_ramp", expand=False)
        row = layout.row()
        row.prop(self, 'cm_preset')
        row = layout.row()
        row.prop(self, 'cm_nr_values')

    def apply_properties(self, vtkobj):
        pass

    def get_output(self, socketname):
        lut = vtk.vtkLookupTable()
        lut.Build()
        return lut

    def special_properties(self):
        '''Make auto_update scanner notice changes in the color ramp'''
        return self.export_properties()['elements']

    def export_properties(self):
        '''Export colormap properties. Called by export operator'''
        t = self.get_texture()
        if t:
            elements = t.color_ramp.elements
            e = [[[x for x in e.color], e.position] for e in elements]
        else:
            e = []
        return {'elements': e}

    def import_properties(self, dict):
        l.debug("importing colormap " + str(self.name))
        '''Import colormap properties. Called by import operator'''
        t = self.get_texture()
        new_elements = dict['elements']
        if t:
            elements = t.color_ramp.elements
            while len(elements) > len(new_elements):
                elements.remove(elements[0])
            for i, new_el in enumerate(new_elements):
                if i < len(elements):
                    elements[i].color = new_el[0]
                    elements[i].position = new_el[1]
                else:
                    e = elements.new(new_el[1])
                    e.color = new_el[0]


# Add classes and menu items
TYPENAMES = []
add_class(BVTK_Node_ColorMapper)
TYPENAMES.append('BVTK_Node_ColorMapperType')
add_class(BVTK_Node_ColorRamp)
TYPENAMES.append('BVTK_Node_ColorRampType')

menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(BVTK_NodeCategory("Color", "Color", items=menu_items))
