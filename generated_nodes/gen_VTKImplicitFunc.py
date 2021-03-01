# Generated definitions for VTK class group: ImplicitFunc
# VTK version: 9.0.1

from ..core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKBox(Node, BVTK_Node):

    bl_idname = 'VTKBoxType'
    bl_label  = 'vtkBox'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKBox )        
TYPENAMES.append('VTKBoxType' )

#--------------------------------------------------------------
class VTKCone(Node, BVTK_Node):

    bl_idname = 'VTKConeType'
    bl_label  = 'vtkCone'
    
    m_Angle: bpy.props.FloatProperty( name='Angle', default=45.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Angle',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKCone )        
TYPENAMES.append('VTKConeType' )

#--------------------------------------------------------------
class VTKCylinder(Node, BVTK_Node):

    bl_idname = 'VTKCylinderType'
    bl_label  = 'vtkCylinder'
    
    m_Radius: bpy.props.FloatProperty      ( name='Radius', default=0.5 )
    m_Axis  : bpy.props.FloatVectorProperty( name='Axis',   default=[0.0, 1.0, 0.0], size=3 )
    m_Center: bpy.props.FloatVectorProperty( name='Center', default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Radius','m_Axis','m_Center',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKCylinder )        
TYPENAMES.append('VTKCylinderType' )

#--------------------------------------------------------------
class VTKImplicitBoolean(Node, BVTK_Node):

    bl_idname = 'VTKImplicitBooleanType'
    bl_label  = 'vtkImplicitBoolean'
    e_OperationType_items=[ (x,x,x) for x in ['Union', 'Intersection', 'Difference', 'UnionOfMagnitudes']]
    
    e_OperationType: bpy.props.EnumProperty( name='OperationType', default="Union", items=e_OperationType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['e_OperationType',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKImplicitBoolean )        
TYPENAMES.append('VTKImplicitBooleanType' )

#--------------------------------------------------------------
class VTKImplicitDataSet(Node, BVTK_Node):

    bl_idname = 'VTKImplicitDataSetType'
    bl_label  = 'vtkImplicitDataSet'
    
    m_OutValue   : bpy.props.FloatProperty      ( name='OutValue',    default=-1e+30 )
    m_OutGradient: bpy.props.FloatVectorProperty( name='OutGradient', default=[0.0, 0.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_OutValue','m_OutGradient',]
    def m_connections( self ):
        return ([], [], ['DataSet', 'Transform'], ['self']) 
    
add_class( VTKImplicitDataSet )        
TYPENAMES.append('VTKImplicitDataSetType' )

#--------------------------------------------------------------
class VTKImplicitHalo(Node, BVTK_Node):

    bl_idname = 'VTKImplicitHaloType'
    bl_label  = 'vtkImplicitHalo'
    
    m_FadeOut: bpy.props.FloatProperty      ( name='FadeOut', default=0.01 )
    m_Radius : bpy.props.FloatProperty      ( name='Radius',  default=1.0 )
    m_Center : bpy.props.FloatVectorProperty( name='Center',  default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FadeOut','m_Radius','m_Center',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKImplicitHalo )        
TYPENAMES.append('VTKImplicitHaloType' )

#--------------------------------------------------------------
class VTKImplicitPolyDataDistance(Node, BVTK_Node):

    bl_idname = 'VTKImplicitPolyDataDistanceType'
    bl_label  = 'vtkImplicitPolyDataDistance'
    
    m_NoValue       : bpy.props.FloatProperty      ( name='NoValue',        default=0.0 )
    m_Tolerance     : bpy.props.FloatProperty      ( name='Tolerance',      default=1e-12 )
    m_NoClosestPoint: bpy.props.FloatVectorProperty( name='NoClosestPoint', default=[0.0, 0.0, 0.0], size=3 )
    m_NoGradient    : bpy.props.FloatVectorProperty( name='NoGradient',     default=[0.0, 0.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NoValue','m_Tolerance','m_NoClosestPoint','m_NoGradient',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKImplicitPolyDataDistance )        
TYPENAMES.append('VTKImplicitPolyDataDistanceType' )

#--------------------------------------------------------------
class VTKImplicitSelectionLoop(Node, BVTK_Node):

    bl_idname = 'VTKImplicitSelectionLoopType'
    bl_label  = 'vtkImplicitSelectionLoop'
    
    m_AutomaticNormalGeneration: bpy.props.BoolProperty       ( name='AutomaticNormalGeneration', default=True )
    m_Normal                   : bpy.props.FloatVectorProperty( name='Normal',                    default=[0.0, 0.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutomaticNormalGeneration','m_Normal',]
    def m_connections( self ):
        return ([], [], ['Loop', 'Transform'], ['self']) 
    
add_class( VTKImplicitSelectionLoop )        
TYPENAMES.append('VTKImplicitSelectionLoopType' )

#--------------------------------------------------------------
class VTKImplicitSum(Node, BVTK_Node):

    bl_idname = 'VTKImplicitSumType'
    bl_label  = 'vtkImplicitSum'
    
    m_NormalizeByWeight: bpy.props.BoolProperty( name='NormalizeByWeight', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NormalizeByWeight',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKImplicitSum )        
TYPENAMES.append('VTKImplicitSumType' )

#--------------------------------------------------------------
class VTKImplicitVolume(Node, BVTK_Node):

    bl_idname = 'VTKImplicitVolumeType'
    bl_label  = 'vtkImplicitVolume'
    
    m_OutValue   : bpy.props.FloatProperty      ( name='OutValue',    default=-1e+30 )
    m_OutGradient: bpy.props.FloatVectorProperty( name='OutGradient', default=[0.0, 0.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_OutValue','m_OutGradient',]
    def m_connections( self ):
        return ([], [], ['Transform', 'Volume'], ['self']) 
    
add_class( VTKImplicitVolume )        
TYPENAMES.append('VTKImplicitVolumeType' )

#--------------------------------------------------------------
class VTKImplicitWindowFunction(Node, BVTK_Node):

    bl_idname = 'VTKImplicitWindowFunctionType'
    bl_label  = 'vtkImplicitWindowFunction'
    
    m_WindowRange : bpy.props.FloatVectorProperty( name='WindowRange',  default=[0.0, 1.0], size=2 )
    m_WindowValues: bpy.props.FloatVectorProperty( name='WindowValues', default=[0.0, 1.0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WindowRange','m_WindowValues',]
    def m_connections( self ):
        return ([], [], ['ImplicitFunction', 'Transform'], ['self']) 
    
add_class( VTKImplicitWindowFunction )        
TYPENAMES.append('VTKImplicitWindowFunctionType' )

#--------------------------------------------------------------
class VTKPerlinNoise(Node, BVTK_Node):

    bl_idname = 'VTKPerlinNoiseType'
    bl_label  = 'vtkPerlinNoise'
    
    m_Amplitude: bpy.props.FloatProperty      ( name='Amplitude', default=1.0 )
    m_Frequency: bpy.props.FloatVectorProperty( name='Frequency', default=[1.0, 1.0, 1.0], size=3 )
    m_Phase    : bpy.props.FloatVectorProperty( name='Phase',     default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Amplitude','m_Frequency','m_Phase',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKPerlinNoise )        
TYPENAMES.append('VTKPerlinNoiseType' )

#--------------------------------------------------------------
class VTKPlane(Node, BVTK_Node):

    bl_idname = 'VTKPlaneType'
    bl_label  = 'vtkPlane'
    
    m_Normal: bpy.props.FloatVectorProperty( name='Normal', default=[0.0, 0.0, 1.0], size=3 )
    m_Origin: bpy.props.FloatVectorProperty( name='Origin', default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Normal','m_Origin',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKPlane )        
TYPENAMES.append('VTKPlaneType' )

#--------------------------------------------------------------
class VTKPlanes(Node, BVTK_Node):

    bl_idname = 'VTKPlanesType'
    bl_label  = 'vtkPlanes'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['Normals', 'Points', 'Transform'], ['self']) 
    
add_class( VTKPlanes )        
TYPENAMES.append('VTKPlanesType' )

#--------------------------------------------------------------
class VTKPlanesIntersection(Node, BVTK_Node):

    bl_idname = 'VTKPlanesIntersectionType'
    bl_label  = 'vtkPlanesIntersection'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['Normals', 'Points', 'Transform'], ['self']) 
    
add_class( VTKPlanesIntersection )        
TYPENAMES.append('VTKPlanesIntersectionType' )

#--------------------------------------------------------------
class VTKPolyPlane(Node, BVTK_Node):

    bl_idname = 'VTKPolyPlaneType'
    bl_label  = 'vtkPolyPlane'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['PolyLine', 'Transform'], ['self']) 
    
add_class( VTKPolyPlane )        
TYPENAMES.append('VTKPolyPlaneType' )

#--------------------------------------------------------------
class VTKQuadric(Node, BVTK_Node):

    bl_idname = 'VTKQuadricType'
    bl_label  = 'vtkQuadric'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKQuadric )        
TYPENAMES.append('VTKQuadricType' )

#--------------------------------------------------------------
class VTKSphere(Node, BVTK_Node):

    bl_idname = 'VTKSphereType'
    bl_label  = 'vtkSphere'
    
    m_Radius: bpy.props.FloatProperty      ( name='Radius', default=0.5 )
    m_Center: bpy.props.FloatVectorProperty( name='Center', default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Radius','m_Center',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKSphere )        
TYPENAMES.append('VTKSphereType' )

#--------------------------------------------------------------
class VTKSuperquadric(Node, BVTK_Node):

    bl_idname = 'VTKSuperquadricType'
    bl_label  = 'vtkSuperquadric'
    
    m_Toroidal      : bpy.props.BoolProperty       ( name='Toroidal',       default=True )
    m_PhiRoundness  : bpy.props.FloatProperty      ( name='PhiRoundness',   default=1.0 )
    m_Size          : bpy.props.FloatProperty      ( name='Size',           default=0.5 )
    m_ThetaRoundness: bpy.props.FloatProperty      ( name='ThetaRoundness', default=1.0 )
    m_Thickness     : bpy.props.FloatProperty      ( name='Thickness',      default=0.3333 )
    m_Center        : bpy.props.FloatVectorProperty( name='Center',         default=[0.0, 0.0, 0.0], size=3 )
    m_Scale         : bpy.props.FloatVectorProperty( name='Scale',          default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Toroidal','m_PhiRoundness','m_Size','m_ThetaRoundness','m_Thickness','m_Center','m_Scale',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKSuperquadric )        
TYPENAMES.append('VTKSuperquadricType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( BVTK_NodeCategory( 'ImplicitFunc', 'ImplicitFunc', items=menu_items) )