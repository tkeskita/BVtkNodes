# Generated definitions for VTK class group: ParametricFunc
# VTK Version: 8.1.2

from ..core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKParametricBohemianDome(Node, BVTK_Node):

    bl_idname = 'VTKParametricBohemianDomeType'
    bl_label  = 'vtkParametricBohemianDome'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_A                   : bpy.props.FloatProperty( name='A',                    default=0.5 )
    m_B                   : bpy.props.FloatProperty( name='B',                    default=1.5 )
    m_C                   : bpy.props.FloatProperty( name='C',                    default=1.0 )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=3.141592653589793 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=3.141592653589793 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=-3.141592653589793 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=-3.141592653589793 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_A','m_B','m_C','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricBohemianDome )        
TYPENAMES.append('VTKParametricBohemianDomeType' )

#--------------------------------------------------------------
class VTKParametricBour(Node, BVTK_Node):

    bl_idname = 'VTKParametricBourType'
    bl_label  = 'vtkParametricBour'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=1.0 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=12.566370614359172 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=0.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=0.0 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricBour )        
TYPENAMES.append('VTKParametricBourType' )

#--------------------------------------------------------------
class VTKParametricBoy(Node, BVTK_Node):

    bl_idname = 'VTKParametricBoyType'
    bl_label  = 'vtkParametricBoy'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=3.141592653589793 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=3.141592653589793 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=0.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=0.0 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    m_ZScale              : bpy.props.FloatProperty( name='ZScale',               default=0.125 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW','m_ZScale',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricBoy )        
TYPENAMES.append('VTKParametricBoyType' )

#--------------------------------------------------------------
class VTKParametricCatalanMinimal(Node, BVTK_Node):

    bl_idname = 'VTKParametricCatalanMinimalType'
    bl_label  = 'vtkParametricCatalanMinimal'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=12.566370614359172 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=1.5 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=-12.566370614359172 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=-1.5 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricCatalanMinimal )        
TYPENAMES.append('VTKParametricCatalanMinimalType' )

#--------------------------------------------------------------
class VTKParametricConicSpiral(Node, BVTK_Node):

    bl_idname = 'VTKParametricConicSpiralType'
    bl_label  = 'vtkParametricConicSpiral'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_A                   : bpy.props.FloatProperty( name='A',                    default=0.2 )
    m_B                   : bpy.props.FloatProperty( name='B',                    default=1.0 )
    m_C                   : bpy.props.FloatProperty( name='C',                    default=0.1 )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=6.283185307179586 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=6.283185307179586 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=0.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=0.0 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    m_N                   : bpy.props.FloatProperty( name='N',                    default=2.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_A','m_B','m_C','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW','m_N',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricConicSpiral )        
TYPENAMES.append('VTKParametricConicSpiralType' )

#--------------------------------------------------------------
class VTKParametricCrossCap(Node, BVTK_Node):

    bl_idname = 'VTKParametricCrossCapType'
    bl_label  = 'vtkParametricCrossCap'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=3.141592653589793 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=3.141592653589793 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=0.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=0.0 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricCrossCap )        
TYPENAMES.append('VTKParametricCrossCapType' )

#--------------------------------------------------------------
class VTKParametricDini(Node, BVTK_Node):

    bl_idname = 'VTKParametricDiniType'
    bl_label  = 'vtkParametricDini'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_A                   : bpy.props.FloatProperty( name='A',                    default=1.0 )
    m_B                   : bpy.props.FloatProperty( name='B',                    default=0.2 )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=12.566370614359172 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=2.0 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=0.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=0.001 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_A','m_B','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricDini )        
TYPENAMES.append('VTKParametricDiniType' )

#--------------------------------------------------------------
class VTKParametricEllipsoid(Node, BVTK_Node):

    bl_idname = 'VTKParametricEllipsoidType'
    bl_label  = 'vtkParametricEllipsoid'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=6.283185307179586 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=3.141592653589793 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=0.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=0.0 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    m_XRadius             : bpy.props.FloatProperty( name='XRadius',              default=1.0 )
    m_YRadius             : bpy.props.FloatProperty( name='YRadius',              default=1.0 )
    m_ZRadius             : bpy.props.FloatProperty( name='ZRadius',              default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW','m_XRadius','m_YRadius','m_ZRadius',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricEllipsoid )        
TYPENAMES.append('VTKParametricEllipsoidType' )

#--------------------------------------------------------------
class VTKParametricEnneper(Node, BVTK_Node):

    bl_idname = 'VTKParametricEnneperType'
    bl_label  = 'vtkParametricEnneper'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=2.0 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=2.0 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=-2.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=-2.0 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricEnneper )        
