# Generated definitions for VTK class group: Transform
# VTK version: 8.1.2

from .core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKBSplineTransform(Node, BVTK_Node):

    bl_idname = 'VTKBSplineTransformType'
    bl_label  = 'vtkBSplineTransform'
    e_BorderMode_items=[ (x,x,x) for x in ['Edge', 'Zero', 'ZeroAtBorder']]
    
    m_InverseIterations: bpy.props.IntProperty  ( name='InverseIterations', default=500 )
    m_DisplacementScale: bpy.props.FloatProperty( name='DisplacementScale', default=1.0 )
    m_InverseTolerance : bpy.props.FloatProperty( name='InverseTolerance',  default=1e-06 )
    e_BorderMode       : bpy.props.EnumProperty ( name='BorderMode',        default="Edge", items=e_BorderMode_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_InverseIterations','m_DisplacementScale','m_InverseTolerance','e_BorderMode',]
    def m_connections( self ):
        return ([], [], ['Inverse', 'CoefficientData'], ['self']) 
    
add_class( VTKBSplineTransform )        
TYPENAMES.append('VTKBSplineTransformType' )

#--------------------------------------------------------------
class VTKCylindricalTransform(Node, BVTK_Node):

    bl_idname = 'VTKCylindricalTransformType'
    bl_label  = 'vtkCylindricalTransform'
    
    m_InverseIterations: bpy.props.IntProperty  ( name='InverseIterations', default=500 )
    m_InverseTolerance : bpy.props.FloatProperty( name='InverseTolerance',  default=0.001 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_InverseIterations','m_InverseTolerance',]
    def m_connections( self ):
        return ([], [], ['Inverse'], ['self']) 
    
add_class( VTKCylindricalTransform )        
TYPENAMES.append('VTKCylindricalTransformType' )

#--------------------------------------------------------------
class VTKGeneralTransform(Node, BVTK_Node):

    bl_idname = 'VTKGeneralTransformType'
    bl_label  = 'vtkGeneralTransform'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['Inverse', 'Input'], ['self']) 
    
add_class( VTKGeneralTransform )        
TYPENAMES.append('VTKGeneralTransformType' )

#--------------------------------------------------------------
class VTKGridTransform(Node, BVTK_Node):

    bl_idname = 'VTKGridTransformType'
    bl_label  = 'vtkGridTransform'
    e_InterpolationMode_items=[ (x,x,x) for x in ['NearestNeighbor', 'Linear', 'Cubic']]
    
    m_InverseIterations: bpy.props.IntProperty  ( name='InverseIterations', default=500 )
    m_DisplacementScale: bpy.props.FloatProperty( name='DisplacementScale', default=1.0 )
    m_DisplacementShift: bpy.props.FloatProperty( name='DisplacementShift', default=0.0 )
    m_InverseTolerance : bpy.props.FloatProperty( name='InverseTolerance',  default=0.01 )
    e_InterpolationMode: bpy.props.EnumProperty ( name='InterpolationMode', default="Linear", items=e_InterpolationMode_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_InverseIterations','m_DisplacementScale','m_DisplacementShift','m_InverseTolerance','e_InterpolationMode',]
    def m_connections( self ):
        return ([], [], ['Inverse'], ['self']) 
    
add_class( VTKGridTransform )        
TYPENAMES.append('VTKGridTransformType' )

#--------------------------------------------------------------
class VTKIdentityTransform(Node, BVTK_Node):

    bl_idname = 'VTKIdentityTransformType'
    bl_label  = 'vtkIdentityTransform'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['Inverse'], ['self']) 
    
add_class( VTKIdentityTransform )        
TYPENAMES.append('VTKIdentityTransformType' )

#--------------------------------------------------------------
class VTKIterativeClosestPointTransform(Node, BVTK_Node):

    bl_idname = 'VTKIterativeClosestPointTransformType'
    bl_label  = 'vtkIterativeClosestPointTransform'
    e_MeanDistanceMode_items=[ (x,x,x) for x in ['RMS', 'AbsoluteValue']]
    
    m_CheckMeanDistance        : bpy.props.BoolProperty ( name='CheckMeanDistance',         default=True )
    m_StartByMatchingCentroids : bpy.props.BoolProperty ( name='StartByMatchingCentroids',  default=True )
    m_MaximumNumberOfIterations: bpy.props.IntProperty  ( name='MaximumNumberOfIterations', default=50 )
    m_MaximumNumberOfLandmarks : bpy.props.IntProperty  ( name='MaximumNumberOfLandmarks',  default=200 )
    m_MaximumMeanDistance      : bpy.props.FloatProperty( name='MaximumMeanDistance',       default=0.01 )
    e_MeanDistanceMode         : bpy.props.EnumProperty ( name='MeanDistanceMode',          default="RMS", items=e_MeanDistanceMode_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CheckMeanDistance','m_StartByMatchingCentroids','m_MaximumNumberOfIterations','m_MaximumNumberOfLandmarks','m_MaximumMeanDistance','e_MeanDistanceMode',]
    def m_connections( self ):
        return ([], [], ['Inverse', 'Source', 'Target'], ['self']) 
    
add_class( VTKIterativeClosestPointTransform )        
TYPENAMES.append('VTKIterativeClosestPointTransformType' )

#--------------------------------------------------------------
class VTKLandmarkTransform(Node, BVTK_Node):

    bl_idname = 'VTKLandmarkTransformType'
    bl_label  = 'vtkLandmarkTransform'
    e_Mode_items=[ (x,x,x) for x in ['RigidBody', 'Similarity', 'Affine']]
    
    e_Mode: bpy.props.EnumProperty( name='Mode', default="Similarity", items=e_Mode_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['e_Mode',]
    def m_connections( self ):
        return ([], [], ['Inverse', 'SourceLandmarks', 'TargetLandmarks'], ['self']) 
    
add_class( VTKLandmarkTransform )        
TYPENAMES.append('VTKLandmarkTransformType' )

#--------------------------------------------------------------
class VTKMatrixToHomogeneousTransform(Node, BVTK_Node):

    bl_idname = 'VTKMatrixToHomogeneousTransformType'
    bl_label  = 'vtkMatrixToHomogeneousTransform'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['Inverse', 'Input'], ['self']) 
    
add_class( VTKMatrixToHomogeneousTransform )        
TYPENAMES.append('VTKMatrixToHomogeneousTransformType' )

#--------------------------------------------------------------
class VTKMatrixToLinearTransform(Node, BVTK_Node):

    bl_idname = 'VTKMatrixToLinearTransformType'
    bl_label  = 'vtkMatrixToLinearTransform'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['Inverse', 'Input'], ['self']) 
    
add_class( VTKMatrixToLinearTransform )        
TYPENAMES.append('VTKMatrixToLinearTransformType' )

#--------------------------------------------------------------
class VTKPerspectiveTransform(Node, BVTK_Node):

    bl_idname = 'VTKPerspectiveTransformType'
    bl_label  = 'vtkPerspectiveTransform'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['Inverse', 'Input'], ['self']) 
    
