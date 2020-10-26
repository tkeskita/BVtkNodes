# Generated definitions for VTK class group: Filter1
# VTK Version: 8.1.2

from ..core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKAMRCutPlane(Node, BVTK_Node):

    bl_idname = 'VTKAMRCutPlaneType'
    bl_label  = 'vtkAMRCutPlane'
    
    m_UseNativeCutter  : bpy.props.BoolProperty( name='UseNativeCutter',   default=True )
    m_LevelOfResolution: bpy.props.IntProperty ( name='LevelOfResolution', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseNativeCutter','m_LevelOfResolution',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAMRCutPlane )        
TYPENAMES.append('VTKAMRCutPlaneType' )

#--------------------------------------------------------------
class VTKAMRResampleFilter(Node, BVTK_Node):

    bl_idname = 'VTKAMRResampleFilterType'
    bl_label  = 'vtkAMRResampleFilter'
    
    m_UseBiasVector     : bpy.props.BoolProperty       ( name='UseBiasVector',      default=False )
    m_DemandDrivenMode  : bpy.props.IntProperty        ( name='DemandDrivenMode',   default=0 )
    m_NumberOfPartitions: bpy.props.IntProperty        ( name='NumberOfPartitions', default=1 )
    m_TransferToNodes   : bpy.props.IntProperty        ( name='TransferToNodes',    default=1 )
    m_NumberOfSamples   : bpy.props.IntVectorProperty  ( name='NumberOfSamples',    default=[10, 10, 10], size=3 )
    m_BiasVector        : bpy.props.FloatVectorProperty( name='BiasVector',         default=[0.0, 0.0, 0.0], size=3 )
    m_Max               : bpy.props.FloatVectorProperty( name='Max',                default=[1.0, 1.0, 1.0], size=3 )
    m_Min               : bpy.props.FloatVectorProperty( name='Min',                default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseBiasVector','m_DemandDrivenMode','m_NumberOfPartitions','m_TransferToNodes','m_NumberOfSamples','m_BiasVector','m_Max','m_Min',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAMRResampleFilter )        
TYPENAMES.append('VTKAMRResampleFilterType' )

#--------------------------------------------------------------
class VTKAMRSliceFilter(Node, BVTK_Node):

    bl_idname = 'VTKAMRSliceFilterType'
    bl_label  = 'vtkAMRSliceFilter'
    
    m_EnablePrefetching: bpy.props.BoolProperty ( name='EnablePrefetching', default=True )
    m_ForwardUpstream  : bpy.props.BoolProperty ( name='ForwardUpstream',   default=True )
    m_MaxResolution    : bpy.props.IntProperty  ( name='MaxResolution',     default=1 )
    m_Normal           : bpy.props.IntProperty  ( name='Normal',            default=1 )
    m_OffSetFromOrigin : bpy.props.FloatProperty( name='OffSetFromOrigin',  default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnablePrefetching','m_ForwardUpstream','m_MaxResolution','m_Normal','m_OffSetFromOrigin',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAMRSliceFilter )        
TYPENAMES.append('VTKAMRSliceFilterType' )

#--------------------------------------------------------------
class VTKAMRToMultiBlockFilter(Node, BVTK_Node):

    bl_idname = 'VTKAMRToMultiBlockFilterType'
    bl_label  = 'vtkAMRToMultiBlockFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAMRToMultiBlockFilter )        
TYPENAMES.append('VTKAMRToMultiBlockFilterType' )

#--------------------------------------------------------------
class VTKAdaptiveDataSetSurfaceFilter(Node, BVTK_Node):

    bl_idname = 'VTKAdaptiveDataSetSurfaceFilterType'
    bl_label  = 'vtkAdaptiveDataSetSurfaceFilter'
    
    m_PassThroughCellIds       : bpy.props.BoolProperty  ( name='PassThroughCellIds',        default=True )
    m_PassThroughPointIds      : bpy.props.BoolProperty  ( name='PassThroughPointIds',       default=True )
    m_UseStrips                : bpy.props.BoolProperty  ( name='UseStrips',                 default=True )
    m_OriginalCellIdsName      : bpy.props.StringProperty( name='OriginalCellIdsName',       default="vtkOriginalCellIds" )
    m_OriginalPointIdsName     : bpy.props.StringProperty( name='OriginalPointIdsName',      default="vtkOriginalPointIds" )
    m_NonlinearSubdivisionLevel: bpy.props.IntProperty   ( name='NonlinearSubdivisionLevel', default=1 )
    m_PieceInvariant           : bpy.props.IntProperty   ( name='PieceInvariant',            default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassThroughCellIds','m_PassThroughPointIds','m_UseStrips','m_OriginalCellIdsName','m_OriginalPointIdsName','m_NonlinearSubdivisionLevel','m_PieceInvariant',]
    def m_connections( self ):
        return (['input'], ['output'], ['Renderer'], []) 
    
add_class( VTKAdaptiveDataSetSurfaceFilter )        
TYPENAMES.append('VTKAdaptiveDataSetSurfaceFilterType' )

#--------------------------------------------------------------
class VTKAdaptiveSubdivisionFilter(Node, BVTK_Node):

    bl_idname = 'VTKAdaptiveSubdivisionFilterType'
    bl_label  = 'vtkAdaptiveSubdivisionFilter'
    
    m_MaximumNumberOfPasses   : bpy.props.IntProperty  ( name='MaximumNumberOfPasses',    default=1000000000 )
    m_MaximumNumberOfTriangles: bpy.props.IntProperty  ( name='MaximumNumberOfTriangles', default=1000000000 )
    m_MaximumEdgeLength       : bpy.props.FloatProperty( name='MaximumEdgeLength',        default=1.0 )
    m_MaximumTriangleArea     : bpy.props.FloatProperty( name='MaximumTriangleArea',      default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_MaximumNumberOfPasses','m_MaximumNumberOfTriangles','m_MaximumEdgeLength','m_MaximumTriangleArea',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAdaptiveSubdivisionFilter )        
TYPENAMES.append('VTKAdaptiveSubdivisionFilterType' )

#--------------------------------------------------------------
class VTKAggregateDataSetFilter(Node, BVTK_Node):

    bl_idname = 'VTKAggregateDataSetFilterType'
    bl_label  = 'vtkAggregateDataSetFilter'
    
    m_NumberOfTargetProcesses: bpy.props.IntProperty( name='NumberOfTargetProcesses', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NumberOfTargetProcesses',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAggregateDataSetFilter )        
TYPENAMES.append('VTKAggregateDataSetFilterType' )

#--------------------------------------------------------------
class VTKAngularPeriodicFilter(Node, BVTK_Node):

    bl_idname = 'VTKAngularPeriodicFilterType'
    bl_label  = 'vtkAngularPeriodicFilter'
    e_IterationMode_items=[ (x,x,x) for x in ['DirectNb', 'Max']]
    e_RotationAxis_items=[ (x,x,x) for x in ['X', 'Y', 'Z']]
    e_RotationMode_items=[ (x,x,x) for x in ['DirectAngle', 'ArrayValue']]
    
    m_ComputeRotationsOnTheFly: bpy.props.BoolProperty       ( name='ComputeRotationsOnTheFly', default=True )
    m_RotationArrayName       : bpy.props.StringProperty     ( name='RotationArrayName',        default="" )
    m_NumberOfPeriods         : bpy.props.IntProperty        ( name='NumberOfPeriods',          default=1 )
    m_RotationAngle           : bpy.props.FloatProperty      ( name='RotationAngle',            default=180.0 )
    e_IterationMode           : bpy.props.EnumProperty       ( name='IterationMode',            default="Max", items=e_IterationMode_items )
    e_RotationAxis            : bpy.props.EnumProperty       ( name='RotationAxis',             default="X", items=e_RotationAxis_items )
    e_RotationMode            : bpy.props.EnumProperty       ( name='RotationMode',             default="DirectAngle", items=e_RotationMode_items )
    m_Center                  : bpy.props.FloatVectorProperty( name='Center',                   default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeRotationsOnTheFly','m_RotationArrayName','m_NumberOfPeriods','m_RotationAngle','e_IterationMode','e_RotationAxis','e_RotationMode','m_Center',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAngularPeriodicFilter )        
TYPENAMES.append('VTKAngularPeriodicFilterType' )

#--------------------------------------------------------------
class VTKAnnotationLayersAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKAnnotationLayersAlgorithmType'
    bl_label  = 'vtkAnnotationLayersAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAnnotationLayersAlgorithm )        
TYPENAMES.append('VTKAnnotationLayersAlgorithmType' )

#--------------------------------------------------------------
class VTKAppendArcLength(Node, BVTK_Node):

    bl_idname = 'VTKAppendArcLengthType'
    bl_label  = 'vtkAppendArcLength'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAppendArcLength )        
TYPENAMES.append('VTKAppendArcLengthType' )

#--------------------------------------------------------------
class VTKAppendCompositeDataLeaves(Node, BVTK_Node):

    bl_idname = 'VTKAppendCompositeDataLeavesType'
    bl_label  = 'vtkAppendCompositeDataLeaves'
    
    m_AppendFieldData: bpy.props.BoolProperty( name='AppendFieldData', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AppendFieldData',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAppendCompositeDataLeaves )        
TYPENAMES.append('VTKAppendCompositeDataLeavesType' )

#--------------------------------------------------------------
class VTKAppendFilter(Node, BVTK_Node):

    bl_idname = 'VTKAppendFilterType'
    bl_label  = 'vtkAppendFilter'
    
    m_MergePoints: bpy.props.BoolProperty( name='MergePoints', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_MergePoints',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAppendFilter )        
TYPENAMES.append('VTKAppendFilterType' )

#--------------------------------------------------------------
class VTKAppendPoints(Node, BVTK_Node):

    bl_idname = 'VTKAppendPointsType'
    bl_label  = 'vtkAppendPoints'
    
    m_InputIdArrayName: bpy.props.StringProperty( name='InputIdArrayName', default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_InputIdArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAppendPoints )        
TYPENAMES.append('VTKAppendPointsType' )

#--------------------------------------------------------------
class VTKAppendPolyData(Node, BVTK_Node):

    bl_idname = 'VTKAppendPolyDataType'
    bl_label  = 'vtkAppendPolyData'
    
    m_ParallelStreaming: bpy.props.BoolProperty( name='ParallelStreaming', default=True )
    m_UserManagedInputs: bpy.props.BoolProperty( name='UserManagedInputs', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ParallelStreaming','m_UserManagedInputs',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAppendPolyData )        
TYPENAMES.append('VTKAppendPolyDataType' )

#--------------------------------------------------------------
class VTKAppendSelection(Node, BVTK_Node):

    bl_idname = 'VTKAppendSelectionType'
    bl_label  = 'vtkAppendSelection'
    
    m_AppendByUnion    : bpy.props.BoolProperty( name='AppendByUnion',     default=True )
    m_UserManagedInputs: bpy.props.BoolProperty( name='UserManagedInputs', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AppendByUnion','m_UserManagedInputs',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAppendSelection )        
TYPENAMES.append('VTKAppendSelectionType' )

#--------------------------------------------------------------
class VTKArcPlotter(Node, BVTK_Node):

    bl_idname = 'VTKArcPlotterType'
    bl_label  = 'vtkArcPlotter'
    e_PlotMode_items=[ (x,x,x) for x in ['PlotScalars', 'PlotVectors', 'PlotNormals', 'PlotTCoords', 'PlotTensors', 'PlotFieldData']]
    
    m_UseDefaultNormal: bpy.props.BoolProperty       ( name='UseDefaultNormal', default=True )
    m_FieldDataArray  : bpy.props.IntProperty        ( name='FieldDataArray',   default=0 )
    m_PlotComponent   : bpy.props.IntProperty        ( name='PlotComponent',    default=-1 )
    m_Height          : bpy.props.FloatProperty      ( name='Height',           default=0.5 )
    m_Offset          : bpy.props.FloatProperty      ( name='Offset',           default=0.0 )
    m_Radius          : bpy.props.FloatProperty      ( name='Radius',           default=0.5 )
    e_PlotMode        : bpy.props.EnumProperty       ( name='PlotMode',         default="PlotScalars", items=e_PlotMode_items )
    m_DefaultNormal   : bpy.props.FloatVectorProperty( name='DefaultNormal',    default=[0.0, 0.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseDefaultNormal','m_FieldDataArray','m_PlotComponent','m_Height','m_Offset','m_Radius','e_PlotMode','m_DefaultNormal',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKArcPlotter )        
TYPENAMES.append('VTKArcPlotterType' )

#--------------------------------------------------------------
class VTKArrayCalculator(Node, BVTK_Node):

    bl_idname = 'VTKArrayCalculatorType'
    bl_label  = 'vtkArrayCalculator'
    e_AttributeMode_items=[ (x,x,x) for x in ['Default', 'UsePointData', 'UseCellData', 'UseVertexData', 'UseEdgeData']]
    e_AttributeType_items=[ (x,x,x) for x in ['Default', 'PointData', 'CellData', 'VertexData', 'EdgeData', 'RowData']]
    
    m_CoordinateResults   : bpy.props.BoolProperty  ( name='CoordinateResults',    default=True )
    m_ReplaceInvalidValues: bpy.props.BoolProperty  ( name='ReplaceInvalidValues', default=True )
    m_ResultNormals       : bpy.props.BoolProperty  ( name='ResultNormals',        default=False )
    m_ResultTCoords       : bpy.props.BoolProperty  ( name='ResultTCoords',        default=False )
    m_Function            : bpy.props.StringProperty( name='Function',             default="" )
    m_ResultArrayName     : bpy.props.StringProperty( name='ResultArrayName',      default="resultArray" )
    m_ResultArrayType     : bpy.props.IntProperty   ( name='ResultArrayType',      default=11 )
    m_ReplacementValue    : bpy.props.FloatProperty ( name='ReplacementValue',     default=0.0 )
    e_AttributeMode       : bpy.props.EnumProperty  ( name='AttributeMode',        default="Default", items=e_AttributeMode_items )
    e_AttributeType       : bpy.props.EnumProperty  ( name='AttributeType',        default="VertexData", items=e_AttributeType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CoordinateResults','m_ReplaceInvalidValues','m_ResultNormals','m_ResultTCoords','m_Function','m_ResultArrayName','m_ResultArrayType','m_ReplacementValue','e_AttributeMode','e_AttributeType',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKArrayCalculator )        
TYPENAMES.append('VTKArrayCalculatorType' )

#--------------------------------------------------------------
class VTKArrayDataAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKArrayDataAlgorithmType'
    bl_label  = 'vtkArrayDataAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKArrayDataAlgorithm )        
TYPENAMES.append('VTKArrayDataAlgorithmType' )

#--------------------------------------------------------------
class VTKAssignAttribute(Node, BVTK_Node):

    bl_idname = 'VTKAssignAttributeType'
    bl_label  = 'vtkAssignAttribute'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAssignAttribute )        
TYPENAMES.append('VTKAssignAttributeType' )

#--------------------------------------------------------------
class VTKAttributeDataToFieldDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKAttributeDataToFieldDataFilterType'
    bl_label  = 'vtkAttributeDataToFieldDataFilter'
    
    m_PassAttributeData: bpy.props.BoolProperty( name='PassAttributeData', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassAttributeData',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKAttributeDataToFieldDataFilter )        
TYPENAMES.append('VTKAttributeDataToFieldDataFilterType' )

#--------------------------------------------------------------
class VTKBlankStructuredGrid(Node, BVTK_Node):

    bl_idname = 'VTKBlankStructuredGridType'
    bl_label  = 'vtkBlankStructuredGrid'
    
    m_ArrayName       : bpy.props.StringProperty( name='ArrayName',        default="" )
    m_ArrayId         : bpy.props.IntProperty   ( name='ArrayId',          default=-1 )
    m_Component       : bpy.props.IntProperty   ( name='Component',        default=0 )
    m_MaxBlankingValue: bpy.props.FloatProperty ( name='MaxBlankingValue', default=1e+30 )
    m_MinBlankingValue: bpy.props.FloatProperty ( name='MinBlankingValue', default=1e+30 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ArrayName','m_ArrayId','m_Component','m_MaxBlankingValue','m_MinBlankingValue',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKBlankStructuredGrid )        
TYPENAMES.append('VTKBlankStructuredGridType' )

#--------------------------------------------------------------
class VTKBlockIdScalars(Node, BVTK_Node):

    bl_idname = 'VTKBlockIdScalarsType'
    bl_label  = 'vtkBlockIdScalars'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKBlockIdScalars )        
TYPENAMES.append('VTKBlockIdScalarsType' )

#--------------------------------------------------------------
class VTKBrownianPoints(Node, BVTK_Node):

    bl_idname = 'VTKBrownianPointsType'
    bl_label  = 'vtkBrownianPoints'
    
    m_MaximumSpeed: bpy.props.FloatProperty( name='MaximumSpeed', default=1.0 )
    m_MinimumSpeed: bpy.props.FloatProperty( name='MinimumSpeed', default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_MaximumSpeed','m_MinimumSpeed',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKBrownianPoints )        
TYPENAMES.append('VTKBrownianPointsType' )

#--------------------------------------------------------------
class VTKButterflySubdivisionFilter(Node, BVTK_Node):

    bl_idname = 'VTKButterflySubdivisionFilterType'
    bl_label  = 'vtkButterflySubdivisionFilter'
    
    m_CheckForTriangles   : bpy.props.BoolProperty( name='CheckForTriangles',    default=True )
    m_NumberOfSubdivisions: bpy.props.IntProperty ( name='NumberOfSubdivisions', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CheckForTriangles','m_NumberOfSubdivisions',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKButterflySubdivisionFilter )        
TYPENAMES.append('VTKButterflySubdivisionFilterType' )

#--------------------------------------------------------------
class VTKCastToConcrete(Node, BVTK_Node):

    bl_idname = 'VTKCastToConcreteType'
    bl_label  = 'vtkCastToConcrete'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCastToConcrete )        
TYPENAMES.append('VTKCastToConcreteType' )

#--------------------------------------------------------------
class VTKCellCenters(Node, BVTK_Node):

    bl_idname = 'VTKCellCentersType'
    bl_label  = 'vtkCellCenters'
    
    m_VertexCells: bpy.props.BoolProperty( name='VertexCells', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_VertexCells',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCellCenters )        
TYPENAMES.append('VTKCellCentersType' )

#--------------------------------------------------------------
class VTKCellDataToPointData(Node, BVTK_Node):

    bl_idname = 'VTKCellDataToPointDataType'
    bl_label  = 'vtkCellDataToPointData'
    
    m_PassCellData          : bpy.props.BoolProperty( name='PassCellData',           default=True )
    m_ContributingCellOption: bpy.props.IntProperty ( name='ContributingCellOption', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassCellData','m_ContributingCellOption',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCellDataToPointData )        
TYPENAMES.append('VTKCellDataToPointDataType' )

#--------------------------------------------------------------
class VTKCellDerivatives(Node, BVTK_Node):

    bl_idname = 'VTKCellDerivativesType'
    bl_label  = 'vtkCellDerivatives'
    e_TensorMode_items=[ (x,x,x) for x in ['PassTensors', 'ComputeGradient', 'ComputeStrain', 'ComputeGreenLagrangeStrain']]
    e_VectorMode_items=[ (x,x,x) for x in ['PassVectors', 'ComputeGradient', 'ComputeVorticity']]
    
    e_TensorMode: bpy.props.EnumProperty( name='TensorMode', default="ComputeGradient", items=e_TensorMode_items )
    e_VectorMode: bpy.props.EnumProperty( name='VectorMode', default="ComputeGradient", items=e_VectorMode_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['e_TensorMode','e_VectorMode',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCellDerivatives )        
TYPENAMES.append('VTKCellDerivativesType' )

#--------------------------------------------------------------
class VTKCellQuality(Node, BVTK_Node):

    bl_idname = 'VTKCellQualityType'
    bl_label  = 'vtkCellQuality'
    e_QualityMeasure_items=[ (x,x,x) for x in ['Area', 'AspectBeta', 'AspectFrobenius', 'AspectGamma', 'AspectRatio', 'CollapseRatio', 'Condition', 'Diagonal', 'Dimension', 'Distortion', 'Jacobian', 'MaxAngle', 'MaxAspectFrobenius', 'MaxEdgeRatio', 'MedAspectFrobenius', 'MinAngle', 'Oddy', 'RadiusRatio', 'RelativeSizeSquared', 'ScaledJacobian', 'Shape', 'ShapeAndSize', 'Shear', 'ShearAndSize', 'Skew', 'Stretch', 'Taper', 'Volume', 'Warpage']]
    
    m_UndefinedQuality   : bpy.props.FloatProperty( name='UndefinedQuality',    default=-1.0 )
    m_UnsupportedGeometry: bpy.props.FloatProperty( name='UnsupportedGeometry', default=-1.0 )
    e_QualityMeasure     : bpy.props.EnumProperty ( name='QualityMeasure',      default="Area", items=e_QualityMeasure_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UndefinedQuality','m_UnsupportedGeometry','e_QualityMeasure',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCellQuality )        
TYPENAMES.append('VTKCellQualityType' )

#--------------------------------------------------------------
class VTKCellSizeFilter(Node, BVTK_Node):

    bl_idname = 'VTKCellSizeFilterType'
    bl_label  = 'vtkCellSizeFilter'
    
    m_ComputeArea         : bpy.props.BoolProperty  ( name='ComputeArea',          default=True )
    m_ComputeLength       : bpy.props.BoolProperty  ( name='ComputeLength',        default=True )
    m_ComputeSum          : bpy.props.BoolProperty  ( name='ComputeSum',           default=False )
    m_ComputeVertexCount  : bpy.props.BoolProperty  ( name='ComputeVertexCount',   default=True )
    m_ComputeVolume       : bpy.props.BoolProperty  ( name='ComputeVolume',        default=True )
    m_AreaArrayName       : bpy.props.StringProperty( name='AreaArrayName',        default="Area" )
    m_LengthArrayName     : bpy.props.StringProperty( name='LengthArrayName',      default="Length" )
    m_VertexCountArrayName: bpy.props.StringProperty( name='VertexCountArrayName', default="VertexCount" )
    m_VolumeArrayName     : bpy.props.StringProperty( name='VolumeArrayName',      default="Volume" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeArea','m_ComputeLength','m_ComputeSum','m_ComputeVertexCount','m_ComputeVolume','m_AreaArrayName','m_LengthArrayName','m_VertexCountArrayName','m_VolumeArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCellSizeFilter )        
TYPENAMES.append('VTKCellSizeFilterType' )

#--------------------------------------------------------------
class VTKCheckerboardSplatter(Node, BVTK_Node):

    bl_idname = 'VTKCheckerboardSplatterType'
    bl_label  = 'vtkCheckerboardSplatter'
    e_AccumulationMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Sum']]
    e_OutputScalarType_items=[ (x,x,x) for x in ['Float', 'Double']]
    
    m_Capping               : bpy.props.BoolProperty       ( name='Capping',                default=True )
    m_NormalWarping         : bpy.props.BoolProperty       ( name='NormalWarping',          default=True )
    m_ScalarWarping         : bpy.props.BoolProperty       ( name='ScalarWarping',          default=True )
    m_Footprint             : bpy.props.IntProperty        ( name='Footprint',              default=2 )
    m_MaximumDimension      : bpy.props.IntProperty        ( name='MaximumDimension',       default=50 )
    m_ParallelSplatCrossover: bpy.props.IntProperty        ( name='ParallelSplatCrossover', default=2 )
    m_CapValue              : bpy.props.FloatProperty      ( name='CapValue',               default=0.0 )
    m_Eccentricity          : bpy.props.FloatProperty      ( name='Eccentricity',           default=2.5 )
    m_ExponentFactor        : bpy.props.FloatProperty      ( name='ExponentFactor',         default=-5.0 )
    m_NullValue             : bpy.props.FloatProperty      ( name='NullValue',              default=0.0 )
    m_Radius                : bpy.props.FloatProperty      ( name='Radius',                 default=0.0 )
    m_ScaleFactor           : bpy.props.FloatProperty      ( name='ScaleFactor',            default=1.0 )
    e_AccumulationMode      : bpy.props.EnumProperty       ( name='AccumulationMode',       default="Max", items=e_AccumulationMode_items )
    e_OutputScalarType      : bpy.props.EnumProperty       ( name='OutputScalarType',       default="Float", items=e_OutputScalarType_items )
    m_SampleDimensions      : bpy.props.IntVectorProperty  ( name='SampleDimensions',       default=[50, 50, 50], size=3 )
    m_ModelBounds           : bpy.props.FloatVectorProperty( name='ModelBounds',            default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Capping','m_NormalWarping','m_ScalarWarping','m_Footprint','m_MaximumDimension','m_ParallelSplatCrossover','m_CapValue','m_Eccentricity','m_ExponentFactor','m_NullValue','m_Radius','m_ScaleFactor','e_AccumulationMode','e_OutputScalarType','m_SampleDimensions','m_ModelBounds',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCheckerboardSplatter )        
TYPENAMES.append('VTKCheckerboardSplatterType' )

#--------------------------------------------------------------
class VTKCleanPolyData(Node, BVTK_Node):

    bl_idname = 'VTKCleanPolyDataType'
    bl_label  = 'vtkCleanPolyData'
    
    m_ConvertLinesToPoints: bpy.props.BoolProperty ( name='ConvertLinesToPoints', default=True )
    m_ConvertPolysToLines : bpy.props.BoolProperty ( name='ConvertPolysToLines',  default=True )
    m_ConvertStripsToPolys: bpy.props.BoolProperty ( name='ConvertStripsToPolys', default=True )
    m_PieceInvariant      : bpy.props.BoolProperty ( name='PieceInvariant',       default=True )
    m_PointMerging        : bpy.props.BoolProperty ( name='PointMerging',         default=True )
    m_ToleranceIsAbsolute : bpy.props.BoolProperty ( name='ToleranceIsAbsolute',  default=True )
    m_AbsoluteTolerance   : bpy.props.FloatProperty( name='AbsoluteTolerance',    default=1.0 )
    m_Tolerance           : bpy.props.FloatProperty( name='Tolerance',            default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ConvertLinesToPoints','m_ConvertPolysToLines','m_ConvertStripsToPolys','m_PieceInvariant','m_PointMerging','m_ToleranceIsAbsolute','m_AbsoluteTolerance','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCleanPolyData )        
TYPENAMES.append('VTKCleanPolyDataType' )

#--------------------------------------------------------------
class VTKClipClosedSurface(Node, BVTK_Node):

    bl_idname = 'VTKClipClosedSurfaceType'
    bl_label  = 'vtkClipClosedSurface'
    e_ScalarMode_items=[ (x,x,x) for x in ['None', 'Colors', 'Labels']]
    
    m_GenerateFaces            : bpy.props.BoolProperty       ( name='GenerateFaces',             default=True )
    m_GenerateOutline          : bpy.props.BoolProperty       ( name='GenerateOutline',           default=True )
    m_PassPointData            : bpy.props.BoolProperty       ( name='PassPointData',             default=True )
    m_TriangulationErrorDisplay: bpy.props.BoolProperty       ( name='TriangulationErrorDisplay', default=True )
    m_ActivePlaneId            : bpy.props.IntProperty        ( name='ActivePlaneId',             default=-1 )
    m_Tolerance                : bpy.props.FloatProperty      ( name='Tolerance',                 default=1e-06 )
    e_ScalarMode               : bpy.props.EnumProperty       ( name='ScalarMode',                default="None", items=e_ScalarMode_items )
    m_ActivePlaneColor         : bpy.props.FloatVectorProperty( name='ActivePlaneColor',          default=[1.0, 1.0, 0.0], size=3 )
    m_BaseColor                : bpy.props.FloatVectorProperty( name='BaseColor',                 default=[1.0, 0.0, 0.0], size=3 )
    m_ClipColor                : bpy.props.FloatVectorProperty( name='ClipColor',                 default=[1.0, 0.5, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateFaces','m_GenerateOutline','m_PassPointData','m_TriangulationErrorDisplay','m_ActivePlaneId','m_Tolerance','e_ScalarMode','m_ActivePlaneColor','m_BaseColor','m_ClipColor',]
    def m_connections( self ):
        return (['input'], ['output'], ['ClippingPlanes'], []) 
    
add_class( VTKClipClosedSurface )        
TYPENAMES.append('VTKClipClosedSurfaceType' )

#--------------------------------------------------------------
class VTKClipConvexPolyData(Node, BVTK_Node):

    bl_idname = 'VTKClipConvexPolyDataType'
    bl_label  = 'vtkClipConvexPolyData'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], ['Planes'], []) 
    
add_class( VTKClipConvexPolyData )        
TYPENAMES.append('VTKClipConvexPolyDataType' )

#--------------------------------------------------------------
class VTKCollectGraph(Node, BVTK_Node):

    bl_idname = 'VTKCollectGraphType'
    bl_label  = 'vtkCollectGraph'
    
    m_PassThrough: bpy.props.BoolProperty( name='PassThrough', default=True )
    m_OutputType : bpy.props.IntProperty ( name='OutputType',  default=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassThrough','m_OutputType',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCollectGraph )        
TYPENAMES.append('VTKCollectGraphType' )

#--------------------------------------------------------------
class VTKCollectPolyData(Node, BVTK_Node):

    bl_idname = 'VTKCollectPolyDataType'
    bl_label  = 'vtkCollectPolyData'
    
    m_PassThrough: bpy.props.BoolProperty( name='PassThrough', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassThrough',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCollectPolyData )        
TYPENAMES.append('VTKCollectPolyDataType' )

#--------------------------------------------------------------
class VTKCollectTable(Node, BVTK_Node):

    bl_idname = 'VTKCollectTableType'
    bl_label  = 'vtkCollectTable'
    
    m_PassThrough: bpy.props.BoolProperty( name='PassThrough', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassThrough',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCollectTable )        
TYPENAMES.append('VTKCollectTableType' )

#--------------------------------------------------------------
class VTKCompositeCutter(Node, BVTK_Node):

    bl_idname = 'VTKCompositeCutterType'
    bl_label  = 'vtkCompositeCutter'
    e_SortBy_items=[ (x,x,x) for x in ['SortByValue', 'SortByCell']]
    
    m_GenerateCutScalars: bpy.props.BoolProperty( name='GenerateCutScalars', default=True )
    m_GenerateTriangles : bpy.props.BoolProperty( name='GenerateTriangles',  default=True )
    m_NumberOfContours  : bpy.props.IntProperty ( name='NumberOfContours',   default=1 )
    e_SortBy            : bpy.props.EnumProperty( name='SortBy',             default="SortByValue", items=e_SortBy_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateCutScalars','m_GenerateTriangles','m_NumberOfContours','e_SortBy',]
    def m_connections( self ):
        return (['input'], ['output'], ['CutFunction'], []) 
    
add_class( VTKCompositeCutter )        
TYPENAMES.append('VTKCompositeCutterType' )

#--------------------------------------------------------------
class VTKCompositeDataGeometryFilter(Node, BVTK_Node):

    bl_idname = 'VTKCompositeDataGeometryFilterType'
    bl_label  = 'vtkCompositeDataGeometryFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCompositeDataGeometryFilter )        
TYPENAMES.append('VTKCompositeDataGeometryFilterType' )

#--------------------------------------------------------------
class VTKCompositeDataSetAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKCompositeDataSetAlgorithmType'
    bl_label  = 'vtkCompositeDataSetAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCompositeDataSetAlgorithm )        
TYPENAMES.append('VTKCompositeDataSetAlgorithmType' )

#--------------------------------------------------------------
class VTKComputeQuartiles(Node, BVTK_Node):

    bl_idname = 'VTKComputeQuartilesType'
    bl_label  = 'vtkComputeQuartiles'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKComputeQuartiles )        
TYPENAMES.append('VTKComputeQuartilesType' )

#--------------------------------------------------------------
class VTKConnectivityFilter(Node, BVTK_Node):

    bl_idname = 'VTKConnectivityFilterType'
    bl_label  = 'vtkConnectivityFilter'
    e_ExtractionMode_items=[ (x,x,x) for x in ['PointSeededRegions', 'CellSeededRegions', 'SpecifiedRegions', 'LargestRegion', 'AllRegions', 'ClosestPointRegion']]
    
    m_ColorRegions      : bpy.props.BoolProperty       ( name='ColorRegions',       default=True )
    m_ScalarConnectivity: bpy.props.BoolProperty       ( name='ScalarConnectivity', default=True )
    e_ExtractionMode    : bpy.props.EnumProperty       ( name='ExtractionMode',     default="LargestRegion", items=e_ExtractionMode_items )
    m_ClosestPoint      : bpy.props.FloatVectorProperty( name='ClosestPoint',       default=[0.0, 0.0, 0.0], size=3 )
    m_ScalarRange       : bpy.props.FloatVectorProperty( name='ScalarRange',        default=[0.0, 1.0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ColorRegions','m_ScalarConnectivity','e_ExtractionMode','m_ClosestPoint','m_ScalarRange',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKConnectivityFilter )        
TYPENAMES.append('VTKConnectivityFilterType' )

#--------------------------------------------------------------
class VTKContourFilter(Node, BVTK_Node):

    bl_idname = 'VTKContourFilterType'
    bl_label  = 'vtkContourFilter'
    
    m_ComputeGradients : bpy.props.BoolProperty( name='ComputeGradients',  default=True )
    m_ComputeNormals   : bpy.props.BoolProperty( name='ComputeNormals',    default=True )
    m_ComputeScalars   : bpy.props.BoolProperty( name='ComputeScalars',    default=True )
    m_GenerateTriangles: bpy.props.BoolProperty( name='GenerateTriangles', default=True )
    m_ArrayComponent   : bpy.props.IntProperty ( name='ArrayComponent',    default=0 )
    m_NumberOfContours : bpy.props.IntProperty ( name='NumberOfContours',  default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_GenerateTriangles','m_ArrayComponent','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKContourFilter )        
TYPENAMES.append('VTKContourFilterType' )

#--------------------------------------------------------------
class VTKContourGrid(Node, BVTK_Node):

    bl_idname = 'VTKContourGridType'
    bl_label  = 'vtkContourGrid'
    
    m_ComputeGradients : bpy.props.BoolProperty( name='ComputeGradients',  default=True )
    m_ComputeNormals   : bpy.props.BoolProperty( name='ComputeNormals',    default=True )
    m_ComputeScalars   : bpy.props.BoolProperty( name='ComputeScalars',    default=True )
    m_GenerateTriangles: bpy.props.BoolProperty( name='GenerateTriangles', default=True )
    m_NumberOfContours : bpy.props.IntProperty ( name='NumberOfContours',  default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_GenerateTriangles','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKContourGrid )        
TYPENAMES.append('VTKContourGridType' )

#--------------------------------------------------------------
class VTKContourLoopExtraction(Node, BVTK_Node):

    bl_idname = 'VTKContourLoopExtractionType'
    bl_label  = 'vtkContourLoopExtraction'
    e_LoopClosure_items=[ (x,x,x) for x in ['Off', 'Boundary', 'All']]
    
    m_ScalarThresholding: bpy.props.BoolProperty       ( name='ScalarThresholding', default=False )
    e_LoopClosure       : bpy.props.EnumProperty       ( name='LoopClosure',        default="Boundary", items=e_LoopClosure_items )
    m_Normal            : bpy.props.FloatVectorProperty( name='Normal',             default=[0.0, 0.0, 1.0], size=3 )
    m_ScalarRange       : bpy.props.FloatVectorProperty( name='ScalarRange',        default=[0.0, 1.0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ScalarThresholding','e_LoopClosure','m_Normal','m_ScalarRange',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKContourLoopExtraction )        
TYPENAMES.append('VTKContourLoopExtractionType' )

#--------------------------------------------------------------
class VTKContourTriangulator(Node, BVTK_Node):

    bl_idname = 'VTKContourTriangulatorType'
    bl_label  = 'vtkContourTriangulator'
    
    m_TriangulationErrorDisplay: bpy.props.BoolProperty( name='TriangulationErrorDisplay', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_TriangulationErrorDisplay',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKContourTriangulator )        
TYPENAMES.append('VTKContourTriangulatorType' )

#--------------------------------------------------------------
class VTKCountFaces(Node, BVTK_Node):

    bl_idname = 'VTKCountFacesType'
    bl_label  = 'vtkCountFaces'
    
    m_OutputArrayName: bpy.props.StringProperty( name='OutputArrayName', default="Face Count" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_OutputArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCountFaces )        
TYPENAMES.append('VTKCountFacesType' )

#--------------------------------------------------------------
class VTKCountVertices(Node, BVTK_Node):

    bl_idname = 'VTKCountVerticesType'
    bl_label  = 'vtkCountVertices'
    
    m_OutputArrayName: bpy.props.StringProperty( name='OutputArrayName', default="Vertex Count" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_OutputArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCountVertices )        
TYPENAMES.append('VTKCountVerticesType' )

#--------------------------------------------------------------
class VTKCurvatures(Node, BVTK_Node):

    bl_idname = 'VTKCurvaturesType'
    bl_label  = 'vtkCurvatures'
    e_CurvatureType_items=[ (x,x,x) for x in ['Gaussian', 'Mean', 'Maximum', 'Minimum']]
    
    m_InvertMeanCurvature: bpy.props.BoolProperty( name='InvertMeanCurvature', default=True )
    e_CurvatureType      : bpy.props.EnumProperty( name='CurvatureType',       default="Gaussian", items=e_CurvatureType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_InvertMeanCurvature','e_CurvatureType',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCurvatures )        
TYPENAMES.append('VTKCurvaturesType' )

#--------------------------------------------------------------
class VTKCutMaterial(Node, BVTK_Node):

    bl_idname = 'VTKCutMaterialType'
    bl_label  = 'vtkCutMaterial'
    
    m_ArrayName        : bpy.props.StringProperty     ( name='ArrayName',         default="" )
    m_MaterialArrayName: bpy.props.StringProperty     ( name='MaterialArrayName', default="material" )
    m_Material         : bpy.props.IntProperty        ( name='Material',          default=0 )
    m_UpVector         : bpy.props.FloatVectorProperty( name='UpVector',          default=[0.0, 0.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ArrayName','m_MaterialArrayName','m_Material','m_UpVector',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKCutMaterial )        
TYPENAMES.append('VTKCutMaterialType' )

#--------------------------------------------------------------
class VTKCutter(Node, BVTK_Node):

    bl_idname = 'VTKCutterType'
    bl_label  = 'vtkCutter'
    e_SortBy_items=[ (x,x,x) for x in ['SortByValue', 'SortByCell']]
    
    m_GenerateCutScalars: bpy.props.BoolProperty( name='GenerateCutScalars', default=True )
    m_GenerateTriangles : bpy.props.BoolProperty( name='GenerateTriangles',  default=True )
    m_NumberOfContours  : bpy.props.IntProperty ( name='NumberOfContours',   default=1 )
    e_SortBy            : bpy.props.EnumProperty( name='SortBy',             default="SortByValue", items=e_SortBy_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateCutScalars','m_GenerateTriangles','m_NumberOfContours','e_SortBy',]
    def m_connections( self ):
        return (['input'], ['output'], ['CutFunction'], []) 
    
add_class( VTKCutter )        
TYPENAMES.append('VTKCutterType' )

#--------------------------------------------------------------
class VTKDataObjectAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKDataObjectAlgorithmType'
    bl_label  = 'vtkDataObjectAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDataObjectAlgorithm )        
TYPENAMES.append('VTKDataObjectAlgorithmType' )

#--------------------------------------------------------------
class VTKDataObjectToDataSetFilter(Node, BVTK_Node):

    bl_idname = 'VTKDataObjectToDataSetFilterType'
    bl_label  = 'vtkDataObjectToDataSetFilter'
    e_DataSetType_items=[ (x,x,x) for x in ['PolyData', 'StructuredPoints', 'StructuredGrid', 'RectilinearGrid', 'UnstructuredGrid']]
    
    m_DefaultNormalize: bpy.props.BoolProperty       ( name='DefaultNormalize', default=True )
    e_DataSetType     : bpy.props.EnumProperty       ( name='DataSetType',      default="PolyData", items=e_DataSetType_items )
    m_Dimensions      : bpy.props.IntVectorProperty  ( name='Dimensions',       default=[0, 0, 0], size=3 )
    m_Origin          : bpy.props.FloatVectorProperty( name='Origin',           default=[0.0, 0.0, 0.0], size=3 )
    m_Spacing         : bpy.props.FloatVectorProperty( name='Spacing',          default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_DefaultNormalize','e_DataSetType','m_Dimensions','m_Origin','m_Spacing',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDataObjectToDataSetFilter )        
TYPENAMES.append('VTKDataObjectToDataSetFilterType' )

#--------------------------------------------------------------
class VTKDataSetAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKDataSetAlgorithmType'
    bl_label  = 'vtkDataSetAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDataSetAlgorithm )        
TYPENAMES.append('VTKDataSetAlgorithmType' )

#--------------------------------------------------------------
class VTKDataSetGradient(Node, BVTK_Node):

    bl_idname = 'VTKDataSetGradientType'
    bl_label  = 'vtkDataSetGradient'
    
    m_ResultArrayName: bpy.props.StringProperty( name='ResultArrayName', default="gradient" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ResultArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDataSetGradient )        
TYPENAMES.append('VTKDataSetGradientType' )

#--------------------------------------------------------------
class VTKDataSetGradientPrecompute(Node, BVTK_Node):

    bl_idname = 'VTKDataSetGradientPrecomputeType'
    bl_label  = 'vtkDataSetGradientPrecompute'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDataSetGradientPrecompute )        
TYPENAMES.append('VTKDataSetGradientPrecomputeType' )

#--------------------------------------------------------------
class VTKDataSetRegionSurfaceFilter(Node, BVTK_Node):

    bl_idname = 'VTKDataSetRegionSurfaceFilterType'
    bl_label  = 'vtkDataSetRegionSurfaceFilter'
    
    m_PassThroughCellIds       : bpy.props.BoolProperty  ( name='PassThroughCellIds',        default=True )
    m_PassThroughPointIds      : bpy.props.BoolProperty  ( name='PassThroughPointIds',       default=True )
    m_SingleSided              : bpy.props.BoolProperty  ( name='SingleSided',               default=True )
    m_UseStrips                : bpy.props.BoolProperty  ( name='UseStrips',                 default=True )
    m_InterfaceIDsName         : bpy.props.StringProperty( name='InterfaceIDsName',          default="interface_ids" )
    m_MaterialIDsName          : bpy.props.StringProperty( name='MaterialIDsName',           default="material_ids" )
    m_MaterialPIDsName         : bpy.props.StringProperty( name='MaterialPIDsName',          default="material_ancestors" )
    m_MaterialPropertiesName   : bpy.props.StringProperty( name='MaterialPropertiesName',    default="material_properties" )
    m_OriginalCellIdsName      : bpy.props.StringProperty( name='OriginalCellIdsName',       default="vtkOriginalCellIds" )
    m_OriginalPointIdsName     : bpy.props.StringProperty( name='OriginalPointIdsName',      default="vtkOriginalPointIds" )
    m_RegionArrayName          : bpy.props.StringProperty( name='RegionArrayName',           default="material" )
    m_NonlinearSubdivisionLevel: bpy.props.IntProperty   ( name='NonlinearSubdivisionLevel', default=1 )
    m_PieceInvariant           : bpy.props.IntProperty   ( name='PieceInvariant',            default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassThroughCellIds','m_PassThroughPointIds','m_SingleSided','m_UseStrips','m_InterfaceIDsName','m_MaterialIDsName','m_MaterialPIDsName','m_MaterialPropertiesName','m_OriginalCellIdsName','m_OriginalPointIdsName','m_RegionArrayName','m_NonlinearSubdivisionLevel','m_PieceInvariant',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDataSetRegionSurfaceFilter )        
TYPENAMES.append('VTKDataSetRegionSurfaceFilterType' )

#--------------------------------------------------------------
class VTKDataSetSurfaceFilter(Node, BVTK_Node):

    bl_idname = 'VTKDataSetSurfaceFilterType'
    bl_label  = 'vtkDataSetSurfaceFilter'
    
    m_PassThroughCellIds       : bpy.props.BoolProperty  ( name='PassThroughCellIds',        default=True )
    m_PassThroughPointIds      : bpy.props.BoolProperty  ( name='PassThroughPointIds',       default=True )
    m_UseStrips                : bpy.props.BoolProperty  ( name='UseStrips',                 default=True )
    m_OriginalCellIdsName      : bpy.props.StringProperty( name='OriginalCellIdsName',       default="vtkOriginalCellIds" )
    m_OriginalPointIdsName     : bpy.props.StringProperty( name='OriginalPointIdsName',      default="vtkOriginalPointIds" )
    m_NonlinearSubdivisionLevel: bpy.props.IntProperty   ( name='NonlinearSubdivisionLevel', default=1 )
    m_PieceInvariant           : bpy.props.IntProperty   ( name='PieceInvariant',            default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassThroughCellIds','m_PassThroughPointIds','m_UseStrips','m_OriginalCellIdsName','m_OriginalPointIdsName','m_NonlinearSubdivisionLevel','m_PieceInvariant',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDataSetSurfaceFilter )        
TYPENAMES.append('VTKDataSetSurfaceFilterType' )

#--------------------------------------------------------------
class VTKDataSetToDataObjectFilter(Node, BVTK_Node):

    bl_idname = 'VTKDataSetToDataObjectFilterType'
    bl_label  = 'vtkDataSetToDataObjectFilter'
    
    m_CellData : bpy.props.BoolProperty( name='CellData',  default=True )
    m_FieldData: bpy.props.BoolProperty( name='FieldData', default=True )
    m_Geometry : bpy.props.BoolProperty( name='Geometry',  default=True )
    m_PointData: bpy.props.BoolProperty( name='PointData', default=True )
    m_Topology : bpy.props.BoolProperty( name='Topology',  default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CellData','m_FieldData','m_Geometry','m_PointData','m_Topology',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDataSetToDataObjectFilter )        
TYPENAMES.append('VTKDataSetToDataObjectFilterType' )

#--------------------------------------------------------------
class VTKDataSetTriangleFilter(Node, BVTK_Node):

    bl_idname = 'VTKDataSetTriangleFilterType'
    bl_label  = 'vtkDataSetTriangleFilter'
    
    m_TetrahedraOnly: bpy.props.BoolProperty( name='TetrahedraOnly', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_TetrahedraOnly',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDataSetTriangleFilter )        
TYPENAMES.append('VTKDataSetTriangleFilterType' )

#--------------------------------------------------------------
class VTKDecimatePolylineFilter(Node, BVTK_Node):

    bl_idname = 'VTKDecimatePolylineFilterType'
    bl_label  = 'vtkDecimatePolylineFilter'
    
    m_TargetReduction: bpy.props.FloatProperty( name='TargetReduction', default=0.9 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_TargetReduction',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDecimatePolylineFilter )        
TYPENAMES.append('VTKDecimatePolylineFilterType' )

#--------------------------------------------------------------
class VTKDecimatePro(Node, BVTK_Node):

    bl_idname = 'VTKDecimateProType'
    bl_label  = 'vtkDecimatePro'
    
    m_AccumulateError       : bpy.props.BoolProperty ( name='AccumulateError',        default=True )
    m_BoundaryVertexDeletion: bpy.props.BoolProperty ( name='BoundaryVertexDeletion', default=True )
    m_PreSplitMesh          : bpy.props.BoolProperty ( name='PreSplitMesh',           default=True )
    m_PreserveTopology      : bpy.props.BoolProperty ( name='PreserveTopology',       default=True )
    m_Splitting             : bpy.props.BoolProperty ( name='Splitting',              default=True )
    m_Degree                : bpy.props.IntProperty  ( name='Degree',                 default=25 )
    m_ErrorIsAbsolute       : bpy.props.IntProperty  ( name='ErrorIsAbsolute',        default=0 )
    m_AbsoluteError         : bpy.props.FloatProperty( name='AbsoluteError',          default=1e+30 )
    m_FeatureAngle          : bpy.props.FloatProperty( name='FeatureAngle',           default=15.0 )
    m_InflectionPointRatio  : bpy.props.FloatProperty( name='InflectionPointRatio',   default=10.0 )
    m_MaximumError          : bpy.props.FloatProperty( name='MaximumError',           default=1e+30 )
    m_SplitAngle            : bpy.props.FloatProperty( name='SplitAngle',             default=75.0 )
    m_TargetReduction       : bpy.props.FloatProperty( name='TargetReduction',        default=0.9 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AccumulateError','m_BoundaryVertexDeletion','m_PreSplitMesh','m_PreserveTopology','m_Splitting','m_Degree','m_ErrorIsAbsolute','m_AbsoluteError','m_FeatureAngle','m_InflectionPointRatio','m_MaximumError','m_SplitAngle','m_TargetReduction',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDecimatePro )        
TYPENAMES.append('VTKDecimateProType' )

#--------------------------------------------------------------
class VTKDelaunay3D(Node, BVTK_Node):

    bl_idname = 'VTKDelaunay3DType'
    bl_label  = 'vtkDelaunay3D'
    
    m_AlphaLines           : bpy.props.BoolProperty ( name='AlphaLines',            default=True )
    m_AlphaTets            : bpy.props.BoolProperty ( name='AlphaTets',             default=True )
    m_AlphaTris            : bpy.props.BoolProperty ( name='AlphaTris',             default=True )
    m_AlphaVerts           : bpy.props.BoolProperty ( name='AlphaVerts',            default=True )
    m_BoundingTriangulation: bpy.props.BoolProperty ( name='BoundingTriangulation', default=True )
    m_Alpha                : bpy.props.FloatProperty( name='Alpha',                 default=0.0 )
    m_Offset               : bpy.props.FloatProperty( name='Offset',                default=2.5 )
    m_Tolerance            : bpy.props.FloatProperty( name='Tolerance',             default=0.001 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AlphaLines','m_AlphaTets','m_AlphaTris','m_AlphaVerts','m_BoundingTriangulation','m_Alpha','m_Offset','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDelaunay3D )        
TYPENAMES.append('VTKDelaunay3DType' )

#--------------------------------------------------------------
class VTKDensifyPointCloudFilter(Node, BVTK_Node):

    bl_idname = 'VTKDensifyPointCloudFilterType'
    bl_label  = 'vtkDensifyPointCloudFilter'
    e_NeighborhoodType_items=[ (x,x,x) for x in ['Radius', 'NClosest']]
    
    m_InterpolateAttributeData : bpy.props.BoolProperty ( name='InterpolateAttributeData',  default=True )
    m_MaximumNumberOfIterations: bpy.props.IntProperty  ( name='MaximumNumberOfIterations', default=3 )
    m_MaximumNumberOfPoints    : bpy.props.IntProperty  ( name='MaximumNumberOfPoints',     default=1000000000 )
    m_NumberOfClosestPoints    : bpy.props.IntProperty  ( name='NumberOfClosestPoints',     default=6 )
    m_Radius                   : bpy.props.FloatProperty( name='Radius',                    default=1.0 )
    m_TargetDistance           : bpy.props.FloatProperty( name='TargetDistance',            default=0.5 )
    e_NeighborhoodType         : bpy.props.EnumProperty ( name='NeighborhoodType',          default="NClosest", items=e_NeighborhoodType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_InterpolateAttributeData','m_MaximumNumberOfIterations','m_MaximumNumberOfPoints','m_NumberOfClosestPoints','m_Radius','m_TargetDistance','e_NeighborhoodType',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDensifyPointCloudFilter )        
TYPENAMES.append('VTKDensifyPointCloudFilterType' )

#--------------------------------------------------------------
class VTKDensifyPolyData(Node, BVTK_Node):

    bl_idname = 'VTKDensifyPolyDataType'
    bl_label  = 'vtkDensifyPolyData'
    
    m_NumberOfSubdivisions: bpy.props.IntProperty( name='NumberOfSubdivisions', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NumberOfSubdivisions',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDensifyPolyData )        
TYPENAMES.append('VTKDensifyPolyDataType' )

#--------------------------------------------------------------
class VTKDepthSortPolyData(Node, BVTK_Node):

    bl_idname = 'VTKDepthSortPolyDataType'
    bl_label  = 'vtkDepthSortPolyData'
    e_DepthSortMode_items=[ (x,x,x) for x in ['FirstPoint', 'BoundsCenter', 'ParametricCenter']]
    e_Direction_items=[ (x,x,x) for x in ['BackToFront', 'FrontToBack', 'SpecifiedVector']]
    
    m_SortScalars  : bpy.props.BoolProperty       ( name='SortScalars',   default=True )
    e_DepthSortMode: bpy.props.EnumProperty       ( name='DepthSortMode', default="FirstPoint", items=e_DepthSortMode_items )
    e_Direction    : bpy.props.EnumProperty       ( name='Direction',     default="BackToFront", items=e_Direction_items )
    m_Origin       : bpy.props.FloatVectorProperty( name='Origin',        default=[0.0, 0.0, 0.0], size=3 )
    m_Vector       : bpy.props.FloatVectorProperty( name='Vector',        default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_SortScalars','e_DepthSortMode','e_Direction','m_Origin','m_Vector',]
    def m_connections( self ):
        return (['input'], ['output'], ['Prop3D'], []) 
    
add_class( VTKDepthSortPolyData )        
TYPENAMES.append('VTKDepthSortPolyDataType' )

#--------------------------------------------------------------
class VTKDijkstraGraphGeodesicPath(Node, BVTK_Node):

    bl_idname = 'VTKDijkstraGraphGeodesicPathType'
    bl_label  = 'vtkDijkstraGraphGeodesicPath'
    
    m_RepelPathFromVertices: bpy.props.BoolProperty( name='RepelPathFromVertices', default=True )
    m_StopWhenEndReached   : bpy.props.BoolProperty( name='StopWhenEndReached',    default=True )
    m_UseScalarWeights     : bpy.props.BoolProperty( name='UseScalarWeights',      default=True )
    m_EndVertex            : bpy.props.IntProperty ( name='EndVertex',             default=0 )
    m_StartVertex          : bpy.props.IntProperty ( name='StartVertex',           default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_RepelPathFromVertices','m_StopWhenEndReached','m_UseScalarWeights','m_EndVertex','m_StartVertex',]
    def m_connections( self ):
        return (['input'], ['output'], ['RepelVertices'], []) 
    
add_class( VTKDijkstraGraphGeodesicPath )        
TYPENAMES.append('VTKDijkstraGraphGeodesicPathType' )

#--------------------------------------------------------------
class VTKDijkstraImageGeodesicPath(Node, BVTK_Node):

    bl_idname = 'VTKDijkstraImageGeodesicPathType'
    bl_label  = 'vtkDijkstraImageGeodesicPath'
    
    m_RepelPathFromVertices: bpy.props.BoolProperty ( name='RepelPathFromVertices', default=True )
    m_StopWhenEndReached   : bpy.props.BoolProperty ( name='StopWhenEndReached',    default=True )
    m_UseScalarWeights     : bpy.props.BoolProperty ( name='UseScalarWeights',      default=True )
    m_EndVertex            : bpy.props.IntProperty  ( name='EndVertex',             default=0 )
    m_StartVertex          : bpy.props.IntProperty  ( name='StartVertex',           default=0 )
    m_CurvatureWeight      : bpy.props.FloatProperty( name='CurvatureWeight',       default=0.0 )
    m_EdgeLengthWeight     : bpy.props.FloatProperty( name='EdgeLengthWeight',      default=0.0 )
    m_ImageWeight          : bpy.props.FloatProperty( name='ImageWeight',           default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_RepelPathFromVertices','m_StopWhenEndReached','m_UseScalarWeights','m_EndVertex','m_StartVertex','m_CurvatureWeight','m_EdgeLengthWeight','m_ImageWeight',]
    def m_connections( self ):
        return (['input'], ['output'], ['RepelVertices'], []) 
    
add_class( VTKDijkstraImageGeodesicPath )        
TYPENAMES.append('VTKDijkstraImageGeodesicPathType' )

#--------------------------------------------------------------
class VTKDirectedGraphAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKDirectedGraphAlgorithmType'
    bl_label  = 'vtkDirectedGraphAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDirectedGraphAlgorithm )        
TYPENAMES.append('VTKDirectedGraphAlgorithmType' )

#--------------------------------------------------------------
class VTKDiscreteMarchingCubes(Node, BVTK_Node):

    bl_idname = 'VTKDiscreteMarchingCubesType'
    bl_label  = 'vtkDiscreteMarchingCubes'
    
    m_ComputeAdjacentScalars: bpy.props.BoolProperty( name='ComputeAdjacentScalars', default=True )
    m_ComputeGradients      : bpy.props.BoolProperty( name='ComputeGradients',       default=True )
    m_ComputeNormals        : bpy.props.BoolProperty( name='ComputeNormals',         default=True )
    m_ComputeScalars        : bpy.props.BoolProperty( name='ComputeScalars',         default=True )
    m_NumberOfContours      : bpy.props.IntProperty ( name='NumberOfContours',       default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeAdjacentScalars','m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDiscreteMarchingCubes )        
TYPENAMES.append('VTKDiscreteMarchingCubesType' )

#--------------------------------------------------------------
class VTKDuplicatePolyData(Node, BVTK_Node):

    bl_idname = 'VTKDuplicatePolyDataType'
    bl_label  = 'vtkDuplicatePolyData'
    
    m_Synchronous: bpy.props.BoolProperty( name='Synchronous', default=True )
    m_ClientFlag : bpy.props.IntProperty ( name='ClientFlag',  default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Synchronous','m_ClientFlag',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKDuplicatePolyData )        
TYPENAMES.append('VTKDuplicatePolyDataType' )

#--------------------------------------------------------------
class VTKEdgePoints(Node, BVTK_Node):

    bl_idname = 'VTKEdgePointsType'
    bl_label  = 'vtkEdgePoints'
    
    m_Value: bpy.props.FloatProperty( name='Value', default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Value',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKEdgePoints )        
TYPENAMES.append('VTKEdgePointsType' )

#--------------------------------------------------------------
class VTKElevationFilter(Node, BVTK_Node):

    bl_idname = 'VTKElevationFilterType'
    bl_label  = 'vtkElevationFilter'
    
    m_HighPoint  : bpy.props.FloatVectorProperty( name='HighPoint',   default=[0.0, 0.0, 1.0], size=3 )
    m_LowPoint   : bpy.props.FloatVectorProperty( name='LowPoint',    default=[0.0, 0.0, 0.0], size=3 )
    m_ScalarRange: bpy.props.FloatVectorProperty( name='ScalarRange', default=[0.0, 1.0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_HighPoint','m_LowPoint','m_ScalarRange',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKElevationFilter )        
TYPENAMES.append('VTKElevationFilterType' )

#--------------------------------------------------------------
class VTKEuclideanClusterExtraction(Node, BVTK_Node):

    bl_idname = 'VTKEuclideanClusterExtractionType'
    bl_label  = 'vtkEuclideanClusterExtraction'
    e_ExtractionMode_items=[ (x,x,x) for x in ['PointSeededClusters', 'SpecifiedClusters', 'LargestCluster', 'AllClusters', 'ClosestPointCluster']]
    
    m_ColorClusters     : bpy.props.BoolProperty       ( name='ColorClusters',      default=False )
    m_ScalarConnectivity: bpy.props.BoolProperty       ( name='ScalarConnectivity', default=False )
    m_Radius            : bpy.props.FloatProperty      ( name='Radius',             default=0.0 )
    e_ExtractionMode    : bpy.props.EnumProperty       ( name='ExtractionMode',     default="LargestCluster", items=e_ExtractionMode_items )
    m_ClosestPoint      : bpy.props.FloatVectorProperty( name='ClosestPoint',       default=[0.0, 0.0, 0.0], size=3 )
    m_ScalarRange       : bpy.props.FloatVectorProperty( name='ScalarRange',        default=[0.0, 1.0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ColorClusters','m_ScalarConnectivity','m_Radius','e_ExtractionMode','m_ClosestPoint','m_ScalarRange',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKEuclideanClusterExtraction )        
TYPENAMES.append('VTKEuclideanClusterExtractionType' )

#--------------------------------------------------------------
class VTKEvenlySpacedStreamlines2D(Node, BVTK_Node):

    bl_idname = 'VTKEvenlySpacedStreamlines2DType'
    bl_label  = 'vtkEvenlySpacedStreamlines2D'
    e_IntegratorType_items=[ (x,x,x) for x in ['RungeKutta2', 'RungeKutta4']]
    
    m_ComputeVorticity         : bpy.props.BoolProperty       ( name='ComputeVorticity',          default=True )
    m_IntegrationStepUnit      : bpy.props.IntProperty        ( name='IntegrationStepUnit',       default=2 )
    m_MaximumNumberOfSteps     : bpy.props.IntProperty        ( name='MaximumNumberOfSteps',      default=2000 )
    m_MinimumNumberOfLoopPoints: bpy.props.IntProperty        ( name='MinimumNumberOfLoopPoints', default=4 )
    m_ClosedLoopMaximumDistance: bpy.props.FloatProperty      ( name='ClosedLoopMaximumDistance', default=1e-06 )
    m_InitialIntegrationStep   : bpy.props.FloatProperty      ( name='InitialIntegrationStep',    default=0.5 )
    m_LoopAngle                : bpy.props.FloatProperty      ( name='LoopAngle',                 default=0.349066 )
    m_SeparatingDistance       : bpy.props.FloatProperty      ( name='SeparatingDistance',        default=1.0 )
    m_SeparatingDistanceRatio  : bpy.props.FloatProperty      ( name='SeparatingDistanceRatio',   default=0.5 )
    m_TerminalSpeed            : bpy.props.FloatProperty      ( name='TerminalSpeed',             default=1e-12 )
    e_IntegratorType           : bpy.props.EnumProperty       ( name='IntegratorType',            default="RungeKutta2", items=e_IntegratorType_items )
    m_StartPosition            : bpy.props.FloatVectorProperty( name='StartPosition',             default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeVorticity','m_IntegrationStepUnit','m_MaximumNumberOfSteps','m_MinimumNumberOfLoopPoints','m_ClosedLoopMaximumDistance','m_InitialIntegrationStep','m_LoopAngle','m_SeparatingDistance','m_SeparatingDistanceRatio','m_TerminalSpeed','e_IntegratorType','m_StartPosition',]
    def m_connections( self ):
        return (['input'], ['output'], ['Integrator'], []) 
    
add_class( VTKEvenlySpacedStreamlines2D )        
TYPENAMES.append('VTKEvenlySpacedStreamlines2DType' )

#--------------------------------------------------------------
class VTKExtractArray(Node, BVTK_Node):

    bl_idname = 'VTKExtractArrayType'
    bl_label  = 'vtkExtractArray'
    
    m_Index: bpy.props.IntProperty( name='Index', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Index',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractArray )        
TYPENAMES.append('VTKExtractArrayType' )

#--------------------------------------------------------------
class VTKExtractBlock(Node, BVTK_Node):

    bl_idname = 'VTKExtractBlockType'
    bl_label  = 'vtkExtractBlock'
    
    m_MaintainStructure: bpy.props.BoolProperty( name='MaintainStructure', default=True )
    m_PruneOutput      : bpy.props.BoolProperty( name='PruneOutput',       default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_MaintainStructure','m_PruneOutput',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractBlock )        
TYPENAMES.append('VTKExtractBlockType' )

#--------------------------------------------------------------
class VTKExtractCTHPart(Node, BVTK_Node):

    bl_idname = 'VTKExtractCTHPartType'
    bl_label  = 'vtkExtractCTHPart'
    
    m_Capping                   : bpy.props.BoolProperty ( name='Capping',                    default=True )
    m_GenerateTriangles         : bpy.props.BoolProperty ( name='GenerateTriangles',          default=True )
    m_RemoveGhostCells          : bpy.props.BoolProperty ( name='RemoveGhostCells',           default=True )
    m_VolumeFractionSurfaceValue: bpy.props.FloatProperty( name='VolumeFractionSurfaceValue', default=0.499 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Capping','m_GenerateTriangles','m_RemoveGhostCells','m_VolumeFractionSurfaceValue',]
    def m_connections( self ):
        return (['input'], ['output'], ['ClipPlane'], []) 
    
add_class( VTKExtractCTHPart )        
TYPENAMES.append('VTKExtractCTHPartType' )

#--------------------------------------------------------------
class VTKExtractCells(Node, BVTK_Node):

    bl_idname = 'VTKExtractCellsType'
    bl_label  = 'vtkExtractCells'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractCells )        
TYPENAMES.append('VTKExtractCellsType' )

#--------------------------------------------------------------
class VTKExtractDataOverTime(Node, BVTK_Node):

    bl_idname = 'VTKExtractDataOverTimeType'
    bl_label  = 'vtkExtractDataOverTime'
    
    m_PointIndex: bpy.props.IntProperty( name='PointIndex', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PointIndex',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractDataOverTime )        
TYPENAMES.append('VTKExtractDataOverTimeType' )

#--------------------------------------------------------------
class VTKExtractDataSets(Node, BVTK_Node):

    bl_idname = 'VTKExtractDataSetsType'
    bl_label  = 'vtkExtractDataSets'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractDataSets )        
TYPENAMES.append('VTKExtractDataSetsType' )

#--------------------------------------------------------------
class VTKExtractEdges(Node, BVTK_Node):

    bl_idname = 'VTKExtractEdgesType'
    bl_label  = 'vtkExtractEdges'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractEdges )        
TYPENAMES.append('VTKExtractEdgesType' )

#--------------------------------------------------------------
class VTKExtractGeometry(Node, BVTK_Node):

    bl_idname = 'VTKExtractGeometryType'
    bl_label  = 'vtkExtractGeometry'
    
    m_ExtractBoundaryCells    : bpy.props.BoolProperty( name='ExtractBoundaryCells',     default=True )
    m_ExtractInside           : bpy.props.BoolProperty( name='ExtractInside',            default=True )
    m_ExtractOnlyBoundaryCells: bpy.props.BoolProperty( name='ExtractOnlyBoundaryCells', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ExtractBoundaryCells','m_ExtractInside','m_ExtractOnlyBoundaryCells',]
    def m_connections( self ):
        return (['input'], ['output'], ['ImplicitFunction'], []) 
    
add_class( VTKExtractGeometry )        
TYPENAMES.append('VTKExtractGeometryType' )

#--------------------------------------------------------------
class VTKExtractGrid(Node, BVTK_Node):

    bl_idname = 'VTKExtractGridType'
    bl_label  = 'vtkExtractGrid'
    
    m_IncludeBoundary: bpy.props.BoolProperty     ( name='IncludeBoundary', default=True )
    m_SampleRate     : bpy.props.IntVectorProperty( name='SampleRate',      default=[1, 1, 1], size=3 )
    m_VOI            : bpy.props.IntVectorProperty( name='VOI',             default=[0, 1000000000, 0, 1000000000, 0, 1000000000], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_IncludeBoundary','m_SampleRate','m_VOI',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractGrid )        
TYPENAMES.append('VTKExtractGridType' )

#--------------------------------------------------------------
class VTKExtractLevel(Node, BVTK_Node):

    bl_idname = 'VTKExtractLevelType'
    bl_label  = 'vtkExtractLevel'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractLevel )        
TYPENAMES.append('VTKExtractLevelType' )

#--------------------------------------------------------------
class VTKExtractPiece(Node, BVTK_Node):

    bl_idname = 'VTKExtractPieceType'
    bl_label  = 'vtkExtractPiece'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractPiece )        
TYPENAMES.append('VTKExtractPieceType' )

#--------------------------------------------------------------
class VTKExtractPointCloudPiece(Node, BVTK_Node):

    bl_idname = 'VTKExtractPointCloudPieceType'
    bl_label  = 'vtkExtractPointCloudPiece'
    
    m_ModuloOrdering: bpy.props.BoolProperty( name='ModuloOrdering', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ModuloOrdering',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractPointCloudPiece )        
TYPENAMES.append('VTKExtractPointCloudPieceType' )

#--------------------------------------------------------------
class VTKExtractPolyDataGeometry(Node, BVTK_Node):

    bl_idname = 'VTKExtractPolyDataGeometryType'
    bl_label  = 'vtkExtractPolyDataGeometry'
    
    m_ExtractBoundaryCells: bpy.props.BoolProperty( name='ExtractBoundaryCells', default=True )
    m_ExtractInside       : bpy.props.BoolProperty( name='ExtractInside',        default=True )
    m_PassPoints          : bpy.props.BoolProperty( name='PassPoints',           default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ExtractBoundaryCells','m_ExtractInside','m_PassPoints',]
    def m_connections( self ):
        return (['input'], ['output'], ['ImplicitFunction'], []) 
    
add_class( VTKExtractPolyDataGeometry )        
TYPENAMES.append('VTKExtractPolyDataGeometryType' )

#--------------------------------------------------------------
class VTKExtractPolyDataPiece(Node, BVTK_Node):

    bl_idname = 'VTKExtractPolyDataPieceType'
    bl_label  = 'vtkExtractPolyDataPiece'
    
    m_CreateGhostCells: bpy.props.BoolProperty( name='CreateGhostCells', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CreateGhostCells',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractPolyDataPiece )        
TYPENAMES.append('VTKExtractPolyDataPieceType' )

#--------------------------------------------------------------
class VTKExtractRectilinearGrid(Node, BVTK_Node):

    bl_idname = 'VTKExtractRectilinearGridType'
    bl_label  = 'vtkExtractRectilinearGrid'
    
    m_IncludeBoundary: bpy.props.BoolProperty     ( name='IncludeBoundary', default=True )
    m_SampleRate     : bpy.props.IntVectorProperty( name='SampleRate',      default=[1, 1, 1], size=3 )
    m_VOI            : bpy.props.IntVectorProperty( name='VOI',             default=[0, 1000000000, 0, 1000000000, 0, 1000000000], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_IncludeBoundary','m_SampleRate','m_VOI',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractRectilinearGrid )        
TYPENAMES.append('VTKExtractRectilinearGridType' )

#--------------------------------------------------------------
class VTKExtractSurface(Node, BVTK_Node):

    bl_idname = 'VTKExtractSurfaceType'
    bl_label  = 'vtkExtractSurface'
    
    m_ComputeGradients: bpy.props.BoolProperty ( name='ComputeGradients', default=True )
    m_ComputeNormals  : bpy.props.BoolProperty ( name='ComputeNormals',   default=True )
    m_HoleFilling     : bpy.props.BoolProperty ( name='HoleFilling',      default=False )
    m_Radius          : bpy.props.FloatProperty( name='Radius',           default=0.1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradients','m_ComputeNormals','m_HoleFilling','m_Radius',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractSurface )        
TYPENAMES.append('VTKExtractSurfaceType' )

#--------------------------------------------------------------
class VTKExtractTemporalFieldData(Node, BVTK_Node):

    bl_idname = 'VTKExtractTemporalFieldDataType'
    bl_label  = 'vtkExtractTemporalFieldData'
    
    m_HandleCompositeDataBlocksIndividually: bpy.props.BoolProperty( name='HandleCompositeDataBlocksIndividually', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_HandleCompositeDataBlocksIndividually',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractTemporalFieldData )        
TYPENAMES.append('VTKExtractTemporalFieldDataType' )

#--------------------------------------------------------------
class VTKExtractTensorComponents(Node, BVTK_Node):

    bl_idname = 'VTKExtractTensorComponentsType'
    bl_label  = 'vtkExtractTensorComponents'
    e_ScalarMode_items=[ (x,x,x) for x in ['Component', 'EffectiveStress', 'Determinant']]
    
    m_ExtractNormals     : bpy.props.BoolProperty     ( name='ExtractNormals',      default=True )
    m_ExtractScalars     : bpy.props.BoolProperty     ( name='ExtractScalars',      default=True )
    m_ExtractTCoords     : bpy.props.BoolProperty     ( name='ExtractTCoords',      default=True )
    m_ExtractVectors     : bpy.props.BoolProperty     ( name='ExtractVectors',      default=True )
    m_NormalizeNormals   : bpy.props.BoolProperty     ( name='NormalizeNormals',    default=True )
    m_PassTensorsToOutput: bpy.props.BoolProperty     ( name='PassTensorsToOutput', default=True )
    m_NumberOfTCoords    : bpy.props.IntProperty      ( name='NumberOfTCoords',     default=2 )
    e_ScalarMode         : bpy.props.EnumProperty     ( name='ScalarMode',          default="Component", items=e_ScalarMode_items )
    m_NormalComponents   : bpy.props.IntVectorProperty( name='NormalComponents',    default=[0, 1, 1, 1, 2, 1], size=6 )
    m_ScalarComponents   : bpy.props.IntVectorProperty( name='ScalarComponents',    default=[0, 0], size=2 )
    m_TCoordComponents   : bpy.props.IntVectorProperty( name='TCoordComponents',    default=[0, 2, 1, 2, 2, 2], size=6 )
    m_VectorComponents   : bpy.props.IntVectorProperty( name='VectorComponents',    default=[0, 0, 1, 0, 2, 0], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ExtractNormals','m_ExtractScalars','m_ExtractTCoords','m_ExtractVectors','m_NormalizeNormals','m_PassTensorsToOutput','m_NumberOfTCoords','e_ScalarMode','m_NormalComponents','m_ScalarComponents','m_TCoordComponents','m_VectorComponents',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractTensorComponents )        
TYPENAMES.append('VTKExtractTensorComponentsType' )

#--------------------------------------------------------------
class VTKExtractTimeSteps(Node, BVTK_Node):

    bl_idname = 'VTKExtractTimeStepsType'
    bl_label  = 'vtkExtractTimeSteps'
    e_TimeEstimationMode_items=[ (x,x,x) for x in ['Previous', 'Next', 'Nearest']]
    
    m_UseRange          : bpy.props.BoolProperty     ( name='UseRange',           default=False )
    m_TimeStepInterval  : bpy.props.IntProperty      ( name='TimeStepInterval',   default=1 )
    e_TimeEstimationMode: bpy.props.EnumProperty     ( name='TimeEstimationMode', default="Previous", items=e_TimeEstimationMode_items )
    m_Range             : bpy.props.IntVectorProperty( name='Range',              default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseRange','m_TimeStepInterval','e_TimeEstimationMode','m_Range',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractTimeSteps )        
TYPENAMES.append('VTKExtractTimeStepsType' )

#--------------------------------------------------------------
class VTKExtractUnstructuredGrid(Node, BVTK_Node):

    bl_idname = 'VTKExtractUnstructuredGridType'
    bl_label  = 'vtkExtractUnstructuredGrid'
    
    m_CellClipping  : bpy.props.BoolProperty       ( name='CellClipping',   default=True )
    m_ExtentClipping: bpy.props.BoolProperty       ( name='ExtentClipping', default=True )
    m_Merging       : bpy.props.BoolProperty       ( name='Merging',        default=True )
    m_PointClipping : bpy.props.BoolProperty       ( name='PointClipping',  default=True )
    m_CellMaximum   : bpy.props.IntProperty        ( name='CellMaximum',    default=1000000000 )
    m_CellMinimum   : bpy.props.IntProperty        ( name='CellMinimum',    default=0 )
    m_PointMaximum  : bpy.props.IntProperty        ( name='PointMaximum',   default=1000000000 )
    m_PointMinimum  : bpy.props.IntProperty        ( name='PointMinimum',   default=0 )
    m_Extent        : bpy.props.FloatVectorProperty( name='Extent',         default=[-1e+30, 1e+30, -1e+30, 1e+30, -1e+30, 1e+30], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CellClipping','m_ExtentClipping','m_Merging','m_PointClipping','m_CellMaximum','m_CellMinimum','m_PointMaximum','m_PointMinimum','m_Extent',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractUnstructuredGrid )        
TYPENAMES.append('VTKExtractUnstructuredGridType' )

#--------------------------------------------------------------
class VTKExtractUnstructuredGridPiece(Node, BVTK_Node):

    bl_idname = 'VTKExtractUnstructuredGridPieceType'
    bl_label  = 'vtkExtractUnstructuredGridPiece'
    
    m_CreateGhostCells: bpy.props.BoolProperty( name='CreateGhostCells', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CreateGhostCells',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractUnstructuredGridPiece )        
TYPENAMES.append('VTKExtractUnstructuredGridPieceType' )

#--------------------------------------------------------------
class VTKExtractUserDefinedPiece(Node, BVTK_Node):

    bl_idname = 'VTKExtractUserDefinedPieceType'
    bl_label  = 'vtkExtractUserDefinedPiece'
    
    m_CreateGhostCells: bpy.props.BoolProperty( name='CreateGhostCells', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CreateGhostCells',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractUserDefinedPiece )        
TYPENAMES.append('VTKExtractUserDefinedPieceType' )

#--------------------------------------------------------------
class VTKExtractVOI(Node, BVTK_Node):

    bl_idname = 'VTKExtractVOIType'
    bl_label  = 'vtkExtractVOI'
    
    m_IncludeBoundary: bpy.props.BoolProperty     ( name='IncludeBoundary', default=True )
    m_SampleRate     : bpy.props.IntVectorProperty( name='SampleRate',      default=[1, 1, 1], size=3 )
    m_VOI            : bpy.props.IntVectorProperty( name='VOI',             default=[0, 1000000000, 0, 1000000000, 0, 1000000000], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_IncludeBoundary','m_SampleRate','m_VOI',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKExtractVOI )        
TYPENAMES.append('VTKExtractVOIType' )

#--------------------------------------------------------------
class VTKFeatureEdges(Node, BVTK_Node):

    bl_idname = 'VTKFeatureEdgesType'
    bl_label  = 'vtkFeatureEdges'
    
    m_BoundaryEdges   : bpy.props.BoolProperty ( name='BoundaryEdges',    default=True )
    m_Coloring        : bpy.props.BoolProperty ( name='Coloring',         default=True )
    m_FeatureEdges    : bpy.props.BoolProperty ( name='FeatureEdges',     default=True )
    m_ManifoldEdges   : bpy.props.BoolProperty ( name='ManifoldEdges',    default=True )
    m_NonManifoldEdges: bpy.props.BoolProperty ( name='NonManifoldEdges', default=True )
    m_FeatureAngle    : bpy.props.FloatProperty( name='FeatureAngle',     default=30.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_BoundaryEdges','m_Coloring','m_FeatureEdges','m_ManifoldEdges','m_NonManifoldEdges','m_FeatureAngle',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKFeatureEdges )        
TYPENAMES.append('VTKFeatureEdgesType' )

#--------------------------------------------------------------
class VTKFieldDataToAttributeDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKFieldDataToAttributeDataFilterType'
    bl_label  = 'vtkFieldDataToAttributeDataFilter'
    e_InputField_items=[ (x,x,x) for x in ['DataObjectField', 'PointDataField', 'CellDataField']]
    e_OutputAttributeData_items=[ (x,x,x) for x in ['CellData', 'PointData']]
    
    m_DefaultNormalize   : bpy.props.BoolProperty( name='DefaultNormalize',    default=True )
    e_InputField         : bpy.props.EnumProperty( name='InputField',          default="DataObjectField", items=e_InputField_items )
    e_OutputAttributeData: bpy.props.EnumProperty( name='OutputAttributeData', default="PointData", items=e_OutputAttributeData_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_DefaultNormalize','e_InputField','e_OutputAttributeData',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKFieldDataToAttributeDataFilter )        
TYPENAMES.append('VTKFieldDataToAttributeDataFilterType' )

#--------------------------------------------------------------
class VTKFillHolesFilter(Node, BVTK_Node):

    bl_idname = 'VTKFillHolesFilterType'
    bl_label  = 'vtkFillHolesFilter'
    
    m_HoleSize: bpy.props.FloatProperty( name='HoleSize', default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_HoleSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKFillHolesFilter )        
TYPENAMES.append('VTKFillHolesFilterType' )

#--------------------------------------------------------------
class VTKFlyingEdges2D(Node, BVTK_Node):

    bl_idname = 'VTKFlyingEdges2DType'
    bl_label  = 'vtkFlyingEdges2D'
    
    m_ComputeScalars  : bpy.props.BoolProperty( name='ComputeScalars',   default=True )
    m_ArrayComponent  : bpy.props.IntProperty ( name='ArrayComponent',   default=0 )
    m_NumberOfContours: bpy.props.IntProperty ( name='NumberOfContours', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeScalars','m_ArrayComponent','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKFlyingEdges2D )        
TYPENAMES.append('VTKFlyingEdges2DType' )

#--------------------------------------------------------------
class VTKFlyingEdges3D(Node, BVTK_Node):

    bl_idname = 'VTKFlyingEdges3DType'
    bl_label  = 'vtkFlyingEdges3D'
    
    m_ComputeGradients     : bpy.props.BoolProperty( name='ComputeGradients',      default=True )
    m_ComputeNormals       : bpy.props.BoolProperty( name='ComputeNormals',        default=True )
    m_ComputeScalars       : bpy.props.BoolProperty( name='ComputeScalars',        default=True )
    m_InterpolateAttributes: bpy.props.BoolProperty( name='InterpolateAttributes', default=True )
    m_ArrayComponent       : bpy.props.IntProperty ( name='ArrayComponent',        default=0 )
    m_NumberOfContours     : bpy.props.IntProperty ( name='NumberOfContours',      default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_InterpolateAttributes','m_ArrayComponent','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKFlyingEdges3D )        
TYPENAMES.append('VTKFlyingEdges3DType' )

#--------------------------------------------------------------
class VTKFlyingEdgesPlaneCutter(Node, BVTK_Node):

    bl_idname = 'VTKFlyingEdgesPlaneCutterType'
    bl_label  = 'vtkFlyingEdgesPlaneCutter'
    
    m_ComputeNormals       : bpy.props.BoolProperty( name='ComputeNormals',        default=True )
    m_InterpolateAttributes: bpy.props.BoolProperty( name='InterpolateAttributes', default=True )
    m_ArrayComponent       : bpy.props.IntProperty ( name='ArrayComponent',        default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeNormals','m_InterpolateAttributes','m_ArrayComponent',]
    def m_connections( self ):
        return (['input'], ['output'], ['Plane'], []) 
    
add_class( VTKFlyingEdgesPlaneCutter )        
TYPENAMES.append('VTKFlyingEdgesPlaneCutterType' )

#--------------------------------------------------------------
class VTKForceTime(Node, BVTK_Node):

    bl_idname = 'VTKForceTimeType'
    bl_label  = 'vtkForceTime'
    
    m_IgnorePipelineTime: bpy.props.BoolProperty ( name='IgnorePipelineTime', default=True )
    m_ForcedTime        : bpy.props.FloatProperty( name='ForcedTime',         default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_IgnorePipelineTime','m_ForcedTime',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKForceTime )        
TYPENAMES.append('VTKForceTimeType' )

#--------------------------------------------------------------
class VTKGaussianSplatter(Node, BVTK_Node):

    bl_idname = 'VTKGaussianSplatterType'
    bl_label  = 'vtkGaussianSplatter'
    e_AccumulationMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Sum']]
    
    m_Capping         : bpy.props.BoolProperty       ( name='Capping',          default=True )
    m_NormalWarping   : bpy.props.BoolProperty       ( name='NormalWarping',    default=True )
    m_ScalarWarping   : bpy.props.BoolProperty       ( name='ScalarWarping',    default=True )
    m_CapValue        : bpy.props.FloatProperty      ( name='CapValue',         default=0.0 )
    m_Eccentricity    : bpy.props.FloatProperty      ( name='Eccentricity',     default=2.5 )
    m_ExponentFactor  : bpy.props.FloatProperty      ( name='ExponentFactor',   default=-5.0 )
    m_NullValue       : bpy.props.FloatProperty      ( name='NullValue',        default=0.0 )
    m_Radius          : bpy.props.FloatProperty      ( name='Radius',           default=0.1 )
    m_ScaleFactor     : bpy.props.FloatProperty      ( name='ScaleFactor',      default=1.0 )
    e_AccumulationMode: bpy.props.EnumProperty       ( name='AccumulationMode', default="Max", items=e_AccumulationMode_items )
    m_SampleDimensions: bpy.props.IntVectorProperty  ( name='SampleDimensions', default=[50, 50, 50], size=3 )
    m_ModelBounds     : bpy.props.FloatVectorProperty( name='ModelBounds',      default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Capping','m_NormalWarping','m_ScalarWarping','m_CapValue','m_Eccentricity','m_ExponentFactor','m_NullValue','m_Radius','m_ScaleFactor','e_AccumulationMode','m_SampleDimensions','m_ModelBounds',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKGaussianSplatter )        
TYPENAMES.append('VTKGaussianSplatterType' )

#--------------------------------------------------------------
class VTKGenericContourFilter(Node, BVTK_Node):

    bl_idname = 'VTKGenericContourFilterType'
    bl_label  = 'vtkGenericContourFilter'
    
    m_ComputeGradients: bpy.props.BoolProperty( name='ComputeGradients', default=True )
    m_ComputeNormals  : bpy.props.BoolProperty( name='ComputeNormals',   default=True )
    m_ComputeScalars  : bpy.props.BoolProperty( name='ComputeScalars',   default=True )
    m_NumberOfContours: bpy.props.IntProperty ( name='NumberOfContours', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKGenericContourFilter )        
TYPENAMES.append('VTKGenericContourFilterType' )

#--------------------------------------------------------------
class VTKGenericCutter(Node, BVTK_Node):

    bl_idname = 'VTKGenericCutterType'
    bl_label  = 'vtkGenericCutter'
    
    m_GenerateCutScalars: bpy.props.BoolProperty( name='GenerateCutScalars', default=True )
    m_NumberOfContours  : bpy.props.IntProperty ( name='NumberOfContours',   default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateCutScalars','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['CutFunction'], []) 
    
add_class( VTKGenericCutter )        
TYPENAMES.append('VTKGenericCutterType' )

#--------------------------------------------------------------
class VTKGenericDataSetTessellator(Node, BVTK_Node):

    bl_idname = 'VTKGenericDataSetTessellatorType'
    bl_label  = 'vtkGenericDataSetTessellator'
    
    m_KeepCellIds: bpy.props.BoolProperty( name='KeepCellIds', default=True )
    m_Merging    : bpy.props.BoolProperty( name='Merging',     default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_KeepCellIds','m_Merging',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKGenericDataSetTessellator )        
TYPENAMES.append('VTKGenericDataSetTessellatorType' )

#--------------------------------------------------------------
class VTKGenericGeometryFilter(Node, BVTK_Node):

    bl_idname = 'VTKGenericGeometryFilterType'
    bl_label  = 'vtkGenericGeometryFilter'
    
    m_CellClipping      : bpy.props.BoolProperty( name='CellClipping',       default=True )
    m_ExtentClipping    : bpy.props.BoolProperty( name='ExtentClipping',     default=True )
    m_Merging           : bpy.props.BoolProperty( name='Merging',            default=True )
    m_PassThroughCellIds: bpy.props.BoolProperty( name='PassThroughCellIds', default=True )
    m_PointClipping     : bpy.props.BoolProperty( name='PointClipping',      default=True )
    m_CellMaximum       : bpy.props.IntProperty ( name='CellMaximum',        default=1000000000 )
    m_CellMinimum       : bpy.props.IntProperty ( name='CellMinimum',        default=0 )
    m_PointMaximum      : bpy.props.IntProperty ( name='PointMaximum',       default=1000000000 )
    m_PointMinimum      : bpy.props.IntProperty ( name='PointMinimum',       default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CellClipping','m_ExtentClipping','m_Merging','m_PassThroughCellIds','m_PointClipping','m_CellMaximum','m_CellMinimum','m_PointMaximum','m_PointMinimum',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKGenericGeometryFilter )        
TYPENAMES.append('VTKGenericGeometryFilterType' )

#--------------------------------------------------------------
class VTKGenericOutlineFilter(Node, BVTK_Node):

    bl_idname = 'VTKGenericOutlineFilterType'
    bl_label  = 'vtkGenericOutlineFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKGenericOutlineFilter )        
TYPENAMES.append('VTKGenericOutlineFilterType' )

#--------------------------------------------------------------
class VTKGeometryFilter(Node, BVTK_Node):

    bl_idname = 'VTKGeometryFilterType'
    bl_label  = 'vtkGeometryFilter'
    
    m_CellClipping  : bpy.props.BoolProperty       ( name='CellClipping',   default=True )
    m_ExtentClipping: bpy.props.BoolProperty       ( name='ExtentClipping', default=True )
    m_Merging       : bpy.props.BoolProperty       ( name='Merging',        default=True )
    m_PointClipping : bpy.props.BoolProperty       ( name='PointClipping',  default=True )
    m_CellMaximum   : bpy.props.IntProperty        ( name='CellMaximum',    default=1000000000 )
    m_CellMinimum   : bpy.props.IntProperty        ( name='CellMinimum',    default=0 )
    m_PointMaximum  : bpy.props.IntProperty        ( name='PointMaximum',   default=1000000000 )
    m_PointMinimum  : bpy.props.IntProperty        ( name='PointMinimum',   default=0 )
    m_Extent        : bpy.props.FloatVectorProperty( name='Extent',         default=[-1e+30, 1e+30, -1e+30, 1e+30, -1e+30, 1e+30], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CellClipping','m_ExtentClipping','m_Merging','m_PointClipping','m_CellMaximum','m_CellMinimum','m_PointMaximum','m_PointMinimum','m_Extent',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKGeometryFilter )        
TYPENAMES.append('VTKGeometryFilterType' )

#--------------------------------------------------------------
class VTKGradientFilter(Node, BVTK_Node):

    bl_idname = 'VTKGradientFilterType'
    bl_label  = 'vtkGradientFilter'
    
    m_ComputeDivergence     : bpy.props.BoolProperty  ( name='ComputeDivergence',      default=True )
    m_ComputeGradient       : bpy.props.BoolProperty  ( name='ComputeGradient',        default=True )
    m_ComputeQCriterion     : bpy.props.BoolProperty  ( name='ComputeQCriterion',      default=True )
    m_ComputeVorticity      : bpy.props.BoolProperty  ( name='ComputeVorticity',       default=True )
    m_FasterApproximation   : bpy.props.BoolProperty  ( name='FasterApproximation',    default=True )
    m_DivergenceArrayName   : bpy.props.StringProperty( name='DivergenceArrayName',    default="" )
    m_QCriterionArrayName   : bpy.props.StringProperty( name='QCriterionArrayName',    default="" )
    m_ResultArrayName       : bpy.props.StringProperty( name='ResultArrayName',        default="" )
    m_VorticityArrayName    : bpy.props.StringProperty( name='VorticityArrayName',     default="" )
    m_ContributingCellOption: bpy.props.IntProperty   ( name='ContributingCellOption', default=0 )
    m_ReplacementValueOption: bpy.props.IntProperty   ( name='ReplacementValueOption', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeDivergence','m_ComputeGradient','m_ComputeQCriterion','m_ComputeVorticity','m_FasterApproximation','m_DivergenceArrayName','m_QCriterionArrayName','m_ResultArrayName','m_VorticityArrayName','m_ContributingCellOption','m_ReplacementValueOption',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKGradientFilter )        
TYPENAMES.append('VTKGradientFilterType' )

#--------------------------------------------------------------
class VTKGraphAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKGraphAlgorithmType'
    bl_label  = 'vtkGraphAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKGraphAlgorithm )        
TYPENAMES.append('VTKGraphAlgorithmType' )

#--------------------------------------------------------------
class VTKGraphLayoutFilter(Node, BVTK_Node):

    bl_idname = 'VTKGraphLayoutFilterType'
    bl_label  = 'vtkGraphLayoutFilter'
    
    m_AutomaticBoundsComputation: bpy.props.BoolProperty       ( name='AutomaticBoundsComputation', default=True )
    m_ThreeDimensionalLayout    : bpy.props.BoolProperty       ( name='ThreeDimensionalLayout',     default=True )
    m_MaxNumberOfIterations     : bpy.props.IntProperty        ( name='MaxNumberOfIterations',      default=50 )
    m_CoolDownRate              : bpy.props.FloatProperty      ( name='CoolDownRate',               default=10.0 )
    m_GraphBounds               : bpy.props.FloatVectorProperty( name='GraphBounds',                default=[-0.5, 0.5, -0.5, 0.5, -0.5, 0.5], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutomaticBoundsComputation','m_ThreeDimensionalLayout','m_MaxNumberOfIterations','m_CoolDownRate','m_GraphBounds',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKGraphLayoutFilter )        
TYPENAMES.append('VTKGraphLayoutFilterType' )

#--------------------------------------------------------------
class VTKGraphToGlyphs(Node, BVTK_Node):

    bl_idname = 'VTKGraphToGlyphsType'
    bl_label  = 'vtkGraphToGlyphs'
    
    m_Filled    : bpy.props.BoolProperty ( name='Filled',     default=True )
    m_Scaling   : bpy.props.BoolProperty ( name='Scaling',    default=False )
    m_GlyphType : bpy.props.IntProperty  ( name='GlyphType',  default=7 )
    m_ScreenSize: bpy.props.FloatProperty( name='ScreenSize', default=10.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Filled','m_Scaling','m_GlyphType','m_ScreenSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['Renderer'], []) 
    
add_class( VTKGraphToGlyphs )        
TYPENAMES.append('VTKGraphToGlyphsType' )

#--------------------------------------------------------------
class VTKGraphToPoints(Node, BVTK_Node):

    bl_idname = 'VTKGraphToPointsType'
    bl_label  = 'vtkGraphToPoints'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKGraphToPoints )        
TYPENAMES.append('VTKGraphToPointsType' )

#--------------------------------------------------------------
class VTKGraphWeightEuclideanDistanceFilter(Node, BVTK_Node):

    bl_idname = 'VTKGraphWeightEuclideanDistanceFilterType'
    bl_label  = 'vtkGraphWeightEuclideanDistanceFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKGraphWeightEuclideanDistanceFilter )        
TYPENAMES.append('VTKGraphWeightEuclideanDistanceFilterType' )

#--------------------------------------------------------------
class VTKGreedyTerrainDecimation(Node, BVTK_Node):

    bl_idname = 'VTKGreedyTerrainDecimationType'
    bl_label  = 'vtkGreedyTerrainDecimation'
    e_ErrorMeasure_items=[ (x,x,x) for x in ['NumberOfTriangles', 'SpecifiedReduction', 'AbsoluteError', 'RelativeError']]
    
    m_BoundaryVertexDeletion: bpy.props.BoolProperty ( name='BoundaryVertexDeletion', default=True )
    m_ComputeNormals        : bpy.props.BoolProperty ( name='ComputeNormals',         default=True )
    m_NumberOfTriangles     : bpy.props.IntProperty  ( name='NumberOfTriangles',      default=1000 )
    m_AbsoluteError         : bpy.props.FloatProperty( name='AbsoluteError',          default=1.0 )
    m_Reduction             : bpy.props.FloatProperty( name='Reduction',              default=0.9 )
    m_RelativeError         : bpy.props.FloatProperty( name='RelativeError',          default=0.01 )
    e_ErrorMeasure          : bpy.props.EnumProperty ( name='ErrorMeasure',           default="SpecifiedReduction", items=e_ErrorMeasure_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_BoundaryVertexDeletion','m_ComputeNormals','m_NumberOfTriangles','m_AbsoluteError','m_Reduction','m_RelativeError','e_ErrorMeasure',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKGreedyTerrainDecimation )        
TYPENAMES.append('VTKGreedyTerrainDecimationType' )

#--------------------------------------------------------------
class VTKGridSynchronizedTemplates3D(Node, BVTK_Node):

    bl_idname = 'VTKGridSynchronizedTemplates3DType'
    bl_label  = 'vtkGridSynchronizedTemplates3D'
    
    m_ComputeGradients : bpy.props.BoolProperty( name='ComputeGradients',  default=True )
    m_ComputeNormals   : bpy.props.BoolProperty( name='ComputeNormals',    default=True )
    m_ComputeScalars   : bpy.props.BoolProperty( name='ComputeScalars',    default=True )
    m_GenerateTriangles: bpy.props.BoolProperty( name='GenerateTriangles', default=True )
    m_NumberOfContours : bpy.props.IntProperty ( name='NumberOfContours',  default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_GenerateTriangles','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKGridSynchronizedTemplates3D )        
TYPENAMES.append('VTKGridSynchronizedTemplates3DType' )

#--------------------------------------------------------------
class VTKHedgeHog(Node, BVTK_Node):

    bl_idname = 'VTKHedgeHogType'
    bl_label  = 'vtkHedgeHog'
    e_VectorMode_items=[ (x,x,x) for x in ['UseVector', 'UseNormal']]
    
    m_ScaleFactor: bpy.props.FloatProperty( name='ScaleFactor', default=1.0 )
    e_VectorMode : bpy.props.EnumProperty ( name='VectorMode',  default="UseVector", items=e_VectorMode_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ScaleFactor','e_VectorMode',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHedgeHog )        
TYPENAMES.append('VTKHedgeHogType' )

#--------------------------------------------------------------
class VTKHierarchicalBinningFilter(Node, BVTK_Node):

    bl_idname = 'VTKHierarchicalBinningFilterType'
    bl_label  = 'vtkHierarchicalBinningFilter'
    
    m_Automatic     : bpy.props.BoolProperty       ( name='Automatic',      default=True )
    m_NumberOfLevels: bpy.props.IntProperty        ( name='NumberOfLevels', default=3 )
    m_Divisions     : bpy.props.IntVectorProperty  ( name='Divisions',      default=[2, 2, 2], size=3 )
    m_Bounds        : bpy.props.FloatVectorProperty( name='Bounds',         default=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Automatic','m_NumberOfLevels','m_Divisions','m_Bounds',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHierarchicalBinningFilter )        
TYPENAMES.append('VTKHierarchicalBinningFilterType' )

#--------------------------------------------------------------
class VTKHierarchicalBoxDataSetAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKHierarchicalBoxDataSetAlgorithmType'
    bl_label  = 'vtkHierarchicalBoxDataSetAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHierarchicalBoxDataSetAlgorithm )        
TYPENAMES.append('VTKHierarchicalBoxDataSetAlgorithmType' )

#--------------------------------------------------------------
class VTKHierarchicalDataExtractDataSets(Node, BVTK_Node):

    bl_idname = 'VTKHierarchicalDataExtractDataSetsType'
    bl_label  = 'vtkHierarchicalDataExtractDataSets'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHierarchicalDataExtractDataSets )        
TYPENAMES.append('VTKHierarchicalDataExtractDataSetsType' )

#--------------------------------------------------------------
class VTKHierarchicalDataExtractLevel(Node, BVTK_Node):

    bl_idname = 'VTKHierarchicalDataExtractLevelType'
    bl_label  = 'vtkHierarchicalDataExtractLevel'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHierarchicalDataExtractLevel )        
TYPENAMES.append('VTKHierarchicalDataExtractLevelType' )

#--------------------------------------------------------------
class VTKHierarchicalDataLevelFilter(Node, BVTK_Node):

    bl_idname = 'VTKHierarchicalDataLevelFilterType'
    bl_label  = 'vtkHierarchicalDataLevelFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHierarchicalDataLevelFilter )        
TYPENAMES.append('VTKHierarchicalDataLevelFilterType' )

#--------------------------------------------------------------
class VTKHierarchicalDataSetGeometryFilter(Node, BVTK_Node):

    bl_idname = 'VTKHierarchicalDataSetGeometryFilterType'
    bl_label  = 'vtkHierarchicalDataSetGeometryFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHierarchicalDataSetGeometryFilter )        
TYPENAMES.append('VTKHierarchicalDataSetGeometryFilterType' )

#--------------------------------------------------------------
class VTKHull(Node, BVTK_Node):

    bl_idname = 'VTKHullType'
    bl_label  = 'vtkHull'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHull )        
TYPENAMES.append('VTKHullType' )

#--------------------------------------------------------------
class VTKHyperOctreeContourFilter(Node, BVTK_Node):

    bl_idname = 'VTKHyperOctreeContourFilterType'
    bl_label  = 'vtkHyperOctreeContourFilter'
    
    m_NumberOfContours: bpy.props.IntProperty( name='NumberOfContours', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperOctreeContourFilter )        
TYPENAMES.append('VTKHyperOctreeContourFilterType' )

#--------------------------------------------------------------
class VTKHyperOctreeCutter(Node, BVTK_Node):

    bl_idname = 'VTKHyperOctreeCutterType'
    bl_label  = 'vtkHyperOctreeCutter'
    e_SortBy_items=[ (x,x,x) for x in ['SortByValue', 'SortByCell']]
    
    m_GenerateCutScalars: bpy.props.BoolProperty( name='GenerateCutScalars', default=True )
    m_NumberOfContours  : bpy.props.IntProperty ( name='NumberOfContours',   default=1 )
    e_SortBy            : bpy.props.EnumProperty( name='SortBy',             default="SortByValue", items=e_SortBy_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateCutScalars','m_NumberOfContours','e_SortBy',]
    def m_connections( self ):
        return (['input'], ['output'], ['CutFunction'], []) 
    
add_class( VTKHyperOctreeCutter )        
TYPENAMES.append('VTKHyperOctreeCutterType' )

#--------------------------------------------------------------
class VTKHyperOctreeDepth(Node, BVTK_Node):

    bl_idname = 'VTKHyperOctreeDepthType'
    bl_label  = 'vtkHyperOctreeDepth'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperOctreeDepth )        
TYPENAMES.append('VTKHyperOctreeDepthType' )

#--------------------------------------------------------------
class VTKHyperOctreeDualGridContourFilter(Node, BVTK_Node):

    bl_idname = 'VTKHyperOctreeDualGridContourFilterType'
    bl_label  = 'vtkHyperOctreeDualGridContourFilter'
    
    m_NumberOfContours: bpy.props.IntProperty( name='NumberOfContours', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperOctreeDualGridContourFilter )        
TYPENAMES.append('VTKHyperOctreeDualGridContourFilterType' )

#--------------------------------------------------------------
class VTKHyperOctreeLimiter(Node, BVTK_Node):

    bl_idname = 'VTKHyperOctreeLimiterType'
    bl_label  = 'vtkHyperOctreeLimiter'
    
    m_MaximumLevel: bpy.props.IntProperty( name='MaximumLevel', default=5 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_MaximumLevel',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperOctreeLimiter )        
TYPENAMES.append('VTKHyperOctreeLimiterType' )

#--------------------------------------------------------------
class VTKHyperOctreeSurfaceFilter(Node, BVTK_Node):

    bl_idname = 'VTKHyperOctreeSurfaceFilterType'
    bl_label  = 'vtkHyperOctreeSurfaceFilter'
    
    m_Merging           : bpy.props.BoolProperty( name='Merging',            default=True )
    m_PassThroughCellIds: bpy.props.BoolProperty( name='PassThroughCellIds', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Merging','m_PassThroughCellIds',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperOctreeSurfaceFilter )        
TYPENAMES.append('VTKHyperOctreeSurfaceFilterType' )

#--------------------------------------------------------------
class VTKHyperOctreeToUniformGridFilter(Node, BVTK_Node):

    bl_idname = 'VTKHyperOctreeToUniformGridFilterType'
    bl_label  = 'vtkHyperOctreeToUniformGridFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperOctreeToUniformGridFilter )        
TYPENAMES.append('VTKHyperOctreeToUniformGridFilterType' )

#--------------------------------------------------------------
class VTKHyperStreamline(Node, BVTK_Node):

    bl_idname = 'VTKHyperStreamlineType'
    bl_label  = 'vtkHyperStreamline'
    e_IntegrationDirection_items=[ (x,x,x) for x in ['Forward', 'Backward', 'IntegrateBothDirections']]
    e_IntegrationEigenvector_items=[ (x,x,x) for x in ['Major', 'Medium', 'Minor']]
    
    m_LogScaling                : bpy.props.BoolProperty ( name='LogScaling',                 default=True )
    m_NumberOfSides             : bpy.props.IntProperty  ( name='NumberOfSides',              default=6 )
    m_IntegrationStepLength     : bpy.props.FloatProperty( name='IntegrationStepLength',      default=0.2 )
    m_MaximumPropagationDistance: bpy.props.FloatProperty( name='MaximumPropagationDistance', default=100.0 )
    m_Radius                    : bpy.props.FloatProperty( name='Radius',                     default=0.5 )
    m_StepLength                : bpy.props.FloatProperty( name='StepLength',                 default=0.01 )
    m_TerminalEigenvalue        : bpy.props.FloatProperty( name='TerminalEigenvalue',         default=0.0 )
    e_IntegrationDirection      : bpy.props.EnumProperty ( name='IntegrationDirection',       default="Forward", items=e_IntegrationDirection_items )
    e_IntegrationEigenvector    : bpy.props.EnumProperty ( name='IntegrationEigenvector',     default="Major", items=e_IntegrationEigenvector_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_LogScaling','m_NumberOfSides','m_IntegrationStepLength','m_MaximumPropagationDistance','m_Radius','m_StepLength','m_TerminalEigenvalue','e_IntegrationDirection','e_IntegrationEigenvector',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperStreamline )        
TYPENAMES.append('VTKHyperStreamlineType' )

#--------------------------------------------------------------
class VTKHyperTreeGridAxisClip(Node, BVTK_Node):

    bl_idname = 'VTKHyperTreeGridAxisClipType'
    bl_label  = 'vtkHyperTreeGridAxisClip'
    e_ClipType_items=[ (x,x,x) for x in ['Plane', 'Box', 'Quadric']]
    
    m_InsideOut      : bpy.props.BoolProperty       ( name='InsideOut',       default=True )
    m_PlaneNormalAxis: bpy.props.IntProperty        ( name='PlaneNormalAxis', default=0 )
    m_PlanePosition  : bpy.props.FloatProperty      ( name='PlanePosition',   default=0.0 )
    e_ClipType       : bpy.props.EnumProperty       ( name='ClipType',        default="Plane", items=e_ClipType_items )
    m_Bounds         : bpy.props.FloatVectorProperty( name='Bounds',          default=[-0.5, 0.5, -0.5, 0.5, -0.5, 0.5], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_InsideOut','m_PlaneNormalAxis','m_PlanePosition','e_ClipType','m_Bounds',]
    def m_connections( self ):
        return (['input'], ['output'], ['Quadric'], []) 
    
add_class( VTKHyperTreeGridAxisClip )        
TYPENAMES.append('VTKHyperTreeGridAxisClipType' )

#--------------------------------------------------------------
class VTKHyperTreeGridAxisCut(Node, BVTK_Node):

    bl_idname = 'VTKHyperTreeGridAxisCutType'
    bl_label  = 'vtkHyperTreeGridAxisCut'
    
    m_PlaneNormalAxis: bpy.props.IntProperty  ( name='PlaneNormalAxis', default=0 )
    m_PlanePosition  : bpy.props.FloatProperty( name='PlanePosition',   default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PlaneNormalAxis','m_PlanePosition',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperTreeGridAxisCut )        
TYPENAMES.append('VTKHyperTreeGridAxisCutType' )

#--------------------------------------------------------------
class VTKHyperTreeGridAxisReflection(Node, BVTK_Node):

    bl_idname = 'VTKHyperTreeGridAxisReflectionType'
    bl_label  = 'vtkHyperTreeGridAxisReflection'
    e_Plane_items=[ (x,x,x) for x in ['XMin', 'YMin', 'ZMin', 'XMax', 'YMax', 'ZMax', 'X', 'Y', 'Z']]
    
    m_Center: bpy.props.FloatProperty( name='Center', default=0.0 )
    e_Plane : bpy.props.EnumProperty ( name='Plane',  default="XMin", items=e_Plane_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Center','e_Plane',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperTreeGridAxisReflection )        
TYPENAMES.append('VTKHyperTreeGridAxisReflectionType' )

#--------------------------------------------------------------
class VTKHyperTreeGridCellCenters(Node, BVTK_Node):

    bl_idname = 'VTKHyperTreeGridCellCentersType'
    bl_label  = 'vtkHyperTreeGridCellCenters'
    
    m_VertexCells: bpy.props.BoolProperty( name='VertexCells', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_VertexCells',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperTreeGridCellCenters )        
TYPENAMES.append('VTKHyperTreeGridCellCentersType' )

#--------------------------------------------------------------
class VTKHyperTreeGridContour(Node, BVTK_Node):

    bl_idname = 'VTKHyperTreeGridContourType'
    bl_label  = 'vtkHyperTreeGridContour'
    
    m_NumberOfContours: bpy.props.IntProperty( name='NumberOfContours', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperTreeGridContour )        
TYPENAMES.append('VTKHyperTreeGridContourType' )

#--------------------------------------------------------------
class VTKHyperTreeGridDepthLimiter(Node, BVTK_Node):

    bl_idname = 'VTKHyperTreeGridDepthLimiterType'
    bl_label  = 'vtkHyperTreeGridDepthLimiter'
    
    m_Depth: bpy.props.IntProperty( name='Depth', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Depth',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperTreeGridDepthLimiter )        
TYPENAMES.append('VTKHyperTreeGridDepthLimiterType' )

#--------------------------------------------------------------
class VTKHyperTreeGridGeometry(Node, BVTK_Node):

    bl_idname = 'VTKHyperTreeGridGeometryType'
    bl_label  = 'vtkHyperTreeGridGeometry'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperTreeGridGeometry )        
TYPENAMES.append('VTKHyperTreeGridGeometryType' )

#--------------------------------------------------------------
class VTKHyperTreeGridPlaneCutter(Node, BVTK_Node):

    bl_idname = 'VTKHyperTreeGridPlaneCutterType'
    bl_label  = 'vtkHyperTreeGridPlaneCutter'
    
    m_Dual : bpy.props.BoolProperty       ( name='Dual',  default=True )
    m_Plane: bpy.props.FloatVectorProperty( name='Plane', default=[0.0, 0.0, 0.0, 0.0], size=4 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Dual','m_Plane',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperTreeGridPlaneCutter )        
TYPENAMES.append('VTKHyperTreeGridPlaneCutterType' )

#--------------------------------------------------------------
class VTKHyperTreeGridThreshold(Node, BVTK_Node):

    bl_idname = 'VTKHyperTreeGridThresholdType'
    bl_label  = 'vtkHyperTreeGridThreshold'
    
    m_LowerThreshold: bpy.props.FloatProperty( name='LowerThreshold', default=2.2250738585072014e-308 )
    m_UpperThreshold: bpy.props.FloatProperty( name='UpperThreshold', default=1e+30 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_LowerThreshold','m_UpperThreshold',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperTreeGridThreshold )        
TYPENAMES.append('VTKHyperTreeGridThresholdType' )

#--------------------------------------------------------------
class VTKHyperTreeGridToUnstructuredGrid(Node, BVTK_Node):

    bl_idname = 'VTKHyperTreeGridToUnstructuredGridType'
    bl_label  = 'vtkHyperTreeGridToUnstructuredGrid'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKHyperTreeGridToUnstructuredGrid )        
TYPENAMES.append('VTKHyperTreeGridToUnstructuredGridType' )

#--------------------------------------------------------------
class VTKIconGlyphFilter(Node, BVTK_Node):

    bl_idname = 'VTKIconGlyphFilterType'
    bl_label  = 'vtkIconGlyphFilter'
    e_Gravity_items=[ (x,x,x) for x in ['TopRight', 'TopCenter', 'TopLeft', 'CenterRight', 'CenterCenter', 'CenterLeft', 'BottomRight', 'BottomCenter', 'BottomLeft']]
    e_IconScaling_items=[ (x,x,x) for x in ['ScalingOff', 'ScalingArray']]
    
    m_PassScalars  : bpy.props.BoolProperty     ( name='PassScalars',   default=False )
    m_UseIconSize  : bpy.props.BoolProperty     ( name='UseIconSize',   default=True )
    e_Gravity      : bpy.props.EnumProperty     ( name='Gravity',       default="CenterCenter", items=e_Gravity_items )
    e_IconScaling  : bpy.props.EnumProperty     ( name='IconScaling',   default="ScalingOff", items=e_IconScaling_items )
    m_DisplaySize  : bpy.props.IntVectorProperty( name='DisplaySize',   default=[25, 25], size=2 )
    m_IconSheetSize: bpy.props.IntVectorProperty( name='IconSheetSize', default=[1, 1], size=2 )
    m_IconSize     : bpy.props.IntVectorProperty( name='IconSize',      default=[1, 1], size=2 )
    m_Offset       : bpy.props.IntVectorProperty( name='Offset',        default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassScalars','m_UseIconSize','e_Gravity','e_IconScaling','m_DisplaySize','m_IconSheetSize','m_IconSize','m_Offset',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKIconGlyphFilter )        
TYPENAMES.append('VTKIconGlyphFilterType' )

#--------------------------------------------------------------
class VTKIdFilter(Node, BVTK_Node):

    bl_idname = 'VTKIdFilterType'
    bl_label  = 'vtkIdFilter'
    
    m_CellIds     : bpy.props.BoolProperty  ( name='CellIds',      default=True )
    m_FieldData   : bpy.props.BoolProperty  ( name='FieldData',    default=True )
    m_PointIds    : bpy.props.BoolProperty  ( name='PointIds',     default=True )
    m_IdsArrayName: bpy.props.StringProperty( name='IdsArrayName', default="vtkIdFilter_Ids" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CellIds','m_FieldData','m_PointIds','m_IdsArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKIdFilter )        
TYPENAMES.append('VTKIdFilterType' )

#--------------------------------------------------------------
class VTKImageAnisotropicDiffusion2D(Node, BVTK_Node):

    bl_idname = 'VTKImageAnisotropicDiffusion2DType'
    bl_label  = 'vtkImageAnisotropicDiffusion2D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_Corners                   : bpy.props.BoolProperty     ( name='Corners',                    default=True )
    m_Edges                     : bpy.props.BoolProperty     ( name='Edges',                      default=True )
    m_EnableSMP                 : bpy.props.BoolProperty     ( name='EnableSMP',                  default=True )
    m_Faces                     : bpy.props.BoolProperty     ( name='Faces',                      default=True )
    m_GlobalDefaultEnableSMP    : bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP',     default=True )
    m_GradientMagnitudeThreshold: bpy.props.BoolProperty     ( name='GradientMagnitudeThreshold', default=True )
    m_DesiredBytesPerPiece      : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',       default=65536 )
    m_NumberOfIterations        : bpy.props.IntProperty      ( name='NumberOfIterations',         default=4 )
    m_NumberOfThreads           : bpy.props.IntProperty      ( name='NumberOfThreads',            default=8 )
    m_DiffusionFactor           : bpy.props.FloatProperty    ( name='DiffusionFactor',            default=1.0 )
    m_DiffusionThreshold        : bpy.props.FloatProperty    ( name='DiffusionThreshold',         default=5.0 )
    e_SplitMode                 : bpy.props.EnumProperty     ( name='SplitMode',                  default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize          : bpy.props.IntVectorProperty( name='MinimumPieceSize',           default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Corners','m_Edges','m_EnableSMP','m_Faces','m_GlobalDefaultEnableSMP','m_GradientMagnitudeThreshold','m_DesiredBytesPerPiece','m_NumberOfIterations','m_NumberOfThreads','m_DiffusionFactor','m_DiffusionThreshold','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageAnisotropicDiffusion2D )        
TYPENAMES.append('VTKImageAnisotropicDiffusion2DType' )

#--------------------------------------------------------------
class VTKImageAnisotropicDiffusion3D(Node, BVTK_Node):

    bl_idname = 'VTKImageAnisotropicDiffusion3DType'
    bl_label  = 'vtkImageAnisotropicDiffusion3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_Corners                   : bpy.props.BoolProperty     ( name='Corners',                    default=True )
    m_Edges                     : bpy.props.BoolProperty     ( name='Edges',                      default=True )
    m_EnableSMP                 : bpy.props.BoolProperty     ( name='EnableSMP',                  default=True )
    m_Faces                     : bpy.props.BoolProperty     ( name='Faces',                      default=True )
    m_GlobalDefaultEnableSMP    : bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP',     default=True )
    m_GradientMagnitudeThreshold: bpy.props.BoolProperty     ( name='GradientMagnitudeThreshold', default=True )
    m_DesiredBytesPerPiece      : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',       default=65536 )
    m_NumberOfIterations        : bpy.props.IntProperty      ( name='NumberOfIterations',         default=4 )
    m_NumberOfThreads           : bpy.props.IntProperty      ( name='NumberOfThreads',            default=8 )
    m_DiffusionFactor           : bpy.props.FloatProperty    ( name='DiffusionFactor',            default=1.0 )
    m_DiffusionThreshold        : bpy.props.FloatProperty    ( name='DiffusionThreshold',         default=5.0 )
    e_SplitMode                 : bpy.props.EnumProperty     ( name='SplitMode',                  default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize          : bpy.props.IntVectorProperty( name='MinimumPieceSize',           default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Corners','m_Edges','m_EnableSMP','m_Faces','m_GlobalDefaultEnableSMP','m_GradientMagnitudeThreshold','m_DesiredBytesPerPiece','m_NumberOfIterations','m_NumberOfThreads','m_DiffusionFactor','m_DiffusionThreshold','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageAnisotropicDiffusion3D )        
TYPENAMES.append('VTKImageAnisotropicDiffusion3DType' )

#--------------------------------------------------------------
class VTKImageAppend(Node, BVTK_Node):

    bl_idname = 'VTKImageAppendType'
    bl_label  = 'vtkImageAppend'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_PreserveExtents       : bpy.props.BoolProperty     ( name='PreserveExtents',        default=True )
    m_AppendAxis            : bpy.props.IntProperty      ( name='AppendAxis',             default=0 )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_PreserveExtents','m_AppendAxis','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageAppend )        
TYPENAMES.append('VTKImageAppendType' )

#--------------------------------------------------------------
class VTKImageAppendComponents(Node, BVTK_Node):

    bl_idname = 'VTKImageAppendComponentsType'
    bl_label  = 'vtkImageAppendComponents'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageAppendComponents )        
TYPENAMES.append('VTKImageAppendComponentsType' )

#--------------------------------------------------------------
class VTKImageBSplineCoefficients(Node, BVTK_Node):

    bl_idname = 'VTKImageBSplineCoefficientsType'
    bl_label  = 'vtkImageBSplineCoefficients'
    e_BorderMode_items=[ (x,x,x) for x in ['Clamp', 'Repeat', 'Mirror']]
    e_OutputScalarType_items=[ (x,x,x) for x in ['Float', 'Double']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_Bypass                : bpy.props.BoolProperty     ( name='Bypass',                 default=True )
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_SplineDegree          : bpy.props.IntProperty      ( name='SplineDegree',           default=3 )
    e_BorderMode            : bpy.props.EnumProperty     ( name='BorderMode',             default="Clamp", items=e_BorderMode_items )
    e_OutputScalarType      : bpy.props.EnumProperty     ( name='OutputScalarType',       default="Float", items=e_OutputScalarType_items )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Bypass','m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_SplineDegree','e_BorderMode','e_OutputScalarType','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageBSplineCoefficients )        
TYPENAMES.append('VTKImageBSplineCoefficientsType' )

#--------------------------------------------------------------
class VTKImageButterworthHighPass(Node, BVTK_Node):

    bl_idname = 'VTKImageButterworthHighPassType'
    bl_label  = 'vtkImageButterworthHighPass'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty       ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty        ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty        ( name='NumberOfThreads',        default=8 )
    m_Order                 : bpy.props.IntProperty        ( name='Order',                  default=1 )
    m_XCutOff               : bpy.props.FloatProperty      ( name='XCutOff',                default=1e+30 )
    m_YCutOff               : bpy.props.FloatProperty      ( name='YCutOff',                default=1e+30 )
    m_ZCutOff               : bpy.props.FloatProperty      ( name='ZCutOff',                default=1e+30 )
    e_SplitMode             : bpy.props.EnumProperty       ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty  ( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_CutOff                : bpy.props.FloatVectorProperty( name='CutOff',                 default=[1e+30, 1e+30, 1e+30], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Order','m_XCutOff','m_YCutOff','m_ZCutOff','e_SplitMode','m_MinimumPieceSize','m_CutOff',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageButterworthHighPass )        
TYPENAMES.append('VTKImageButterworthHighPassType' )

#--------------------------------------------------------------
class VTKImageButterworthLowPass(Node, BVTK_Node):

    bl_idname = 'VTKImageButterworthLowPassType'
    bl_label  = 'vtkImageButterworthLowPass'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty       ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty        ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty        ( name='NumberOfThreads',        default=8 )
    m_Order                 : bpy.props.IntProperty        ( name='Order',                  default=1 )
    m_XCutOff               : bpy.props.FloatProperty      ( name='XCutOff',                default=1e+30 )
    m_YCutOff               : bpy.props.FloatProperty      ( name='YCutOff',                default=1e+30 )
    m_ZCutOff               : bpy.props.FloatProperty      ( name='ZCutOff',                default=1e+30 )
    e_SplitMode             : bpy.props.EnumProperty       ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty  ( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_CutOff                : bpy.props.FloatVectorProperty( name='CutOff',                 default=[1e+30, 1e+30, 1e+30], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Order','m_XCutOff','m_YCutOff','m_ZCutOff','e_SplitMode','m_MinimumPieceSize','m_CutOff',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageButterworthLowPass )        
TYPENAMES.append('VTKImageButterworthLowPassType' )

#--------------------------------------------------------------
class VTKImageCacheFilter(Node, BVTK_Node):

    bl_idname = 'VTKImageCacheFilterType'
    bl_label  = 'vtkImageCacheFilter'
    
    m_CacheSize: bpy.props.IntProperty( name='CacheSize', default=10 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CacheSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageCacheFilter )        
TYPENAMES.append('VTKImageCacheFilterType' )

#--------------------------------------------------------------
class VTKImageCast(Node, BVTK_Node):

    bl_idname = 'VTKImageCastType'
    bl_label  = 'vtkImageCast'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_ClampOverflow         : bpy.props.BoolProperty     ( name='ClampOverflow',          default=True )
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_OutputScalarType      : bpy.props.EnumProperty     ( name='OutputScalarType',       default="Float", items=e_OutputScalarType_items )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClampOverflow','m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_OutputScalarType','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageCast )        
TYPENAMES.append('VTKImageCastType' )

#--------------------------------------------------------------
class VTKImageCityBlockDistance(Node, BVTK_Node):

    bl_idname = 'VTKImageCityBlockDistanceType'
    bl_label  = 'vtkImageCityBlockDistance'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality        : bpy.props.IntProperty      ( name='Dimensionality',         default=3 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageCityBlockDistance )        
TYPENAMES.append('VTKImageCityBlockDistanceType' )

#--------------------------------------------------------------
class VTKImageClip(Node, BVTK_Node):

    bl_idname = 'VTKImageClipType'
    bl_label  = 'vtkImageClip'
    
    m_ClipData: bpy.props.BoolProperty( name='ClipData', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClipData',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageClip )        
TYPENAMES.append('VTKImageClipType' )

#--------------------------------------------------------------
class VTKImageConstantPad(Node, BVTK_Node):

    bl_idname = 'VTKImageConstantPadType'
    bl_label  = 'vtkImageConstantPad'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP                     : bpy.props.BoolProperty     ( name='EnableSMP',                      default=True )
    m_GlobalDefaultEnableSMP        : bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP',         default=True )
    m_DesiredBytesPerPiece          : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',           default=65536 )
    m_NumberOfThreads               : bpy.props.IntProperty      ( name='NumberOfThreads',                default=8 )
    m_OutputNumberOfScalarComponents: bpy.props.IntProperty      ( name='OutputNumberOfScalarComponents', default=-1 )
    m_Constant                      : bpy.props.FloatProperty    ( name='Constant',                       default=0.0 )
    e_SplitMode                     : bpy.props.EnumProperty     ( name='SplitMode',                      default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize              : bpy.props.IntVectorProperty( name='MinimumPieceSize',               default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputNumberOfScalarComponents','m_Constant','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageConstantPad )        
TYPENAMES.append('VTKImageConstantPadType' )

#--------------------------------------------------------------
class VTKImageContinuousDilate3D(Node, BVTK_Node):

    bl_idname = 'VTKImageContinuousDilate3DType'
    bl_label  = 'vtkImageContinuousDilate3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_KernelSize            : bpy.props.IntVectorProperty( name='KernelSize',             default=[1, 1, 1], size=3 )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageContinuousDilate3D )        
TYPENAMES.append('VTKImageContinuousDilate3DType' )

#--------------------------------------------------------------
class VTKImageContinuousErode3D(Node, BVTK_Node):

    bl_idname = 'VTKImageContinuousErode3DType'
    bl_label  = 'vtkImageContinuousErode3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_KernelSize            : bpy.props.IntVectorProperty( name='KernelSize',             default=[1, 1, 1], size=3 )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageContinuousErode3D )        
TYPENAMES.append('VTKImageContinuousErode3DType' )

#--------------------------------------------------------------
class VTKImageConvolve(Node, BVTK_Node):

    bl_idname = 'VTKImageConvolveType'
    bl_label  = 'vtkImageConvolve'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageConvolve )        
TYPENAMES.append('VTKImageConvolveType' )

#--------------------------------------------------------------
class VTKImageCursor3D(Node, BVTK_Node):

    bl_idname = 'VTKImageCursor3DType'
    bl_label  = 'vtkImageCursor3D'
    
    m_CursorRadius  : bpy.props.IntProperty        ( name='CursorRadius',   default=5 )
    m_CursorValue   : bpy.props.FloatProperty      ( name='CursorValue',    default=255.0 )
    m_CursorPosition: bpy.props.FloatVectorProperty( name='CursorPosition', default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CursorRadius','m_CursorValue','m_CursorPosition',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageCursor3D )        
TYPENAMES.append('VTKImageCursor3DType' )

#--------------------------------------------------------------
class VTKImageDataGeometryFilter(Node, BVTK_Node):

    bl_idname = 'VTKImageDataGeometryFilterType'
    bl_label  = 'vtkImageDataGeometryFilter'
    
    m_OutputTriangles: bpy.props.BoolProperty( name='OutputTriangles', default=True )
    m_ThresholdCells : bpy.props.BoolProperty( name='ThresholdCells',  default=True )
    m_ThresholdValue : bpy.props.BoolProperty( name='ThresholdValue',  default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_OutputTriangles','m_ThresholdCells','m_ThresholdValue',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageDataGeometryFilter )        
TYPENAMES.append('VTKImageDataGeometryFilterType' )

#--------------------------------------------------------------
class VTKImageDataStreamer(Node, BVTK_Node):

    bl_idname = 'VTKImageDataStreamerType'
    bl_label  = 'vtkImageDataStreamer'
    
    m_NumberOfStreamDivisions: bpy.props.IntProperty( name='NumberOfStreamDivisions', default=10 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NumberOfStreamDivisions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ExtentTranslator'], []) 
    
add_class( VTKImageDataStreamer )        
TYPENAMES.append('VTKImageDataStreamerType' )

#--------------------------------------------------------------
class VTKImageDataToPointSet(Node, BVTK_Node):

    bl_idname = 'VTKImageDataToPointSetType'
    bl_label  = 'vtkImageDataToPointSet'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageDataToPointSet )        
TYPENAMES.append('VTKImageDataToPointSetType' )

#--------------------------------------------------------------
class VTKImageDataToUniformGrid(Node, BVTK_Node):

    bl_idname = 'VTKImageDataToUniformGridType'
    bl_label  = 'vtkImageDataToUniformGrid'
    
    m_Reverse: bpy.props.BoolProperty( name='Reverse', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Reverse',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageDataToUniformGrid )        
TYPENAMES.append('VTKImageDataToUniformGridType' )

#--------------------------------------------------------------
class VTKImageDilateErode3D(Node, BVTK_Node):

    bl_idname = 'VTKImageDilateErode3DType'
    bl_label  = 'vtkImageDilateErode3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_DilateValue           : bpy.props.FloatProperty    ( name='DilateValue',            default=0.0 )
    m_ErodeValue            : bpy.props.FloatProperty    ( name='ErodeValue',             default=255.0 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_KernelSize            : bpy.props.IntVectorProperty( name='KernelSize',             default=[1, 1, 1], size=3 )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_DilateValue','m_ErodeValue','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageDilateErode3D )        
TYPENAMES.append('VTKImageDilateErode3DType' )

#--------------------------------------------------------------
class VTKImageDivergence(Node, BVTK_Node):

    bl_idname = 'VTKImageDivergenceType'
    bl_label  = 'vtkImageDivergence'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageDivergence )        
TYPENAMES.append('VTKImageDivergenceType' )

#--------------------------------------------------------------
class VTKImageEuclideanDistance(Node, BVTK_Node):

    bl_idname = 'VTKImageEuclideanDistanceType'
    bl_label  = 'vtkImageEuclideanDistance'
    e_Algorithm_items=[ (x,x,x) for x in ['SaitoCached', 'Saito']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_ConsiderAnisotropy    : bpy.props.BoolProperty     ( name='ConsiderAnisotropy',     default=True )
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_Initialize            : bpy.props.BoolProperty     ( name='Initialize',             default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality        : bpy.props.IntProperty      ( name='Dimensionality',         default=3 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_MaximumDistance       : bpy.props.FloatProperty    ( name='MaximumDistance',        default=2147483647.0 )
    e_Algorithm             : bpy.props.EnumProperty     ( name='Algorithm',              default="Saito", items=e_Algorithm_items )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ConsiderAnisotropy','m_EnableSMP','m_GlobalDefaultEnableSMP','m_Initialize','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','m_MaximumDistance','e_Algorithm','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageEuclideanDistance )        
TYPENAMES.append('VTKImageEuclideanDistanceType' )

#--------------------------------------------------------------
class VTKImageEuclideanToPolar(Node, BVTK_Node):

    bl_idname = 'VTKImageEuclideanToPolarType'
    bl_label  = 'vtkImageEuclideanToPolar'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_ThetaMaximum          : bpy.props.FloatProperty    ( name='ThetaMaximum',           default=255.0 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_ThetaMaximum','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageEuclideanToPolar )        
TYPENAMES.append('VTKImageEuclideanToPolarType' )

#--------------------------------------------------------------
class VTKImageExtractComponents(Node, BVTK_Node):

    bl_idname = 'VTKImageExtractComponentsType'
    bl_label  = 'vtkImageExtractComponents'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageExtractComponents )        
TYPENAMES.append('VTKImageExtractComponentsType' )

#--------------------------------------------------------------
class VTKImageFFT(Node, BVTK_Node):

    bl_idname = 'VTKImageFFTType'
    bl_label  = 'vtkImageFFT'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality        : bpy.props.IntProperty      ( name='Dimensionality',         default=3 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageFFT )        
TYPENAMES.append('VTKImageFFTType' )

#--------------------------------------------------------------
class VTKImageFourierCenter(Node, BVTK_Node):

    bl_idname = 'VTKImageFourierCenterType'
    bl_label  = 'vtkImageFourierCenter'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality        : bpy.props.IntProperty      ( name='Dimensionality',         default=3 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageFourierCenter )        
TYPENAMES.append('VTKImageFourierCenterType' )

#--------------------------------------------------------------
class VTKImageGaussianSmooth(Node, BVTK_Node):

    bl_idname = 'VTKImageGaussianSmoothType'
    bl_label  = 'vtkImageGaussianSmooth'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty       ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty        ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality        : bpy.props.IntProperty        ( name='Dimensionality',         default=3 )
    m_NumberOfThreads       : bpy.props.IntProperty        ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty       ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty  ( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_RadiusFactors         : bpy.props.FloatVectorProperty( name='RadiusFactors',          default=[1.5, 1.5, 1.5], size=3 )
    m_StandardDeviations    : bpy.props.FloatVectorProperty( name='StandardDeviations',     default=[2.0, 2.0, 2.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize','m_RadiusFactors','m_StandardDeviations',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageGaussianSmooth )        
TYPENAMES.append('VTKImageGaussianSmoothType' )

#--------------------------------------------------------------
class VTKImageGradient(Node, BVTK_Node):

    bl_idname = 'VTKImageGradientType'
    bl_label  = 'vtkImageGradient'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_HandleBoundaries      : bpy.props.BoolProperty     ( name='HandleBoundaries',       default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality        : bpy.props.IntProperty      ( name='Dimensionality',         default=2 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_HandleBoundaries','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageGradient )        
TYPENAMES.append('VTKImageGradientType' )

#--------------------------------------------------------------
class VTKImageGradientMagnitude(Node, BVTK_Node):

    bl_idname = 'VTKImageGradientMagnitudeType'
    bl_label  = 'vtkImageGradientMagnitude'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_HandleBoundaries      : bpy.props.BoolProperty     ( name='HandleBoundaries',       default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality        : bpy.props.IntProperty      ( name='Dimensionality',         default=2 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_HandleBoundaries','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageGradientMagnitude )        
TYPENAMES.append('VTKImageGradientMagnitudeType' )

#--------------------------------------------------------------
class VTKImageHSIToRGB(Node, BVTK_Node):

    bl_idname = 'VTKImageHSIToRGBType'
    bl_label  = 'vtkImageHSIToRGB'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Maximum               : bpy.props.FloatProperty    ( name='Maximum',                default=255.0 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageHSIToRGB )        
TYPENAMES.append('VTKImageHSIToRGBType' )

#--------------------------------------------------------------
class VTKImageHSVToRGB(Node, BVTK_Node):

    bl_idname = 'VTKImageHSVToRGBType'
    bl_label  = 'vtkImageHSVToRGB'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Maximum               : bpy.props.FloatProperty    ( name='Maximum',                default=255.0 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageHSVToRGB )        
TYPENAMES.append('VTKImageHSVToRGBType' )

#--------------------------------------------------------------
class VTKImageHybridMedian2D(Node, BVTK_Node):

    bl_idname = 'VTKImageHybridMedian2DType'
    bl_label  = 'vtkImageHybridMedian2D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageHybridMedian2D )        
TYPENAMES.append('VTKImageHybridMedian2DType' )

#--------------------------------------------------------------
class VTKImageIdealHighPass(Node, BVTK_Node):

    bl_idname = 'VTKImageIdealHighPassType'
    bl_label  = 'vtkImageIdealHighPass'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty       ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty        ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty        ( name='NumberOfThreads',        default=8 )
    m_XCutOff               : bpy.props.FloatProperty      ( name='XCutOff',                default=1e+30 )
    m_YCutOff               : bpy.props.FloatProperty      ( name='YCutOff',                default=1e+30 )
    m_ZCutOff               : bpy.props.FloatProperty      ( name='ZCutOff',                default=1e+30 )
    e_SplitMode             : bpy.props.EnumProperty       ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty  ( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_CutOff                : bpy.props.FloatVectorProperty( name='CutOff',                 default=[1e+30, 1e+30, 1e+30], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_XCutOff','m_YCutOff','m_ZCutOff','e_SplitMode','m_MinimumPieceSize','m_CutOff',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageIdealHighPass )        
TYPENAMES.append('VTKImageIdealHighPassType' )

#--------------------------------------------------------------
class VTKImageIdealLowPass(Node, BVTK_Node):

    bl_idname = 'VTKImageIdealLowPassType'
    bl_label  = 'vtkImageIdealLowPass'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty       ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty        ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty        ( name='NumberOfThreads',        default=8 )
    m_XCutOff               : bpy.props.FloatProperty      ( name='XCutOff',                default=1e+30 )
    m_YCutOff               : bpy.props.FloatProperty      ( name='YCutOff',                default=1e+30 )
    m_ZCutOff               : bpy.props.FloatProperty      ( name='ZCutOff',                default=1e+30 )
    e_SplitMode             : bpy.props.EnumProperty       ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty  ( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_CutOff                : bpy.props.FloatVectorProperty( name='CutOff',                 default=[1e+30, 1e+30, 1e+30], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_XCutOff','m_YCutOff','m_ZCutOff','e_SplitMode','m_MinimumPieceSize','m_CutOff',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageIdealLowPass )        
TYPENAMES.append('VTKImageIdealLowPassType' )

#--------------------------------------------------------------
class VTKImageIslandRemoval2D(Node, BVTK_Node):

    bl_idname = 'VTKImageIslandRemoval2DType'
    bl_label  = 'vtkImageIslandRemoval2D'
    
    m_SquareNeighborhood: bpy.props.BoolProperty ( name='SquareNeighborhood', default=True )
    m_AreaThreshold     : bpy.props.IntProperty  ( name='AreaThreshold',      default=4 )
    m_IslandValue       : bpy.props.FloatProperty( name='IslandValue',        default=0.0 )
    m_ReplaceValue      : bpy.props.FloatProperty( name='ReplaceValue',       default=255.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_SquareNeighborhood','m_AreaThreshold','m_IslandValue','m_ReplaceValue',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageIslandRemoval2D )        
TYPENAMES.append('VTKImageIslandRemoval2DType' )

#--------------------------------------------------------------
class VTKImageLaplacian(Node, BVTK_Node):

    bl_idname = 'VTKImageLaplacianType'
    bl_label  = 'vtkImageLaplacian'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality        : bpy.props.IntProperty      ( name='Dimensionality',         default=2 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageLaplacian )        
TYPENAMES.append('VTKImageLaplacianType' )

#--------------------------------------------------------------
class VTKImageLogarithmicScale(Node, BVTK_Node):

    bl_idname = 'VTKImageLogarithmicScaleType'
    bl_label  = 'vtkImageLogarithmicScale'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Constant              : bpy.props.FloatProperty    ( name='Constant',               default=10.0 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Constant','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageLogarithmicScale )        
TYPENAMES.append('VTKImageLogarithmicScaleType' )

#--------------------------------------------------------------
class VTKImageLuminance(Node, BVTK_Node):

    bl_idname = 'VTKImageLuminanceType'
    bl_label  = 'vtkImageLuminance'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageLuminance )        
TYPENAMES.append('VTKImageLuminanceType' )

#--------------------------------------------------------------
class VTKImageMagnify(Node, BVTK_Node):

    bl_idname = 'VTKImageMagnifyType'
    bl_label  = 'vtkImageMagnify'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_Interpolate           : bpy.props.BoolProperty     ( name='Interpolate',            default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MagnificationFactors  : bpy.props.IntVectorProperty( name='MagnificationFactors',   default=[1, 1, 1], size=3 )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_Interpolate','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MagnificationFactors','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageMagnify )        
TYPENAMES.append('VTKImageMagnifyType' )

#--------------------------------------------------------------
class VTKImageMagnitude(Node, BVTK_Node):

    bl_idname = 'VTKImageMagnitudeType'
    bl_label  = 'vtkImageMagnitude'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageMagnitude )        
TYPENAMES.append('VTKImageMagnitudeType' )

#--------------------------------------------------------------
class VTKImageMapToColors(Node, BVTK_Node):

    bl_idname = 'VTKImageMapToColorsType'
    bl_label  = 'vtkImageMapToColors'
    e_OutputFormat_items=[ (x,x,x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_PassAlphaToOutput     : bpy.props.BoolProperty     ( name='PassAlphaToOutput',      default=True )
    m_ActiveComponent       : bpy.props.IntProperty      ( name='ActiveComponent',        default=0 )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_OutputFormat          : bpy.props.EnumProperty     ( name='OutputFormat',           default="RGBA", items=e_OutputFormat_items )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_NaNColor              : bpy.props.IntVectorProperty( name='NaNColor',               default=[0, 0, 0, 0], size=4 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_PassAlphaToOutput','m_ActiveComponent','m_DesiredBytesPerPiece','m_NumberOfThreads','e_OutputFormat','e_SplitMode','m_MinimumPieceSize','m_NaNColor',]
    def m_connections( self ):
        return (['input'], ['output'], ['LookupTable'], []) 
    
add_class( VTKImageMapToColors )        
TYPENAMES.append('VTKImageMapToColorsType' )

#--------------------------------------------------------------
class VTKImageMapToRGBA(Node, BVTK_Node):

    bl_idname = 'VTKImageMapToRGBAType'
    bl_label  = 'vtkImageMapToRGBA'
    e_OutputFormat_items=[ (x,x,x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_PassAlphaToOutput     : bpy.props.BoolProperty     ( name='PassAlphaToOutput',      default=True )
    m_ActiveComponent       : bpy.props.IntProperty      ( name='ActiveComponent',        default=0 )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_OutputFormat          : bpy.props.EnumProperty     ( name='OutputFormat',           default="RGBA", items=e_OutputFormat_items )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_NaNColor              : bpy.props.IntVectorProperty( name='NaNColor',               default=[0, 0, 0, 0], size=4 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_PassAlphaToOutput','m_ActiveComponent','m_DesiredBytesPerPiece','m_NumberOfThreads','e_OutputFormat','e_SplitMode','m_MinimumPieceSize','m_NaNColor',]
    def m_connections( self ):
        return (['input'], ['output'], ['LookupTable'], []) 
    
add_class( VTKImageMapToRGBA )        
TYPENAMES.append('VTKImageMapToRGBAType' )

#--------------------------------------------------------------
class VTKImageMapToWindowLevelColors(Node, BVTK_Node):

    bl_idname = 'VTKImageMapToWindowLevelColorsType'
    bl_label  = 'vtkImageMapToWindowLevelColors'
    e_OutputFormat_items=[ (x,x,x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_PassAlphaToOutput     : bpy.props.BoolProperty     ( name='PassAlphaToOutput',      default=True )
    m_ActiveComponent       : bpy.props.IntProperty      ( name='ActiveComponent',        default=0 )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Level                 : bpy.props.FloatProperty    ( name='Level',                  default=127.5 )
    m_Window                : bpy.props.FloatProperty    ( name='Window',                 default=255.0 )
    e_OutputFormat          : bpy.props.EnumProperty     ( name='OutputFormat',           default="RGBA", items=e_OutputFormat_items )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_NaNColor              : bpy.props.IntVectorProperty( name='NaNColor',               default=[0, 0, 0, 0], size=4 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_PassAlphaToOutput','m_ActiveComponent','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Level','m_Window','e_OutputFormat','e_SplitMode','m_MinimumPieceSize','m_NaNColor',]
    def m_connections( self ):
        return (['input'], ['output'], ['LookupTable'], []) 
    
add_class( VTKImageMapToWindowLevelColors )        
TYPENAMES.append('VTKImageMapToWindowLevelColorsType' )

#--------------------------------------------------------------
class VTKImageMarchingCubes(Node, BVTK_Node):

    bl_idname = 'VTKImageMarchingCubesType'
    bl_label  = 'vtkImageMarchingCubes'
    
    m_ComputeGradients: bpy.props.BoolProperty( name='ComputeGradients', default=True )
    m_ComputeNormals  : bpy.props.BoolProperty( name='ComputeNormals',   default=True )
    m_ComputeScalars  : bpy.props.BoolProperty( name='ComputeScalars',   default=True )
    m_InputMemoryLimit: bpy.props.IntProperty ( name='InputMemoryLimit', default=10240 )
    m_NumberOfContours: bpy.props.IntProperty ( name='NumberOfContours', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_InputMemoryLimit','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageMarchingCubes )        
TYPENAMES.append('VTKImageMarchingCubesType' )

#--------------------------------------------------------------
class VTKImageMaskBits(Node, BVTK_Node):

    bl_idname = 'VTKImageMaskBitsType'
    bl_label  = 'vtkImageMaskBits'
    e_Operation_items=[ (x,x,x) for x in ['And', 'Or', 'Xor', 'Nand', 'Nor']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_Operation             : bpy.props.EnumProperty     ( name='Operation',              default="And", items=e_Operation_items )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_Masks                 : bpy.props.IntVectorProperty( name='Masks',                  default=[1000000000, 1000000000, 1000000000, 1000000000], size=4 )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_Operation','e_SplitMode','m_Masks','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageMaskBits )        
TYPENAMES.append('VTKImageMaskBitsType' )

#--------------------------------------------------------------
class VTKImageMedian3D(Node, BVTK_Node):

    bl_idname = 'VTKImageMedian3DType'
    bl_label  = 'vtkImageMedian3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_KernelSize            : bpy.props.IntVectorProperty( name='KernelSize',             default=[1, 1, 1], size=3 )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageMedian3D )        
TYPENAMES.append('VTKImageMedian3DType' )

#--------------------------------------------------------------
class VTKImageMirrorPad(Node, BVTK_Node):

    bl_idname = 'VTKImageMirrorPadType'
    bl_label  = 'vtkImageMirrorPad'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP                     : bpy.props.BoolProperty     ( name='EnableSMP',                      default=True )
    m_GlobalDefaultEnableSMP        : bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP',         default=True )
    m_DesiredBytesPerPiece          : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',           default=65536 )
    m_NumberOfThreads               : bpy.props.IntProperty      ( name='NumberOfThreads',                default=8 )
    m_OutputNumberOfScalarComponents: bpy.props.IntProperty      ( name='OutputNumberOfScalarComponents', default=-1 )
    e_SplitMode                     : bpy.props.EnumProperty     ( name='SplitMode',                      default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize              : bpy.props.IntVectorProperty( name='MinimumPieceSize',               default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputNumberOfScalarComponents','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageMirrorPad )        
TYPENAMES.append('VTKImageMirrorPadType' )

#--------------------------------------------------------------
class VTKImageNormalize(Node, BVTK_Node):

    bl_idname = 'VTKImageNormalizeType'
    bl_label  = 'vtkImageNormalize'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageNormalize )        
TYPENAMES.append('VTKImageNormalizeType' )

#--------------------------------------------------------------
class VTKImageOpenClose3D(Node, BVTK_Node):

    bl_idname = 'VTKImageOpenClose3DType'
    bl_label  = 'vtkImageOpenClose3D'
    
    m_CloseValue: bpy.props.FloatProperty( name='CloseValue', default=255.0 )
    m_OpenValue : bpy.props.FloatProperty( name='OpenValue',  default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CloseValue','m_OpenValue',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageOpenClose3D )        
TYPENAMES.append('VTKImageOpenClose3DType' )

#--------------------------------------------------------------
class VTKImagePadFilter(Node, BVTK_Node):

    bl_idname = 'VTKImagePadFilterType'
    bl_label  = 'vtkImagePadFilter'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP                     : bpy.props.BoolProperty     ( name='EnableSMP',                      default=True )
    m_GlobalDefaultEnableSMP        : bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP',         default=True )
    m_DesiredBytesPerPiece          : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',           default=65536 )
    m_NumberOfThreads               : bpy.props.IntProperty      ( name='NumberOfThreads',                default=8 )
    m_OutputNumberOfScalarComponents: bpy.props.IntProperty      ( name='OutputNumberOfScalarComponents', default=-1 )
    e_SplitMode                     : bpy.props.EnumProperty     ( name='SplitMode',                      default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize              : bpy.props.IntVectorProperty( name='MinimumPieceSize',               default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputNumberOfScalarComponents','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImagePadFilter )        
TYPENAMES.append('VTKImagePadFilterType' )

#--------------------------------------------------------------
class VTKImageQuantizeRGBToIndex(Node, BVTK_Node):

    bl_idname = 'VTKImageQuantizeRGBToIndexType'
    bl_label  = 'vtkImageQuantizeRGBToIndex'
    
    m_SortIndexByLuminance  : bpy.props.BoolProperty     ( name='SortIndexByLuminance',   default=False )
    m_NumberOfColors        : bpy.props.IntProperty      ( name='NumberOfColors',         default=256 )
    m_BuildTreeExecuteTime  : bpy.props.FloatProperty    ( name='BuildTreeExecuteTime',   default=0.0 )
    m_InitializeExecuteTime : bpy.props.FloatProperty    ( name='InitializeExecuteTime',  default=0.0 )
    m_LookupIndexExecuteTime: bpy.props.FloatProperty    ( name='LookupIndexExecuteTime', default=0.0 )
    m_SamplingRate          : bpy.props.IntVectorProperty( name='SamplingRate',           default=[1, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_SortIndexByLuminance','m_NumberOfColors','m_BuildTreeExecuteTime','m_InitializeExecuteTime','m_LookupIndexExecuteTime','m_SamplingRate',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageQuantizeRGBToIndex )        
TYPENAMES.append('VTKImageQuantizeRGBToIndexType' )

#--------------------------------------------------------------
class VTKImageRFFT(Node, BVTK_Node):

    bl_idname = 'VTKImageRFFTType'
    bl_label  = 'vtkImageRFFT'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality        : bpy.props.IntProperty      ( name='Dimensionality',         default=3 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageRFFT )        
TYPENAMES.append('VTKImageRFFTType' )

#--------------------------------------------------------------
class VTKImageRGBToHSI(Node, BVTK_Node):

    bl_idname = 'VTKImageRGBToHSIType'
    bl_label  = 'vtkImageRGBToHSI'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Maximum               : bpy.props.FloatProperty    ( name='Maximum',                default=255.0 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageRGBToHSI )        
TYPENAMES.append('VTKImageRGBToHSIType' )

#--------------------------------------------------------------
class VTKImageRGBToHSV(Node, BVTK_Node):

    bl_idname = 'VTKImageRGBToHSVType'
    bl_label  = 'vtkImageRGBToHSV'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Maximum               : bpy.props.FloatProperty    ( name='Maximum',                default=255.0 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageRGBToHSV )        
TYPENAMES.append('VTKImageRGBToHSVType' )

#--------------------------------------------------------------
class VTKImageRGBToYIQ(Node, BVTK_Node):

    bl_idname = 'VTKImageRGBToYIQType'
    bl_label  = 'vtkImageRGBToYIQ'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Maximum               : bpy.props.FloatProperty    ( name='Maximum',                default=255.0 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageRGBToYIQ )        
TYPENAMES.append('VTKImageRGBToYIQType' )

#--------------------------------------------------------------
class VTKImageRange3D(Node, BVTK_Node):

    bl_idname = 'VTKImageRange3DType'
    bl_label  = 'vtkImageRange3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_KernelSize            : bpy.props.IntVectorProperty( name='KernelSize',             default=[1, 1, 1], size=3 )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageRange3D )        
TYPENAMES.append('VTKImageRange3DType' )

#--------------------------------------------------------------
class VTKImageResize(Node, BVTK_Node):

    bl_idname = 'VTKImageResizeType'
    bl_label  = 'vtkImageResize'
    e_ResizeMethod_items=[ (x,x,x) for x in ['OutputDimensions', 'OutputSpacing', 'MagnificationFactors']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_Border                : bpy.props.BoolProperty       ( name='Border',                 default=True )
    m_Cropping              : bpy.props.BoolProperty       ( name='Cropping',               default=True )
    m_EnableSMP             : bpy.props.BoolProperty       ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP', default=True )
    m_Interpolate           : bpy.props.BoolProperty       ( name='Interpolate',            default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty        ( name='DesiredBytesPerPiece',   default=0 )
    m_NumberOfThreads       : bpy.props.IntProperty        ( name='NumberOfThreads',        default=8 )
    e_ResizeMethod          : bpy.props.EnumProperty       ( name='ResizeMethod',           default="OutputDimensions", items=e_ResizeMethod_items )
    e_SplitMode             : bpy.props.EnumProperty       ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty  ( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_OutputDimensions      : bpy.props.IntVectorProperty  ( name='OutputDimensions',       default=[-1, -1, -1], size=3 )
    m_MagnificationFactors  : bpy.props.FloatVectorProperty( name='MagnificationFactors',   default=[1.0, 1.0, 1.0], size=3 )
    m_OutputSpacing         : bpy.props.FloatVectorProperty( name='OutputSpacing',          default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Border','m_Cropping','m_EnableSMP','m_GlobalDefaultEnableSMP','m_Interpolate','m_DesiredBytesPerPiece','m_NumberOfThreads','e_ResizeMethod','e_SplitMode','m_MinimumPieceSize','m_OutputDimensions','m_MagnificationFactors','m_OutputSpacing',]
    def m_connections( self ):
        return (['input'], ['output'], ['Interpolator'], []) 
    
add_class( VTKImageResize )        
TYPENAMES.append('VTKImageResizeType' )

#--------------------------------------------------------------
class VTKImageSeedConnectivity(Node, BVTK_Node):

    bl_idname = 'VTKImageSeedConnectivityType'
    bl_label  = 'vtkImageSeedConnectivity'
    
    m_Dimensionality        : bpy.props.IntProperty( name='Dimensionality',         default=3 )
    m_InputConnectValue     : bpy.props.IntProperty( name='InputConnectValue',      default=255 )
    m_OutputConnectedValue  : bpy.props.IntProperty( name='OutputConnectedValue',   default=255 )
    m_OutputUnconnectedValue: bpy.props.IntProperty( name='OutputUnconnectedValue', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Dimensionality','m_InputConnectValue','m_OutputConnectedValue','m_OutputUnconnectedValue',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageSeedConnectivity )        
TYPENAMES.append('VTKImageSeedConnectivityType' )

#--------------------------------------------------------------
class VTKImageSeparableConvolution(Node, BVTK_Node):

    bl_idname = 'VTKImageSeparableConvolutionType'
    bl_label  = 'vtkImageSeparableConvolution'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality        : bpy.props.IntProperty      ( name='Dimensionality',         default=3 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['XKernel', 'YKernel', 'ZKernel'], []) 
    
add_class( VTKImageSeparableConvolution )        
TYPENAMES.append('VTKImageSeparableConvolutionType' )

#--------------------------------------------------------------
class VTKImageShiftScale(Node, BVTK_Node):

    bl_idname = 'VTKImageShiftScaleType'
    bl_label  = 'vtkImageShiftScale'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_ClampOverflow         : bpy.props.BoolProperty     ( name='ClampOverflow',          default=True )
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Scale                 : bpy.props.FloatProperty    ( name='Scale',                  default=1.0 )
    m_Shift                 : bpy.props.FloatProperty    ( name='Shift',                  default=0.0 )
    e_OutputScalarType      : bpy.props.EnumProperty     ( name='OutputScalarType',       default="Char", items=e_OutputScalarType_items )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClampOverflow','m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Scale','m_Shift','e_OutputScalarType','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageShiftScale )        
TYPENAMES.append('VTKImageShiftScaleType' )

#--------------------------------------------------------------
class VTKImageShrink3D(Node, BVTK_Node):

    bl_idname = 'VTKImageShrink3DType'
    bl_label  = 'vtkImageShrink3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_Averaging             : bpy.props.BoolProperty     ( name='Averaging',              default=True )
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_Maximum               : bpy.props.BoolProperty     ( name='Maximum',                default=True )
    m_Mean                  : bpy.props.BoolProperty     ( name='Mean',                   default=True )
    m_Median                : bpy.props.BoolProperty     ( name='Median',                 default=True )
    m_Minimum               : bpy.props.BoolProperty     ( name='Minimum',                default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_Shift                 : bpy.props.IntVectorProperty( name='Shift',                  default=[0, 0, 0], size=3 )
    m_ShrinkFactors         : bpy.props.IntVectorProperty( name='ShrinkFactors',          default=[1, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Averaging','m_EnableSMP','m_GlobalDefaultEnableSMP','m_Maximum','m_Mean','m_Median','m_Minimum','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize','m_Shift','m_ShrinkFactors',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageShrink3D )        
TYPENAMES.append('VTKImageShrink3DType' )

#--------------------------------------------------------------
class VTKImageSkeleton2D(Node, BVTK_Node):

    bl_idname = 'VTKImageSkeleton2DType'
    bl_label  = 'vtkImageSkeleton2D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_Prune                 : bpy.props.BoolProperty     ( name='Prune',                  default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfIterations    : bpy.props.IntProperty      ( name='NumberOfIterations',     default=1 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_Prune','m_DesiredBytesPerPiece','m_NumberOfIterations','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageSkeleton2D )        
TYPENAMES.append('VTKImageSkeleton2DType' )

#--------------------------------------------------------------
class VTKImageSlab(Node, BVTK_Node):

    bl_idname = 'VTKImageSlabType'
    bl_label  = 'vtkImageSlab'
    e_Operation_items=[ (x,x,x) for x in ['Min', 'Max', 'Mean', 'Sum']]
    e_Orientation_items=[ (x,x,x) for x in ['X', 'Y', 'Z']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_MultiSliceOutput      : bpy.props.BoolProperty     ( name='MultiSliceOutput',       default=True )
    m_TrapezoidIntegration  : bpy.props.BoolProperty     ( name='TrapezoidIntegration',   default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_Operation             : bpy.props.EnumProperty     ( name='Operation',              default="Mean", items=e_Operation_items )
    e_Orientation           : bpy.props.EnumProperty     ( name='Orientation',            default="Z", items=e_Orientation_items )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_SliceRange            : bpy.props.IntVectorProperty( name='SliceRange',             default=[-1000000000, 1000000000], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_MultiSliceOutput','m_TrapezoidIntegration','m_DesiredBytesPerPiece','m_NumberOfThreads','e_Operation','e_Orientation','e_SplitMode','m_MinimumPieceSize','m_SliceRange',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageSlab )        
TYPENAMES.append('VTKImageSlabType' )

#--------------------------------------------------------------
class VTKImageSobel2D(Node, BVTK_Node):

    bl_idname = 'VTKImageSobel2DType'
    bl_label  = 'vtkImageSobel2D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageSobel2D )        
TYPENAMES.append('VTKImageSobel2DType' )

#--------------------------------------------------------------
class VTKImageSobel3D(Node, BVTK_Node):

    bl_idname = 'VTKImageSobel3DType'
    bl_label  = 'vtkImageSobel3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageSobel3D )        
TYPENAMES.append('VTKImageSobel3DType' )

#--------------------------------------------------------------
class VTKImageSpatialAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKImageSpatialAlgorithmType'
    bl_label  = 'vtkImageSpatialAlgorithm'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageSpatialAlgorithm )        
TYPENAMES.append('VTKImageSpatialAlgorithmType' )

#--------------------------------------------------------------
class VTKImageStencilAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKImageStencilAlgorithmType'
    bl_label  = 'vtkImageStencilAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageStencilAlgorithm )        
TYPENAMES.append('VTKImageStencilAlgorithmType' )

#--------------------------------------------------------------
class VTKImageStencilSource(Node, BVTK_Node):

    bl_idname = 'VTKImageStencilSourceType'
    bl_label  = 'vtkImageStencilSource'
    
    m_OutputWholeExtent: bpy.props.IntVectorProperty  ( name='OutputWholeExtent', default=[0, -1, 0, -1, 0, -1], size=6 )
    m_OutputOrigin     : bpy.props.FloatVectorProperty( name='OutputOrigin',      default=[0.0, 0.0, 0.0], size=3 )
    m_OutputSpacing    : bpy.props.FloatVectorProperty( name='OutputSpacing',     default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_OutputWholeExtent','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageStencilSource )        
TYPENAMES.append('VTKImageStencilSourceType' )

#--------------------------------------------------------------
class VTKImageStencilToImage(Node, BVTK_Node):

    bl_idname = 'VTKImageStencilToImageType'
    bl_label  = 'vtkImageStencilToImage'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    
    m_InsideValue     : bpy.props.FloatProperty( name='InsideValue',      default=1.0 )
    m_OutsideValue    : bpy.props.FloatProperty( name='OutsideValue',     default=0.0 )
    e_OutputScalarType: bpy.props.EnumProperty ( name='OutputScalarType', default="UnsignedChar", items=e_OutputScalarType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_InsideValue','m_OutsideValue','e_OutputScalarType',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageStencilToImage )        
TYPENAMES.append('VTKImageStencilToImageType' )

#--------------------------------------------------------------
class VTKImageThreshold(Node, BVTK_Node):

    bl_idname = 'VTKImageThresholdType'
    bl_label  = 'vtkImageThreshold'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double', 'SignedChar']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_ReplaceIn             : bpy.props.BoolProperty     ( name='ReplaceIn',              default=True )
    m_ReplaceOut            : bpy.props.BoolProperty     ( name='ReplaceOut',             default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_InValue               : bpy.props.FloatProperty    ( name='InValue',                default=0.0 )
    m_OutValue              : bpy.props.FloatProperty    ( name='OutValue',               default=0.0 )
    e_OutputScalarType      : bpy.props.EnumProperty     ( name='OutputScalarType',       default="Char", items=e_OutputScalarType_items )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_ReplaceIn','m_ReplaceOut','m_DesiredBytesPerPiece','m_NumberOfThreads','m_InValue','m_OutValue','e_OutputScalarType','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageThreshold )        
TYPENAMES.append('VTKImageThresholdType' )

#--------------------------------------------------------------
class VTKImageToAMR(Node, BVTK_Node):

    bl_idname = 'VTKImageToAMRType'
    bl_label  = 'vtkImageToAMR'
    
    m_MaximumNumberOfBlocks: bpy.props.IntProperty( name='MaximumNumberOfBlocks', default=100 )
    m_NumberOfLevels       : bpy.props.IntProperty( name='NumberOfLevels',        default=2 )
    m_RefinementRatio      : bpy.props.IntProperty( name='RefinementRatio',       default=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_MaximumNumberOfBlocks','m_NumberOfLevels','m_RefinementRatio',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageToAMR )        
TYPENAMES.append('VTKImageToAMRType' )

#--------------------------------------------------------------
class VTKImageToImageStencil(Node, BVTK_Node):

    bl_idname = 'VTKImageToImageStencilType'
    bl_label  = 'vtkImageToImageStencil'
    
    m_LowerThreshold: bpy.props.FloatProperty( name='LowerThreshold', default=-1e+30 )
    m_UpperThreshold: bpy.props.FloatProperty( name='UpperThreshold', default=1e+30 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_LowerThreshold','m_UpperThreshold',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageToImageStencil )        
TYPENAMES.append('VTKImageToImageStencilType' )

#--------------------------------------------------------------
class VTKImageToPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKImageToPolyDataFilterType'
    bl_label  = 'vtkImageToPolyDataFilter'
    e_ColorMode_items=[ (x,x,x) for x in ['LUT', 'Linear256']]
    e_OutputStyle_items=[ (x,x,x) for x in ['Pixelize', 'Polygonalize', 'RunLength']]
    
    m_Decimation                 : bpy.props.BoolProperty ( name='Decimation',                  default=True )
    m_Smoothing                  : bpy.props.BoolProperty ( name='Smoothing',                   default=True )
    m_Error                      : bpy.props.IntProperty  ( name='Error',                       default=100 )
    m_NumberOfSmoothingIterations: bpy.props.IntProperty  ( name='NumberOfSmoothingIterations', default=40 )
    m_SubImageSize               : bpy.props.IntProperty  ( name='SubImageSize',                default=250 )
    m_DecimationError            : bpy.props.FloatProperty( name='DecimationError',             default=1.5 )
    e_ColorMode                  : bpy.props.EnumProperty ( name='ColorMode',                   default="Linear256", items=e_ColorMode_items )
    e_OutputStyle                : bpy.props.EnumProperty ( name='OutputStyle',                 default="Polygonalize", items=e_OutputStyle_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Decimation','m_Smoothing','m_Error','m_NumberOfSmoothingIterations','m_SubImageSize','m_DecimationError','e_ColorMode','e_OutputStyle',]
    def m_connections( self ):
        return (['input'], ['output'], ['LookupTable'], []) 
    
add_class( VTKImageToPolyDataFilter )        
TYPENAMES.append('VTKImageToPolyDataFilterType' )

#--------------------------------------------------------------
class VTKImageToStructuredGrid(Node, BVTK_Node):

    bl_idname = 'VTKImageToStructuredGridType'
    bl_label  = 'vtkImageToStructuredGrid'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageToStructuredGrid )        
TYPENAMES.append('VTKImageToStructuredGridType' )

#--------------------------------------------------------------
class VTKImageTranslateExtent(Node, BVTK_Node):

    bl_idname = 'VTKImageTranslateExtentType'
    bl_label  = 'vtkImageTranslateExtent'
    
    m_Translation: bpy.props.IntVectorProperty( name='Translation', default=[0, 0, 0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Translation',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageTranslateExtent )        
TYPENAMES.append('VTKImageTranslateExtentType' )

#--------------------------------------------------------------
class VTKImageVariance3D(Node, BVTK_Node):

    bl_idname = 'VTKImageVariance3DType'
    bl_label  = 'vtkImageVariance3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_KernelSize            : bpy.props.IntVectorProperty( name='KernelSize',             default=[1, 1, 1], size=3 )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageVariance3D )        
TYPENAMES.append('VTKImageVariance3DType' )

#--------------------------------------------------------------
class VTKImageWeightedSum(Node, BVTK_Node):

    bl_idname = 'VTKImageWeightedSumType'
    bl_label  = 'vtkImageWeightedSum'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_NormalizeByWeight     : bpy.props.BoolProperty     ( name='NormalizeByWeight',      default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_NormalizeByWeight','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['Weights'], []) 
    
add_class( VTKImageWeightedSum )        
TYPENAMES.append('VTKImageWeightedSumType' )

#--------------------------------------------------------------
class VTKImageWrapPad(Node, BVTK_Node):

    bl_idname = 'VTKImageWrapPadType'
    bl_label  = 'vtkImageWrapPad'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP                     : bpy.props.BoolProperty     ( name='EnableSMP',                      default=True )
    m_GlobalDefaultEnableSMP        : bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP',         default=True )
    m_DesiredBytesPerPiece          : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',           default=65536 )
    m_NumberOfThreads               : bpy.props.IntProperty      ( name='NumberOfThreads',                default=8 )
    m_OutputNumberOfScalarComponents: bpy.props.IntProperty      ( name='OutputNumberOfScalarComponents', default=-1 )
    e_SplitMode                     : bpy.props.EnumProperty     ( name='SplitMode',                      default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize              : bpy.props.IntVectorProperty( name='MinimumPieceSize',               default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputNumberOfScalarComponents','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageWrapPad )        
TYPENAMES.append('VTKImageWrapPadType' )

#--------------------------------------------------------------
class VTKImageYIQToRGB(Node, BVTK_Node):

    bl_idname = 'VTKImageYIQToRGBType'
    bl_label  = 'vtkImageYIQToRGB'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty     ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Maximum               : bpy.props.FloatProperty    ( name='Maximum',                default=255.0 )
    e_SplitMode             : bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImageYIQToRGB )        
TYPENAMES.append('VTKImageYIQToRGBType' )

#--------------------------------------------------------------
class VTKImplicitModeller(Node, BVTK_Node):

    bl_idname = 'VTKImplicitModellerType'
    bl_label  = 'vtkImplicitModeller'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    e_ProcessMode_items=[ (x,x,x) for x in ['PerVoxel', 'PerCell']]
    
    m_AdjustBounds          : bpy.props.BoolProperty       ( name='AdjustBounds',           default=True )
    m_Capping               : bpy.props.BoolProperty       ( name='Capping',                default=True )
    m_ScaleToMaximumDistance: bpy.props.BoolProperty       ( name='ScaleToMaximumDistance', default=True )
    m_LocatorMaxLevel       : bpy.props.IntProperty        ( name='LocatorMaxLevel',        default=5 )
    m_NumberOfThreads       : bpy.props.IntProperty        ( name='NumberOfThreads',        default=8 )
    m_AdjustDistance        : bpy.props.FloatProperty      ( name='AdjustDistance',         default=0.0125 )
    m_CapValue              : bpy.props.FloatProperty      ( name='CapValue',               default=1e+30 )
    m_MaximumDistance       : bpy.props.FloatProperty      ( name='MaximumDistance',        default=0.1 )
    e_OutputScalarType      : bpy.props.EnumProperty       ( name='OutputScalarType',       default="Float", items=e_OutputScalarType_items )
    e_ProcessMode           : bpy.props.EnumProperty       ( name='ProcessMode',            default="PerCell", items=e_ProcessMode_items )
    m_SampleDimensions      : bpy.props.IntVectorProperty  ( name='SampleDimensions',       default=[50, 50, 50], size=3 )
    m_ModelBounds           : bpy.props.FloatVectorProperty( name='ModelBounds',            default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AdjustBounds','m_Capping','m_ScaleToMaximumDistance','m_LocatorMaxLevel','m_NumberOfThreads','m_AdjustDistance','m_CapValue','m_MaximumDistance','e_OutputScalarType','e_ProcessMode','m_SampleDimensions','m_ModelBounds',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKImplicitModeller )        
TYPENAMES.append('VTKImplicitModellerType' )

#--------------------------------------------------------------
class VTKImplicitTextureCoords(Node, BVTK_Node):

    bl_idname = 'VTKImplicitTextureCoordsType'
    bl_label  = 'vtkImplicitTextureCoords'
    
    m_FlipTexture: bpy.props.BoolProperty( name='FlipTexture', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FlipTexture',]
    def m_connections( self ):
        return (['input'], ['output'], ['RFunction', 'SFunction', 'TFunction'], []) 
    
add_class( VTKImplicitTextureCoords )        
TYPENAMES.append('VTKImplicitTextureCoordsType' )

#--------------------------------------------------------------
class VTKInterpolateDataSetAttributes(Node, BVTK_Node):

    bl_idname = 'VTKInterpolateDataSetAttributesType'
    bl_label  = 'vtkInterpolateDataSetAttributes'
    
    m_T: bpy.props.FloatProperty( name='T', default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_T',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKInterpolateDataSetAttributes )        
TYPENAMES.append('VTKInterpolateDataSetAttributesType' )

#--------------------------------------------------------------
class VTKKdTreeSelector(Node, BVTK_Node):

    bl_idname = 'VTKKdTreeSelectorType'
    bl_label  = 'vtkKdTreeSelector'
    
    m_SingleSelection         : bpy.props.BoolProperty  ( name='SingleSelection',          default=False )
    m_SelectionFieldName      : bpy.props.StringProperty( name='SelectionFieldName',       default="" )
    m_SelectionAttribute      : bpy.props.IntProperty   ( name='SelectionAttribute',       default=-1 )
    m_SingleSelectionThreshold: bpy.props.FloatProperty ( name='SingleSelectionThreshold', default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_SingleSelection','m_SelectionFieldName','m_SelectionAttribute','m_SingleSelectionThreshold',]
    def m_connections( self ):
        return (['input'], ['output'], ['KdTree'], []) 
    
add_class( VTKKdTreeSelector )        
TYPENAMES.append('VTKKdTreeSelectorType' )

#--------------------------------------------------------------
class VTKLabelHierarchyAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKLabelHierarchyAlgorithmType'
    bl_label  = 'vtkLabelHierarchyAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKLabelHierarchyAlgorithm )        
TYPENAMES.append('VTKLabelHierarchyAlgorithmType' )

#--------------------------------------------------------------
class VTKLabelSizeCalculator(Node, BVTK_Node):

    bl_idname = 'VTKLabelSizeCalculatorType'
    bl_label  = 'vtkLabelSizeCalculator'
    
    m_LabelSizeArrayName: bpy.props.StringProperty( name='LabelSizeArrayName', default="LabelSize" )
    m_DPI               : bpy.props.IntProperty   ( name='DPI',                default=72 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_LabelSizeArrayName','m_DPI',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKLabelSizeCalculator )        
TYPENAMES.append('VTKLabelSizeCalculatorType' )

#--------------------------------------------------------------
class VTKLevelIdScalars(Node, BVTK_Node):

    bl_idname = 'VTKLevelIdScalarsType'
    bl_label  = 'vtkLevelIdScalars'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKLevelIdScalars )        
TYPENAMES.append('VTKLevelIdScalarsType' )

#--------------------------------------------------------------
class VTKLinearExtrusionFilter(Node, BVTK_Node):

    bl_idname = 'VTKLinearExtrusionFilterType'
    bl_label  = 'vtkLinearExtrusionFilter'
    e_ExtrusionType_items=[ (x,x,x) for x in ['VectorExtrusion', 'NormalExtrusion', 'PointExtrusion']]
    
    m_Capping       : bpy.props.BoolProperty       ( name='Capping',        default=True )
    m_ScaleFactor   : bpy.props.FloatProperty      ( name='ScaleFactor',    default=1.0 )
    e_ExtrusionType : bpy.props.EnumProperty       ( name='ExtrusionType',  default="NormalExtrusion", items=e_ExtrusionType_items )
    m_ExtrusionPoint: bpy.props.FloatVectorProperty( name='ExtrusionPoint', default=[0.0, 0.0, 0.0], size=3 )
    m_Vector        : bpy.props.FloatVectorProperty( name='Vector',         default=[0.0, 0.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Capping','m_ScaleFactor','e_ExtrusionType','m_ExtrusionPoint','m_Vector',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKLinearExtrusionFilter )        
TYPENAMES.append('VTKLinearExtrusionFilterType' )

#--------------------------------------------------------------
class VTKLinearSelector(Node, BVTK_Node):

    bl_idname = 'VTKLinearSelectorType'
    bl_label  = 'vtkLinearSelector'
    
    m_IncludeVertices           : bpy.props.BoolProperty       ( name='IncludeVertices',            default=True )
    m_Tolerance                 : bpy.props.FloatProperty      ( name='Tolerance',                  default=0.0 )
    m_VertexEliminationTolerance: bpy.props.FloatProperty      ( name='VertexEliminationTolerance', default=1e-06 )
    m_EndPoint                  : bpy.props.FloatVectorProperty( name='EndPoint',                   default=[1.0, 1.0, 1.0], size=3 )
    m_StartPoint                : bpy.props.FloatVectorProperty( name='StartPoint',                 default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_IncludeVertices','m_Tolerance','m_VertexEliminationTolerance','m_EndPoint','m_StartPoint',]
    def m_connections( self ):
        return (['input'], ['output'], ['Points'], []) 
    
add_class( VTKLinearSelector )        
TYPENAMES.append('VTKLinearSelectorType' )

#--------------------------------------------------------------
class VTKLinearSubdivisionFilter(Node, BVTK_Node):

    bl_idname = 'VTKLinearSubdivisionFilterType'
    bl_label  = 'vtkLinearSubdivisionFilter'
    
    m_CheckForTriangles   : bpy.props.BoolProperty( name='CheckForTriangles',    default=True )
    m_NumberOfSubdivisions: bpy.props.IntProperty ( name='NumberOfSubdivisions', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CheckForTriangles','m_NumberOfSubdivisions',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKLinearSubdivisionFilter )        
TYPENAMES.append('VTKLinearSubdivisionFilterType' )

#--------------------------------------------------------------
class VTKLinearToQuadraticCellsFilter(Node, BVTK_Node):

    bl_idname = 'VTKLinearToQuadraticCellsFilterType'
    bl_label  = 'vtkLinearToQuadraticCellsFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKLinearToQuadraticCellsFilter )        
TYPENAMES.append('VTKLinearToQuadraticCellsFilterType' )

#--------------------------------------------------------------
class VTKLinkEdgels(Node, BVTK_Node):

    bl_idname = 'VTKLinkEdgelsType'
    bl_label  = 'vtkLinkEdgels'
    
    m_GradientThreshold: bpy.props.FloatProperty( name='GradientThreshold', default=0.1 )
    m_LinkThreshold    : bpy.props.FloatProperty( name='LinkThreshold',     default=90.0 )
    m_PhiThreshold     : bpy.props.FloatProperty( name='PhiThreshold',      default=90.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GradientThreshold','m_LinkThreshold','m_PhiThreshold',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKLinkEdgels )        
TYPENAMES.append('VTKLinkEdgelsType' )

#--------------------------------------------------------------
class VTKLoopSubdivisionFilter(Node, BVTK_Node):

    bl_idname = 'VTKLoopSubdivisionFilterType'
    bl_label  = 'vtkLoopSubdivisionFilter'
    
    m_CheckForTriangles   : bpy.props.BoolProperty( name='CheckForTriangles',    default=True )
    m_NumberOfSubdivisions: bpy.props.IntProperty ( name='NumberOfSubdivisions', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CheckForTriangles','m_NumberOfSubdivisions',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKLoopSubdivisionFilter )        
TYPENAMES.append('VTKLoopSubdivisionFilterType' )

#--------------------------------------------------------------
class VTKMapArrayValues(Node, BVTK_Node):

    bl_idname = 'VTKMapArrayValuesType'
    bl_label  = 'vtkMapArrayValues'
    
    m_PassArray      : bpy.props.BoolProperty  ( name='PassArray',       default=True )
    m_InputArrayName : bpy.props.StringProperty( name='InputArrayName',  default="" )
    m_OutputArrayName: bpy.props.StringProperty( name='OutputArrayName', default="ArrayMap" )
    m_FieldType      : bpy.props.IntProperty   ( name='FieldType',       default=0 )
    m_OutputArrayType: bpy.props.IntProperty   ( name='OutputArrayType', default=6 )
    m_FillValue      : bpy.props.FloatProperty ( name='FillValue',       default=-1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassArray','m_InputArrayName','m_OutputArrayName','m_FieldType','m_OutputArrayType','m_FillValue',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMapArrayValues )        
TYPENAMES.append('VTKMapArrayValuesType' )

#--------------------------------------------------------------
class VTKMarchingContourFilter(Node, BVTK_Node):

    bl_idname = 'VTKMarchingContourFilterType'
    bl_label  = 'vtkMarchingContourFilter'
    
    m_ComputeGradients: bpy.props.BoolProperty( name='ComputeGradients', default=True )
    m_ComputeNormals  : bpy.props.BoolProperty( name='ComputeNormals',   default=True )
    m_ComputeScalars  : bpy.props.BoolProperty( name='ComputeScalars',   default=True )
    m_NumberOfContours: bpy.props.IntProperty ( name='NumberOfContours', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMarchingContourFilter )        
TYPENAMES.append('VTKMarchingContourFilterType' )

#--------------------------------------------------------------
class VTKMarchingCubes(Node, BVTK_Node):

    bl_idname = 'VTKMarchingCubesType'
    bl_label  = 'vtkMarchingCubes'
    
    m_ComputeGradients: bpy.props.BoolProperty( name='ComputeGradients', default=True )
    m_ComputeNormals  : bpy.props.BoolProperty( name='ComputeNormals',   default=True )
    m_ComputeScalars  : bpy.props.BoolProperty( name='ComputeScalars',   default=True )
    m_NumberOfContours: bpy.props.IntProperty ( name='NumberOfContours', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMarchingCubes )        
TYPENAMES.append('VTKMarchingCubesType' )

#--------------------------------------------------------------
class VTKMarchingSquares(Node, BVTK_Node):

    bl_idname = 'VTKMarchingSquaresType'
    bl_label  = 'vtkMarchingSquares'
    
    m_NumberOfContours: bpy.props.IntProperty( name='NumberOfContours', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMarchingSquares )        
TYPENAMES.append('VTKMarchingSquaresType' )

#--------------------------------------------------------------
class VTKMaskFields(Node, BVTK_Node):

    bl_idname = 'VTKMaskFieldsType'
    bl_label  = 'vtkMaskFields'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMaskFields )        
TYPENAMES.append('VTKMaskFieldsType' )

#--------------------------------------------------------------
class VTKMaskPoints(Node, BVTK_Node):

    bl_idname = 'VTKMaskPointsType'
    bl_label  = 'vtkMaskPoints'
    
    m_GenerateVertices                 : bpy.props.BoolProperty( name='GenerateVertices',                  default=True )
    m_ProportionalMaximumNumberOfPoints: bpy.props.BoolProperty( name='ProportionalMaximumNumberOfPoints', default=True )
    m_RandomMode                       : bpy.props.BoolProperty( name='RandomMode',                        default=True )
    m_SingleVertexPerCell              : bpy.props.BoolProperty( name='SingleVertexPerCell',               default=True )
    m_MaximumNumberOfPoints            : bpy.props.IntProperty ( name='MaximumNumberOfPoints',             default=1000000000 )
    m_Offset                           : bpy.props.IntProperty ( name='Offset',                            default=0 )
    m_OnRatio                          : bpy.props.IntProperty ( name='OnRatio',                           default=2 )
    m_RandomModeType                   : bpy.props.IntProperty ( name='RandomModeType',                    default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateVertices','m_ProportionalMaximumNumberOfPoints','m_RandomMode','m_SingleVertexPerCell','m_MaximumNumberOfPoints','m_Offset','m_OnRatio','m_RandomModeType',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMaskPoints )        
TYPENAMES.append('VTKMaskPointsType' )

#--------------------------------------------------------------
class VTKMaskPolyData(Node, BVTK_Node):

    bl_idname = 'VTKMaskPolyDataType'
    bl_label  = 'vtkMaskPolyData'
    
    m_Offset : bpy.props.IntProperty( name='Offset',  default=0 )
    m_OnRatio: bpy.props.IntProperty( name='OnRatio', default=11 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Offset','m_OnRatio',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMaskPolyData )        
TYPENAMES.append('VTKMaskPolyDataType' )

#--------------------------------------------------------------
class VTKMatricizeArray(Node, BVTK_Node):

    bl_idname = 'VTKMatricizeArrayType'
    bl_label  = 'vtkMatricizeArray'
    
    m_SliceDimension: bpy.props.IntProperty( name='SliceDimension', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_SliceDimension',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMatricizeArray )        
TYPENAMES.append('VTKMatricizeArrayType' )

#--------------------------------------------------------------
class VTKMatrixMathFilter(Node, BVTK_Node):

    bl_idname = 'VTKMatrixMathFilterType'
    bl_label  = 'vtkMatrixMathFilter'
    e_Operation_items=[ (x,x,x) for x in ['Determinant', 'Eigenvalue', 'Eigenvector', 'Inverse']]
    
    e_Operation: bpy.props.EnumProperty( name='Operation', default="Determinant", items=e_Operation_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['e_Operation',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMatrixMathFilter )        
TYPENAMES.append('VTKMatrixMathFilterType' )

#--------------------------------------------------------------
class VTKMemoryLimitImageDataStreamer(Node, BVTK_Node):

    bl_idname = 'VTKMemoryLimitImageDataStreamerType'
    bl_label  = 'vtkMemoryLimitImageDataStreamer'
    
    m_MemoryLimit            : bpy.props.IntProperty( name='MemoryLimit',             default=51200 )
    m_NumberOfStreamDivisions: bpy.props.IntProperty( name='NumberOfStreamDivisions', default=10 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_MemoryLimit','m_NumberOfStreamDivisions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ExtentTranslator'], []) 
    
add_class( VTKMemoryLimitImageDataStreamer )        
TYPENAMES.append('VTKMemoryLimitImageDataStreamerType' )

#--------------------------------------------------------------
class VTKMergeFields(Node, BVTK_Node):

    bl_idname = 'VTKMergeFieldsType'
    bl_label  = 'vtkMergeFields'
    
    m_NumberOfComponents: bpy.props.IntProperty( name='NumberOfComponents', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NumberOfComponents',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMergeFields )        
TYPENAMES.append('VTKMergeFieldsType' )

#--------------------------------------------------------------
class VTKMeshQuality(Node, BVTK_Node):

    bl_idname = 'VTKMeshQualityType'
    bl_label  = 'vtkMeshQuality'
    e_HexQualityMeasure_items=[ (x,x,x) for x in ['EdgeRatio', 'MedAspectFrobenius', 'MaxAspectFrobenius', 'Condition', 'ScaledJacobian', 'Shear', 'RelativeSizeSquared', 'Shape', 'ShapeAndSize', 'Distortion', 'MaxEdgeRatios', 'Skew', 'Taper', 'Volume', 'Stretch', 'Diagonal', 'Dimension', 'Oddy', 'ShearAndSize', 'Jacobian']]
    e_QuadQualityMeasure_items=[ (x,x,x) for x in ['EdgeRatio', 'AspectRatio', 'RadiusRatio', 'MedAspectFrobenius', 'MaxAspectFrobenius', 'MinAngle', 'MaxAngle', 'Condition', 'ScaledJacobian', 'Shear', 'RelativeSizeSquared', 'Shape', 'ShapeAndSize', 'Distortion', 'MaxEdgeRatios', 'Skew', 'Taper', 'Stretch', 'Oddy', 'ShearAndSize', 'Jacobian', 'Warpage', 'Area']]
    e_TetQualityMeasure_items=[ (x,x,x) for x in ['EdgeRatio', 'AspectRatio', 'RadiusRatio', 'AspectFrobenius', 'MinAngle', 'CollapseRatio', 'Condition', 'ScaledJacobian', 'RelativeSizeSquared', 'Shape', 'ShapeAndSize', 'Distortion', 'Volume', 'Jacobian', 'AspectGamma', 'AspectBeta']]
    e_TriangleQualityMeasure_items=[ (x,x,x) for x in ['EdgeRatio', 'AspectRatio', 'RadiusRatio', 'AspectFrobenius', 'MinAngle', 'MaxAngle', 'Condition', 'ScaledJacobian', 'RelativeSizeSquared', 'Shape', 'ShapeAndSize', 'Distortion', 'Area']]
    
    m_CompatibilityMode     : bpy.props.BoolProperty( name='CompatibilityMode',      default=True )
    m_Ratio                 : bpy.props.BoolProperty( name='Ratio',                  default=True )
    m_SaveCellQuality       : bpy.props.BoolProperty( name='SaveCellQuality',        default=True )
    m_Volume                : bpy.props.BoolProperty( name='Volume',                 default=True )
    e_HexQualityMeasure     : bpy.props.EnumProperty( name='HexQualityMeasure',      default="MaxAspectFrobenius", items=e_HexQualityMeasure_items )
    e_QuadQualityMeasure    : bpy.props.EnumProperty( name='QuadQualityMeasure',     default="EdgeRatio", items=e_QuadQualityMeasure_items )
    e_TetQualityMeasure     : bpy.props.EnumProperty( name='TetQualityMeasure',      default="AspectRatio", items=e_TetQualityMeasure_items )
    e_TriangleQualityMeasure: bpy.props.EnumProperty( name='TriangleQualityMeasure', default="AspectRatio", items=e_TriangleQualityMeasure_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CompatibilityMode','m_Ratio','m_SaveCellQuality','m_Volume','e_HexQualityMeasure','e_QuadQualityMeasure','e_TetQualityMeasure','e_TriangleQualityMeasure',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMeshQuality )        
TYPENAMES.append('VTKMeshQualityType' )

#--------------------------------------------------------------
class VTKMoleculeAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKMoleculeAlgorithmType'
    bl_label  = 'vtkMoleculeAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMoleculeAlgorithm )        
TYPENAMES.append('VTKMoleculeAlgorithmType' )

#--------------------------------------------------------------
class VTKMoleculeToAtomBallFilter(Node, BVTK_Node):

    bl_idname = 'VTKMoleculeToAtomBallFilterType'
    bl_label  = 'vtkMoleculeToAtomBallFilter'
    
    m_RadiusSource: bpy.props.IntProperty  ( name='RadiusSource', default=0 )
    m_Resolution  : bpy.props.IntProperty  ( name='Resolution',   default=50 )
    m_RadiusScale : bpy.props.FloatProperty( name='RadiusScale',  default=0.8 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_RadiusSource','m_Resolution','m_RadiusScale',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMoleculeToAtomBallFilter )        
TYPENAMES.append('VTKMoleculeToAtomBallFilterType' )

#--------------------------------------------------------------
class VTKMoleculeToBondStickFilter(Node, BVTK_Node):

    bl_idname = 'VTKMoleculeToBondStickFilterType'
    bl_label  = 'vtkMoleculeToBondStickFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMoleculeToBondStickFilter )        
TYPENAMES.append('VTKMoleculeToBondStickFilterType' )

#--------------------------------------------------------------
class VTKMultiBlockDataGroupFilter(Node, BVTK_Node):

    bl_idname = 'VTKMultiBlockDataGroupFilterType'
    bl_label  = 'vtkMultiBlockDataGroupFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMultiBlockDataGroupFilter )        
TYPENAMES.append('VTKMultiBlockDataGroupFilterType' )

#--------------------------------------------------------------
class VTKMultiBlockDataSetAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKMultiBlockDataSetAlgorithmType'
    bl_label  = 'vtkMultiBlockDataSetAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMultiBlockDataSetAlgorithm )        
TYPENAMES.append('VTKMultiBlockDataSetAlgorithmType' )

#--------------------------------------------------------------
class VTKMultiBlockFromTimeSeriesFilter(Node, BVTK_Node):

    bl_idname = 'VTKMultiBlockFromTimeSeriesFilterType'
    bl_label  = 'vtkMultiBlockFromTimeSeriesFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMultiBlockFromTimeSeriesFilter )        
TYPENAMES.append('VTKMultiBlockFromTimeSeriesFilterType' )

#--------------------------------------------------------------
class VTKMultiBlockMergeFilter(Node, BVTK_Node):

    bl_idname = 'VTKMultiBlockMergeFilterType'
    bl_label  = 'vtkMultiBlockMergeFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMultiBlockMergeFilter )        
TYPENAMES.append('VTKMultiBlockMergeFilterType' )

#--------------------------------------------------------------
class VTKMultiThreshold(Node, BVTK_Node):

    bl_idname = 'VTKMultiThresholdType'
    bl_label  = 'vtkMultiThreshold'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKMultiThreshold )        
TYPENAMES.append('VTKMultiThresholdType' )

#--------------------------------------------------------------
class VTKNonOverlappingAMRAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKNonOverlappingAMRAlgorithmType'
    bl_label  = 'vtkNonOverlappingAMRAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKNonOverlappingAMRAlgorithm )        
TYPENAMES.append('VTKNonOverlappingAMRAlgorithmType' )

#--------------------------------------------------------------
class VTKNormalizeMatrixVectors(Node, BVTK_Node):

    bl_idname = 'VTKNormalizeMatrixVectorsType'
    bl_label  = 'vtkNormalizeMatrixVectors'
    
    m_VectorDimension: bpy.props.IntProperty  ( name='VectorDimension', default=1 )
    m_PValue         : bpy.props.FloatProperty( name='PValue',          default=2.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_VectorDimension','m_PValue',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKNormalizeMatrixVectors )        
TYPENAMES.append('VTKNormalizeMatrixVectorsType' )

#--------------------------------------------------------------
class VTKOBBDicer(Node, BVTK_Node):

    bl_idname = 'VTKOBBDicerType'
    bl_label  = 'vtkOBBDicer'
    e_DiceMode_items=[ (x,x,x) for x in ['NumberOfPointsPerPiece', 'SpecifiedNumberOfPieces', 'MemoryLimitPerPiece']]
    
    m_FieldData             : bpy.props.BoolProperty( name='FieldData',              default=True )
    m_MemoryLimit           : bpy.props.IntProperty ( name='MemoryLimit',            default=51200 )
    m_NumberOfPieces        : bpy.props.IntProperty ( name='NumberOfPieces',         default=10 )
    m_NumberOfPointsPerPiece: bpy.props.IntProperty ( name='NumberOfPointsPerPiece', default=5000 )
    e_DiceMode              : bpy.props.EnumProperty( name='DiceMode',               default="NumberOfPointsPerPiece", items=e_DiceMode_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FieldData','m_MemoryLimit','m_NumberOfPieces','m_NumberOfPointsPerPiece','e_DiceMode',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKOBBDicer )        
TYPENAMES.append('VTKOBBDicerType' )

#--------------------------------------------------------------
class VTKOutlineCornerFilter(Node, BVTK_Node):

    bl_idname = 'VTKOutlineCornerFilterType'
    bl_label  = 'vtkOutlineCornerFilter'
    
    m_CornerFactor: bpy.props.FloatProperty( name='CornerFactor', default=0.2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CornerFactor',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKOutlineCornerFilter )        
TYPENAMES.append('VTKOutlineCornerFilterType' )

#--------------------------------------------------------------
class VTKOutlineFilter(Node, BVTK_Node):

    bl_idname = 'VTKOutlineFilterType'
    bl_label  = 'vtkOutlineFilter'
    
    m_GenerateFaces: bpy.props.BoolProperty( name='GenerateFaces', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateFaces',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKOutlineFilter )        
TYPENAMES.append('VTKOutlineFilterType' )

#--------------------------------------------------------------
class VTKOverlappingAMRAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKOverlappingAMRAlgorithmType'
    bl_label  = 'vtkOverlappingAMRAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKOverlappingAMRAlgorithm )        
TYPENAMES.append('VTKOverlappingAMRAlgorithmType' )

#--------------------------------------------------------------
class VTKOverlappingAMRLevelIdScalars(Node, BVTK_Node):

    bl_idname = 'VTKOverlappingAMRLevelIdScalarsType'
    bl_label  = 'vtkOverlappingAMRLevelIdScalars'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKOverlappingAMRLevelIdScalars )        
TYPENAMES.append('VTKOverlappingAMRLevelIdScalarsType' )

#--------------------------------------------------------------
class VTKPCAAnalysisFilter(Node, BVTK_Node):

    bl_idname = 'VTKPCAAnalysisFilterType'
    bl_label  = 'vtkPCAAnalysisFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPCAAnalysisFilter )        
TYPENAMES.append('VTKPCAAnalysisFilterType' )

#--------------------------------------------------------------
class VTKPCACurvatureEstimation(Node, BVTK_Node):

    bl_idname = 'VTKPCACurvatureEstimationType'
    bl_label  = 'vtkPCACurvatureEstimation'
    
    m_SampleSize: bpy.props.IntProperty( name='SampleSize', default=25 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_SampleSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPCACurvatureEstimation )        
TYPENAMES.append('VTKPCACurvatureEstimationType' )

#--------------------------------------------------------------
class VTKPCANormalEstimation(Node, BVTK_Node):

    bl_idname = 'VTKPCANormalEstimationType'
    bl_label  = 'vtkPCANormalEstimation'
    e_NormalOrientation_items=[ (x,x,x) for x in ['AsComputed', 'Point', 'GraphTraversal']]
    
    m_FlipNormals      : bpy.props.BoolProperty       ( name='FlipNormals',       default=False )
    m_SampleSize       : bpy.props.IntProperty        ( name='SampleSize',        default=25 )
    e_NormalOrientation: bpy.props.EnumProperty       ( name='NormalOrientation', default="Point", items=e_NormalOrientation_items )
    m_OrientationPoint : bpy.props.FloatVectorProperty( name='OrientationPoint',  default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FlipNormals','m_SampleSize','e_NormalOrientation','m_OrientationPoint',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPCANormalEstimation )        
TYPENAMES.append('VTKPCANormalEstimationType' )

#--------------------------------------------------------------
class VTKPCellDataToPointData(Node, BVTK_Node):

    bl_idname = 'VTKPCellDataToPointDataType'
    bl_label  = 'vtkPCellDataToPointData'
    
    m_PassCellData          : bpy.props.BoolProperty( name='PassCellData',           default=True )
    m_PieceInvariant        : bpy.props.BoolProperty( name='PieceInvariant',         default=True )
    m_ContributingCellOption: bpy.props.IntProperty ( name='ContributingCellOption', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassCellData','m_PieceInvariant','m_ContributingCellOption',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPCellDataToPointData )        
TYPENAMES.append('VTKPCellDataToPointDataType' )

#--------------------------------------------------------------
class VTKPLinearExtrusionFilter(Node, BVTK_Node):

    bl_idname = 'VTKPLinearExtrusionFilterType'
    bl_label  = 'vtkPLinearExtrusionFilter'
    e_ExtrusionType_items=[ (x,x,x) for x in ['VectorExtrusion', 'NormalExtrusion', 'PointExtrusion']]
    
    m_Capping       : bpy.props.BoolProperty       ( name='Capping',        default=True )
    m_PieceInvariant: bpy.props.BoolProperty       ( name='PieceInvariant', default=True )
    m_ScaleFactor   : bpy.props.FloatProperty      ( name='ScaleFactor',    default=1.0 )
    e_ExtrusionType : bpy.props.EnumProperty       ( name='ExtrusionType',  default="NormalExtrusion", items=e_ExtrusionType_items )
    m_ExtrusionPoint: bpy.props.FloatVectorProperty( name='ExtrusionPoint', default=[0.0, 0.0, 0.0], size=3 )
    m_Vector        : bpy.props.FloatVectorProperty( name='Vector',         default=[0.0, 0.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Capping','m_PieceInvariant','m_ScaleFactor','e_ExtrusionType','m_ExtrusionPoint','m_Vector',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPLinearExtrusionFilter )        
TYPENAMES.append('VTKPLinearExtrusionFilterType' )

#--------------------------------------------------------------
class VTKPMaskPoints(Node, BVTK_Node):

    bl_idname = 'VTKPMaskPointsType'
    bl_label  = 'vtkPMaskPoints'
    
    m_GenerateVertices                 : bpy.props.BoolProperty( name='GenerateVertices',                  default=True )
    m_ProportionalMaximumNumberOfPoints: bpy.props.BoolProperty( name='ProportionalMaximumNumberOfPoints', default=True )
    m_RandomMode                       : bpy.props.BoolProperty( name='RandomMode',                        default=True )
    m_SingleVertexPerCell              : bpy.props.BoolProperty( name='SingleVertexPerCell',               default=True )
    m_MaximumNumberOfPoints            : bpy.props.IntProperty ( name='MaximumNumberOfPoints',             default=1000000000 )
    m_Offset                           : bpy.props.IntProperty ( name='Offset',                            default=0 )
    m_OnRatio                          : bpy.props.IntProperty ( name='OnRatio',                           default=2 )
    m_RandomModeType                   : bpy.props.IntProperty ( name='RandomModeType',                    default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateVertices','m_ProportionalMaximumNumberOfPoints','m_RandomMode','m_SingleVertexPerCell','m_MaximumNumberOfPoints','m_Offset','m_OnRatio','m_RandomModeType',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPMaskPoints )        
TYPENAMES.append('VTKPMaskPointsType' )

#--------------------------------------------------------------
class VTKPOutlineCornerFilter(Node, BVTK_Node):

    bl_idname = 'VTKPOutlineCornerFilterType'
    bl_label  = 'vtkPOutlineCornerFilter'
    
    m_CornerFactor: bpy.props.FloatProperty( name='CornerFactor', default=0.2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CornerFactor',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPOutlineCornerFilter )        
TYPENAMES.append('VTKPOutlineCornerFilterType' )

#--------------------------------------------------------------
class VTKPOutlineFilter(Node, BVTK_Node):

    bl_idname = 'VTKPOutlineFilterType'
    bl_label  = 'vtkPOutlineFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPOutlineFilter )        
TYPENAMES.append('VTKPOutlineFilterType' )

#--------------------------------------------------------------
class VTKPPolyDataNormals(Node, BVTK_Node):

    bl_idname = 'VTKPPolyDataNormalsType'
    bl_label  = 'vtkPPolyDataNormals'
    
    m_AutoOrientNormals   : bpy.props.BoolProperty ( name='AutoOrientNormals',    default=True )
    m_ComputeCellNormals  : bpy.props.BoolProperty ( name='ComputeCellNormals',   default=True )
    m_ComputePointNormals : bpy.props.BoolProperty ( name='ComputePointNormals',  default=True )
    m_Consistency         : bpy.props.BoolProperty ( name='Consistency',          default=True )
    m_FlipNormals         : bpy.props.BoolProperty ( name='FlipNormals',          default=True )
    m_NonManifoldTraversal: bpy.props.BoolProperty ( name='NonManifoldTraversal', default=True )
    m_PieceInvariant      : bpy.props.BoolProperty ( name='PieceInvariant',       default=True )
    m_Splitting           : bpy.props.BoolProperty ( name='Splitting',            default=True )
    m_FeatureAngle        : bpy.props.FloatProperty( name='FeatureAngle',         default=30.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutoOrientNormals','m_ComputeCellNormals','m_ComputePointNormals','m_Consistency','m_FlipNormals','m_NonManifoldTraversal','m_PieceInvariant','m_Splitting','m_FeatureAngle',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPPolyDataNormals )        
TYPENAMES.append('VTKPPolyDataNormalsType' )

#--------------------------------------------------------------
class VTKPProjectSphereFilter(Node, BVTK_Node):

    bl_idname = 'VTKPProjectSphereFilterType'
    bl_label  = 'vtkPProjectSphereFilter'
    
    m_KeepPolePoints: bpy.props.BoolProperty       ( name='KeepPolePoints', default=False )
    m_TranslateZ    : bpy.props.BoolProperty       ( name='TranslateZ',     default=False )
    m_Center        : bpy.props.FloatVectorProperty( name='Center',         default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_KeepPolePoints','m_TranslateZ','m_Center',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPProjectSphereFilter )        
TYPENAMES.append('VTKPProjectSphereFilterType' )

#--------------------------------------------------------------
class VTKPReflectionFilter(Node, BVTK_Node):

    bl_idname = 'VTKPReflectionFilterType'
    bl_label  = 'vtkPReflectionFilter'
    e_Plane_items=[ (x,x,x) for x in ['XMin', 'YMin', 'ZMin', 'XMax', 'YMax', 'ZMax', 'X', 'Y', 'Z']]
    
    m_CopyInput         : bpy.props.BoolProperty ( name='CopyInput',          default=True )
    m_FlipAllInputArrays: bpy.props.BoolProperty ( name='FlipAllInputArrays', default=False )
    m_Center            : bpy.props.FloatProperty( name='Center',             default=0.0 )
    e_Plane             : bpy.props.EnumProperty ( name='Plane',              default="XMin", items=e_Plane_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CopyInput','m_FlipAllInputArrays','m_Center','e_Plane',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPReflectionFilter )        
TYPENAMES.append('VTKPReflectionFilterType' )

#--------------------------------------------------------------
class VTKPResampleFilter(Node, BVTK_Node):

    bl_idname = 'VTKPResampleFilterType'
    bl_label  = 'vtkPResampleFilter'
    
    m_UseInputBounds   : bpy.props.BoolProperty     ( name='UseInputBounds',    default=True )
    m_SamplingDimension: bpy.props.IntVectorProperty( name='SamplingDimension', default=[10, 10, 10], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseInputBounds','m_SamplingDimension',]
    def m_connections( self ):
        return (['input'], ['output'], ['CustomSamplingBounds'], []) 
    
add_class( VTKPResampleFilter )        
TYPENAMES.append('VTKPResampleFilterType' )

#--------------------------------------------------------------
class VTKPYoungsMaterialInterface(Node, BVTK_Node):

    bl_idname = 'VTKPYoungsMaterialInterfaceType'
    bl_label  = 'vtkPYoungsMaterialInterface'
    
    m_AxisSymetric         : bpy.props.BoolProperty       ( name='AxisSymetric',          default=True )
    m_FillMaterial         : bpy.props.BoolProperty       ( name='FillMaterial',          default=True )
    m_InverseNormal        : bpy.props.BoolProperty       ( name='InverseNormal',         default=True )
    m_OnionPeel            : bpy.props.BoolProperty       ( name='OnionPeel',             default=True )
    m_ReverseMaterialOrder : bpy.props.BoolProperty       ( name='ReverseMaterialOrder',  default=True )
    m_UseAllBlocks         : bpy.props.BoolProperty       ( name='UseAllBlocks',          default=True )
    m_UseFractionAsDistance: bpy.props.BoolProperty       ( name='UseFractionAsDistance', default=True )
    m_NumberOfMaterials    : bpy.props.IntProperty        ( name='NumberOfMaterials',     default=0 )
    m_VolumeFractionRange  : bpy.props.FloatVectorProperty( name='VolumeFractionRange',   default=[0.01, 0.99], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AxisSymetric','m_FillMaterial','m_InverseNormal','m_OnionPeel','m_ReverseMaterialOrder','m_UseAllBlocks','m_UseFractionAsDistance','m_NumberOfMaterials','m_VolumeFractionRange',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPYoungsMaterialInterface )        
TYPENAMES.append('VTKPYoungsMaterialInterfaceType' )

#--------------------------------------------------------------
class VTKPassArrays(Node, BVTK_Node):

    bl_idname = 'VTKPassArraysType'
    bl_label  = 'vtkPassArrays'
    
    m_RemoveArrays : bpy.props.BoolProperty( name='RemoveArrays',  default=False )
    m_UseFieldTypes: bpy.props.BoolProperty( name='UseFieldTypes', default=False )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_RemoveArrays','m_UseFieldTypes',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPassArrays )        
TYPENAMES.append('VTKPassArraysType' )

#--------------------------------------------------------------
class VTKPassInputTypeAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKPassInputTypeAlgorithmType'
    bl_label  = 'vtkPassInputTypeAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPassInputTypeAlgorithm )        
TYPENAMES.append('VTKPassInputTypeAlgorithmType' )

#--------------------------------------------------------------
class VTKPassThrough(Node, BVTK_Node):

    bl_idname = 'VTKPassThroughType'
    bl_label  = 'vtkPassThrough'
    
    m_AllowNullInput: bpy.props.BoolProperty( name='AllowNullInput', default=False )
    m_DeepCopyInput : bpy.props.BoolProperty( name='DeepCopyInput',  default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AllowNullInput','m_DeepCopyInput',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPassThrough )        
TYPENAMES.append('VTKPassThroughType' )

#--------------------------------------------------------------
class VTKPassThroughFilter(Node, BVTK_Node):

    bl_idname = 'VTKPassThroughFilterType'
    bl_label  = 'vtkPassThroughFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPassThroughFilter )        
TYPENAMES.append('VTKPassThroughFilterType' )

#--------------------------------------------------------------
class VTKPieceRequestFilter(Node, BVTK_Node):

    bl_idname = 'VTKPieceRequestFilterType'
    bl_label  = 'vtkPieceRequestFilter'
    
    m_NumberOfPieces: bpy.props.IntProperty( name='NumberOfPieces', default=1 )
    m_Piece         : bpy.props.IntProperty( name='Piece',          default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NumberOfPieces','m_Piece',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPieceRequestFilter )        
TYPENAMES.append('VTKPieceRequestFilterType' )

#--------------------------------------------------------------
class VTKPieceScalars(Node, BVTK_Node):

    bl_idname = 'VTKPieceScalarsType'
    bl_label  = 'vtkPieceScalars'
    
    m_RandomMode: bpy.props.BoolProperty( name='RandomMode', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_RandomMode',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPieceScalars )        
TYPENAMES.append('VTKPieceScalarsType' )

#--------------------------------------------------------------
class VTKPiecewiseFunctionAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKPiecewiseFunctionAlgorithmType'
    bl_label  = 'vtkPiecewiseFunctionAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPiecewiseFunctionAlgorithm )        
TYPENAMES.append('VTKPiecewiseFunctionAlgorithmType' )

#--------------------------------------------------------------
class VTKPiecewiseFunctionShiftScale(Node, BVTK_Node):

    bl_idname = 'VTKPiecewiseFunctionShiftScaleType'
    bl_label  = 'vtkPiecewiseFunctionShiftScale'
    
    m_PositionScale: bpy.props.FloatProperty( name='PositionScale', default=1.0 )
    m_PositionShift: bpy.props.FloatProperty( name='PositionShift', default=0.0 )
    m_ValueScale   : bpy.props.FloatProperty( name='ValueScale',    default=1.0 )
    m_ValueShift   : bpy.props.FloatProperty( name='ValueShift',    default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PositionScale','m_PositionShift','m_ValueScale','m_ValueShift',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPiecewiseFunctionShiftScale )        
TYPENAMES.append('VTKPiecewiseFunctionShiftScaleType' )

#--------------------------------------------------------------
class VTKPlaneCutter(Node, BVTK_Node):

    bl_idname = 'VTKPlaneCutterType'
    bl_label  = 'vtkPlaneCutter'
    
    m_BuildHierarchy       : bpy.props.BoolProperty( name='BuildHierarchy',        default=True )
    m_BuildTree            : bpy.props.BoolProperty( name='BuildTree',             default=True )
    m_ComputeNormals       : bpy.props.BoolProperty( name='ComputeNormals',        default=False )
    m_GeneratePolygons     : bpy.props.BoolProperty( name='GeneratePolygons',      default=True )
    m_InterpolateAttributes: bpy.props.BoolProperty( name='InterpolateAttributes', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_BuildHierarchy','m_BuildTree','m_ComputeNormals','m_GeneratePolygons','m_InterpolateAttributes',]
    def m_connections( self ):
        return (['input'], ['output'], ['Plane'], []) 
    
add_class( VTKPlaneCutter )        
TYPENAMES.append('VTKPlaneCutterType' )

#--------------------------------------------------------------
class VTKPointConnectivityFilter(Node, BVTK_Node):

    bl_idname = 'VTKPointConnectivityFilterType'
    bl_label  = 'vtkPointConnectivityFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPointConnectivityFilter )        
TYPENAMES.append('VTKPointConnectivityFilterType' )

#--------------------------------------------------------------
class VTKPointDataToCellData(Node, BVTK_Node):

    bl_idname = 'VTKPointDataToCellDataType'
    bl_label  = 'vtkPointDataToCellData'
    
    m_CategoricalData: bpy.props.BoolProperty( name='CategoricalData', default=True )
    m_PassPointData  : bpy.props.BoolProperty( name='PassPointData',   default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CategoricalData','m_PassPointData',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPointDataToCellData )        
TYPENAMES.append('VTKPointDataToCellDataType' )

#--------------------------------------------------------------
class VTKPointDensityFilter(Node, BVTK_Node):

    bl_idname = 'VTKPointDensityFilterType'
    bl_label  = 'vtkPointDensityFilter'
    e_DensityEstimate_items=[ (x,x,x) for x in ['FixedRadius', 'RelativeRadius']]
    e_DensityForm_items=[ (x,x,x) for x in ['VolumeNormalized', 'NumberOfPoints']]
    
    m_ComputeGradient : bpy.props.BoolProperty       ( name='ComputeGradient',  default=False )
    m_ScalarWeighting : bpy.props.BoolProperty       ( name='ScalarWeighting',  default=False )
    m_AdjustDistance  : bpy.props.FloatProperty      ( name='AdjustDistance',   default=0.1 )
    m_Radius          : bpy.props.FloatProperty      ( name='Radius',           default=1.0 )
    m_RelativeRadius  : bpy.props.FloatProperty      ( name='RelativeRadius',   default=1.0 )
    e_DensityEstimate : bpy.props.EnumProperty       ( name='DensityEstimate',  default="RelativeRadius", items=e_DensityEstimate_items )
    e_DensityForm     : bpy.props.EnumProperty       ( name='DensityForm',      default="NumberOfPoints", items=e_DensityForm_items )
    m_SampleDimensions: bpy.props.IntVectorProperty  ( name='SampleDimensions', default=[100, 100, 100], size=3 )
    m_ModelBounds     : bpy.props.FloatVectorProperty( name='ModelBounds',      default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradient','m_ScalarWeighting','m_AdjustDistance','m_Radius','m_RelativeRadius','e_DensityEstimate','e_DensityForm','m_SampleDimensions','m_ModelBounds',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPointDensityFilter )        
TYPENAMES.append('VTKPointDensityFilterType' )

#--------------------------------------------------------------
class VTKPointOccupancyFilter(Node, BVTK_Node):

    bl_idname = 'VTKPointOccupancyFilterType'
    bl_label  = 'vtkPointOccupancyFilter'
    
    m_EmptyValue      : bpy.props.IntProperty        ( name='EmptyValue',       default=0 )
    m_OccupiedValue   : bpy.props.IntProperty        ( name='OccupiedValue',    default=1 )
    m_SampleDimensions: bpy.props.IntVectorProperty  ( name='SampleDimensions', default=[100, 100, 100], size=3 )
    m_ModelBounds     : bpy.props.FloatVectorProperty( name='ModelBounds',      default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EmptyValue','m_OccupiedValue','m_SampleDimensions','m_ModelBounds',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPointOccupancyFilter )        
TYPENAMES.append('VTKPointOccupancyFilterType' )

#--------------------------------------------------------------
class VTKPointSetAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKPointSetAlgorithmType'
    bl_label  = 'vtkPointSetAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPointSetAlgorithm )        
TYPENAMES.append('VTKPointSetAlgorithmType' )

#--------------------------------------------------------------
class VTKPointSetToLabelHierarchy(Node, BVTK_Node):

    bl_idname = 'VTKPointSetToLabelHierarchyType'
    bl_label  = 'vtkPointSetToLabelHierarchy'
    
    m_UseUnicodeStrings   : bpy.props.BoolProperty  ( name='UseUnicodeStrings',    default=False )
    m_BoundedSizeArrayName: bpy.props.StringProperty( name='BoundedSizeArrayName', default="BoundedSize" )
    m_IconIndexArrayName  : bpy.props.StringProperty( name='IconIndexArrayName',   default="IconIndex" )
    m_LabelArrayName      : bpy.props.StringProperty( name='LabelArrayName',       default="LabelText" )
    m_OrientationArrayName: bpy.props.StringProperty( name='OrientationArrayName', default="Orientation" )
    m_PriorityArrayName   : bpy.props.StringProperty( name='PriorityArrayName',    default="Priority" )
    m_SizeArrayName       : bpy.props.StringProperty( name='SizeArrayName',        default="LabelSize" )
    m_MaximumDepth        : bpy.props.IntProperty   ( name='MaximumDepth',         default=5 )
    m_TargetLabelCount    : bpy.props.IntProperty   ( name='TargetLabelCount',     default=32 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseUnicodeStrings','m_BoundedSizeArrayName','m_IconIndexArrayName','m_LabelArrayName','m_OrientationArrayName','m_PriorityArrayName','m_SizeArrayName','m_MaximumDepth','m_TargetLabelCount',]
    def m_connections( self ):
        return (['input'], ['output'], ['TextProperty'], []) 
    
add_class( VTKPointSetToLabelHierarchy )        
TYPENAMES.append('VTKPointSetToLabelHierarchyType' )

#--------------------------------------------------------------
class VTKPolyDataAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKPolyDataAlgorithmType'
    bl_label  = 'vtkPolyDataAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPolyDataAlgorithm )        
TYPENAMES.append('VTKPolyDataAlgorithmType' )

#--------------------------------------------------------------
class VTKPolyDataConnectivityFilter(Node, BVTK_Node):

    bl_idname = 'VTKPolyDataConnectivityFilterType'
    bl_label  = 'vtkPolyDataConnectivityFilter'
    e_ExtractionMode_items=[ (x,x,x) for x in ['PointSeededRegions', 'CellSeededRegions', 'SpecifiedRegions', 'LargestRegion', 'AllRegions', 'ClosestPointRegion']]
    
    m_ColorRegions          : bpy.props.BoolProperty       ( name='ColorRegions',           default=True )
    m_FullScalarConnectivity: bpy.props.BoolProperty       ( name='FullScalarConnectivity', default=True )
    m_MarkVisitedPointIds   : bpy.props.BoolProperty       ( name='MarkVisitedPointIds',    default=True )
    m_ScalarConnectivity    : bpy.props.BoolProperty       ( name='ScalarConnectivity',     default=True )
    e_ExtractionMode        : bpy.props.EnumProperty       ( name='ExtractionMode',         default="LargestRegion", items=e_ExtractionMode_items )
    m_ClosestPoint          : bpy.props.FloatVectorProperty( name='ClosestPoint',           default=[0.0, 0.0, 0.0], size=3 )
    m_ScalarRange           : bpy.props.FloatVectorProperty( name='ScalarRange',            default=[0.0, 1.0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ColorRegions','m_FullScalarConnectivity','m_MarkVisitedPointIds','m_ScalarConnectivity','e_ExtractionMode','m_ClosestPoint','m_ScalarRange',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPolyDataConnectivityFilter )        
TYPENAMES.append('VTKPolyDataConnectivityFilterType' )

#--------------------------------------------------------------
class VTKPolyDataNormals(Node, BVTK_Node):

    bl_idname = 'VTKPolyDataNormalsType'
    bl_label  = 'vtkPolyDataNormals'
    
    m_AutoOrientNormals   : bpy.props.BoolProperty ( name='AutoOrientNormals',    default=True )
    m_ComputeCellNormals  : bpy.props.BoolProperty ( name='ComputeCellNormals',   default=True )
    m_ComputePointNormals : bpy.props.BoolProperty ( name='ComputePointNormals',  default=True )
    m_Consistency         : bpy.props.BoolProperty ( name='Consistency',          default=True )
    m_FlipNormals         : bpy.props.BoolProperty ( name='FlipNormals',          default=True )
    m_NonManifoldTraversal: bpy.props.BoolProperty ( name='NonManifoldTraversal', default=True )
    m_Splitting           : bpy.props.BoolProperty ( name='Splitting',            default=True )
    m_FeatureAngle        : bpy.props.FloatProperty( name='FeatureAngle',         default=30.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutoOrientNormals','m_ComputeCellNormals','m_ComputePointNormals','m_Consistency','m_FlipNormals','m_NonManifoldTraversal','m_Splitting','m_FeatureAngle',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPolyDataNormals )        
TYPENAMES.append('VTKPolyDataNormalsType' )

#--------------------------------------------------------------
class VTKPolyDataPointSampler(Node, BVTK_Node):

    bl_idname = 'VTKPolyDataPointSamplerType'
    bl_label  = 'vtkPolyDataPointSampler'
    
    m_GenerateEdgePoints    : bpy.props.BoolProperty ( name='GenerateEdgePoints',     default=True )
    m_GenerateInteriorPoints: bpy.props.BoolProperty ( name='GenerateInteriorPoints', default=True )
    m_GenerateVertexPoints  : bpy.props.BoolProperty ( name='GenerateVertexPoints',   default=True )
    m_GenerateVertices      : bpy.props.BoolProperty ( name='GenerateVertices',       default=True )
    m_Distance              : bpy.props.FloatProperty( name='Distance',               default=0.01 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateEdgePoints','m_GenerateInteriorPoints','m_GenerateVertexPoints','m_GenerateVertices','m_Distance',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPolyDataPointSampler )        
TYPENAMES.append('VTKPolyDataPointSamplerType' )

#--------------------------------------------------------------
class VTKPolyDataSilhouette(Node, BVTK_Node):

    bl_idname = 'VTKPolyDataSilhouetteType'
    bl_label  = 'vtkPolyDataSilhouette'
    e_Direction_items=[ (x,x,x) for x in ['SpecifiedVector', 'SpecifiedOrigin', 'CameraOrigin', 'CameraVector']]
    
    m_BorderEdges       : bpy.props.BoolProperty       ( name='BorderEdges',        default=True )
    m_PieceInvariant    : bpy.props.BoolProperty       ( name='PieceInvariant',     default=True )
    m_EnableFeatureAngle: bpy.props.IntProperty        ( name='EnableFeatureAngle', default=1 )
    m_FeatureAngle      : bpy.props.FloatProperty      ( name='FeatureAngle',       default=60.0 )
    e_Direction         : bpy.props.EnumProperty       ( name='Direction',          default="CameraOrigin", items=e_Direction_items )
    m_Origin            : bpy.props.FloatVectorProperty( name='Origin',             default=[0.0, 0.0, 0.0], size=3 )
    m_Vector            : bpy.props.FloatVectorProperty( name='Vector',             default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_BorderEdges','m_PieceInvariant','m_EnableFeatureAngle','m_FeatureAngle','e_Direction','m_Origin','m_Vector',]
    def m_connections( self ):
        return (['input'], ['output'], ['Prop3D'], []) 
    
add_class( VTKPolyDataSilhouette )        
TYPENAMES.append('VTKPolyDataSilhouetteType' )

#--------------------------------------------------------------
class VTKPolyDataStreamer(Node, BVTK_Node):

    bl_idname = 'VTKPolyDataStreamerType'
    bl_label  = 'vtkPolyDataStreamer'
    
    m_ColorByPiece           : bpy.props.BoolProperty( name='ColorByPiece',            default=True )
    m_NumberOfStreamDivisions: bpy.props.IntProperty ( name='NumberOfStreamDivisions', default=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ColorByPiece','m_NumberOfStreamDivisions',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPolyDataStreamer )        
TYPENAMES.append('VTKPolyDataStreamerType' )

#--------------------------------------------------------------
class VTKPolyDataToImageStencil(Node, BVTK_Node):

    bl_idname = 'VTKPolyDataToImageStencilType'
    bl_label  = 'vtkPolyDataToImageStencil'
    
    m_Tolerance        : bpy.props.FloatProperty      ( name='Tolerance',         default=7.62939453125e-06 )
    m_OutputWholeExtent: bpy.props.IntVectorProperty  ( name='OutputWholeExtent', default=[0, -1, 0, -1, 0, -1], size=6 )
    m_OutputOrigin     : bpy.props.FloatVectorProperty( name='OutputOrigin',      default=[0.0, 0.0, 0.0], size=3 )
    m_OutputSpacing    : bpy.props.FloatVectorProperty( name='OutputSpacing',     default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Tolerance','m_OutputWholeExtent','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPolyDataToImageStencil )        
TYPENAMES.append('VTKPolyDataToImageStencilType' )

#--------------------------------------------------------------
class VTKPolyDataToReebGraphFilter(Node, BVTK_Node):

    bl_idname = 'VTKPolyDataToReebGraphFilterType'
    bl_label  = 'vtkPolyDataToReebGraphFilter'
    
    m_FieldId: bpy.props.IntProperty( name='FieldId', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FieldId',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKPolyDataToReebGraphFilter )        
TYPENAMES.append('VTKPolyDataToReebGraphFilterType' )

#--------------------------------------------------------------
class VTKProcessIdScalars(Node, BVTK_Node):

    bl_idname = 'VTKProcessIdScalarsType'
    bl_label  = 'vtkProcessIdScalars'
    
    m_RandomMode: bpy.props.BoolProperty( name='RandomMode', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_RandomMode',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKProcessIdScalars )        
TYPENAMES.append('VTKProcessIdScalarsType' )

#--------------------------------------------------------------
class VTKProcrustesAlignmentFilter(Node, BVTK_Node):

    bl_idname = 'VTKProcrustesAlignmentFilterType'
    bl_label  = 'vtkProcrustesAlignmentFilter'
    
    m_StartFromCentroid: bpy.props.BoolProperty( name='StartFromCentroid', default=False )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_StartFromCentroid',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKProcrustesAlignmentFilter )        
TYPENAMES.append('VTKProcrustesAlignmentFilterType' )

#--------------------------------------------------------------
class VTKProgrammableAttributeDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKProgrammableAttributeDataFilterType'
    bl_label  = 'vtkProgrammableAttributeDataFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKProgrammableAttributeDataFilter )        
TYPENAMES.append('VTKProgrammableAttributeDataFilterType' )

#--------------------------------------------------------------
class VTKProgrammableFilter(Node, BVTK_Node):

    bl_idname = 'VTKProgrammableFilterType'
    bl_label  = 'vtkProgrammableFilter'
    
    m_CopyArrays: bpy.props.BoolProperty( name='CopyArrays', default=False )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CopyArrays',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKProgrammableFilter )        
TYPENAMES.append('VTKProgrammableFilterType' )

#--------------------------------------------------------------
class VTKProjectSphereFilter(Node, BVTK_Node):

    bl_idname = 'VTKProjectSphereFilterType'
    bl_label  = 'vtkProjectSphereFilter'
    
    m_KeepPolePoints: bpy.props.BoolProperty       ( name='KeepPolePoints', default=False )
    m_TranslateZ    : bpy.props.BoolProperty       ( name='TranslateZ',     default=False )
    m_Center        : bpy.props.FloatVectorProperty( name='Center',         default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_KeepPolePoints','m_TranslateZ','m_Center',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKProjectSphereFilter )        
TYPENAMES.append('VTKProjectSphereFilterType' )

#--------------------------------------------------------------
class VTKProjectedTexture(Node, BVTK_Node):

    bl_idname = 'VTKProjectedTextureType'
    bl_label  = 'vtkProjectedTexture'
    e_CameraMode_items=[ (x,x,x) for x in ['Pinhole', 'TwoMirror']]
    
    m_MirrorSeparation: bpy.props.FloatProperty      ( name='MirrorSeparation', default=1.0 )
    e_CameraMode      : bpy.props.EnumProperty       ( name='CameraMode',       default="Pinhole", items=e_CameraMode_items )
    m_AspectRatio     : bpy.props.FloatVectorProperty( name='AspectRatio',      default=[1.0, 1.0, 1.0], size=3 )
    m_Position        : bpy.props.FloatVectorProperty( name='Position',         default=[0.0, 0.0, 1.0], size=3 )
    m_SRange          : bpy.props.FloatVectorProperty( name='SRange',           default=[0.0, 1.0], size=2 )
    m_TRange          : bpy.props.FloatVectorProperty( name='TRange',           default=[0.0, 1.0], size=2 )
    m_Up              : bpy.props.FloatVectorProperty( name='Up',               default=[0.0, 1.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_MirrorSeparation','e_CameraMode','m_AspectRatio','m_Position','m_SRange','m_TRange','m_Up',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKProjectedTexture )        
TYPENAMES.append('VTKProjectedTextureType' )

#--------------------------------------------------------------
class VTKProteinRibbonFilter(Node, BVTK_Node):

    bl_idname = 'VTKProteinRibbonFilterType'
    bl_label  = 'vtkProteinRibbonFilter'
    
    m_DrawSmallMoleculesAsSpheres: bpy.props.BoolProperty ( name='DrawSmallMoleculesAsSpheres', default=True )
    m_SphereResolution           : bpy.props.IntProperty  ( name='SphereResolution',            default=20 )
    m_SubdivideFactor            : bpy.props.IntProperty  ( name='SubdivideFactor',             default=20 )
    m_CoilWidth                  : bpy.props.FloatProperty( name='CoilWidth',                   default=0.30000001192092896 )
    m_HelixWidth                 : bpy.props.FloatProperty( name='HelixWidth',                  default=1.2999999523162842 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_DrawSmallMoleculesAsSpheres','m_SphereResolution','m_SubdivideFactor','m_CoilWidth','m_HelixWidth',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKProteinRibbonFilter )        
TYPENAMES.append('VTKProteinRibbonFilterType' )

#--------------------------------------------------------------
class VTKQuadRotationalExtrusionFilter(Node, BVTK_Node):

    bl_idname = 'VTKQuadRotationalExtrusionFilterType'
    bl_label  = 'vtkQuadRotationalExtrusionFilter'
    e_Axis_items=[ (x,x,x) for x in ['X', 'Y', 'Z']]
    
    m_Capping     : bpy.props.BoolProperty ( name='Capping',      default=True )
    m_Resolution  : bpy.props.IntProperty  ( name='Resolution',   default=12 )
    m_DefaultAngle: bpy.props.FloatProperty( name='DefaultAngle', default=360.0 )
    m_DeltaRadius : bpy.props.FloatProperty( name='DeltaRadius',  default=0.0 )
    m_Translation : bpy.props.FloatProperty( name='Translation',  default=0.0 )
    e_Axis        : bpy.props.EnumProperty ( name='Axis',         default="Z", items=e_Axis_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Capping','m_Resolution','m_DefaultAngle','m_DeltaRadius','m_Translation','e_Axis',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKQuadRotationalExtrusionFilter )        
TYPENAMES.append('VTKQuadRotationalExtrusionFilterType' )

#--------------------------------------------------------------
class VTKQuadraturePointInterpolator(Node, BVTK_Node):

    bl_idname = 'VTKQuadraturePointInterpolatorType'
    bl_label  = 'vtkQuadraturePointInterpolator'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKQuadraturePointInterpolator )        
TYPENAMES.append('VTKQuadraturePointInterpolatorType' )

#--------------------------------------------------------------
class VTKQuadraturePointsGenerator(Node, BVTK_Node):

    bl_idname = 'VTKQuadraturePointsGeneratorType'
    bl_label  = 'vtkQuadraturePointsGenerator'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKQuadraturePointsGenerator )        
TYPENAMES.append('VTKQuadraturePointsGeneratorType' )

#--------------------------------------------------------------
class VTKQuadratureSchemeDictionaryGenerator(Node, BVTK_Node):

    bl_idname = 'VTKQuadratureSchemeDictionaryGeneratorType'
    bl_label  = 'vtkQuadratureSchemeDictionaryGenerator'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKQuadratureSchemeDictionaryGenerator )        
TYPENAMES.append('VTKQuadratureSchemeDictionaryGeneratorType' )

#--------------------------------------------------------------
class VTKQuadricClustering(Node, BVTK_Node):

    bl_idname = 'VTKQuadricClusteringType'
    bl_label  = 'vtkQuadricClustering'
    
    m_AutoAdjustNumberOfDivisions: bpy.props.BoolProperty       ( name='AutoAdjustNumberOfDivisions', default=True )
    m_CopyCellData               : bpy.props.BoolProperty       ( name='CopyCellData',                default=True )
    m_PreventDuplicateCells      : bpy.props.BoolProperty       ( name='PreventDuplicateCells',       default=True )
    m_UseFeatureEdges            : bpy.props.BoolProperty       ( name='UseFeatureEdges',             default=True )
    m_UseFeaturePoints           : bpy.props.BoolProperty       ( name='UseFeaturePoints',            default=True )
    m_UseInputPoints             : bpy.props.BoolProperty       ( name='UseInputPoints',              default=True )
    m_UseInternalTriangles       : bpy.props.BoolProperty       ( name='UseInternalTriangles',        default=True )
    m_NumberOfXDivisions         : bpy.props.IntProperty        ( name='NumberOfXDivisions',          default=50 )
    m_NumberOfYDivisions         : bpy.props.IntProperty        ( name='NumberOfYDivisions',          default=50 )
    m_NumberOfZDivisions         : bpy.props.IntProperty        ( name='NumberOfZDivisions',          default=50 )
    m_FeaturePointsAngle         : bpy.props.FloatProperty      ( name='FeaturePointsAngle',          default=30.0 )
    m_DivisionOrigin             : bpy.props.FloatVectorProperty( name='DivisionOrigin',              default=[0.0, 0.0, 0.0], size=3 )
    m_DivisionSpacing            : bpy.props.FloatVectorProperty( name='DivisionSpacing',             default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutoAdjustNumberOfDivisions','m_CopyCellData','m_PreventDuplicateCells','m_UseFeatureEdges','m_UseFeaturePoints','m_UseInputPoints','m_UseInternalTriangles','m_NumberOfXDivisions','m_NumberOfYDivisions','m_NumberOfZDivisions','m_FeaturePointsAngle','m_DivisionOrigin','m_DivisionSpacing',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKQuadricClustering )        
TYPENAMES.append('VTKQuadricClusteringType' )

#--------------------------------------------------------------
class VTKQuadricDecimation(Node, BVTK_Node):

    bl_idname = 'VTKQuadricDecimationType'
    bl_label  = 'vtkQuadricDecimation'
    
    m_AttributeErrorMetric: bpy.props.BoolProperty ( name='AttributeErrorMetric', default=True )
    m_NormalsAttribute    : bpy.props.BoolProperty ( name='NormalsAttribute',     default=True )
    m_ScalarsAttribute    : bpy.props.BoolProperty ( name='ScalarsAttribute',     default=True )
    m_TCoordsAttribute    : bpy.props.BoolProperty ( name='TCoordsAttribute',     default=True )
    m_TensorsAttribute    : bpy.props.BoolProperty ( name='TensorsAttribute',     default=True )
    m_VectorsAttribute    : bpy.props.BoolProperty ( name='VectorsAttribute',     default=True )
    m_VolumePreservation  : bpy.props.BoolProperty ( name='VolumePreservation',   default=True )
    m_NormalsWeight       : bpy.props.FloatProperty( name='NormalsWeight',        default=0.1 )
    m_ScalarsWeight       : bpy.props.FloatProperty( name='ScalarsWeight',        default=0.1 )
    m_TCoordsWeight       : bpy.props.FloatProperty( name='TCoordsWeight',        default=0.1 )
    m_TargetReduction     : bpy.props.FloatProperty( name='TargetReduction',      default=0.9 )
    m_TensorsWeight       : bpy.props.FloatProperty( name='TensorsWeight',        default=0.1 )
    m_VectorsWeight       : bpy.props.FloatProperty( name='VectorsWeight',        default=0.1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AttributeErrorMetric','m_NormalsAttribute','m_ScalarsAttribute','m_TCoordsAttribute','m_TensorsAttribute','m_VectorsAttribute','m_VolumePreservation','m_NormalsWeight','m_ScalarsWeight','m_TCoordsWeight','m_TargetReduction','m_TensorsWeight','m_VectorsWeight',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKQuadricDecimation )        
TYPENAMES.append('VTKQuadricDecimationType' )

#--------------------------------------------------------------
class VTKQuantizePolyDataPoints(Node, BVTK_Node):

    bl_idname = 'VTKQuantizePolyDataPointsType'
    bl_label  = 'vtkQuantizePolyDataPoints'
    
    m_ConvertLinesToPoints: bpy.props.BoolProperty ( name='ConvertLinesToPoints', default=True )
    m_ConvertPolysToLines : bpy.props.BoolProperty ( name='ConvertPolysToLines',  default=True )
    m_ConvertStripsToPolys: bpy.props.BoolProperty ( name='ConvertStripsToPolys', default=True )
    m_PieceInvariant      : bpy.props.BoolProperty ( name='PieceInvariant',       default=True )
    m_PointMerging        : bpy.props.BoolProperty ( name='PointMerging',         default=True )
    m_ToleranceIsAbsolute : bpy.props.BoolProperty ( name='ToleranceIsAbsolute',  default=True )
    m_AbsoluteTolerance   : bpy.props.FloatProperty( name='AbsoluteTolerance',    default=1.0 )
    m_QFactor             : bpy.props.FloatProperty( name='QFactor',              default=0.25 )
    m_Tolerance           : bpy.props.FloatProperty( name='Tolerance',            default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ConvertLinesToPoints','m_ConvertPolysToLines','m_ConvertStripsToPolys','m_PieceInvariant','m_PointMerging','m_ToleranceIsAbsolute','m_AbsoluteTolerance','m_QFactor','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKQuantizePolyDataPoints )        
TYPENAMES.append('VTKQuantizePolyDataPointsType' )

#--------------------------------------------------------------
class VTKRandomAttributeGenerator(Node, BVTK_Node):

    bl_idname = 'VTKRandomAttributeGeneratorType'
    bl_label  = 'vtkRandomAttributeGenerator'
    
    m_AttributesConstantPerBlock: bpy.props.BoolProperty ( name='AttributesConstantPerBlock', default=False )
    m_GenerateCellArray         : bpy.props.BoolProperty ( name='GenerateCellArray',          default=True )
    m_GenerateCellNormals       : bpy.props.BoolProperty ( name='GenerateCellNormals',        default=True )
    m_GenerateCellScalars       : bpy.props.BoolProperty ( name='GenerateCellScalars',        default=True )
    m_GenerateCellTCoords       : bpy.props.BoolProperty ( name='GenerateCellTCoords',        default=True )
    m_GenerateCellTensors       : bpy.props.BoolProperty ( name='GenerateCellTensors',        default=True )
    m_GenerateCellVectors       : bpy.props.BoolProperty ( name='GenerateCellVectors',        default=True )
    m_GenerateFieldArray        : bpy.props.BoolProperty ( name='GenerateFieldArray',         default=True )
    m_GeneratePointArray        : bpy.props.BoolProperty ( name='GeneratePointArray',         default=True )
    m_GeneratePointNormals      : bpy.props.BoolProperty ( name='GeneratePointNormals',       default=True )
    m_GeneratePointScalars      : bpy.props.BoolProperty ( name='GeneratePointScalars',       default=True )
    m_GeneratePointTCoords      : bpy.props.BoolProperty ( name='GeneratePointTCoords',       default=True )
    m_GeneratePointTensors      : bpy.props.BoolProperty ( name='GeneratePointTensors',       default=True )
    m_GeneratePointVectors      : bpy.props.BoolProperty ( name='GeneratePointVectors',       default=True )
    m_NumberOfComponents        : bpy.props.IntProperty  ( name='NumberOfComponents',         default=1 )
    m_NumberOfTuples            : bpy.props.IntProperty  ( name='NumberOfTuples',             default=0 )
    m_MaximumComponentValue     : bpy.props.FloatProperty( name='MaximumComponentValue',      default=1.0 )
    m_MinimumComponentValue     : bpy.props.FloatProperty( name='MinimumComponentValue',      default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AttributesConstantPerBlock','m_GenerateCellArray','m_GenerateCellNormals','m_GenerateCellScalars','m_GenerateCellTCoords','m_GenerateCellTensors','m_GenerateCellVectors','m_GenerateFieldArray','m_GeneratePointArray','m_GeneratePointNormals','m_GeneratePointScalars','m_GeneratePointTCoords','m_GeneratePointTensors','m_GeneratePointVectors','m_NumberOfComponents','m_NumberOfTuples','m_MaximumComponentValue','m_MinimumComponentValue',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRandomAttributeGenerator )        
TYPENAMES.append('VTKRandomAttributeGeneratorType' )

#--------------------------------------------------------------
class VTKRearrangeFields(Node, BVTK_Node):

    bl_idname = 'VTKRearrangeFieldsType'
    bl_label  = 'vtkRearrangeFields'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRearrangeFields )        
TYPENAMES.append('VTKRearrangeFieldsType' )

#--------------------------------------------------------------
class VTKRectilinearGridAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKRectilinearGridAlgorithmType'
    bl_label  = 'vtkRectilinearGridAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRectilinearGridAlgorithm )        
TYPENAMES.append('VTKRectilinearGridAlgorithmType' )

#--------------------------------------------------------------
class VTKRectilinearGridClip(Node, BVTK_Node):

    bl_idname = 'VTKRectilinearGridClipType'
    bl_label  = 'vtkRectilinearGridClip'
    
    m_ClipData: bpy.props.BoolProperty( name='ClipData', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClipData',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRectilinearGridClip )        
TYPENAMES.append('VTKRectilinearGridClipType' )

#--------------------------------------------------------------
class VTKRectilinearGridGeometryFilter(Node, BVTK_Node):

    bl_idname = 'VTKRectilinearGridGeometryFilterType'
    bl_label  = 'vtkRectilinearGridGeometryFilter'
    
    m_Extent: bpy.props.IntVectorProperty( name='Extent', default=[0, 1000000000, 0, 1000000000, 0, 1000000000], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Extent',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRectilinearGridGeometryFilter )        
TYPENAMES.append('VTKRectilinearGridGeometryFilterType' )

#--------------------------------------------------------------
class VTKRectilinearGridOutlineFilter(Node, BVTK_Node):

    bl_idname = 'VTKRectilinearGridOutlineFilterType'
    bl_label  = 'vtkRectilinearGridOutlineFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRectilinearGridOutlineFilter )        
TYPENAMES.append('VTKRectilinearGridOutlineFilterType' )

#--------------------------------------------------------------
class VTKRectilinearGridPartitioner(Node, BVTK_Node):

    bl_idname = 'VTKRectilinearGridPartitionerType'
    bl_label  = 'vtkRectilinearGridPartitioner'
    
    m_DuplicateNodes     : bpy.props.BoolProperty( name='DuplicateNodes',      default=True )
    m_NumberOfGhostLayers: bpy.props.IntProperty ( name='NumberOfGhostLayers', default=0 )
    m_NumberOfPartitions : bpy.props.IntProperty ( name='NumberOfPartitions',  default=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_DuplicateNodes','m_NumberOfGhostLayers','m_NumberOfPartitions',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRectilinearGridPartitioner )        
TYPENAMES.append('VTKRectilinearGridPartitionerType' )

#--------------------------------------------------------------
class VTKRectilinearGridToPointSet(Node, BVTK_Node):

    bl_idname = 'VTKRectilinearGridToPointSetType'
    bl_label  = 'vtkRectilinearGridToPointSet'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRectilinearGridToPointSet )        
TYPENAMES.append('VTKRectilinearGridToPointSetType' )

#--------------------------------------------------------------
class VTKRectilinearGridToTetrahedra(Node, BVTK_Node):

    bl_idname = 'VTKRectilinearGridToTetrahedraType'
    bl_label  = 'vtkRectilinearGridToTetrahedra'
    e_TetraPerCell_items=[ (x,x,x) for x in ['5And12', '5', '6', '12']]
    
    m_RememberVoxelId: bpy.props.BoolProperty( name='RememberVoxelId', default=True )
    e_TetraPerCell   : bpy.props.EnumProperty( name='TetraPerCell',    default="5", items=e_TetraPerCell_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_RememberVoxelId','e_TetraPerCell',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRectilinearGridToTetrahedra )        
TYPENAMES.append('VTKRectilinearGridToTetrahedraType' )

#--------------------------------------------------------------
class VTKRectilinearSynchronizedTemplates(Node, BVTK_Node):

    bl_idname = 'VTKRectilinearSynchronizedTemplatesType'
    bl_label  = 'vtkRectilinearSynchronizedTemplates'
    
    m_ComputeGradients : bpy.props.BoolProperty( name='ComputeGradients',  default=True )
    m_ComputeNormals   : bpy.props.BoolProperty( name='ComputeNormals',    default=True )
    m_ComputeScalars   : bpy.props.BoolProperty( name='ComputeScalars',    default=True )
    m_GenerateTriangles: bpy.props.BoolProperty( name='GenerateTriangles', default=True )
    m_ArrayComponent   : bpy.props.IntProperty ( name='ArrayComponent',    default=0 )
    m_NumberOfContours : bpy.props.IntProperty ( name='NumberOfContours',  default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_GenerateTriangles','m_ArrayComponent','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRectilinearSynchronizedTemplates )        
TYPENAMES.append('VTKRectilinearSynchronizedTemplatesType' )

#--------------------------------------------------------------
class VTKRecursiveDividingCubes(Node, BVTK_Node):

    bl_idname = 'VTKRecursiveDividingCubesType'
    bl_label  = 'vtkRecursiveDividingCubes'
    
    m_Increment: bpy.props.IntProperty  ( name='Increment', default=1 )
    m_Distance : bpy.props.FloatProperty( name='Distance',  default=0.1 )
    m_Value    : bpy.props.FloatProperty( name='Value',     default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Increment','m_Distance','m_Value',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRecursiveDividingCubes )        
TYPENAMES.append('VTKRecursiveDividingCubesType' )

#--------------------------------------------------------------
class VTKReflectionFilter(Node, BVTK_Node):

    bl_idname = 'VTKReflectionFilterType'
    bl_label  = 'vtkReflectionFilter'
    e_Plane_items=[ (x,x,x) for x in ['XMin', 'YMin', 'ZMin', 'XMax', 'YMax', 'ZMax', 'X', 'Y', 'Z']]
    
    m_CopyInput         : bpy.props.BoolProperty ( name='CopyInput',          default=True )
    m_FlipAllInputArrays: bpy.props.BoolProperty ( name='FlipAllInputArrays', default=False )
    m_Center            : bpy.props.FloatProperty( name='Center',             default=0.0 )
    e_Plane             : bpy.props.EnumProperty ( name='Plane',              default="XMin", items=e_Plane_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CopyInput','m_FlipAllInputArrays','m_Center','e_Plane',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKReflectionFilter )        
TYPENAMES.append('VTKReflectionFilterType' )

#--------------------------------------------------------------
class VTKRemoveGhosts(Node, BVTK_Node):

    bl_idname = 'VTKRemoveGhostsType'
    bl_label  = 'vtkRemoveGhosts'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRemoveGhosts )        
TYPENAMES.append('VTKRemoveGhostsType' )

#--------------------------------------------------------------
class VTKResampleToImage(Node, BVTK_Node):

    bl_idname = 'VTKResampleToImageType'
    bl_label  = 'vtkResampleToImage'
    
    m_UseInputBounds    : bpy.props.BoolProperty     ( name='UseInputBounds',     default=True )
    m_SamplingDimensions: bpy.props.IntVectorProperty( name='SamplingDimensions', default=[10, 10, 10], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseInputBounds','m_SamplingDimensions',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKResampleToImage )        
TYPENAMES.append('VTKResampleToImageType' )

#--------------------------------------------------------------
class VTKReverseSense(Node, BVTK_Node):

    bl_idname = 'VTKReverseSenseType'
    bl_label  = 'vtkReverseSense'
    
    m_ReverseCells  : bpy.props.BoolProperty( name='ReverseCells',   default=True )
    m_ReverseNormals: bpy.props.BoolProperty( name='ReverseNormals', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReverseCells','m_ReverseNormals',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKReverseSense )        
TYPENAMES.append('VTKReverseSenseType' )

#--------------------------------------------------------------
class VTKRibbonFilter(Node, BVTK_Node):

    bl_idname = 'VTKRibbonFilterType'
    bl_label  = 'vtkRibbonFilter'
    e_GenerateTCoords_items=[ (x,x,x) for x in ['Off', 'NormalizedLength', 'UseLength', 'UseScalars']]
    
    m_UseDefaultNormal: bpy.props.BoolProperty       ( name='UseDefaultNormal', default=True )
    m_VaryWidth       : bpy.props.BoolProperty       ( name='VaryWidth',        default=True )
    m_Angle           : bpy.props.FloatProperty      ( name='Angle',            default=0.0 )
    m_TextureLength   : bpy.props.FloatProperty      ( name='TextureLength',    default=1.0 )
    m_Width           : bpy.props.FloatProperty      ( name='Width',            default=0.5 )
    m_WidthFactor     : bpy.props.FloatProperty      ( name='WidthFactor',      default=2.0 )
    e_GenerateTCoords : bpy.props.EnumProperty       ( name='GenerateTCoords',  default="Off", items=e_GenerateTCoords_items )
    m_DefaultNormal   : bpy.props.FloatVectorProperty( name='DefaultNormal',    default=[0.0, 0.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseDefaultNormal','m_VaryWidth','m_Angle','m_TextureLength','m_Width','m_WidthFactor','e_GenerateTCoords','m_DefaultNormal',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRibbonFilter )        
TYPENAMES.append('VTKRibbonFilterType' )

#--------------------------------------------------------------
class VTKRotationFilter(Node, BVTK_Node):

    bl_idname = 'VTKRotationFilterType'
    bl_label  = 'vtkRotationFilter'
    e_Axis_items=[ (x,x,x) for x in ['X', 'Y', 'Z']]
    
    m_CopyInput     : bpy.props.BoolProperty       ( name='CopyInput',      default=True )
    m_NumberOfCopies: bpy.props.IntProperty        ( name='NumberOfCopies', default=0 )
    m_Angle         : bpy.props.FloatProperty      ( name='Angle',          default=0.0 )
    e_Axis          : bpy.props.EnumProperty       ( name='Axis',           default="Z", items=e_Axis_items )
    m_Center        : bpy.props.FloatVectorProperty( name='Center',         default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CopyInput','m_NumberOfCopies','m_Angle','e_Axis','m_Center',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRotationFilter )        
TYPENAMES.append('VTKRotationFilterType' )

#--------------------------------------------------------------
class VTKRotationalExtrusionFilter(Node, BVTK_Node):

    bl_idname = 'VTKRotationalExtrusionFilterType'
    bl_label  = 'vtkRotationalExtrusionFilter'
    
    m_Capping    : bpy.props.BoolProperty ( name='Capping',     default=True )
    m_Resolution : bpy.props.IntProperty  ( name='Resolution',  default=12 )
    m_Angle      : bpy.props.FloatProperty( name='Angle',       default=360.0 )
    m_DeltaRadius: bpy.props.FloatProperty( name='DeltaRadius', default=0.0 )
    m_Translation: bpy.props.FloatProperty( name='Translation', default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Capping','m_Resolution','m_Angle','m_DeltaRadius','m_Translation',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRotationalExtrusionFilter )        
TYPENAMES.append('VTKRotationalExtrusionFilterType' )

#--------------------------------------------------------------
class VTKRuledSurfaceFilter(Node, BVTK_Node):

    bl_idname = 'VTKRuledSurfaceFilterType'
    bl_label  = 'vtkRuledSurfaceFilter'
    e_RuledMode_items=[ (x,x,x) for x in ['Resample', 'PointWalk']]
    
    m_CloseSurface  : bpy.props.BoolProperty     ( name='CloseSurface',   default=True )
    m_OrientLoops   : bpy.props.BoolProperty     ( name='OrientLoops',    default=True )
    m_PassLines     : bpy.props.BoolProperty     ( name='PassLines',      default=True )
    m_Offset        : bpy.props.IntProperty      ( name='Offset',         default=0 )
    m_OnRatio       : bpy.props.IntProperty      ( name='OnRatio',        default=1 )
    m_DistanceFactor: bpy.props.FloatProperty    ( name='DistanceFactor', default=3.0 )
    e_RuledMode     : bpy.props.EnumProperty     ( name='RuledMode',      default="Resample", items=e_RuledMode_items )
    m_Resolution    : bpy.props.IntVectorProperty( name='Resolution',     default=[1, 1], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CloseSurface','m_OrientLoops','m_PassLines','m_Offset','m_OnRatio','m_DistanceFactor','e_RuledMode','m_Resolution',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKRuledSurfaceFilter )        
TYPENAMES.append('VTKRuledSurfaceFilterType' )

#--------------------------------------------------------------
class VTKSMPContourGrid(Node, BVTK_Node):

    bl_idname = 'VTKSMPContourGridType'
    bl_label  = 'vtkSMPContourGrid'
    
    m_ComputeGradients : bpy.props.BoolProperty( name='ComputeGradients',  default=True )
    m_ComputeNormals   : bpy.props.BoolProperty( name='ComputeNormals',    default=True )
    m_ComputeScalars   : bpy.props.BoolProperty( name='ComputeScalars',    default=True )
    m_GenerateTriangles: bpy.props.BoolProperty( name='GenerateTriangles', default=True )
    m_MergePieces      : bpy.props.BoolProperty( name='MergePieces',       default=True )
    m_NumberOfContours : bpy.props.IntProperty ( name='NumberOfContours',  default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_GenerateTriangles','m_MergePieces','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKSMPContourGrid )        
TYPENAMES.append('VTKSMPContourGridType' )

#--------------------------------------------------------------
class VTKSMPContourGridManyPieces(Node, BVTK_Node):

    bl_idname = 'VTKSMPContourGridManyPiecesType'
    bl_label  = 'vtkSMPContourGridManyPieces'
    
    m_ComputeGradients : bpy.props.BoolProperty( name='ComputeGradients',  default=True )
    m_ComputeNormals   : bpy.props.BoolProperty( name='ComputeNormals',    default=True )
    m_ComputeScalars   : bpy.props.BoolProperty( name='ComputeScalars',    default=True )
    m_GenerateTriangles: bpy.props.BoolProperty( name='GenerateTriangles', default=True )
    m_NumberOfContours : bpy.props.IntProperty ( name='NumberOfContours',  default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_GenerateTriangles','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKSMPContourGridManyPieces )        
TYPENAMES.append('VTKSMPContourGridManyPiecesType' )

#--------------------------------------------------------------
class VTKSMPWarpVector(Node, BVTK_Node):

    bl_idname = 'VTKSMPWarpVectorType'
    bl_label  = 'vtkSMPWarpVector'
    
    m_ScaleFactor: bpy.props.FloatProperty( name='ScaleFactor', default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ScaleFactor',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKSMPWarpVector )        
TYPENAMES.append('VTKSMPWarpVectorType' )

#--------------------------------------------------------------
class VTKSampleImplicitFunctionFilter(Node, BVTK_Node):

    bl_idname = 'VTKSampleImplicitFunctionFilterType'
    bl_label  = 'vtkSampleImplicitFunctionFilter'
    
    m_ComputeGradients : bpy.props.BoolProperty  ( name='ComputeGradients',  default=True )
    m_GradientArrayName: bpy.props.StringProperty( name='GradientArrayName', default="Implicit gradients" )
    m_ScalarArrayName  : bpy.props.StringProperty( name='ScalarArrayName',   default="Implicit scalars" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradients','m_GradientArrayName','m_ScalarArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ImplicitFunction'], []) 
    
add_class( VTKSampleImplicitFunctionFilter )        
TYPENAMES.append('VTKSampleImplicitFunctionFilterType' )

#--------------------------------------------------------------
class VTKSelectionAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKSelectionAlgorithmType'
    bl_label  = 'vtkSelectionAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKSelectionAlgorithm )        
TYPENAMES.append('VTKSelectionAlgorithmType' )

#--------------------------------------------------------------
class VTKShepardMethod(Node, BVTK_Node):

    bl_idname = 'VTKShepardMethodType'
    bl_label  = 'vtkShepardMethod'
    
    m_MaximumDistance : bpy.props.FloatProperty      ( name='MaximumDistance',  default=0.25 )
    m_NullValue       : bpy.props.FloatProperty      ( name='NullValue',        default=0.0 )
    m_PowerParameter  : bpy.props.FloatProperty      ( name='PowerParameter',   default=2.0 )
    m_SampleDimensions: bpy.props.IntVectorProperty  ( name='SampleDimensions', default=[50, 50, 50], size=3 )
    m_ModelBounds     : bpy.props.FloatVectorProperty( name='ModelBounds',      default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_MaximumDistance','m_NullValue','m_PowerParameter','m_SampleDimensions','m_ModelBounds',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKShepardMethod )        
TYPENAMES.append('VTKShepardMethodType' )

#--------------------------------------------------------------
class VTKShrinkFilter(Node, BVTK_Node):

    bl_idname = 'VTKShrinkFilterType'
    bl_label  = 'vtkShrinkFilter'
    
    m_ShrinkFactor: bpy.props.FloatProperty( name='ShrinkFactor', default=0.5 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ShrinkFactor',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKShrinkFilter )        
TYPENAMES.append('VTKShrinkFilterType' )

#--------------------------------------------------------------
class VTKShrinkPolyData(Node, BVTK_Node):

    bl_idname = 'VTKShrinkPolyDataType'
    bl_label  = 'vtkShrinkPolyData'
    
    m_ShrinkFactor: bpy.props.FloatProperty( name='ShrinkFactor', default=0.5 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ShrinkFactor',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKShrinkPolyData )        
TYPENAMES.append('VTKShrinkPolyDataType' )

#--------------------------------------------------------------
class VTKSignedDistance(Node, BVTK_Node):

    bl_idname = 'VTKSignedDistanceType'
    bl_label  = 'vtkSignedDistance'
    
    m_Radius    : bpy.props.FloatProperty      ( name='Radius',     default=0.1 )
    m_Dimensions: bpy.props.IntVectorProperty  ( name='Dimensions', default=[256, 256, 256], size=3 )
    m_Bounds    : bpy.props.FloatVectorProperty( name='Bounds',     default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Radius','m_Dimensions','m_Bounds',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKSignedDistance )        
TYPENAMES.append('VTKSignedDistanceType' )

#--------------------------------------------------------------
class VTKSimpleBondPerceiver(Node, BVTK_Node):

    bl_idname = 'VTKSimpleBondPerceiverType'
    bl_label  = 'vtkSimpleBondPerceiver'
    
    m_Tolerance: bpy.props.FloatProperty( name='Tolerance', default=0.44999998807907104 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKSimpleBondPerceiver )        
TYPENAMES.append('VTKSimpleBondPerceiverType' )

#--------------------------------------------------------------
class VTKSimpleElevationFilter(Node, BVTK_Node):

    bl_idname = 'VTKSimpleElevationFilterType'
    bl_label  = 'vtkSimpleElevationFilter'
    
    m_Vector: bpy.props.FloatVectorProperty( name='Vector', default=[0.0, 0.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Vector',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKSimpleElevationFilter )        
TYPENAMES.append('VTKSimpleElevationFilterType' )

#--------------------------------------------------------------
class VTKSimpleImageFilterExample(Node, BVTK_Node):

    bl_idname = 'VTKSimpleImageFilterExampleType'
    bl_label  = 'vtkSimpleImageFilterExample'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKSimpleImageFilterExample )        
TYPENAMES.append('VTKSimpleImageFilterExampleType' )

#--------------------------------------------------------------
class VTKSpatialRepresentationFilter(Node, BVTK_Node):

    bl_idname = 'VTKSpatialRepresentationFilterType'
    bl_label  = 'vtkSpatialRepresentationFilter'
    
    m_GenerateLeaves: bpy.props.BoolProperty( name='GenerateLeaves', default=False )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateLeaves',]
    def m_connections( self ):
        return (['input'], ['output'], ['SpatialRepresentation'], []) 
    
add_class( VTKSpatialRepresentationFilter )        
TYPENAMES.append('VTKSpatialRepresentationFilterType' )

#--------------------------------------------------------------
class VTKSphereTreeFilter(Node, BVTK_Node):

    bl_idname = 'VTKSphereTreeFilterType'
    bl_label  = 'vtkSphereTreeFilter'
    e_ExtractionMode_items=[ (x,x,x) for x in ['Levels', 'Point', 'Line', 'Plane']]
    
    m_TreeHierarchy : bpy.props.BoolProperty       ( name='TreeHierarchy',  default=True )
    m_Level         : bpy.props.IntProperty        ( name='Level',          default=-1 )
    e_ExtractionMode: bpy.props.EnumProperty       ( name='ExtractionMode', default="Levels", items=e_ExtractionMode_items )
    m_Normal        : bpy.props.FloatVectorProperty( name='Normal',         default=[0.0, 0.0, 1.0], size=3 )
    m_Point         : bpy.props.FloatVectorProperty( name='Point',          default=[0.0, 0.0, 0.0], size=3 )
    m_Ray           : bpy.props.FloatVectorProperty( name='Ray',            default=[1.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_TreeHierarchy','m_Level','e_ExtractionMode','m_Normal','m_Point','m_Ray',]
    def m_connections( self ):
        return (['input'], ['output'], ['SphereTree'], []) 
    
add_class( VTKSphereTreeFilter )        
TYPENAMES.append('VTKSphereTreeFilterType' )

#--------------------------------------------------------------
class VTKSplineFilter(Node, BVTK_Node):

    bl_idname = 'VTKSplineFilterType'
    bl_label  = 'vtkSplineFilter'
    e_GenerateTCoords_items=[ (x,x,x) for x in ['Off', 'NormalizedLength', 'UseLength', 'UseScalars']]
    e_Subdivide_items=[ (x,x,x) for x in ['Specified', 'Length']]
    
    m_MaximumNumberOfSubdivisions: bpy.props.IntProperty  ( name='MaximumNumberOfSubdivisions', default=1000000000 )
    m_NumberOfSubdivisions       : bpy.props.IntProperty  ( name='NumberOfSubdivisions',        default=100 )
    m_Length                     : bpy.props.FloatProperty( name='Length',                      default=0.1 )
    m_TextureLength              : bpy.props.FloatProperty( name='TextureLength',               default=1.0 )
    e_GenerateTCoords            : bpy.props.EnumProperty ( name='GenerateTCoords',             default="NormalizedLength", items=e_GenerateTCoords_items )
    e_Subdivide                  : bpy.props.EnumProperty ( name='Subdivide',                   default="Specified", items=e_Subdivide_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_MaximumNumberOfSubdivisions','m_NumberOfSubdivisions','m_Length','m_TextureLength','e_GenerateTCoords','e_Subdivide',]
    def m_connections( self ):
        return (['input'], ['output'], ['Spline'], []) 
    
add_class( VTKSplineFilter )        
TYPENAMES.append('VTKSplineFilterType' )

#--------------------------------------------------------------
class VTKSplitByCellScalarFilter(Node, BVTK_Node):

    bl_idname = 'VTKSplitByCellScalarFilterType'
    bl_label  = 'vtkSplitByCellScalarFilter'
    
    m_PassAllPoints: bpy.props.BoolProperty( name='PassAllPoints', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassAllPoints',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKSplitByCellScalarFilter )        
TYPENAMES.append('VTKSplitByCellScalarFilterType' )

#--------------------------------------------------------------
class VTKSplitColumnComponents(Node, BVTK_Node):

    bl_idname = 'VTKSplitColumnComponentsType'
    bl_label  = 'vtkSplitColumnComponents'
    e_NamingMode_items=[ (x,x,x) for x in ['NumberWithParens', 'NamesWithParens', 'NumberWithUnderscores', 'NamesWithUnderscores']]
    
    m_CalculateMagnitudes: bpy.props.BoolProperty( name='CalculateMagnitudes', default=True )
    e_NamingMode         : bpy.props.EnumProperty( name='NamingMode',          default="NumberWithParens", items=e_NamingMode_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CalculateMagnitudes','e_NamingMode',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKSplitColumnComponents )        
TYPENAMES.append('VTKSplitColumnComponentsType' )

#--------------------------------------------------------------
class VTKSplitField(Node, BVTK_Node):

    bl_idname = 'VTKSplitFieldType'
    bl_label  = 'vtkSplitField'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKSplitField )        
TYPENAMES.append('VTKSplitFieldType' )

#--------------------------------------------------------------
class VTKStrahlerMetric(Node, BVTK_Node):

    bl_idname = 'VTKStrahlerMetricType'
    bl_label  = 'vtkStrahlerMetric'
    
    m_Normalize: bpy.props.BoolProperty( name='Normalize', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Normalize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKStrahlerMetric )        
TYPENAMES.append('VTKStrahlerMetricType' )

#--------------------------------------------------------------
class VTKStripper(Node, BVTK_Node):

    bl_idname = 'VTKStripperType'
    bl_label  = 'vtkStripper'
    
    m_JoinContiguousSegments : bpy.props.BoolProperty( name='JoinContiguousSegments',  default=True )
    m_PassCellDataAsFieldData: bpy.props.BoolProperty( name='PassCellDataAsFieldData', default=True )
    m_PassThroughCellIds     : bpy.props.BoolProperty( name='PassThroughCellIds',      default=True )
    m_PassThroughPointIds    : bpy.props.BoolProperty( name='PassThroughPointIds',     default=True )
    m_MaximumLength          : bpy.props.IntProperty ( name='MaximumLength',           default=1000 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_JoinContiguousSegments','m_PassCellDataAsFieldData','m_PassThroughCellIds','m_PassThroughPointIds','m_MaximumLength',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKStripper )        
TYPENAMES.append('VTKStripperType' )

#--------------------------------------------------------------
class VTKStructuredGridAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKStructuredGridAlgorithmType'
    bl_label  = 'vtkStructuredGridAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKStructuredGridAlgorithm )        
TYPENAMES.append('VTKStructuredGridAlgorithmType' )

#--------------------------------------------------------------
class VTKStructuredGridAppend(Node, BVTK_Node):

    bl_idname = 'VTKStructuredGridAppendType'
    bl_label  = 'vtkStructuredGridAppend'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKStructuredGridAppend )        
TYPENAMES.append('VTKStructuredGridAppendType' )

#--------------------------------------------------------------
class VTKStructuredGridClip(Node, BVTK_Node):

    bl_idname = 'VTKStructuredGridClipType'
    bl_label  = 'vtkStructuredGridClip'
    
    m_ClipData: bpy.props.BoolProperty( name='ClipData', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClipData',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKStructuredGridClip )        
TYPENAMES.append('VTKStructuredGridClipType' )

#--------------------------------------------------------------
class VTKStructuredGridGeometryFilter(Node, BVTK_Node):

    bl_idname = 'VTKStructuredGridGeometryFilterType'
    bl_label  = 'vtkStructuredGridGeometryFilter'
    
    m_Extent: bpy.props.IntVectorProperty( name='Extent', default=[0, 1000000000, 0, 1000000000, 0, 1000000000], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Extent',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKStructuredGridGeometryFilter )        
TYPENAMES.append('VTKStructuredGridGeometryFilterType' )

#--------------------------------------------------------------
class VTKStructuredGridGhostDataGenerator(Node, BVTK_Node):

    bl_idname = 'VTKStructuredGridGhostDataGeneratorType'
    bl_label  = 'vtkStructuredGridGhostDataGenerator'
    
    m_NumberOfGhostLayers: bpy.props.IntProperty( name='NumberOfGhostLayers', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NumberOfGhostLayers',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKStructuredGridGhostDataGenerator )        
TYPENAMES.append('VTKStructuredGridGhostDataGeneratorType' )

#--------------------------------------------------------------
class VTKStructuredGridOutlineFilter(Node, BVTK_Node):

    bl_idname = 'VTKStructuredGridOutlineFilterType'
    bl_label  = 'vtkStructuredGridOutlineFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKStructuredGridOutlineFilter )        
TYPENAMES.append('VTKStructuredGridOutlineFilterType' )

#--------------------------------------------------------------
class VTKStructuredGridPartitioner(Node, BVTK_Node):

    bl_idname = 'VTKStructuredGridPartitionerType'
    bl_label  = 'vtkStructuredGridPartitioner'
    
    m_DuplicateNodes     : bpy.props.BoolProperty( name='DuplicateNodes',      default=True )
    m_NumberOfGhostLayers: bpy.props.IntProperty ( name='NumberOfGhostLayers', default=0 )
    m_NumberOfPartitions : bpy.props.IntProperty ( name='NumberOfPartitions',  default=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_DuplicateNodes','m_NumberOfGhostLayers','m_NumberOfPartitions',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKStructuredGridPartitioner )        
TYPENAMES.append('VTKStructuredGridPartitionerType' )

#--------------------------------------------------------------
class VTKSubdivideTetra(Node, BVTK_Node):

    bl_idname = 'VTKSubdivideTetraType'
    bl_label  = 'vtkSubdivideTetra'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKSubdivideTetra )        
TYPENAMES.append('VTKSubdivideTetraType' )

#--------------------------------------------------------------
class VTKSurfaceReconstructionFilter(Node, BVTK_Node):

    bl_idname = 'VTKSurfaceReconstructionFilterType'
    bl_label  = 'vtkSurfaceReconstructionFilter'
    
    m_NeighborhoodSize: bpy.props.IntProperty  ( name='NeighborhoodSize', default=20 )
    m_SampleSpacing   : bpy.props.FloatProperty( name='SampleSpacing',    default=-1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NeighborhoodSize','m_SampleSpacing',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKSurfaceReconstructionFilter )        
TYPENAMES.append('VTKSurfaceReconstructionFilterType' )

#--------------------------------------------------------------
class VTKSynchronizedTemplates2D(Node, BVTK_Node):

    bl_idname = 'VTKSynchronizedTemplates2DType'
    bl_label  = 'vtkSynchronizedTemplates2D'
    
    m_ComputeScalars  : bpy.props.BoolProperty( name='ComputeScalars',   default=True )
    m_ArrayComponent  : bpy.props.IntProperty ( name='ArrayComponent',   default=0 )
    m_NumberOfContours: bpy.props.IntProperty ( name='NumberOfContours', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeScalars','m_ArrayComponent','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKSynchronizedTemplates2D )        
TYPENAMES.append('VTKSynchronizedTemplates2DType' )

#--------------------------------------------------------------
class VTKTableAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKTableAlgorithmType'
    bl_label  = 'vtkTableAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTableAlgorithm )        
TYPENAMES.append('VTKTableAlgorithmType' )

#--------------------------------------------------------------
class VTKTableFFT(Node, BVTK_Node):

    bl_idname = 'VTKTableFFTType'
    bl_label  = 'vtkTableFFT'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTableFFT )        
TYPENAMES.append('VTKTableFFTType' )

#--------------------------------------------------------------
class VTKTableToPolyData(Node, BVTK_Node):

    bl_idname = 'VTKTableToPolyDataType'
    bl_label  = 'vtkTableToPolyData'
    
    m_Create2DPoints                       : bpy.props.BoolProperty  ( name='Create2DPoints',                        default=False )
    m_PreserveCoordinateColumnsAsDataArrays: bpy.props.BoolProperty  ( name='PreserveCoordinateColumnsAsDataArrays', default=False )
    m_XColumn                              : bpy.props.StringProperty( name='XColumn',                               default="" )
    m_YColumn                              : bpy.props.StringProperty( name='YColumn',                               default="" )
    m_ZColumn                              : bpy.props.StringProperty( name='ZColumn',                               default="" )
    m_XColumnIndex                         : bpy.props.IntProperty   ( name='XColumnIndex',                          default=-1 )
    m_XComponent                           : bpy.props.IntProperty   ( name='XComponent',                            default=0 )
    m_YColumnIndex                         : bpy.props.IntProperty   ( name='YColumnIndex',                          default=-1 )
    m_YComponent                           : bpy.props.IntProperty   ( name='YComponent',                            default=0 )
    m_ZColumnIndex                         : bpy.props.IntProperty   ( name='ZColumnIndex',                          default=-1 )
    m_ZComponent                           : bpy.props.IntProperty   ( name='ZComponent',                            default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Create2DPoints','m_PreserveCoordinateColumnsAsDataArrays','m_XColumn','m_YColumn','m_ZColumn','m_XColumnIndex','m_XComponent','m_YColumnIndex','m_YComponent','m_ZColumnIndex','m_ZComponent',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTableToPolyData )        
TYPENAMES.append('VTKTableToPolyDataType' )

#--------------------------------------------------------------
class VTKTableToStructuredGrid(Node, BVTK_Node):

    bl_idname = 'VTKTableToStructuredGridType'
    bl_label  = 'vtkTableToStructuredGrid'
    
    m_XColumn   : bpy.props.StringProperty( name='XColumn',    default="" )
    m_YColumn   : bpy.props.StringProperty( name='YColumn',    default="" )
    m_ZColumn   : bpy.props.StringProperty( name='ZColumn',    default="" )
    m_XComponent: bpy.props.IntProperty   ( name='XComponent', default=0 )
    m_YComponent: bpy.props.IntProperty   ( name='YComponent', default=0 )
    m_ZComponent: bpy.props.IntProperty   ( name='ZComponent', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_XColumn','m_YColumn','m_ZColumn','m_XComponent','m_YComponent','m_ZComponent',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTableToStructuredGrid )        
TYPENAMES.append('VTKTableToStructuredGridType' )

#--------------------------------------------------------------
class VTKTemporalArrayOperatorFilter(Node, BVTK_Node):

    bl_idname = 'VTKTemporalArrayOperatorFilterType'
    bl_label  = 'vtkTemporalArrayOperatorFilter'
    
    m_OutputArrayNameSuffix: bpy.props.StringProperty( name='OutputArrayNameSuffix', default="" )
    m_FirstTimeStepIndex   : bpy.props.IntProperty   ( name='FirstTimeStepIndex',    default=0 )
    m_Operator             : bpy.props.IntProperty   ( name='Operator',              default=0 )
    m_SecondTimeStepIndex  : bpy.props.IntProperty   ( name='SecondTimeStepIndex',   default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_OutputArrayNameSuffix','m_FirstTimeStepIndex','m_Operator','m_SecondTimeStepIndex',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTemporalArrayOperatorFilter )        
TYPENAMES.append('VTKTemporalArrayOperatorFilterType' )

#--------------------------------------------------------------
class VTKTemporalDataSetCache(Node, BVTK_Node):

    bl_idname = 'VTKTemporalDataSetCacheType'
    bl_label  = 'vtkTemporalDataSetCache'
    
    m_CacheSize: bpy.props.IntProperty( name='CacheSize', default=10 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CacheSize',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTemporalDataSetCache )        
TYPENAMES.append('VTKTemporalDataSetCacheType' )

#--------------------------------------------------------------
class VTKTemporalInterpolator(Node, BVTK_Node):

    bl_idname = 'VTKTemporalInterpolatorType'
    bl_label  = 'vtkTemporalInterpolator'
    
    m_CacheData               : bpy.props.BoolProperty ( name='CacheData',                default=True )
    m_ResampleFactor          : bpy.props.IntProperty  ( name='ResampleFactor',           default=0 )
    m_DiscreteTimeStepInterval: bpy.props.FloatProperty( name='DiscreteTimeStepInterval', default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CacheData','m_ResampleFactor','m_DiscreteTimeStepInterval',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTemporalInterpolator )        
TYPENAMES.append('VTKTemporalInterpolatorType' )

#--------------------------------------------------------------
class VTKTemporalShiftScale(Node, BVTK_Node):

    bl_idname = 'VTKTemporalShiftScaleType'
    bl_label  = 'vtkTemporalShiftScale'
    
    m_Periodic              : bpy.props.BoolProperty ( name='Periodic',               default=True )
    m_PeriodicEndCorrection : bpy.props.BoolProperty ( name='PeriodicEndCorrection',  default=True )
    m_MaximumNumberOfPeriods: bpy.props.FloatProperty( name='MaximumNumberOfPeriods', default=1.0 )
    m_PostShift             : bpy.props.FloatProperty( name='PostShift',              default=0.0 )
    m_PreShift              : bpy.props.FloatProperty( name='PreShift',               default=0.0 )
    m_Scale                 : bpy.props.FloatProperty( name='Scale',                  default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Periodic','m_PeriodicEndCorrection','m_MaximumNumberOfPeriods','m_PostShift','m_PreShift','m_Scale',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTemporalShiftScale )        
TYPENAMES.append('VTKTemporalShiftScaleType' )

#--------------------------------------------------------------
class VTKTemporalSnapToTimeStep(Node, BVTK_Node):

    bl_idname = 'VTKTemporalSnapToTimeStepType'
    bl_label  = 'vtkTemporalSnapToTimeStep'
    e_SnapMode_items=[ (x,x,x) for x in ['Nearest', 'NextBelowOrEqual', 'NextAboveOrEqual']]
    
    e_SnapMode: bpy.props.EnumProperty( name='SnapMode', default="Nearest", items=e_SnapMode_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['e_SnapMode',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTemporalSnapToTimeStep )        
TYPENAMES.append('VTKTemporalSnapToTimeStepType' )

#--------------------------------------------------------------
class VTKTemporalStatistics(Node, BVTK_Node):

    bl_idname = 'VTKTemporalStatisticsType'
    bl_label  = 'vtkTemporalStatistics'
    
    m_ComputeAverage          : bpy.props.BoolProperty( name='ComputeAverage',           default=True )
    m_ComputeMaximum          : bpy.props.BoolProperty( name='ComputeMaximum',           default=True )
    m_ComputeMinimum          : bpy.props.BoolProperty( name='ComputeMinimum',           default=True )
    m_ComputeStandardDeviation: bpy.props.BoolProperty( name='ComputeStandardDeviation', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeAverage','m_ComputeMaximum','m_ComputeMinimum','m_ComputeStandardDeviation',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTemporalStatistics )        
TYPENAMES.append('VTKTemporalStatisticsType' )

#--------------------------------------------------------------
class VTKTessellatorFilter(Node, BVTK_Node):

    bl_idname = 'VTKTessellatorFilterType'
    bl_label  = 'vtkTessellatorFilter'
    
    m_MergePoints                : bpy.props.BoolProperty ( name='MergePoints',                 default=True )
    m_MaximumNumberOfSubdivisions: bpy.props.IntProperty  ( name='MaximumNumberOfSubdivisions', default=3 )
    m_OutputDimension            : bpy.props.IntProperty  ( name='OutputDimension',             default=3 )
    m_ChordError                 : bpy.props.FloatProperty( name='ChordError',                  default=0.001 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_MergePoints','m_MaximumNumberOfSubdivisions','m_OutputDimension','m_ChordError',]
    def m_connections( self ):
        return (['input'], ['output'], ['Subdivider', 'Tessellator'], []) 
    
add_class( VTKTessellatorFilter )        
TYPENAMES.append('VTKTessellatorFilterType' )

#--------------------------------------------------------------
class VTKTextureMapToCylinder(Node, BVTK_Node):

    bl_idname = 'VTKTextureMapToCylinderType'
    bl_label  = 'vtkTextureMapToCylinder'
    
    m_AutomaticCylinderGeneration: bpy.props.BoolProperty       ( name='AutomaticCylinderGeneration', default=True )
    m_PreventSeam                : bpy.props.BoolProperty       ( name='PreventSeam',                 default=True )
    m_Point1                     : bpy.props.FloatVectorProperty( name='Point1',                      default=[0.0, 0.0, -0.5], size=3 )
    m_Point2                     : bpy.props.FloatVectorProperty( name='Point2',                      default=[0.0, 0.0, 0.5], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutomaticCylinderGeneration','m_PreventSeam','m_Point1','m_Point2',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTextureMapToCylinder )        
TYPENAMES.append('VTKTextureMapToCylinderType' )

#--------------------------------------------------------------
class VTKTextureMapToPlane(Node, BVTK_Node):

    bl_idname = 'VTKTextureMapToPlaneType'
    bl_label  = 'vtkTextureMapToPlane'
    
    m_AutomaticPlaneGeneration: bpy.props.BoolProperty       ( name='AutomaticPlaneGeneration', default=True )
    m_Normal                  : bpy.props.FloatVectorProperty( name='Normal',                   default=[0.0, 0.0, 1.0], size=3 )
    m_Origin                  : bpy.props.FloatVectorProperty( name='Origin',                   default=[0.0, 0.0, 0.0], size=3 )
    m_Point1                  : bpy.props.FloatVectorProperty( name='Point1',                   default=[0.0, 0.0, 0.0], size=3 )
    m_Point2                  : bpy.props.FloatVectorProperty( name='Point2',                   default=[0.0, 0.0, 0.0], size=3 )
    m_SRange                  : bpy.props.FloatVectorProperty( name='SRange',                   default=[0.0, 1.0], size=2 )
    m_TRange                  : bpy.props.FloatVectorProperty( name='TRange',                   default=[0.0, 1.0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutomaticPlaneGeneration','m_Normal','m_Origin','m_Point1','m_Point2','m_SRange','m_TRange',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTextureMapToPlane )        
TYPENAMES.append('VTKTextureMapToPlaneType' )

#--------------------------------------------------------------
class VTKTextureMapToSphere(Node, BVTK_Node):

    bl_idname = 'VTKTextureMapToSphereType'
    bl_label  = 'vtkTextureMapToSphere'
    
    m_AutomaticSphereGeneration: bpy.props.BoolProperty       ( name='AutomaticSphereGeneration', default=True )
    m_PreventSeam              : bpy.props.BoolProperty       ( name='PreventSeam',               default=True )
    m_Center                   : bpy.props.FloatVectorProperty( name='Center',                    default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutomaticSphereGeneration','m_PreventSeam','m_Center',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTextureMapToSphere )        
TYPENAMES.append('VTKTextureMapToSphereType' )

#--------------------------------------------------------------
class VTKThreshold(Node, BVTK_Node):

    bl_idname = 'VTKThresholdType'
    bl_label  = 'vtkThreshold'
    e_AttributeMode_items=[ (x,x,x) for x in ['Default', 'UsePointData', 'UseCellData']]
    e_ComponentMode_items=[ (x,x,x) for x in ['UseSelected', 'UseAll', 'UseAny']]
    e_PointsDataType_items=[ (x,x,x) for x in ['Float', 'Double']]
    
    m_AllScalars            : bpy.props.BoolProperty( name='AllScalars',             default=True )
    m_UseContinuousCellRange: bpy.props.BoolProperty( name='UseContinuousCellRange', default=True )
    m_SelectedComponent     : bpy.props.IntProperty ( name='SelectedComponent',      default=0 )
    e_AttributeMode         : bpy.props.EnumProperty( name='AttributeMode',          default="Default", items=e_AttributeMode_items )
    e_ComponentMode         : bpy.props.EnumProperty( name='ComponentMode',          default="UseSelected", items=e_ComponentMode_items )
    e_PointsDataType        : bpy.props.EnumProperty( name='PointsDataType',         default="Double", items=e_PointsDataType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AllScalars','m_UseContinuousCellRange','m_SelectedComponent','e_AttributeMode','e_ComponentMode','e_PointsDataType',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKThreshold )        
TYPENAMES.append('VTKThresholdType' )

#--------------------------------------------------------------
class VTKThresholdPoints(Node, BVTK_Node):

    bl_idname = 'VTKThresholdPointsType'
    bl_label  = 'vtkThresholdPoints'
    
    m_LowerThreshold: bpy.props.FloatProperty( name='LowerThreshold', default=0.0 )
    m_UpperThreshold: bpy.props.FloatProperty( name='UpperThreshold', default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_LowerThreshold','m_UpperThreshold',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKThresholdPoints )        
TYPENAMES.append('VTKThresholdPointsType' )

#--------------------------------------------------------------
class VTKThresholdTextureCoords(Node, BVTK_Node):

    bl_idname = 'VTKThresholdTextureCoordsType'
    bl_label  = 'vtkThresholdTextureCoords'
    
    m_TextureDimension: bpy.props.IntProperty        ( name='TextureDimension', default=2 )
    m_InTextureCoord  : bpy.props.FloatVectorProperty( name='InTextureCoord',   default=[0.75, 0.0, 0.0], size=3 )
    m_OutTextureCoord : bpy.props.FloatVectorProperty( name='OutTextureCoord',  default=[0.25, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_TextureDimension','m_InTextureCoord','m_OutTextureCoord',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKThresholdTextureCoords )        
TYPENAMES.append('VTKThresholdTextureCoordsType' )

#--------------------------------------------------------------
class VTKTransformCoordinateSystems(Node, BVTK_Node):

    bl_idname = 'VTKTransformCoordinateSystemsType'
    bl_label  = 'vtkTransformCoordinateSystems'
    e_InputCoordinateSystem_items=[ (x,x,x) for x in ['Display', 'Viewport', 'World']]
    e_OutputCoordinateSystem_items=[ (x,x,x) for x in ['Display', 'Viewport', 'World']]
    
    e_InputCoordinateSystem : bpy.props.EnumProperty( name='InputCoordinateSystem',  default="World", items=e_InputCoordinateSystem_items )
    e_OutputCoordinateSystem: bpy.props.EnumProperty( name='OutputCoordinateSystem', default="Display", items=e_OutputCoordinateSystem_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['e_InputCoordinateSystem','e_OutputCoordinateSystem',]
    def m_connections( self ):
        return (['input'], ['output'], ['Viewport'], []) 
    
add_class( VTKTransformCoordinateSystems )        
TYPENAMES.append('VTKTransformCoordinateSystemsType' )

#--------------------------------------------------------------
class VTKTransformFilter(Node, BVTK_Node):

    bl_idname = 'VTKTransformFilterType'
    bl_label  = 'vtkTransformFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], ['Transform'], []) 
    
add_class( VTKTransformFilter )        
TYPENAMES.append('VTKTransformFilterType' )

#--------------------------------------------------------------
class VTKTransformPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKTransformPolyDataFilterType'
    bl_label  = 'vtkTransformPolyDataFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], ['Transform'], []) 
    
add_class( VTKTransformPolyDataFilter )        
TYPENAMES.append('VTKTransformPolyDataFilterType' )

#--------------------------------------------------------------
class VTKTransformTextureCoords(Node, BVTK_Node):

    bl_idname = 'VTKTransformTextureCoordsType'
    bl_label  = 'vtkTransformTextureCoords'
    
    m_FlipR   : bpy.props.BoolProperty       ( name='FlipR',    default=True )
    m_FlipS   : bpy.props.BoolProperty       ( name='FlipS',    default=True )
    m_FlipT   : bpy.props.BoolProperty       ( name='FlipT',    default=True )
    m_Origin  : bpy.props.FloatVectorProperty( name='Origin',   default=[0.5, 0.5, 0.5], size=3 )
    m_Position: bpy.props.FloatVectorProperty( name='Position', default=[0.0, 0.0, 0.0], size=3 )
    m_Scale   : bpy.props.FloatVectorProperty( name='Scale',    default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FlipR','m_FlipS','m_FlipT','m_Origin','m_Position','m_Scale',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTransformTextureCoords )        
TYPENAMES.append('VTKTransformTextureCoordsType' )

#--------------------------------------------------------------
class VTKTransmitImageDataPiece(Node, BVTK_Node):

    bl_idname = 'VTKTransmitImageDataPieceType'
    bl_label  = 'vtkTransmitImageDataPiece'
    
    m_CreateGhostCells: bpy.props.BoolProperty( name='CreateGhostCells', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CreateGhostCells',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTransmitImageDataPiece )        
TYPENAMES.append('VTKTransmitImageDataPieceType' )

#--------------------------------------------------------------
class VTKTransmitPolyDataPiece(Node, BVTK_Node):

    bl_idname = 'VTKTransmitPolyDataPieceType'
    bl_label  = 'vtkTransmitPolyDataPiece'
    
    m_CreateGhostCells: bpy.props.BoolProperty( name='CreateGhostCells', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CreateGhostCells',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTransmitPolyDataPiece )        
TYPENAMES.append('VTKTransmitPolyDataPieceType' )

#--------------------------------------------------------------
class VTKTransmitRectilinearGridPiece(Node, BVTK_Node):

    bl_idname = 'VTKTransmitRectilinearGridPieceType'
    bl_label  = 'vtkTransmitRectilinearGridPiece'
    
    m_CreateGhostCells: bpy.props.BoolProperty( name='CreateGhostCells', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CreateGhostCells',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTransmitRectilinearGridPiece )        
TYPENAMES.append('VTKTransmitRectilinearGridPieceType' )

#--------------------------------------------------------------
class VTKTransmitStructuredDataPiece(Node, BVTK_Node):

    bl_idname = 'VTKTransmitStructuredDataPieceType'
    bl_label  = 'vtkTransmitStructuredDataPiece'
    
    m_CreateGhostCells: bpy.props.BoolProperty( name='CreateGhostCells', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CreateGhostCells',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTransmitStructuredDataPiece )        
TYPENAMES.append('VTKTransmitStructuredDataPieceType' )

#--------------------------------------------------------------
class VTKTransmitStructuredGridPiece(Node, BVTK_Node):

    bl_idname = 'VTKTransmitStructuredGridPieceType'
    bl_label  = 'vtkTransmitStructuredGridPiece'
    
    m_CreateGhostCells: bpy.props.BoolProperty( name='CreateGhostCells', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CreateGhostCells',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTransmitStructuredGridPiece )        
TYPENAMES.append('VTKTransmitStructuredGridPieceType' )

#--------------------------------------------------------------
class VTKTransmitUnstructuredGridPiece(Node, BVTK_Node):

    bl_idname = 'VTKTransmitUnstructuredGridPieceType'
    bl_label  = 'vtkTransmitUnstructuredGridPiece'
    
    m_CreateGhostCells: bpy.props.BoolProperty( name='CreateGhostCells', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CreateGhostCells',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTransmitUnstructuredGridPiece )        
TYPENAMES.append('VTKTransmitUnstructuredGridPieceType' )

#--------------------------------------------------------------
class VTKTransposeTable(Node, BVTK_Node):

    bl_idname = 'VTKTransposeTableType'
    bl_label  = 'vtkTransposeTable'
    
    m_AddIdColumn : bpy.props.BoolProperty  ( name='AddIdColumn',  default=True )
    m_UseIdColumn : bpy.props.BoolProperty  ( name='UseIdColumn',  default=False )
    m_IdColumnName: bpy.props.StringProperty( name='IdColumnName', default="ColName" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AddIdColumn','m_UseIdColumn','m_IdColumnName',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTransposeTable )        
TYPENAMES.append('VTKTransposeTableType' )

#--------------------------------------------------------------
class VTKTreeAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKTreeAlgorithmType'
    bl_label  = 'vtkTreeAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTreeAlgorithm )        
TYPENAMES.append('VTKTreeAlgorithmType' )

#--------------------------------------------------------------
class VTKTriangleFilter(Node, BVTK_Node):

    bl_idname = 'VTKTriangleFilterType'
    bl_label  = 'vtkTriangleFilter'
    
    m_PassLines: bpy.props.BoolProperty( name='PassLines', default=True )
    m_PassVerts: bpy.props.BoolProperty( name='PassVerts', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassLines','m_PassVerts',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTriangleFilter )        
TYPENAMES.append('VTKTriangleFilterType' )

#--------------------------------------------------------------
class VTKTriangleMeshPointNormals(Node, BVTK_Node):

    bl_idname = 'VTKTriangleMeshPointNormalsType'
    bl_label  = 'vtkTriangleMeshPointNormals'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTriangleMeshPointNormals )        
TYPENAMES.append('VTKTriangleMeshPointNormalsType' )

#--------------------------------------------------------------
class VTKTriangularTCoords(Node, BVTK_Node):

    bl_idname = 'VTKTriangularTCoordsType'
    bl_label  = 'vtkTriangularTCoords'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTriangularTCoords )        
TYPENAMES.append('VTKTriangularTCoordsType' )

#--------------------------------------------------------------
class VTKTubeFilter(Node, BVTK_Node):

    bl_idname = 'VTKTubeFilterType'
    bl_label  = 'vtkTubeFilter'
    e_GenerateTCoords_items=[ (x,x,x) for x in ['Off', 'NormalizedLength', 'UseLength', 'UseScalars']]
    e_VaryRadius_items=[ (x,x,x) for x in ['VaryRadiusOff', 'VaryRadiusByScalar', 'VaryRadiusByVector', 'VaryRadiusByAbsoluteScalar']]
    
    m_Capping           : bpy.props.BoolProperty       ( name='Capping',            default=True )
    m_SidesShareVertices: bpy.props.BoolProperty       ( name='SidesShareVertices', default=True )
    m_UseDefaultNormal  : bpy.props.BoolProperty       ( name='UseDefaultNormal',   default=True )
    m_NumberOfSides     : bpy.props.IntProperty        ( name='NumberOfSides',      default=3 )
    m_Offset            : bpy.props.IntProperty        ( name='Offset',             default=0 )
    m_OnRatio           : bpy.props.IntProperty        ( name='OnRatio',            default=1 )
    m_Radius            : bpy.props.FloatProperty      ( name='Radius',             default=0.5 )
    m_RadiusFactor      : bpy.props.FloatProperty      ( name='RadiusFactor',       default=10.0 )
    m_TextureLength     : bpy.props.FloatProperty      ( name='TextureLength',      default=1.0 )
    e_GenerateTCoords   : bpy.props.EnumProperty       ( name='GenerateTCoords',    default="Off", items=e_GenerateTCoords_items )
    e_VaryRadius        : bpy.props.EnumProperty       ( name='VaryRadius',         default="VaryRadiusOff", items=e_VaryRadius_items )
    m_DefaultNormal     : bpy.props.FloatVectorProperty( name='DefaultNormal',      default=[0.0, 0.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Capping','m_SidesShareVertices','m_UseDefaultNormal','m_NumberOfSides','m_Offset','m_OnRatio','m_Radius','m_RadiusFactor','m_TextureLength','e_GenerateTCoords','e_VaryRadius','m_DefaultNormal',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKTubeFilter )        
TYPENAMES.append('VTKTubeFilterType' )

#--------------------------------------------------------------
class VTKUncertaintyTubeFilter(Node, BVTK_Node):

    bl_idname = 'VTKUncertaintyTubeFilterType'
    bl_label  = 'vtkUncertaintyTubeFilter'
    
    m_NumberOfSides: bpy.props.IntProperty( name='NumberOfSides', default=12 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NumberOfSides',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKUncertaintyTubeFilter )        
TYPENAMES.append('VTKUncertaintyTubeFilterType' )

#--------------------------------------------------------------
class VTKUndirectedGraphAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKUndirectedGraphAlgorithmType'
    bl_label  = 'vtkUndirectedGraphAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKUndirectedGraphAlgorithm )        
TYPENAMES.append('VTKUndirectedGraphAlgorithmType' )

#--------------------------------------------------------------
class VTKUniformGridAMRAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKUniformGridAMRAlgorithmType'
    bl_label  = 'vtkUniformGridAMRAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKUniformGridAMRAlgorithm )        
TYPENAMES.append('VTKUniformGridAMRAlgorithmType' )

#--------------------------------------------------------------
class VTKUniformGridGhostDataGenerator(Node, BVTK_Node):

    bl_idname = 'VTKUniformGridGhostDataGeneratorType'
    bl_label  = 'vtkUniformGridGhostDataGenerator'
    
    m_NumberOfGhostLayers: bpy.props.IntProperty( name='NumberOfGhostLayers', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NumberOfGhostLayers',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKUniformGridGhostDataGenerator )        
TYPENAMES.append('VTKUniformGridGhostDataGeneratorType' )

#--------------------------------------------------------------
class VTKUniformGridPartitioner(Node, BVTK_Node):

    bl_idname = 'VTKUniformGridPartitionerType'
    bl_label  = 'vtkUniformGridPartitioner'
    
    m_DuplicateNodes     : bpy.props.BoolProperty( name='DuplicateNodes',      default=True )
    m_NumberOfGhostLayers: bpy.props.IntProperty ( name='NumberOfGhostLayers', default=0 )
    m_NumberOfPartitions : bpy.props.IntProperty ( name='NumberOfPartitions',  default=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_DuplicateNodes','m_NumberOfGhostLayers','m_NumberOfPartitions',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKUniformGridPartitioner )        
TYPENAMES.append('VTKUniformGridPartitionerType' )

#--------------------------------------------------------------
class VTKUnsignedDistance(Node, BVTK_Node):

    bl_idname = 'VTKUnsignedDistanceType'
    bl_label  = 'vtkUnsignedDistance'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Float', 'Double']]
    
    m_AdjustBounds    : bpy.props.BoolProperty       ( name='AdjustBounds',     default=True )
    m_Capping         : bpy.props.BoolProperty       ( name='Capping',          default=True )
    m_AdjustDistance  : bpy.props.FloatProperty      ( name='AdjustDistance',   default=0.0125 )
    m_CapValue        : bpy.props.FloatProperty      ( name='CapValue',         default=1e+30 )
    m_Radius          : bpy.props.FloatProperty      ( name='Radius',           default=0.1 )
    e_OutputScalarType: bpy.props.EnumProperty       ( name='OutputScalarType', default="Float", items=e_OutputScalarType_items )
    m_Dimensions      : bpy.props.IntVectorProperty  ( name='Dimensions',       default=[256, 256, 256], size=3 )
    m_Bounds          : bpy.props.FloatVectorProperty( name='Bounds',           default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AdjustBounds','m_Capping','m_AdjustDistance','m_CapValue','m_Radius','e_OutputScalarType','m_Dimensions','m_Bounds',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKUnsignedDistance )        
TYPENAMES.append('VTKUnsignedDistanceType' )

#--------------------------------------------------------------
class VTKUnstructuredGridAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKUnstructuredGridAlgorithmType'
    bl_label  = 'vtkUnstructuredGridAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKUnstructuredGridAlgorithm )        
TYPENAMES.append('VTKUnstructuredGridAlgorithmType' )

#--------------------------------------------------------------
class VTKUnstructuredGridBaseAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKUnstructuredGridBaseAlgorithmType'
    bl_label  = 'vtkUnstructuredGridBaseAlgorithm'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKUnstructuredGridBaseAlgorithm )        
TYPENAMES.append('VTKUnstructuredGridBaseAlgorithmType' )

#--------------------------------------------------------------
class VTKUnstructuredGridGeometryFilter(Node, BVTK_Node):

    bl_idname = 'VTKUnstructuredGridGeometryFilterType'
    bl_label  = 'vtkUnstructuredGridGeometryFilter'
    
    m_CellClipping              : bpy.props.BoolProperty  ( name='CellClipping',               default=True )
    m_DuplicateGhostCellClipping: bpy.props.BoolProperty  ( name='DuplicateGhostCellClipping', default=True )
    m_ExtentClipping            : bpy.props.BoolProperty  ( name='ExtentClipping',             default=True )
    m_Merging                   : bpy.props.BoolProperty  ( name='Merging',                    default=True )
    m_PassThroughCellIds        : bpy.props.BoolProperty  ( name='PassThroughCellIds',         default=True )
    m_PassThroughPointIds       : bpy.props.BoolProperty  ( name='PassThroughPointIds',        default=True )
    m_PointClipping             : bpy.props.BoolProperty  ( name='PointClipping',              default=True )
    m_OriginalCellIdsName       : bpy.props.StringProperty( name='OriginalCellIdsName',        default="vtkOriginalCellIds" )
    m_OriginalPointIdsName      : bpy.props.StringProperty( name='OriginalPointIdsName',       default="vtkOriginalPointIds" )
    m_CellMaximum               : bpy.props.IntProperty   ( name='CellMaximum',                default=1000000000 )
    m_CellMinimum               : bpy.props.IntProperty   ( name='CellMinimum',                default=0 )
    m_PointMaximum              : bpy.props.IntProperty   ( name='PointMaximum',               default=1000000000 )
    m_PointMinimum              : bpy.props.IntProperty   ( name='PointMinimum',               default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CellClipping','m_DuplicateGhostCellClipping','m_ExtentClipping','m_Merging','m_PassThroughCellIds','m_PassThroughPointIds','m_PointClipping','m_OriginalCellIdsName','m_OriginalPointIdsName','m_CellMaximum','m_CellMinimum','m_PointMaximum','m_PointMinimum',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKUnstructuredGridGeometryFilter )        
TYPENAMES.append('VTKUnstructuredGridGeometryFilterType' )

#--------------------------------------------------------------
class VTKUnstructuredGridQuadricDecimation(Node, BVTK_Node):

    bl_idname = 'VTKUnstructuredGridQuadricDecimationType'
    bl_label  = 'vtkUnstructuredGridQuadricDecimation'
    
    m_ScalarsName               : bpy.props.StringProperty( name='ScalarsName',                default="" )
    m_AutoAddCandidates         : bpy.props.IntProperty   ( name='AutoAddCandidates',          default=1 )
    m_NumberOfCandidates        : bpy.props.IntProperty   ( name='NumberOfCandidates',         default=8 )
    m_NumberOfEdgesToDecimate   : bpy.props.IntProperty   ( name='NumberOfEdgesToDecimate',    default=0 )
    m_NumberOfTetsOutput        : bpy.props.IntProperty   ( name='NumberOfTetsOutput',         default=0 )
    m_AutoAddCandidatesThreshold: bpy.props.FloatProperty ( name='AutoAddCandidatesThreshold', default=0.4 )
    m_BoundaryWeight            : bpy.props.FloatProperty ( name='BoundaryWeight',             default=100.0 )
    m_TargetReduction           : bpy.props.FloatProperty ( name='TargetReduction',            default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ScalarsName','m_AutoAddCandidates','m_NumberOfCandidates','m_NumberOfEdgesToDecimate','m_NumberOfTetsOutput','m_AutoAddCandidatesThreshold','m_BoundaryWeight','m_TargetReduction',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKUnstructuredGridQuadricDecimation )        
TYPENAMES.append('VTKUnstructuredGridQuadricDecimationType' )

#--------------------------------------------------------------
class VTKVectorDot(Node, BVTK_Node):

    bl_idname = 'VTKVectorDotType'
    bl_label  = 'vtkVectorDot'
    
    m_MapScalars : bpy.props.BoolProperty       ( name='MapScalars',  default=True )
    m_ScalarRange: bpy.props.FloatVectorProperty( name='ScalarRange', default=[-1.0, 1.0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_MapScalars','m_ScalarRange',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKVectorDot )        
TYPENAMES.append('VTKVectorDotType' )

#--------------------------------------------------------------
class VTKVectorNorm(Node, BVTK_Node):

    bl_idname = 'VTKVectorNormType'
    bl_label  = 'vtkVectorNorm'
    e_AttributeMode_items=[ (x,x,x) for x in ['Default', 'UsePointData', 'UseCellData']]
    
    m_Normalize    : bpy.props.BoolProperty( name='Normalize',     default=True )
    e_AttributeMode: bpy.props.EnumProperty( name='AttributeMode', default="Default", items=e_AttributeMode_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Normalize','e_AttributeMode',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKVectorNorm )        
TYPENAMES.append('VTKVectorNormType' )

#--------------------------------------------------------------
class VTKVertexGlyphFilter(Node, BVTK_Node):

    bl_idname = 'VTKVertexGlyphFilterType'
    bl_label  = 'vtkVertexGlyphFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKVertexGlyphFilter )        
TYPENAMES.append('VTKVertexGlyphFilterType' )

#--------------------------------------------------------------
class VTKVolumeOfRevolutionFilter(Node, BVTK_Node):

    bl_idname = 'VTKVolumeOfRevolutionFilterType'
    bl_label  = 'vtkVolumeOfRevolutionFilter'
    
    m_Resolution   : bpy.props.IntProperty        ( name='Resolution',    default=12 )
    m_SweepAngle   : bpy.props.FloatProperty      ( name='SweepAngle',    default=360.0 )
    m_AxisDirection: bpy.props.FloatVectorProperty( name='AxisDirection', default=[0.0, 0.0, 1.0], size=3 )
    m_AxisPosition : bpy.props.FloatVectorProperty( name='AxisPosition',  default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Resolution','m_SweepAngle','m_AxisDirection','m_AxisPosition',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKVolumeOfRevolutionFilter )        
TYPENAMES.append('VTKVolumeOfRevolutionFilterType' )

#--------------------------------------------------------------
class VTKVolumeRayCastSpaceLeapingImageFilter(Node, BVTK_Node):

    bl_idname = 'VTKVolumeRayCastSpaceLeapingImageFilterType'
    bl_label  = 'vtkVolumeRayCastSpaceLeapingImageFilter'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_ComputeGradientOpacity    : bpy.props.BoolProperty       ( name='ComputeGradientOpacity',     default=True )
    m_ComputeMinMax             : bpy.props.BoolProperty       ( name='ComputeMinMax',              default=True )
    m_EnableSMP                 : bpy.props.BoolProperty       ( name='EnableSMP',                  default=True )
    m_GlobalDefaultEnableSMP    : bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP',     default=True )
    m_UpdateGradientOpacityFlags: bpy.props.BoolProperty       ( name='UpdateGradientOpacityFlags', default=True )
    m_DesiredBytesPerPiece      : bpy.props.IntProperty        ( name='DesiredBytesPerPiece',       default=65536 )
    m_IndependentComponents     : bpy.props.IntProperty        ( name='IndependentComponents',      default=1 )
    m_NumberOfThreads           : bpy.props.IntProperty        ( name='NumberOfThreads',            default=8 )
    e_SplitMode                 : bpy.props.EnumProperty       ( name='SplitMode',                  default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize          : bpy.props.IntVectorProperty  ( name='MinimumPieceSize',           default=[16, 1, 1], size=3 )
    m_TableSize                 : bpy.props.IntVectorProperty  ( name='TableSize',                  default=[0, 0, 0, 0], size=4 )
    m_TableScale                : bpy.props.FloatVectorProperty( name='TableScale',                 default=[1.0, 1.0, 1.0, 1.0], size=4 )
    m_TableShift                : bpy.props.FloatVectorProperty( name='TableShift',                 default=[0.0, 0.0, 0.0, 0.0], size=4 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeGradientOpacity','m_ComputeMinMax','m_EnableSMP','m_GlobalDefaultEnableSMP','m_UpdateGradientOpacityFlags','m_DesiredBytesPerPiece','m_IndependentComponents','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize','m_TableSize','m_TableScale','m_TableShift',]
    def m_connections( self ):
        return (['input'], ['output'], ['CurrentScalars'], []) 
    
add_class( VTKVolumeRayCastSpaceLeapingImageFilter )        
TYPENAMES.append('VTKVolumeRayCastSpaceLeapingImageFilterType' )

#--------------------------------------------------------------
class VTKVoxelContoursToSurfaceFilter(Node, BVTK_Node):

    bl_idname = 'VTKVoxelContoursToSurfaceFilterType'
    bl_label  = 'vtkVoxelContoursToSurfaceFilter'
    
    m_MemoryLimitInBytes: bpy.props.IntProperty        ( name='MemoryLimitInBytes', default=10000000 )
    m_Spacing           : bpy.props.FloatVectorProperty( name='Spacing',            default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_MemoryLimitInBytes','m_Spacing',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKVoxelContoursToSurfaceFilter )        
TYPENAMES.append('VTKVoxelContoursToSurfaceFilterType' )

#--------------------------------------------------------------
class VTKVoxelGrid(Node, BVTK_Node):

    bl_idname = 'VTKVoxelGridType'
    bl_label  = 'vtkVoxelGrid'
    e_ConfigurationStyle_items=[ (x,x,x) for x in ['Manual', 'LeafSize', 'Automatic']]
    
    m_NumberOfPointsPerBin: bpy.props.IntProperty        ( name='NumberOfPointsPerBin', default=10 )
    e_ConfigurationStyle  : bpy.props.EnumProperty       ( name='ConfigurationStyle',   default="Automatic", items=e_ConfigurationStyle_items )
    m_Divisions           : bpy.props.IntVectorProperty  ( name='Divisions',            default=[50, 50, 50], size=3 )
    m_LeafSize            : bpy.props.FloatVectorProperty( name='LeafSize',             default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NumberOfPointsPerBin','e_ConfigurationStyle','m_Divisions','m_LeafSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['Kernel'], []) 
    
add_class( VTKVoxelGrid )        
TYPENAMES.append('VTKVoxelGridType' )

#--------------------------------------------------------------
class VTKVoxelModeller(Node, BVTK_Node):

    bl_idname = 'VTKVoxelModellerType'
    bl_label  = 'vtkVoxelModeller'
    e_ScalarType_items=[ (x,x,x) for x in ['Bit', 'Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    
    m_BackgroundValue : bpy.props.FloatProperty    ( name='BackgroundValue',  default=0.0 )
    m_ForegroundValue : bpy.props.FloatProperty    ( name='ForegroundValue',  default=1.0 )
    m_MaximumDistance : bpy.props.FloatProperty    ( name='MaximumDistance',  default=1.0 )
    e_ScalarType      : bpy.props.EnumProperty     ( name='ScalarType',       default="Bit", items=e_ScalarType_items )
    m_SampleDimensions: bpy.props.IntVectorProperty( name='SampleDimensions', default=[50, 50, 50], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_BackgroundValue','m_ForegroundValue','m_MaximumDistance','e_ScalarType','m_SampleDimensions',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKVoxelModeller )        
TYPENAMES.append('VTKVoxelModellerType' )

#--------------------------------------------------------------
class VTKWarpLens(Node, BVTK_Node):

    bl_idname = 'VTKWarpLensType'
    bl_label  = 'vtkWarpLens'
    
    m_ImageHeight   : bpy.props.IntProperty        ( name='ImageHeight',    default=1 )
    m_ImageWidth    : bpy.props.IntProperty        ( name='ImageWidth',     default=1 )
    m_FormatHeight  : bpy.props.FloatProperty      ( name='FormatHeight',   default=1.0 )
    m_FormatWidth   : bpy.props.FloatProperty      ( name='FormatWidth',    default=1.0 )
    m_K1            : bpy.props.FloatProperty      ( name='K1',             default=-1e-06 )
    m_K2            : bpy.props.FloatProperty      ( name='K2',             default=0.0 )
    m_Kappa         : bpy.props.FloatProperty      ( name='Kappa',          default=-1e-06 )
    m_P1            : bpy.props.FloatProperty      ( name='P1',             default=0.0 )
    m_P2            : bpy.props.FloatProperty      ( name='P2',             default=0.0 )
    m_Center        : bpy.props.FloatVectorProperty( name='Center',         default=[0.0, 0.0], size=2 )
    m_PrincipalPoint: bpy.props.FloatVectorProperty( name='PrincipalPoint', default=[0.0, 0.0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ImageHeight','m_ImageWidth','m_FormatHeight','m_FormatWidth','m_K1','m_K2','m_Kappa','m_P1','m_P2','m_Center','m_PrincipalPoint',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKWarpLens )        
TYPENAMES.append('VTKWarpLensType' )

#--------------------------------------------------------------
class VTKWarpScalar(Node, BVTK_Node):

    bl_idname = 'VTKWarpScalarType'
    bl_label  = 'vtkWarpScalar'
    
    m_UseNormal  : bpy.props.BoolProperty       ( name='UseNormal',   default=True )
    m_XYPlane    : bpy.props.BoolProperty       ( name='XYPlane',     default=True )
    m_ScaleFactor: bpy.props.FloatProperty      ( name='ScaleFactor', default=1.0 )
    m_Normal     : bpy.props.FloatVectorProperty( name='Normal',      default=[0.0, 0.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseNormal','m_XYPlane','m_ScaleFactor','m_Normal',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKWarpScalar )        
TYPENAMES.append('VTKWarpScalarType' )

#--------------------------------------------------------------
class VTKWarpTo(Node, BVTK_Node):

    bl_idname = 'VTKWarpToType'
    bl_label  = 'vtkWarpTo'
    
    m_Absolute   : bpy.props.BoolProperty       ( name='Absolute',    default=True )
    m_ScaleFactor: bpy.props.FloatProperty      ( name='ScaleFactor', default=0.5 )
    m_Position   : bpy.props.FloatVectorProperty( name='Position',    default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Absolute','m_ScaleFactor','m_Position',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKWarpTo )        
TYPENAMES.append('VTKWarpToType' )

#--------------------------------------------------------------
class VTKWarpVector(Node, BVTK_Node):

    bl_idname = 'VTKWarpVectorType'
    bl_label  = 'vtkWarpVector'
    
    m_ScaleFactor: bpy.props.FloatProperty( name='ScaleFactor', default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ScaleFactor',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKWarpVector )        
TYPENAMES.append('VTKWarpVectorType' )

#--------------------------------------------------------------
class VTKWeightedTransformFilter(Node, BVTK_Node):

    bl_idname = 'VTKWeightedTransformFilterType'
    bl_label  = 'vtkWeightedTransformFilter'
    
    m_AddInputValues             : bpy.props.BoolProperty  ( name='AddInputValues',              default=True )
    m_CellDataTransformIndexArray: bpy.props.StringProperty( name='CellDataTransformIndexArray', default="" )
    m_CellDataWeightArray        : bpy.props.StringProperty( name='CellDataWeightArray',         default="" )
    m_TransformIndexArray        : bpy.props.StringProperty( name='TransformIndexArray',         default="" )
    m_WeightArray                : bpy.props.StringProperty( name='WeightArray',                 default="" )
    m_NumberOfTransforms         : bpy.props.IntProperty   ( name='NumberOfTransforms',          default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AddInputValues','m_CellDataTransformIndexArray','m_CellDataWeightArray','m_TransformIndexArray','m_WeightArray','m_NumberOfTransforms',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKWeightedTransformFilter )        
TYPENAMES.append('VTKWeightedTransformFilterType' )

#--------------------------------------------------------------
class VTKWindowedSincPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKWindowedSincPolyDataFilterType'
    bl_label  = 'vtkWindowedSincPolyDataFilter'
    
    m_BoundarySmoothing   : bpy.props.BoolProperty ( name='BoundarySmoothing',    default=True )
    m_FeatureEdgeSmoothing: bpy.props.BoolProperty ( name='FeatureEdgeSmoothing', default=True )
    m_GenerateErrorScalars: bpy.props.BoolProperty ( name='GenerateErrorScalars', default=True )
    m_GenerateErrorVectors: bpy.props.BoolProperty ( name='GenerateErrorVectors', default=True )
    m_NonManifoldSmoothing: bpy.props.BoolProperty ( name='NonManifoldSmoothing', default=True )
    m_NormalizeCoordinates: bpy.props.BoolProperty ( name='NormalizeCoordinates', default=True )
    m_NumberOfIterations  : bpy.props.IntProperty  ( name='NumberOfIterations',   default=20 )
    m_EdgeAngle           : bpy.props.FloatProperty( name='EdgeAngle',            default=15.0 )
    m_FeatureAngle        : bpy.props.FloatProperty( name='FeatureAngle',         default=45.0 )
    m_PassBand            : bpy.props.FloatProperty( name='PassBand',             default=0.1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_BoundarySmoothing','m_FeatureEdgeSmoothing','m_GenerateErrorScalars','m_GenerateErrorVectors','m_NonManifoldSmoothing','m_NormalizeCoordinates','m_NumberOfIterations','m_EdgeAngle','m_FeatureAngle','m_PassBand',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKWindowedSincPolyDataFilter )        
TYPENAMES.append('VTKWindowedSincPolyDataFilterType' )

#--------------------------------------------------------------
class VTKYoungsMaterialInterface(Node, BVTK_Node):

    bl_idname = 'VTKYoungsMaterialInterfaceType'
    bl_label  = 'vtkYoungsMaterialInterface'
    
    m_AxisSymetric         : bpy.props.BoolProperty       ( name='AxisSymetric',          default=True )
    m_FillMaterial         : bpy.props.BoolProperty       ( name='FillMaterial',          default=True )
    m_InverseNormal        : bpy.props.BoolProperty       ( name='InverseNormal',         default=True )
    m_OnionPeel            : bpy.props.BoolProperty       ( name='OnionPeel',             default=True )
    m_ReverseMaterialOrder : bpy.props.BoolProperty       ( name='ReverseMaterialOrder',  default=True )
    m_UseAllBlocks         : bpy.props.BoolProperty       ( name='UseAllBlocks',          default=True )
    m_UseFractionAsDistance: bpy.props.BoolProperty       ( name='UseFractionAsDistance', default=True )
    m_NumberOfMaterials    : bpy.props.IntProperty        ( name='NumberOfMaterials',     default=0 )
    m_VolumeFractionRange  : bpy.props.FloatVectorProperty( name='VolumeFractionRange',   default=[0.01, 0.99], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AxisSymetric','m_FillMaterial','m_InverseNormal','m_OnionPeel','m_ReverseMaterialOrder','m_UseAllBlocks','m_UseFractionAsDistance','m_NumberOfMaterials','m_VolumeFractionRange',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKYoungsMaterialInterface )        
TYPENAMES.append('VTKYoungsMaterialInterfaceType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( BVTK_NodeCategory( 'Filter1', 'Filter1', items=menu_items) )