TYPENAMES.append('VTKParametricEnneperType' )

#--------------------------------------------------------------
class VTKParametricFigure8Klein(Node, BVTK_Node):

    bl_idname = 'VTKParametricFigure8KleinType'
    bl_label  = 'vtkParametricFigure8Klein'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=3.141592653589793 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=3.141592653589793 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=-3.141592653589793 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=-3.141592653589793 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    m_Radius              : bpy.props.FloatProperty( name='Radius',               default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW','m_Radius',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricFigure8Klein )        
TYPENAMES.append('VTKParametricFigure8KleinType' )

#--------------------------------------------------------------
class VTKParametricHenneberg(Node, BVTK_Node):

    bl_idname = 'VTKParametricHennebergType'
    bl_label  = 'vtkParametricHenneberg'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=1.0 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=1.5707963267948966 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=-1.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=-1.5707963267948966 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricHenneberg )        
TYPENAMES.append('VTKParametricHennebergType' )

#--------------------------------------------------------------
class VTKParametricKlein(Node, BVTK_Node):

    bl_idname = 'VTKParametricKleinType'
    bl_label  = 'vtkParametricKlein'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=3.141592653589793 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=6.283185307179586 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=0.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=0.0 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricKlein )        
TYPENAMES.append('VTKParametricKleinType' )

#--------------------------------------------------------------
class VTKParametricKuen(Node, BVTK_Node):

    bl_idname = 'VTKParametricKuenType'
    bl_label  = 'vtkParametricKuen'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_DeltaV0             : bpy.props.FloatProperty( name='DeltaV0',              default=0.05 )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=4.5 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=3.141592653589793 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=-4.5 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=0.0 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_DeltaV0','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricKuen )        
TYPENAMES.append('VTKParametricKuenType' )

#--------------------------------------------------------------
class VTKParametricMobius(Node, BVTK_Node):

    bl_idname = 'VTKParametricMobiusType'
    bl_label  = 'vtkParametricMobius'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=6.283185307179586 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=1.0 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=0.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=-1.0 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    m_Radius              : bpy.props.FloatProperty( name='Radius',               default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW','m_Radius',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricMobius )        
TYPENAMES.append('VTKParametricMobiusType' )

#--------------------------------------------------------------
class VTKParametricPluckerConoid(Node, BVTK_Node):

    bl_idname = 'VTKParametricPluckerConoidType'
    bl_label  = 'vtkParametricPluckerConoid'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_N                   : bpy.props.IntProperty  ( name='N',                    default=2 )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=3.0 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=6.283185307179586 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=0.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=0.0 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_N','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricPluckerConoid )        
TYPENAMES.append('VTKParametricPluckerConoidType' )

#--------------------------------------------------------------
class VTKParametricPseudosphere(Node, BVTK_Node):

    bl_idname = 'VTKParametricPseudosphereType'
    bl_label  = 'vtkParametricPseudosphere'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=5.0 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=3.141592653589793 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=-5.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=-3.141592653589793 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricPseudosphere )        
TYPENAMES.append('VTKParametricPseudosphereType' )