add_class( VTKPerspectiveTransform )        
TYPENAMES.append('VTKPerspectiveTransformType' )

#--------------------------------------------------------------
class VTKSMPTransform(Node, BVTK_Node):

    bl_idname = 'VTKSMPTransformType'
    bl_label  = 'vtkSMPTransform'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['Input'], ['self']) 
    
add_class( VTKSMPTransform )        
TYPENAMES.append('VTKSMPTransformType' )

#--------------------------------------------------------------
class VTKSphericalTransform(Node, BVTK_Node):

    bl_idname = 'VTKSphericalTransformType'
    bl_label  = 'vtkSphericalTransform'
    
    m_InverseIterations: bpy.props.IntProperty  ( name='InverseIterations', default=500 )
    m_InverseTolerance : bpy.props.FloatProperty( name='InverseTolerance',  default=0.001 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_InverseIterations','m_InverseTolerance',]
    def m_connections( self ):
        return ([], [], ['Inverse'], ['self']) 
    
add_class( VTKSphericalTransform )        
TYPENAMES.append('VTKSphericalTransformType' )

#--------------------------------------------------------------
class VTKThinPlateSplineTransform(Node, BVTK_Node):

    bl_idname = 'VTKThinPlateSplineTransformType'
    bl_label  = 'vtkThinPlateSplineTransform'
    e_Basis_items=[ (x,x,x) for x in ['R', 'R2LogR']]
    
    m_InverseIterations: bpy.props.IntProperty  ( name='InverseIterations', default=500 )
    m_InverseTolerance : bpy.props.FloatProperty( name='InverseTolerance',  default=0.001 )
    m_Sigma            : bpy.props.FloatProperty( name='Sigma',             default=1.0 )
    e_Basis            : bpy.props.EnumProperty ( name='Basis',             default="R2LogR", items=e_Basis_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_InverseIterations','m_InverseTolerance','m_Sigma','e_Basis',]
    def m_connections( self ):
        return ([], [], ['Inverse', 'SourceLandmarks', 'TargetLandmarks'], ['self']) 
    
add_class( VTKThinPlateSplineTransform )        
TYPENAMES.append('VTKThinPlateSplineTransformType' )

#--------------------------------------------------------------
class VTKTransform(Node, BVTK_Node):

    bl_idname = 'VTKTransformType'
    bl_label  = 'vtkTransform'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['Input'], ['self']) 
    
add_class( VTKTransform )        
TYPENAMES.append('VTKTransformType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( BVTK_NodeCategory( 'Transform', 'Transform', items=menu_items) )