#--------------------------------------------------------------
class VTKParametricRandomHills(Node, BVTK_Node):

    bl_idname = 'VTKParametricRandomHillsType'
    bl_label  = 'vtkParametricRandomHills'
    
    m_AllowRandomGeneration: bpy.props.BoolProperty ( name='AllowRandomGeneration', default=True )
    m_ClockwiseOrdering    : bpy.props.BoolProperty ( name='ClockwiseOrdering',     default=True )
    m_DerivativesAvailable : bpy.props.BoolProperty ( name='DerivativesAvailable',  default=True )
    m_JoinU                : bpy.props.BoolProperty ( name='JoinU',                 default=True )
    m_JoinV                : bpy.props.BoolProperty ( name='JoinV',                 default=True )
    m_JoinW                : bpy.props.BoolProperty ( name='JoinW',                 default=True )
    m_TwistU               : bpy.props.BoolProperty ( name='TwistU',                default=True )
    m_TwistV               : bpy.props.BoolProperty ( name='TwistV',                default=True )
    m_TwistW               : bpy.props.BoolProperty ( name='TwistW',                default=True )
    m_NumberOfHills        : bpy.props.IntProperty  ( name='NumberOfHills',         default=30 )
    m_RandomSeed           : bpy.props.IntProperty  ( name='RandomSeed',            default=1 )
    m_AmplitudeScaleFactor : bpy.props.FloatProperty( name='AmplitudeScaleFactor',  default=0.3333333333333333 )
    m_HillAmplitude        : bpy.props.FloatProperty( name='HillAmplitude',         default=2.0 )
    m_HillXVariance        : bpy.props.FloatProperty( name='HillXVariance',         default=2.5 )
    m_HillYVariance        : bpy.props.FloatProperty( name='HillYVariance',         default=2.5 )
    m_MaximumU             : bpy.props.FloatProperty( name='MaximumU',              default=10.0 )
    m_MaximumV             : bpy.props.FloatProperty( name='MaximumV',              default=10.0 )
    m_MaximumW             : bpy.props.FloatProperty( name='MaximumW',              default=1.0 )
    m_MinimumU             : bpy.props.FloatProperty( name='MinimumU',              default=-10.0 )
    m_MinimumV             : bpy.props.FloatProperty( name='MinimumV',              default=-10.0 )
    m_MinimumW             : bpy.props.FloatProperty( name='MinimumW',              default=0.0 )
    m_XVarianceScaleFactor : bpy.props.FloatProperty( name='XVarianceScaleFactor',  default=0.3333333333333333 )
    m_YVarianceScaleFactor : bpy.props.FloatProperty( name='YVarianceScaleFactor',  default=0.3333333333333333 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=23, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AllowRandomGeneration','m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_NumberOfHills','m_RandomSeed','m_AmplitudeScaleFactor','m_HillAmplitude','m_HillXVariance','m_HillYVariance','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW','m_XVarianceScaleFactor','m_YVarianceScaleFactor',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricRandomHills )        
TYPENAMES.append('VTKParametricRandomHillsType' )

#--------------------------------------------------------------
class VTKParametricRoman(Node, BVTK_Node):

    bl_idname = 'VTKParametricRomanType'
    bl_label  = 'vtkParametricRoman'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=3.141592653589793 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=3.141592653589793 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=0.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=0.0 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    m_Radius              : bpy.props.FloatProperty( name='Radius',               default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW','m_Radius',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricRoman )        
TYPENAMES.append('VTKParametricRomanType' )

#--------------------------------------------------------------
class VTKParametricSpline(Node, BVTK_Node):

    bl_idname = 'VTKParametricSplineType'
    bl_label  = 'vtkParametricSpline'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_Closed              : bpy.props.BoolProperty ( name='Closed',               default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_ParameterizeByLength: bpy.props.BoolProperty ( name='ParameterizeByLength', default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_LeftConstraint      : bpy.props.IntProperty  ( name='LeftConstraint',       default=1 )
    m_RightConstraint     : bpy.props.IntProperty  ( name='RightConstraint',      default=1 )
    m_LeftValue           : bpy.props.FloatProperty( name='LeftValue',            default=0.0 )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=1.0 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=1.0 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=0.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=0.0 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    m_RightValue          : bpy.props.FloatProperty( name='RightValue',           default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=20, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_Closed','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_ParameterizeByLength','m_TwistU','m_TwistV','m_TwistW','m_LeftConstraint','m_RightConstraint','m_LeftValue','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW','m_RightValue',]
    def m_connections( self ):
        return ([], [], ['XSpline', 'YSpline', 'ZSpline', 'Points'], ['self']) 
    
add_class( VTKParametricSpline )        
TYPENAMES.append('VTKParametricSplineType' )

#--------------------------------------------------------------
class VTKParametricSuperEllipsoid(Node, BVTK_Node):

    bl_idname = 'VTKParametricSuperEllipsoidType'
    bl_label  = 'vtkParametricSuperEllipsoid'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=3.141592653589793 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=1.5707963267948966 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=-3.141592653589793 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=-1.5707963267948966 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    m_N1                  : bpy.props.FloatProperty( name='N1',                   default=1.0 )
    m_N2                  : bpy.props.FloatProperty( name='N2',                   default=1.0 )
    m_XRadius             : bpy.props.FloatProperty( name='XRadius',              default=1.0 )
    m_YRadius             : bpy.props.FloatProperty( name='YRadius',              default=1.0 )
    m_ZRadius             : bpy.props.FloatProperty( name='ZRadius',              default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=19, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW','m_N1','m_N2','m_XRadius','m_YRadius','m_ZRadius',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricSuperEllipsoid )        
TYPENAMES.append('VTKParametricSuperEllipsoidType' )

#--------------------------------------------------------------
class VTKParametricSuperToroid(Node, BVTK_Node):

    bl_idname = 'VTKParametricSuperToroidType'
    bl_label  = 'vtkParametricSuperToroid'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_CrossSectionRadius  : bpy.props.FloatProperty( name='CrossSectionRadius',   default=0.5 )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=6.283185307179586 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=6.283185307179586 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=0.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=0.0 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    m_N1                  : bpy.props.FloatProperty( name='N1',                   default=1.0 )
    m_N2                  : bpy.props.FloatProperty( name='N2',                   default=1.0 )
    m_RingRadius          : bpy.props.FloatProperty( name='RingRadius',           default=1.0 )
    m_XRadius             : bpy.props.FloatProperty( name='XRadius',              default=1.0 )
    m_YRadius             : bpy.props.FloatProperty( name='YRadius',              default=1.0 )
    m_ZRadius             : bpy.props.FloatProperty( name='ZRadius',              default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=21, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_CrossSectionRadius','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW','m_N1','m_N2','m_RingRadius','m_XRadius','m_YRadius','m_ZRadius',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricSuperToroid )        
TYPENAMES.append('VTKParametricSuperToroidType' )

#--------------------------------------------------------------
class VTKParametricTorus(Node, BVTK_Node):

    bl_idname = 'VTKParametricTorusType'
    bl_label  = 'vtkParametricTorus'
    
    m_ClockwiseOrdering   : bpy.props.BoolProperty ( name='ClockwiseOrdering',    default=True )
    m_DerivativesAvailable: bpy.props.BoolProperty ( name='DerivativesAvailable', default=True )
    m_JoinU               : bpy.props.BoolProperty ( name='JoinU',                default=True )
    m_JoinV               : bpy.props.BoolProperty ( name='JoinV',                default=True )
    m_JoinW               : bpy.props.BoolProperty ( name='JoinW',                default=True )
    m_TwistU              : bpy.props.BoolProperty ( name='TwistU',               default=True )
    m_TwistV              : bpy.props.BoolProperty ( name='TwistV',               default=True )
    m_TwistW              : bpy.props.BoolProperty ( name='TwistW',               default=True )
    m_CrossSectionRadius  : bpy.props.FloatProperty( name='CrossSectionRadius',   default=0.5 )
    m_MaximumU            : bpy.props.FloatProperty( name='MaximumU',             default=6.283185307179586 )
    m_MaximumV            : bpy.props.FloatProperty( name='MaximumV',             default=6.283185307179586 )
    m_MaximumW            : bpy.props.FloatProperty( name='MaximumW',             default=1.0 )
    m_MinimumU            : bpy.props.FloatProperty( name='MinimumU',             default=0.0 )
    m_MinimumV            : bpy.props.FloatProperty( name='MinimumV',             default=0.0 )
    m_MinimumW            : bpy.props.FloatProperty( name='MinimumW',             default=0.0 )
    m_RingRadius          : bpy.props.FloatProperty( name='RingRadius',           default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClockwiseOrdering','m_DerivativesAvailable','m_JoinU','m_JoinV','m_JoinW','m_TwistU','m_TwistV','m_TwistW','m_CrossSectionRadius','m_MaximumU','m_MaximumV','m_MaximumW','m_MinimumU','m_MinimumV','m_MinimumW','m_RingRadius',]
    def m_connections( self ):
        return ([], [], [], ['self']) 
    
add_class( VTKParametricTorus )        
TYPENAMES.append('VTKParametricTorusType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( BVTK_NodeCategory( 'ParametricFunc', 'ParametricFunc', items=menu_items) )