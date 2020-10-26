# Generated definitions for VTK class group: Filter
# VTK Version: 8.1.2

from ..core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKAnnotationLink(Node, BVTK_Node):

    bl_idname = 'VTKAnnotationLinkType'
    bl_label  = 'vtkAnnotationLink'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1', 'output 2'], ['AnnotationLayers', 'CurrentSelection'], []) 
    
add_class( VTKAnnotationLink )        
TYPENAMES.append('VTKAnnotationLinkType' )

#--------------------------------------------------------------
class VTKAutoCorrelativeStatistics(Node, BVTK_Node):

    bl_idname = 'VTKAutoCorrelativeStatisticsType'
    bl_label  = 'vtkAutoCorrelativeStatistics'
    
    m_AssessOption         : bpy.props.BoolProperty( name='AssessOption',          default=False )
    m_DeriveOption         : bpy.props.BoolProperty( name='DeriveOption',          default=True )
    m_LearnOption          : bpy.props.BoolProperty( name='LearnOption',           default=True )
    m_TestOption           : bpy.props.BoolProperty( name='TestOption',            default=False )
    m_NumberOfPrimaryTables: bpy.props.IntProperty ( name='NumberOfPrimaryTables', default=1 )
    m_SliceCardinality     : bpy.props.IntProperty ( name='SliceCardinality',      default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_NumberOfPrimaryTables','m_SliceCardinality',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKAutoCorrelativeStatistics )        
TYPENAMES.append('VTKAutoCorrelativeStatisticsType' )

#--------------------------------------------------------------
class VTKBandedPolyDataContourFilter(Node, BVTK_Node):

    bl_idname = 'VTKBandedPolyDataContourFilterType'
    bl_label  = 'vtkBandedPolyDataContourFilter'
    e_ScalarMode_items=[ (x,x,x) for x in ['Index', 'Value']]
    
    m_Clipping            : bpy.props.BoolProperty ( name='Clipping',             default=True )
    m_GenerateContourEdges: bpy.props.BoolProperty ( name='GenerateContourEdges', default=True )
    m_Component           : bpy.props.IntProperty  ( name='Component',            default=0 )
    m_NumberOfContours    : bpy.props.IntProperty  ( name='NumberOfContours',     default=1 )
    m_ClipTolerance       : bpy.props.FloatProperty( name='ClipTolerance',        default=1.1920928955078125e-07 )
    e_ScalarMode          : bpy.props.EnumProperty ( name='ScalarMode',           default="Index", items=e_ScalarMode_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Clipping','m_GenerateContourEdges','m_Component','m_NumberOfContours','m_ClipTolerance','e_ScalarMode',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKBandedPolyDataContourFilter )        
TYPENAMES.append('VTKBandedPolyDataContourFilterType' )

#--------------------------------------------------------------
class VTKBivariateLinearTableThreshold(Node, BVTK_Node):

    bl_idname = 'VTKBivariateLinearTableThresholdType'
    bl_label  = 'vtkBivariateLinearTableThreshold'
    e_LinearThresholdType_items=[ (x,x,x) for x in ['Above', 'Below', 'Near', 'Between']]
    
    m_UseNormalizedDistance: bpy.props.BoolProperty       ( name='UseNormalizedDistance', default=True )
    m_Inclusive            : bpy.props.IntProperty        ( name='Inclusive',             default=0 )
    m_DistanceThreshold    : bpy.props.FloatProperty      ( name='DistanceThreshold',     default=1.0 )
    e_LinearThresholdType  : bpy.props.EnumProperty       ( name='LinearThresholdType',   default="Near", items=e_LinearThresholdType_items )
    m_ColumnRanges         : bpy.props.FloatVectorProperty( name='ColumnRanges',          default=[1.0, 1.0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseNormalizedDistance','m_Inclusive','m_DistanceThreshold','e_LinearThresholdType','m_ColumnRanges',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKBivariateLinearTableThreshold )        
TYPENAMES.append('VTKBivariateLinearTableThresholdType' )

#--------------------------------------------------------------
class VTKBooleanOperationPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKBooleanOperationPolyDataFilterType'
    bl_label  = 'vtkBooleanOperationPolyDataFilter'
    e_Operation_items=[ (x,x,x) for x in ['Union', 'Intersection', 'Difference']]
    
    m_ReorientDifferenceCells: bpy.props.BoolProperty ( name='ReorientDifferenceCells', default=True )
    m_Tolerance              : bpy.props.FloatProperty( name='Tolerance',               default=1e-06 )
    e_Operation              : bpy.props.EnumProperty ( name='Operation',               default="Union", items=e_Operation_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReorientDifferenceCells','m_Tolerance','e_Operation',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKBooleanOperationPolyDataFilter )        
TYPENAMES.append('VTKBooleanOperationPolyDataFilterType' )

#--------------------------------------------------------------
class VTKBoxClipDataSet(Node, BVTK_Node):

    bl_idname = 'VTKBoxClipDataSetType'
    bl_label  = 'vtkBoxClipDataSet'
    
    m_GenerateClipScalars  : bpy.props.BoolProperty( name='GenerateClipScalars',   default=True )
    m_GenerateClippedOutput: bpy.props.BoolProperty( name='GenerateClippedOutput', default=True )
    m_Orientation          : bpy.props.IntProperty ( name='Orientation',           default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateClipScalars','m_GenerateClippedOutput','m_Orientation',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKBoxClipDataSet )        
TYPENAMES.append('VTKBoxClipDataSetType' )

#--------------------------------------------------------------
class VTKClipDataSet(Node, BVTK_Node):

    bl_idname = 'VTKClipDataSetType'
    bl_label  = 'vtkClipDataSet'
    
    m_GenerateClipScalars  : bpy.props.BoolProperty ( name='GenerateClipScalars',   default=True )
    m_GenerateClippedOutput: bpy.props.BoolProperty ( name='GenerateClippedOutput', default=True )
    m_InsideOut            : bpy.props.BoolProperty ( name='InsideOut',             default=True )
    m_UseValueAsOffset     : bpy.props.BoolProperty ( name='UseValueAsOffset',      default=True )
    m_MergeTolerance       : bpy.props.FloatProperty( name='MergeTolerance',        default=0.01 )
    m_Value                : bpy.props.FloatProperty( name='Value',                 default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateClipScalars','m_GenerateClippedOutput','m_InsideOut','m_UseValueAsOffset','m_MergeTolerance','m_Value',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ClipFunction'], []) 
    
add_class( VTKClipDataSet )        
TYPENAMES.append('VTKClipDataSetType' )

#--------------------------------------------------------------
class VTKClipHyperOctree(Node, BVTK_Node):

    bl_idname = 'VTKClipHyperOctreeType'
    bl_label  = 'vtkClipHyperOctree'
    
    m_GenerateClipScalars  : bpy.props.BoolProperty ( name='GenerateClipScalars',   default=True )
    m_GenerateClippedOutput: bpy.props.BoolProperty ( name='GenerateClippedOutput', default=True )
    m_InsideOut            : bpy.props.BoolProperty ( name='InsideOut',             default=True )
    m_Value                : bpy.props.FloatProperty( name='Value',                 default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateClipScalars','m_GenerateClippedOutput','m_InsideOut','m_Value',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ClipFunction'], []) 
    
add_class( VTKClipHyperOctree )        
TYPENAMES.append('VTKClipHyperOctreeType' )

#--------------------------------------------------------------
class VTKClipPolyData(Node, BVTK_Node):

    bl_idname = 'VTKClipPolyDataType'
    bl_label  = 'vtkClipPolyData'
    
    m_GenerateClipScalars  : bpy.props.BoolProperty ( name='GenerateClipScalars',   default=True )
    m_GenerateClippedOutput: bpy.props.BoolProperty ( name='GenerateClippedOutput', default=True )
    m_InsideOut            : bpy.props.BoolProperty ( name='InsideOut',             default=True )
    m_Value                : bpy.props.FloatProperty( name='Value',                 default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateClipScalars','m_GenerateClippedOutput','m_InsideOut','m_Value',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ClipFunction'], []) 
    
add_class( VTKClipPolyData )        
TYPENAMES.append('VTKClipPolyDataType' )

#--------------------------------------------------------------
class VTKClipVolume(Node, BVTK_Node):

    bl_idname = 'VTKClipVolumeType'
    bl_label  = 'vtkClipVolume'
    
    m_GenerateClipScalars  : bpy.props.BoolProperty ( name='GenerateClipScalars',   default=True )
    m_GenerateClippedOutput: bpy.props.BoolProperty ( name='GenerateClippedOutput', default=True )
    m_InsideOut            : bpy.props.BoolProperty ( name='InsideOut',             default=True )
    m_Mixed3DCellGeneration: bpy.props.BoolProperty ( name='Mixed3DCellGeneration', default=True )
    m_MergeTolerance       : bpy.props.FloatProperty( name='MergeTolerance',        default=0.01 )
    m_Value                : bpy.props.FloatProperty( name='Value',                 default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateClipScalars','m_GenerateClippedOutput','m_InsideOut','m_Mixed3DCellGeneration','m_MergeTolerance','m_Value',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ClipFunction'], []) 
    
add_class( VTKClipVolume )        
TYPENAMES.append('VTKClipVolumeType' )

#--------------------------------------------------------------
class VTKComputeHistogram2DOutliers(Node, BVTK_Node):

    bl_idname = 'VTKComputeHistogram2DOutliersType'
    bl_label  = 'vtkComputeHistogram2DOutliers'
    
    m_PreferredNumberOfOutliers: bpy.props.IntProperty( name='PreferredNumberOfOutliers', default=10 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PreferredNumberOfOutliers',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKComputeHistogram2DOutliers )        
TYPENAMES.append('VTKComputeHistogram2DOutliersType' )

#--------------------------------------------------------------
class VTKContingencyStatistics(Node, BVTK_Node):

    bl_idname = 'VTKContingencyStatisticsType'
    bl_label  = 'vtkContingencyStatistics'
    
    m_AssessOption         : bpy.props.BoolProperty( name='AssessOption',          default=False )
    m_DeriveOption         : bpy.props.BoolProperty( name='DeriveOption',          default=True )
    m_LearnOption          : bpy.props.BoolProperty( name='LearnOption',           default=True )
    m_TestOption           : bpy.props.BoolProperty( name='TestOption',            default=False )
    m_NumberOfPrimaryTables: bpy.props.IntProperty ( name='NumberOfPrimaryTables', default=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKContingencyStatistics )        
TYPENAMES.append('VTKContingencyStatisticsType' )

#--------------------------------------------------------------
class VTKConvertSelectionDomain(Node, BVTK_Node):

    bl_idname = 'VTKConvertSelectionDomainType'
    bl_label  = 'vtkConvertSelectionDomain'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKConvertSelectionDomain )        
TYPENAMES.append('VTKConvertSelectionDomainType' )

#--------------------------------------------------------------
class VTKCorrelativeStatistics(Node, BVTK_Node):

    bl_idname = 'VTKCorrelativeStatisticsType'
    bl_label  = 'vtkCorrelativeStatistics'
    
    m_AssessOption         : bpy.props.BoolProperty( name='AssessOption',          default=False )
    m_DeriveOption         : bpy.props.BoolProperty( name='DeriveOption',          default=True )
    m_LearnOption          : bpy.props.BoolProperty( name='LearnOption',           default=True )
    m_TestOption           : bpy.props.BoolProperty( name='TestOption',            default=False )
    m_NumberOfPrimaryTables: bpy.props.IntProperty ( name='NumberOfPrimaryTables', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKCorrelativeStatistics )        
TYPENAMES.append('VTKCorrelativeStatisticsType' )

#--------------------------------------------------------------
class VTKDescriptiveStatistics(Node, BVTK_Node):

    bl_idname = 'VTKDescriptiveStatisticsType'
    bl_label  = 'vtkDescriptiveStatistics'
    
    m_AssessOption         : bpy.props.BoolProperty( name='AssessOption',          default=False )
    m_DeriveOption         : bpy.props.BoolProperty( name='DeriveOption',          default=True )
    m_G1Skewness           : bpy.props.BoolProperty( name='G1Skewness',            default=True )
    m_G2Kurtosis           : bpy.props.BoolProperty( name='G2Kurtosis',            default=True )
    m_LearnOption          : bpy.props.BoolProperty( name='LearnOption',           default=True )
    m_SignedDeviations     : bpy.props.BoolProperty( name='SignedDeviations',      default=True )
    m_TestOption           : bpy.props.BoolProperty( name='TestOption',            default=False )
    m_UnbiasedVariance     : bpy.props.BoolProperty( name='UnbiasedVariance',      default=True )
    m_NumberOfPrimaryTables: bpy.props.IntProperty ( name='NumberOfPrimaryTables', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_G1Skewness','m_G2Kurtosis','m_LearnOption','m_SignedDeviations','m_TestOption','m_UnbiasedVariance','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKDescriptiveStatistics )        
TYPENAMES.append('VTKDescriptiveStatisticsType' )

#--------------------------------------------------------------
class VTKDistancePolyDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKDistancePolyDataFilterType'
    bl_label  = 'vtkDistancePolyDataFilter'
    
    m_ComputeSecondDistance: bpy.props.BoolProperty( name='ComputeSecondDistance', default=True )
    m_NegateDistance       : bpy.props.BoolProperty( name='NegateDistance',        default=True )
    m_SignedDistance       : bpy.props.BoolProperty( name='SignedDistance',        default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeSecondDistance','m_NegateDistance','m_SignedDistance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKDistancePolyDataFilter )        
TYPENAMES.append('VTKDistancePolyDataFilterType' )

#--------------------------------------------------------------
class VTKExtractHierarchicalBins(Node, BVTK_Node):

    bl_idname = 'VTKExtractHierarchicalBinsType'
    bl_label  = 'vtkExtractHierarchicalBins'
    
    m_GenerateOutliers: bpy.props.BoolProperty( name='GenerateOutliers', default=False )
    m_GenerateVertices: bpy.props.BoolProperty( name='GenerateVertices', default=False )
    m_Bin             : bpy.props.IntProperty ( name='Bin',              default=-1 )
    m_Level           : bpy.props.IntProperty ( name='Level',            default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateOutliers','m_GenerateVertices','m_Bin','m_Level',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['BinningFilter'], []) 
    
add_class( VTKExtractHierarchicalBins )        
TYPENAMES.append('VTKExtractHierarchicalBinsType' )

#--------------------------------------------------------------
class VTKExtractHistogram2D(Node, BVTK_Node):

    bl_idname = 'VTKExtractHistogram2DType'
    bl_label  = 'vtkExtractHistogram2D'
    e_ScalarType_items=[ (x,x,x) for x in ['UnsignedChar', 'UnsignedShort', 'UnsignedInt', 'UnsignedLong', 'Float', 'Double']]
    
    m_AssessOption             : bpy.props.BoolProperty       ( name='AssessOption',              default=False )
    m_DeriveOption             : bpy.props.BoolProperty       ( name='DeriveOption',              default=True )
    m_LearnOption              : bpy.props.BoolProperty       ( name='LearnOption',               default=True )
    m_SwapColumns              : bpy.props.BoolProperty       ( name='SwapColumns',               default=True )
    m_TestOption               : bpy.props.BoolProperty       ( name='TestOption',                default=False )
    m_UseCustomHistogramExtents: bpy.props.BoolProperty       ( name='UseCustomHistogramExtents', default=True )
    m_NumberOfPrimaryTables    : bpy.props.IntProperty        ( name='NumberOfPrimaryTables',     default=1 )
    e_ScalarType               : bpy.props.EnumProperty       ( name='ScalarType',                default="UnsignedInt", items=e_ScalarType_items )
    m_ComponentsToProcess      : bpy.props.IntVectorProperty  ( name='ComponentsToProcess',       default=[0, 0], size=2 )
    m_NumberOfBins             : bpy.props.IntVectorProperty  ( name='NumberOfBins',              default=[0, 0], size=2 )
    m_CustomHistogramExtents   : bpy.props.FloatVectorProperty( name='CustomHistogramExtents',    default=[0.0, 0.0, 0.0, 0.0], size=4 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_SwapColumns','m_TestOption','m_UseCustomHistogramExtents','m_NumberOfPrimaryTables','e_ScalarType','m_ComponentsToProcess','m_NumberOfBins','m_CustomHistogramExtents',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2', 'output 3'], ['RowMask'], []) 
    
add_class( VTKExtractHistogram2D )        
TYPENAMES.append('VTKExtractHistogram2DType' )

#--------------------------------------------------------------
class VTKExtractPoints(Node, BVTK_Node):

    bl_idname = 'VTKExtractPointsType'
    bl_label  = 'vtkExtractPoints'
    
    m_ExtractInside   : bpy.props.BoolProperty( name='ExtractInside',    default=True )
    m_GenerateOutliers: bpy.props.BoolProperty( name='GenerateOutliers', default=False )
    m_GenerateVertices: bpy.props.BoolProperty( name='GenerateVertices', default=False )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ExtractInside','m_GenerateOutliers','m_GenerateVertices',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ImplicitFunction'], []) 
    
add_class( VTKExtractPoints )        
TYPENAMES.append('VTKExtractPointsType' )

#--------------------------------------------------------------
class VTKExtractSelectedRows(Node, BVTK_Node):

    bl_idname = 'VTKExtractSelectedRowsType'
    bl_label  = 'vtkExtractSelectedRows'
    
    m_AddOriginalRowIdsArray: bpy.props.BoolProperty( name='AddOriginalRowIdsArray', default=False )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AddOriginalRowIdsArray',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output'], [], []) 
    
add_class( VTKExtractSelectedRows )        
TYPENAMES.append('VTKExtractSelectedRowsType' )

#--------------------------------------------------------------
class VTKExtractVectorComponents(Node, BVTK_Node):

    bl_idname = 'VTKExtractVectorComponentsType'
    bl_label  = 'vtkExtractVectorComponents'
    
    m_ExtractToFieldData: bpy.props.BoolProperty( name='ExtractToFieldData', default=True )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ExtractToFieldData',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKExtractVectorComponents )        
TYPENAMES.append('VTKExtractVectorComponentsType' )

#--------------------------------------------------------------
class VTKFitImplicitFunction(Node, BVTK_Node):

    bl_idname = 'VTKFitImplicitFunctionType'
    bl_label  = 'vtkFitImplicitFunction'
    
    m_GenerateOutliers: bpy.props.BoolProperty ( name='GenerateOutliers', default=False )
    m_GenerateVertices: bpy.props.BoolProperty ( name='GenerateVertices', default=False )
    m_Threshold       : bpy.props.FloatProperty( name='Threshold',        default=0.01 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateOutliers','m_GenerateVertices','m_Threshold',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ImplicitFunction'], []) 
    
add_class( VTKFitImplicitFunction )        
TYPENAMES.append('VTKFitImplicitFunctionType' )

#--------------------------------------------------------------
class VTKGenericClip(Node, BVTK_Node):

    bl_idname = 'VTKGenericClipType'
    bl_label  = 'vtkGenericClip'
    
    m_GenerateClipScalars  : bpy.props.BoolProperty ( name='GenerateClipScalars',   default=True )
    m_GenerateClippedOutput: bpy.props.BoolProperty ( name='GenerateClippedOutput', default=True )
    m_InsideOut            : bpy.props.BoolProperty ( name='InsideOut',             default=True )
    m_MergeTolerance       : bpy.props.FloatProperty( name='MergeTolerance',        default=0.01 )
    m_Value                : bpy.props.FloatProperty( name='Value',                 default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateClipScalars','m_GenerateClippedOutput','m_InsideOut','m_MergeTolerance','m_Value',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ClipFunction'], []) 
    
add_class( VTKGenericClip )        
TYPENAMES.append('VTKGenericClipType' )

#--------------------------------------------------------------
class VTKGraphAnnotationLayersFilter(Node, BVTK_Node):

    bl_idname = 'VTKGraphAnnotationLayersFilterType'
    bl_label  = 'vtkGraphAnnotationLayersFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKGraphAnnotationLayersFilter )        
TYPENAMES.append('VTKGraphAnnotationLayersFilterType' )

#--------------------------------------------------------------
class VTKGraphToPolyData(Node, BVTK_Node):

    bl_idname = 'VTKGraphToPolyDataType'
    bl_label  = 'vtkGraphToPolyData'
    
    m_EdgeGlyphOutput  : bpy.props.BoolProperty ( name='EdgeGlyphOutput',   default=False )
    m_EdgeGlyphPosition: bpy.props.FloatProperty( name='EdgeGlyphPosition', default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EdgeGlyphOutput','m_EdgeGlyphPosition',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKGraphToPolyData )        
TYPENAMES.append('VTKGraphToPolyDataType' )

#--------------------------------------------------------------
class VTKHighestDensityRegionsStatistics(Node, BVTK_Node):

    bl_idname = 'VTKHighestDensityRegionsStatisticsType'
    bl_label  = 'vtkHighestDensityRegionsStatistics'
    
    m_AssessOption         : bpy.props.BoolProperty( name='AssessOption',          default=False )
    m_DeriveOption         : bpy.props.BoolProperty( name='DeriveOption',          default=True )
    m_LearnOption          : bpy.props.BoolProperty( name='LearnOption',           default=True )
    m_TestOption           : bpy.props.BoolProperty( name='TestOption',            default=False )
    m_NumberOfPrimaryTables: bpy.props.IntProperty ( name='NumberOfPrimaryTables', default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKHighestDensityRegionsStatistics )        
TYPENAMES.append('VTKHighestDensityRegionsStatisticsType' )

#--------------------------------------------------------------
class VTKImageConnectivityFilter(Node, BVTK_Node):

    bl_idname = 'VTKImageConnectivityFilterType'
    bl_label  = 'vtkImageConnectivityFilter'
    e_ExtractionMode_items=[ (x,x,x) for x in ['SeededRegions', 'AllRegions', 'LargestRegion']]
    e_LabelMode_items=[ (x,x,x) for x in ['SeedScalar', 'ConstantValue', 'SizeRank']]
    e_LabelScalarType_items=[ (x,x,x) for x in ['UnsignedChar', 'Short', 'UnsignedShort', 'Int']]
    
    m_GenerateRegionExtents: bpy.props.BoolProperty       ( name='GenerateRegionExtents', default=True )
    m_ActiveComponent      : bpy.props.IntProperty        ( name='ActiveComponent',       default=0 )
    m_LabelConstantValue   : bpy.props.IntProperty        ( name='LabelConstantValue',    default=255 )
    e_ExtractionMode       : bpy.props.EnumProperty       ( name='ExtractionMode',        default="SeededRegions", items=e_ExtractionMode_items )
    e_LabelMode            : bpy.props.EnumProperty       ( name='LabelMode',             default="SeedScalar", items=e_LabelMode_items )
    e_LabelScalarType      : bpy.props.EnumProperty       ( name='LabelScalarType',       default="UnsignedChar", items=e_LabelScalarType_items )
    m_SizeRange            : bpy.props.IntVectorProperty  ( name='SizeRange',             default=[1, 1000000000], size=2 )
    m_ScalarRange          : bpy.props.FloatVectorProperty( name='ScalarRange',           default=[0.5, 1e+30], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateRegionExtents','m_ActiveComponent','m_LabelConstantValue','e_ExtractionMode','e_LabelMode','e_LabelScalarType','m_SizeRange','m_ScalarRange',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output'], ['SeedConnection', 'StencilConnection'], []) 
    
add_class( VTKImageConnectivityFilter )        
TYPENAMES.append('VTKImageConnectivityFilterType' )

#--------------------------------------------------------------
class VTKImageFlip(Node, BVTK_Node):

    bl_idname = 'VTKImageFlipType'
    bl_label  = 'vtkImageFlip'
    e_InterpolationMode_items=[ (x,x,x) for x in ['NearestNeighbor', 'Linear', 'Cubic']]
    e_SlabMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Mean', 'Sum']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AutoCropOutput          : bpy.props.BoolProperty       ( name='AutoCropOutput',           default=True )
    m_Border                  : bpy.props.BoolProperty       ( name='Border',                   default=True )
    m_EnableSMP               : bpy.props.BoolProperty       ( name='EnableSMP',                default=True )
    m_FlipAboutOrigin         : bpy.props.BoolProperty       ( name='FlipAboutOrigin',          default=True )
    m_GenerateStencilOutput   : bpy.props.BoolProperty       ( name='GenerateStencilOutput',    default=True )
    m_GlobalDefaultEnableSMP  : bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP',   default=True )
    m_Interpolate             : bpy.props.BoolProperty       ( name='Interpolate',              default=True )
    m_Mirror                  : bpy.props.BoolProperty       ( name='Mirror',                   default=True )
    m_Optimization            : bpy.props.BoolProperty       ( name='Optimization',             default=True )
    m_PreserveImageExtent     : bpy.props.BoolProperty       ( name='PreserveImageExtent',      default=True )
    m_SlabTrapezoidIntegration: bpy.props.BoolProperty       ( name='SlabTrapezoidIntegration', default=True )
    m_TransformInputSampling  : bpy.props.BoolProperty       ( name='TransformInputSampling',   default=True )
    m_Wrap                    : bpy.props.BoolProperty       ( name='Wrap',                     default=True )
    m_DesiredBytesPerPiece    : bpy.props.IntProperty        ( name='DesiredBytesPerPiece',     default=65536 )
    m_FilteredAxes            : bpy.props.IntProperty        ( name='FilteredAxes',             default=0 )
    m_FilteredAxis            : bpy.props.IntProperty        ( name='FilteredAxis',             default=0 )
    m_NumberOfThreads         : bpy.props.IntProperty        ( name='NumberOfThreads',          default=8 )
    m_OutputDimensionality    : bpy.props.IntProperty        ( name='OutputDimensionality',     default=3 )
    m_OutputScalarType        : bpy.props.IntProperty        ( name='OutputScalarType',         default=-1 )
    m_SlabNumberOfSlices      : bpy.props.IntProperty        ( name='SlabNumberOfSlices',       default=1 )
    m_BackgroundLevel         : bpy.props.FloatProperty      ( name='BackgroundLevel',          default=0.0 )
    m_ScalarScale             : bpy.props.FloatProperty      ( name='ScalarScale',              default=1.0 )
    m_ScalarShift             : bpy.props.FloatProperty      ( name='ScalarShift',              default=0.0 )
    m_SlabSliceSpacingFraction: bpy.props.FloatProperty      ( name='SlabSliceSpacingFraction', default=1.0 )
    e_InterpolationMode       : bpy.props.EnumProperty       ( name='InterpolationMode',        default="NearestNeighbor", items=e_InterpolationMode_items )
    e_SlabMode                : bpy.props.EnumProperty       ( name='SlabMode',                 default="Mean", items=e_SlabMode_items )
    e_SplitMode               : bpy.props.EnumProperty       ( name='SplitMode',                default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize        : bpy.props.IntVectorProperty  ( name='MinimumPieceSize',         default=[16, 1, 1], size=3 )
    m_OutputExtent            : bpy.props.IntVectorProperty  ( name='OutputExtent',             default=[0, 0, 0, 0, 0, 0], size=6 )
    m_BackgroundColor         : bpy.props.FloatVectorProperty( name='BackgroundColor',          default=[0.0, 0.0, 0.0, 0.0], size=4 )
    m_OutputOrigin            : bpy.props.FloatVectorProperty( name='OutputOrigin',             default=[0.0, 0.0, 0.0], size=3 )
    m_OutputSpacing           : bpy.props.FloatVectorProperty( name='OutputSpacing',            default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=32, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutoCropOutput','m_Border','m_EnableSMP','m_FlipAboutOrigin','m_GenerateStencilOutput','m_GlobalDefaultEnableSMP','m_Interpolate','m_Mirror','m_Optimization','m_PreserveImageExtent','m_SlabTrapezoidIntegration','m_TransformInputSampling','m_Wrap','m_DesiredBytesPerPiece','m_FilteredAxes','m_FilteredAxis','m_NumberOfThreads','m_OutputDimensionality','m_OutputScalarType','m_SlabNumberOfSlices','m_BackgroundLevel','m_ScalarScale','m_ScalarShift','m_SlabSliceSpacingFraction','e_InterpolationMode','e_SlabMode','e_SplitMode','m_MinimumPieceSize','m_OutputExtent','m_BackgroundColor','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], ['Interpolator', 'ResliceAxes', 'StencilOutput', 'ResliceTransform'], []) 
    
add_class( VTKImageFlip )        
TYPENAMES.append('VTKImageFlipType' )

#--------------------------------------------------------------
class VTKImagePermute(Node, BVTK_Node):

    bl_idname = 'VTKImagePermuteType'
    bl_label  = 'vtkImagePermute'
    e_InterpolationMode_items=[ (x,x,x) for x in ['NearestNeighbor', 'Linear', 'Cubic']]
    e_SlabMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Mean', 'Sum']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AutoCropOutput          : bpy.props.BoolProperty       ( name='AutoCropOutput',           default=True )
    m_Border                  : bpy.props.BoolProperty       ( name='Border',                   default=True )
    m_EnableSMP               : bpy.props.BoolProperty       ( name='EnableSMP',                default=True )
    m_GenerateStencilOutput   : bpy.props.BoolProperty       ( name='GenerateStencilOutput',    default=True )
    m_GlobalDefaultEnableSMP  : bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP',   default=True )
    m_Interpolate             : bpy.props.BoolProperty       ( name='Interpolate',              default=True )
    m_Mirror                  : bpy.props.BoolProperty       ( name='Mirror',                   default=True )
    m_Optimization            : bpy.props.BoolProperty       ( name='Optimization',             default=True )
    m_SlabTrapezoidIntegration: bpy.props.BoolProperty       ( name='SlabTrapezoidIntegration', default=True )
    m_TransformInputSampling  : bpy.props.BoolProperty       ( name='TransformInputSampling',   default=True )
    m_Wrap                    : bpy.props.BoolProperty       ( name='Wrap',                     default=True )
    m_DesiredBytesPerPiece    : bpy.props.IntProperty        ( name='DesiredBytesPerPiece',     default=65536 )
    m_NumberOfThreads         : bpy.props.IntProperty        ( name='NumberOfThreads',          default=8 )
    m_OutputDimensionality    : bpy.props.IntProperty        ( name='OutputDimensionality',     default=3 )
    m_OutputScalarType        : bpy.props.IntProperty        ( name='OutputScalarType',         default=-1 )
    m_SlabNumberOfSlices      : bpy.props.IntProperty        ( name='SlabNumberOfSlices',       default=1 )
    m_BackgroundLevel         : bpy.props.FloatProperty      ( name='BackgroundLevel',          default=0.0 )
    m_ScalarScale             : bpy.props.FloatProperty      ( name='ScalarScale',              default=1.0 )
    m_ScalarShift             : bpy.props.FloatProperty      ( name='ScalarShift',              default=0.0 )
    m_SlabSliceSpacingFraction: bpy.props.FloatProperty      ( name='SlabSliceSpacingFraction', default=1.0 )
    e_InterpolationMode       : bpy.props.EnumProperty       ( name='InterpolationMode',        default="NearestNeighbor", items=e_InterpolationMode_items )
    e_SlabMode                : bpy.props.EnumProperty       ( name='SlabMode',                 default="Mean", items=e_SlabMode_items )
    e_SplitMode               : bpy.props.EnumProperty       ( name='SplitMode',                default="Slab", items=e_SplitMode_items )
    m_FilteredAxes            : bpy.props.IntVectorProperty  ( name='FilteredAxes',             default=[0, 1, 2], size=3 )
    m_MinimumPieceSize        : bpy.props.IntVectorProperty  ( name='MinimumPieceSize',         default=[16, 1, 1], size=3 )
    m_OutputExtent            : bpy.props.IntVectorProperty  ( name='OutputExtent',             default=[0, 0, 0, 0, 0, 0], size=6 )
    m_BackgroundColor         : bpy.props.FloatVectorProperty( name='BackgroundColor',          default=[0.0, 0.0, 0.0, 0.0], size=4 )
    m_OutputOrigin            : bpy.props.FloatVectorProperty( name='OutputOrigin',             default=[0.0, 0.0, 0.0], size=3 )
    m_OutputSpacing           : bpy.props.FloatVectorProperty( name='OutputSpacing',            default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=29, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutoCropOutput','m_Border','m_EnableSMP','m_GenerateStencilOutput','m_GlobalDefaultEnableSMP','m_Interpolate','m_Mirror','m_Optimization','m_SlabTrapezoidIntegration','m_TransformInputSampling','m_Wrap','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputDimensionality','m_OutputScalarType','m_SlabNumberOfSlices','m_BackgroundLevel','m_ScalarScale','m_ScalarShift','m_SlabSliceSpacingFraction','e_InterpolationMode','e_SlabMode','e_SplitMode','m_FilteredAxes','m_MinimumPieceSize','m_OutputExtent','m_BackgroundColor','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], ['Interpolator', 'StencilOutput', 'ResliceAxes', 'ResliceTransform'], []) 
    
add_class( VTKImagePermute )        
TYPENAMES.append('VTKImagePermuteType' )

#--------------------------------------------------------------
class VTKImageResample(Node, BVTK_Node):

    bl_idname = 'VTKImageResampleType'
    bl_label  = 'vtkImageResample'
    e_InterpolationMode_items=[ (x,x,x) for x in ['NearestNeighbor', 'Linear', 'Cubic']]
    e_SlabMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Mean', 'Sum']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AutoCropOutput          : bpy.props.BoolProperty       ( name='AutoCropOutput',           default=True )
    m_Border                  : bpy.props.BoolProperty       ( name='Border',                   default=True )
    m_EnableSMP               : bpy.props.BoolProperty       ( name='EnableSMP',                default=True )
    m_GenerateStencilOutput   : bpy.props.BoolProperty       ( name='GenerateStencilOutput',    default=True )
    m_GlobalDefaultEnableSMP  : bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP',   default=True )
    m_Interpolate             : bpy.props.BoolProperty       ( name='Interpolate',              default=True )
    m_Mirror                  : bpy.props.BoolProperty       ( name='Mirror',                   default=True )
    m_Optimization            : bpy.props.BoolProperty       ( name='Optimization',             default=True )
    m_SlabTrapezoidIntegration: bpy.props.BoolProperty       ( name='SlabTrapezoidIntegration', default=True )
    m_TransformInputSampling  : bpy.props.BoolProperty       ( name='TransformInputSampling',   default=True )
    m_Wrap                    : bpy.props.BoolProperty       ( name='Wrap',                     default=True )
    m_DesiredBytesPerPiece    : bpy.props.IntProperty        ( name='DesiredBytesPerPiece',     default=65536 )
    m_Dimensionality          : bpy.props.IntProperty        ( name='Dimensionality',           default=3 )
    m_NumberOfThreads         : bpy.props.IntProperty        ( name='NumberOfThreads',          default=8 )
    m_OutputDimensionality    : bpy.props.IntProperty        ( name='OutputDimensionality',     default=3 )
    m_OutputScalarType        : bpy.props.IntProperty        ( name='OutputScalarType',         default=-1 )
    m_SlabNumberOfSlices      : bpy.props.IntProperty        ( name='SlabNumberOfSlices',       default=1 )
    m_BackgroundLevel         : bpy.props.FloatProperty      ( name='BackgroundLevel',          default=0.0 )
    m_ScalarScale             : bpy.props.FloatProperty      ( name='ScalarScale',              default=1.0 )
    m_ScalarShift             : bpy.props.FloatProperty      ( name='ScalarShift',              default=0.0 )
    m_SlabSliceSpacingFraction: bpy.props.FloatProperty      ( name='SlabSliceSpacingFraction', default=1.0 )
    e_InterpolationMode       : bpy.props.EnumProperty       ( name='InterpolationMode',        default="Linear", items=e_InterpolationMode_items )
    e_SlabMode                : bpy.props.EnumProperty       ( name='SlabMode',                 default="Mean", items=e_SlabMode_items )
    e_SplitMode               : bpy.props.EnumProperty       ( name='SplitMode',                default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize        : bpy.props.IntVectorProperty  ( name='MinimumPieceSize',         default=[16, 1, 1], size=3 )
    m_OutputExtent            : bpy.props.IntVectorProperty  ( name='OutputExtent',             default=[0, 0, 0, 0, 0, 0], size=6 )
    m_BackgroundColor         : bpy.props.FloatVectorProperty( name='BackgroundColor',          default=[0.0, 0.0, 0.0, 0.0], size=4 )
    m_MagnificationFactors    : bpy.props.FloatVectorProperty( name='MagnificationFactors',     default=[1.0, 1.0, 1.0], size=3 )
    m_OutputOrigin            : bpy.props.FloatVectorProperty( name='OutputOrigin',             default=[0.0, 0.0, 0.0], size=3 )
    m_OutputSpacing           : bpy.props.FloatVectorProperty( name='OutputSpacing',            default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=30, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutoCropOutput','m_Border','m_EnableSMP','m_GenerateStencilOutput','m_GlobalDefaultEnableSMP','m_Interpolate','m_Mirror','m_Optimization','m_SlabTrapezoidIntegration','m_TransformInputSampling','m_Wrap','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','m_OutputDimensionality','m_OutputScalarType','m_SlabNumberOfSlices','m_BackgroundLevel','m_ScalarScale','m_ScalarShift','m_SlabSliceSpacingFraction','e_InterpolationMode','e_SlabMode','e_SplitMode','m_MinimumPieceSize','m_OutputExtent','m_BackgroundColor','m_MagnificationFactors','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], ['Interpolator', 'StencilOutput', 'ResliceAxes', 'ResliceTransform'], []) 
    
add_class( VTKImageResample )        
TYPENAMES.append('VTKImageResampleType' )

#--------------------------------------------------------------
class VTKImageReslice(Node, BVTK_Node):

    bl_idname = 'VTKImageResliceType'
    bl_label  = 'vtkImageReslice'
    e_InterpolationMode_items=[ (x,x,x) for x in ['NearestNeighbor', 'Linear', 'Cubic']]
    e_SlabMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Mean', 'Sum']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AutoCropOutput          : bpy.props.BoolProperty       ( name='AutoCropOutput',           default=True )
    m_Border                  : bpy.props.BoolProperty       ( name='Border',                   default=True )
    m_EnableSMP               : bpy.props.BoolProperty       ( name='EnableSMP',                default=True )
    m_GenerateStencilOutput   : bpy.props.BoolProperty       ( name='GenerateStencilOutput',    default=True )
    m_GlobalDefaultEnableSMP  : bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP',   default=True )
    m_Interpolate             : bpy.props.BoolProperty       ( name='Interpolate',              default=True )
    m_Mirror                  : bpy.props.BoolProperty       ( name='Mirror',                   default=True )
    m_Optimization            : bpy.props.BoolProperty       ( name='Optimization',             default=True )
    m_SlabTrapezoidIntegration: bpy.props.BoolProperty       ( name='SlabTrapezoidIntegration', default=True )
    m_TransformInputSampling  : bpy.props.BoolProperty       ( name='TransformInputSampling',   default=True )
    m_Wrap                    : bpy.props.BoolProperty       ( name='Wrap',                     default=True )
    m_DesiredBytesPerPiece    : bpy.props.IntProperty        ( name='DesiredBytesPerPiece',     default=65536 )
    m_NumberOfThreads         : bpy.props.IntProperty        ( name='NumberOfThreads',          default=8 )
    m_OutputDimensionality    : bpy.props.IntProperty        ( name='OutputDimensionality',     default=3 )
    m_OutputScalarType        : bpy.props.IntProperty        ( name='OutputScalarType',         default=-1 )
    m_SlabNumberOfSlices      : bpy.props.IntProperty        ( name='SlabNumberOfSlices',       default=1 )
    m_BackgroundLevel         : bpy.props.FloatProperty      ( name='BackgroundLevel',          default=0.0 )
    m_ScalarScale             : bpy.props.FloatProperty      ( name='ScalarScale',              default=1.0 )
    m_ScalarShift             : bpy.props.FloatProperty      ( name='ScalarShift',              default=0.0 )
    m_SlabSliceSpacingFraction: bpy.props.FloatProperty      ( name='SlabSliceSpacingFraction', default=1.0 )
    e_InterpolationMode       : bpy.props.EnumProperty       ( name='InterpolationMode',        default="NearestNeighbor", items=e_InterpolationMode_items )
    e_SlabMode                : bpy.props.EnumProperty       ( name='SlabMode',                 default="Mean", items=e_SlabMode_items )
    e_SplitMode               : bpy.props.EnumProperty       ( name='SplitMode',                default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize        : bpy.props.IntVectorProperty  ( name='MinimumPieceSize',         default=[16, 1, 1], size=3 )
    m_OutputExtent            : bpy.props.IntVectorProperty  ( name='OutputExtent',             default=[0, 0, 0, 0, 0, 0], size=6 )
    m_BackgroundColor         : bpy.props.FloatVectorProperty( name='BackgroundColor',          default=[0.0, 0.0, 0.0, 0.0], size=4 )
    m_OutputOrigin            : bpy.props.FloatVectorProperty( name='OutputOrigin',             default=[0.0, 0.0, 0.0], size=3 )
    m_OutputSpacing           : bpy.props.FloatVectorProperty( name='OutputSpacing',            default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=28, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutoCropOutput','m_Border','m_EnableSMP','m_GenerateStencilOutput','m_GlobalDefaultEnableSMP','m_Interpolate','m_Mirror','m_Optimization','m_SlabTrapezoidIntegration','m_TransformInputSampling','m_Wrap','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputDimensionality','m_OutputScalarType','m_SlabNumberOfSlices','m_BackgroundLevel','m_ScalarScale','m_ScalarShift','m_SlabSliceSpacingFraction','e_InterpolationMode','e_SlabMode','e_SplitMode','m_MinimumPieceSize','m_OutputExtent','m_BackgroundColor','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], ['Interpolator', 'StencilOutput', 'ResliceAxes', 'ResliceTransform'], []) 
    
add_class( VTKImageReslice )        
TYPENAMES.append('VTKImageResliceType' )

#--------------------------------------------------------------
class VTKImageResliceToColors(Node, BVTK_Node):

    bl_idname = 'VTKImageResliceToColorsType'
    bl_label  = 'vtkImageResliceToColors'
    e_InterpolationMode_items=[ (x,x,x) for x in ['NearestNeighbor', 'Linear', 'Cubic']]
    e_OutputFormat_items=[ (x,x,x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_SlabMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Mean', 'Sum']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AutoCropOutput          : bpy.props.BoolProperty       ( name='AutoCropOutput',           default=True )
    m_Border                  : bpy.props.BoolProperty       ( name='Border',                   default=True )
    m_Bypass                  : bpy.props.BoolProperty       ( name='Bypass',                   default=True )
    m_EnableSMP               : bpy.props.BoolProperty       ( name='EnableSMP',                default=True )
    m_GenerateStencilOutput   : bpy.props.BoolProperty       ( name='GenerateStencilOutput',    default=True )
    m_GlobalDefaultEnableSMP  : bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP',   default=True )
    m_Interpolate             : bpy.props.BoolProperty       ( name='Interpolate',              default=True )
    m_Mirror                  : bpy.props.BoolProperty       ( name='Mirror',                   default=True )
    m_Optimization            : bpy.props.BoolProperty       ( name='Optimization',             default=True )
    m_SlabTrapezoidIntegration: bpy.props.BoolProperty       ( name='SlabTrapezoidIntegration', default=True )
    m_TransformInputSampling  : bpy.props.BoolProperty       ( name='TransformInputSampling',   default=True )
    m_Wrap                    : bpy.props.BoolProperty       ( name='Wrap',                     default=True )
    m_DesiredBytesPerPiece    : bpy.props.IntProperty        ( name='DesiredBytesPerPiece',     default=65536 )
    m_NumberOfThreads         : bpy.props.IntProperty        ( name='NumberOfThreads',          default=8 )
    m_OutputDimensionality    : bpy.props.IntProperty        ( name='OutputDimensionality',     default=3 )
    m_OutputScalarType        : bpy.props.IntProperty        ( name='OutputScalarType',         default=-1 )
    m_SlabNumberOfSlices      : bpy.props.IntProperty        ( name='SlabNumberOfSlices',       default=1 )
    m_BackgroundLevel         : bpy.props.FloatProperty      ( name='BackgroundLevel',          default=0.0 )
    m_ScalarScale             : bpy.props.FloatProperty      ( name='ScalarScale',              default=1.0 )
    m_ScalarShift             : bpy.props.FloatProperty      ( name='ScalarShift',              default=0.0 )
    m_SlabSliceSpacingFraction: bpy.props.FloatProperty      ( name='SlabSliceSpacingFraction', default=1.0 )
    e_InterpolationMode       : bpy.props.EnumProperty       ( name='InterpolationMode',        default="NearestNeighbor", items=e_InterpolationMode_items )
    e_OutputFormat            : bpy.props.EnumProperty       ( name='OutputFormat',             default="RGBA", items=e_OutputFormat_items )
    e_SlabMode                : bpy.props.EnumProperty       ( name='SlabMode',                 default="Mean", items=e_SlabMode_items )
    e_SplitMode               : bpy.props.EnumProperty       ( name='SplitMode',                default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize        : bpy.props.IntVectorProperty  ( name='MinimumPieceSize',         default=[16, 1, 1], size=3 )
    m_OutputExtent            : bpy.props.IntVectorProperty  ( name='OutputExtent',             default=[0, 0, 0, 0, 0, 0], size=6 )
    m_BackgroundColor         : bpy.props.FloatVectorProperty( name='BackgroundColor',          default=[0.0, 0.0, 0.0, 0.0], size=4 )
    m_OutputOrigin            : bpy.props.FloatVectorProperty( name='OutputOrigin',             default=[0.0, 0.0, 0.0], size=3 )
    m_OutputSpacing           : bpy.props.FloatVectorProperty( name='OutputSpacing',            default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=30, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutoCropOutput','m_Border','m_Bypass','m_EnableSMP','m_GenerateStencilOutput','m_GlobalDefaultEnableSMP','m_Interpolate','m_Mirror','m_Optimization','m_SlabTrapezoidIntegration','m_TransformInputSampling','m_Wrap','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputDimensionality','m_OutputScalarType','m_SlabNumberOfSlices','m_BackgroundLevel','m_ScalarScale','m_ScalarShift','m_SlabSliceSpacingFraction','e_InterpolationMode','e_OutputFormat','e_SlabMode','e_SplitMode','m_MinimumPieceSize','m_OutputExtent','m_BackgroundColor','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], ['Interpolator', 'StencilOutput', 'LookupTable', 'ResliceAxes', 'ResliceTransform'], []) 
    
add_class( VTKImageResliceToColors )        
TYPENAMES.append('VTKImageResliceToColorsType' )

#--------------------------------------------------------------
class VTKImageSlabReslice(Node, BVTK_Node):

    bl_idname = 'VTKImageSlabResliceType'
    bl_label  = 'vtkImageSlabReslice'
    e_BlendMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Mean']]
    e_InterpolationMode_items=[ (x,x,x) for x in ['NearestNeighbor', 'Linear', 'Cubic']]
    e_SlabMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Mean', 'Sum']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AutoCropOutput          : bpy.props.BoolProperty       ( name='AutoCropOutput',           default=True )
    m_Border                  : bpy.props.BoolProperty       ( name='Border',                   default=True )
    m_EnableSMP               : bpy.props.BoolProperty       ( name='EnableSMP',                default=True )
    m_GenerateStencilOutput   : bpy.props.BoolProperty       ( name='GenerateStencilOutput',    default=True )
    m_GlobalDefaultEnableSMP  : bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP',   default=True )
    m_Interpolate             : bpy.props.BoolProperty       ( name='Interpolate',              default=True )
    m_Mirror                  : bpy.props.BoolProperty       ( name='Mirror',                   default=True )
    m_Optimization            : bpy.props.BoolProperty       ( name='Optimization',             default=True )
    m_SlabTrapezoidIntegration: bpy.props.BoolProperty       ( name='SlabTrapezoidIntegration', default=True )
    m_TransformInputSampling  : bpy.props.BoolProperty       ( name='TransformInputSampling',   default=True )
    m_Wrap                    : bpy.props.BoolProperty       ( name='Wrap',                     default=True )
    m_DesiredBytesPerPiece    : bpy.props.IntProperty        ( name='DesiredBytesPerPiece',     default=65536 )
    m_NumberOfThreads         : bpy.props.IntProperty        ( name='NumberOfThreads',          default=8 )
    m_OutputDimensionality    : bpy.props.IntProperty        ( name='OutputDimensionality',     default=2 )
    m_OutputScalarType        : bpy.props.IntProperty        ( name='OutputScalarType',         default=-1 )
    m_SlabNumberOfSlices      : bpy.props.IntProperty        ( name='SlabNumberOfSlices',       default=1 )
    m_BackgroundLevel         : bpy.props.FloatProperty      ( name='BackgroundLevel',          default=0.0 )
    m_ScalarScale             : bpy.props.FloatProperty      ( name='ScalarScale',              default=1.0 )
    m_ScalarShift             : bpy.props.FloatProperty      ( name='ScalarShift',              default=0.0 )
    m_SlabResolution          : bpy.props.FloatProperty      ( name='SlabResolution',           default=1.0 )
    m_SlabSliceSpacingFraction: bpy.props.FloatProperty      ( name='SlabSliceSpacingFraction', default=1.0 )
    m_SlabThickness           : bpy.props.FloatProperty      ( name='SlabThickness',            default=10.0 )
    e_BlendMode               : bpy.props.EnumProperty       ( name='BlendMode',                default="Max", items=e_BlendMode_items )
    e_InterpolationMode       : bpy.props.EnumProperty       ( name='InterpolationMode',        default="NearestNeighbor", items=e_InterpolationMode_items )
    e_SlabMode                : bpy.props.EnumProperty       ( name='SlabMode',                 default="Mean", items=e_SlabMode_items )
    e_SplitMode               : bpy.props.EnumProperty       ( name='SplitMode',                default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize        : bpy.props.IntVectorProperty  ( name='MinimumPieceSize',         default=[16, 1, 1], size=3 )
    m_OutputExtent            : bpy.props.IntVectorProperty  ( name='OutputExtent',             default=[0, 0, 0, 0, 0, 0], size=6 )
    m_BackgroundColor         : bpy.props.FloatVectorProperty( name='BackgroundColor',          default=[0.0, 0.0, 0.0, 0.0], size=4 )
    m_OutputOrigin            : bpy.props.FloatVectorProperty( name='OutputOrigin',             default=[0.0, 0.0, 0.0], size=3 )
    m_OutputSpacing           : bpy.props.FloatVectorProperty( name='OutputSpacing',            default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=31, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutoCropOutput','m_Border','m_EnableSMP','m_GenerateStencilOutput','m_GlobalDefaultEnableSMP','m_Interpolate','m_Mirror','m_Optimization','m_SlabTrapezoidIntegration','m_TransformInputSampling','m_Wrap','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputDimensionality','m_OutputScalarType','m_SlabNumberOfSlices','m_BackgroundLevel','m_ScalarScale','m_ScalarShift','m_SlabResolution','m_SlabSliceSpacingFraction','m_SlabThickness','e_BlendMode','e_InterpolationMode','e_SlabMode','e_SplitMode','m_MinimumPieceSize','m_OutputExtent','m_BackgroundColor','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], ['Interpolator', 'StencilOutput', 'ResliceAxes', 'ResliceTransform'], []) 
    
add_class( VTKImageSlabReslice )        
TYPENAMES.append('VTKImageSlabResliceType' )

#--------------------------------------------------------------
class VTKImageStencil(Node, BVTK_Node):

    bl_idname = 'VTKImageStencilType'
    bl_label  = 'vtkImageStencil'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP             : bpy.props.BoolProperty       ( name='EnableSMP',              default=True )
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP', default=True )
    m_ReverseStencil        : bpy.props.BoolProperty       ( name='ReverseStencil',         default=True )
    m_DesiredBytesPerPiece  : bpy.props.IntProperty        ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads       : bpy.props.IntProperty        ( name='NumberOfThreads',        default=8 )
    m_BackgroundValue       : bpy.props.FloatProperty      ( name='BackgroundValue',        default=1.0 )
    e_SplitMode             : bpy.props.EnumProperty       ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize      : bpy.props.IntVectorProperty  ( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_BackgroundColor       : bpy.props.FloatVectorProperty( name='BackgroundColor',        default=[1.0, 1.0, 1.0, 1.0], size=4 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_ReverseStencil','m_DesiredBytesPerPiece','m_NumberOfThreads','m_BackgroundValue','e_SplitMode','m_MinimumPieceSize','m_BackgroundColor',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output'], [], []) 
    
add_class( VTKImageStencil )        
TYPENAMES.append('VTKImageStencilType' )

#--------------------------------------------------------------
class VTKIntersectionPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKIntersectionPolyDataFilterType'
    bl_label  = 'vtkIntersectionPolyDataFilter'
    
    m_CheckInput                   : bpy.props.BoolProperty ( name='CheckInput',                    default=True )
    m_CheckMesh                    : bpy.props.BoolProperty ( name='CheckMesh',                     default=True )
    m_ComputeIntersectionPointArray: bpy.props.BoolProperty ( name='ComputeIntersectionPointArray', default=True )
    m_SplitFirstOutput             : bpy.props.BoolProperty ( name='SplitFirstOutput',              default=True )
    m_SplitSecondOutput            : bpy.props.BoolProperty ( name='SplitSecondOutput',             default=True )
    m_RelativeSubtriangleArea      : bpy.props.FloatProperty( name='RelativeSubtriangleArea',       default=0.0001 )
    m_Tolerance                    : bpy.props.FloatProperty( name='Tolerance',                     default=1e-06 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CheckInput','m_CheckMesh','m_ComputeIntersectionPointArray','m_SplitFirstOutput','m_SplitSecondOutput','m_RelativeSubtriangleArea','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKIntersectionPolyDataFilter )        
TYPENAMES.append('VTKIntersectionPolyDataFilterType' )

#--------------------------------------------------------------
class VTKKMeansStatistics(Node, BVTK_Node):

    bl_idname = 'VTKKMeansStatisticsType'
    bl_label  = 'vtkKMeansStatistics'
    
    m_AssessOption           : bpy.props.BoolProperty  ( name='AssessOption',            default=False )
    m_DeriveOption           : bpy.props.BoolProperty  ( name='DeriveOption',            default=True )
    m_LearnOption            : bpy.props.BoolProperty  ( name='LearnOption',             default=True )
    m_TestOption             : bpy.props.BoolProperty  ( name='TestOption',              default=False )
    m_KValuesArrayName       : bpy.props.StringProperty( name='KValuesArrayName',        default="K" )
    m_DefaultNumberOfClusters: bpy.props.IntProperty   ( name='DefaultNumberOfClusters', default=3 )
    m_MaxNumIterations       : bpy.props.IntProperty   ( name='MaxNumIterations',        default=50 )
    m_NumberOfPrimaryTables  : bpy.props.IntProperty   ( name='NumberOfPrimaryTables',   default=1 )
    m_Tolerance              : bpy.props.FloatProperty ( name='Tolerance',               default=0.01 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_KValuesArrayName','m_DefaultNumberOfClusters','m_MaxNumIterations','m_NumberOfPrimaryTables','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], ['DistanceFunctor'], []) 
    
add_class( VTKKMeansStatistics )        
TYPENAMES.append('VTKKMeansStatisticsType' )

#--------------------------------------------------------------
class VTKLagrangianParticleTracker(Node, BVTK_Node):

    bl_idname = 'VTKLagrangianParticleTrackerType'
    bl_label  = 'vtkLagrangianParticleTracker'
    
    m_AdaptiveStepReintegration            : bpy.props.BoolProperty ( name='AdaptiveStepReintegration',             default=False )
    m_CreateOutOfDomainParticle            : bpy.props.BoolProperty ( name='CreateOutOfDomainParticle',             default=False )
    m_UseParticlePathsRenderingThreshold   : bpy.props.BoolProperty ( name='UseParticlePathsRenderingThreshold',    default=False )
    m_CellLengthComputationMode            : bpy.props.IntProperty  ( name='CellLengthComputationMode',             default=0 )
    m_MaximumNumberOfSteps                 : bpy.props.IntProperty  ( name='MaximumNumberOfSteps',                  default=100 )
    m_ParticlePathsRenderingPointsThreshold: bpy.props.IntProperty  ( name='ParticlePathsRenderingPointsThreshold', default=100 )
    m_StepFactor                           : bpy.props.FloatProperty( name='StepFactor',                            default=1.0 )
    m_StepFactorMax                        : bpy.props.FloatProperty( name='StepFactorMax',                         default=1.5 )
    m_StepFactorMin                        : bpy.props.FloatProperty( name='StepFactorMin',                         default=0.5 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AdaptiveStepReintegration','m_CreateOutOfDomainParticle','m_UseParticlePathsRenderingThreshold','m_CellLengthComputationMode','m_MaximumNumberOfSteps','m_ParticlePathsRenderingPointsThreshold','m_StepFactor','m_StepFactorMax','m_StepFactorMin',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1'], ['IntegrationModel', 'Integrator'], []) 
    
add_class( VTKLagrangianParticleTracker )        
TYPENAMES.append('VTKLagrangianParticleTrackerType' )

#--------------------------------------------------------------
class VTKLoopBooleanPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKLoopBooleanPolyDataFilterType'
    bl_label  = 'vtkLoopBooleanPolyDataFilter'
    e_Operation_items=[ (x,x,x) for x in ['Union', 'Intersection', 'Difference']]
    
    m_NoIntersectionOutput: bpy.props.BoolProperty ( name='NoIntersectionOutput', default=True )
    m_Tolerance           : bpy.props.FloatProperty( name='Tolerance',            default=1e-06 )
    e_Operation           : bpy.props.EnumProperty ( name='Operation',            default="Union", items=e_Operation_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NoIntersectionOutput','m_Tolerance','e_Operation',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKLoopBooleanPolyDataFilter )        
TYPENAMES.append('VTKLoopBooleanPolyDataFilterType' )

#--------------------------------------------------------------
class VTKMaskPointsFilter(Node, BVTK_Node):

    bl_idname = 'VTKMaskPointsFilterType'
    bl_label  = 'vtkMaskPointsFilter'
    
    m_GenerateOutliers: bpy.props.BoolProperty( name='GenerateOutliers', default=False )
    m_GenerateVertices: bpy.props.BoolProperty( name='GenerateVertices', default=False )
    m_EmptyValue      : bpy.props.IntProperty ( name='EmptyValue',       default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateOutliers','m_GenerateVertices','m_EmptyValue',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKMaskPointsFilter )        
TYPENAMES.append('VTKMaskPointsFilterType' )

#--------------------------------------------------------------
class VTKMergeFilter(Node, BVTK_Node):

    bl_idname = 'VTKMergeFilterType'
    bl_label  = 'vtkMergeFilter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2', 'input 3', 'input 4', 'input 5'], ['output'], [], []) 
    
add_class( VTKMergeFilter )        
TYPENAMES.append('VTKMergeFilterType' )

#--------------------------------------------------------------
class VTKMultiCorrelativeStatistics(Node, BVTK_Node):

    bl_idname = 'VTKMultiCorrelativeStatisticsType'
    bl_label  = 'vtkMultiCorrelativeStatistics'
    
    m_AssessOption           : bpy.props.BoolProperty( name='AssessOption',            default=False )
    m_DeriveOption           : bpy.props.BoolProperty( name='DeriveOption',            default=True )
    m_LearnOption            : bpy.props.BoolProperty( name='LearnOption',             default=True )
    m_MedianAbsoluteDeviation: bpy.props.BoolProperty( name='MedianAbsoluteDeviation', default=False )
    m_TestOption             : bpy.props.BoolProperty( name='TestOption',              default=False )
    m_NumberOfPrimaryTables  : bpy.props.IntProperty ( name='NumberOfPrimaryTables',   default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_MedianAbsoluteDeviation','m_TestOption','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKMultiCorrelativeStatistics )        
TYPENAMES.append('VTKMultiCorrelativeStatisticsType' )

#--------------------------------------------------------------
class VTKOrderStatistics(Node, BVTK_Node):

    bl_idname = 'VTKOrderStatisticsType'
    bl_label  = 'vtkOrderStatistics'
    
    m_AssessOption         : bpy.props.BoolProperty( name='AssessOption',          default=False )
    m_DeriveOption         : bpy.props.BoolProperty( name='DeriveOption',          default=True )
    m_LearnOption          : bpy.props.BoolProperty( name='LearnOption',           default=True )
    m_Quantize             : bpy.props.BoolProperty( name='Quantize',              default=False )
    m_TestOption           : bpy.props.BoolProperty( name='TestOption',            default=False )
    m_MaximumHistogramSize : bpy.props.IntProperty ( name='MaximumHistogramSize',  default=1000 )
    m_NumberOfIntervals    : bpy.props.IntProperty ( name='NumberOfIntervals',     default=4 )
    m_NumberOfPrimaryTables: bpy.props.IntProperty ( name='NumberOfPrimaryTables', default=-1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_Quantize','m_TestOption','m_MaximumHistogramSize','m_NumberOfIntervals','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKOrderStatistics )        
TYPENAMES.append('VTKOrderStatisticsType' )

#--------------------------------------------------------------
class VTKPCAStatistics(Node, BVTK_Node):

    bl_idname = 'VTKPCAStatisticsType'
    bl_label  = 'vtkPCAStatistics'
    
    m_AssessOption           : bpy.props.BoolProperty ( name='AssessOption',            default=False )
    m_DeriveOption           : bpy.props.BoolProperty ( name='DeriveOption',            default=True )
    m_LearnOption            : bpy.props.BoolProperty ( name='LearnOption',             default=True )
    m_MedianAbsoluteDeviation: bpy.props.BoolProperty ( name='MedianAbsoluteDeviation', default=False )
    m_TestOption             : bpy.props.BoolProperty ( name='TestOption',              default=False )
    m_BasisScheme            : bpy.props.IntProperty  ( name='BasisScheme',             default=0 )
    m_FixedBasisSize         : bpy.props.IntProperty  ( name='FixedBasisSize',          default=-1 )
    m_NormalizationScheme    : bpy.props.IntProperty  ( name='NormalizationScheme',     default=0 )
    m_NumberOfPrimaryTables  : bpy.props.IntProperty  ( name='NumberOfPrimaryTables',   default=1 )
    m_FixedBasisEnergy       : bpy.props.FloatProperty( name='FixedBasisEnergy',        default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_MedianAbsoluteDeviation','m_TestOption','m_BasisScheme','m_FixedBasisSize','m_NormalizationScheme','m_NumberOfPrimaryTables','m_FixedBasisEnergy',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2', 'input 3'], ['output 0', 'output 1', 'output 2'], ['SpecifiedNormalization'], []) 
    
add_class( VTKPCAStatistics )        
TYPENAMES.append('VTKPCAStatisticsType' )

#--------------------------------------------------------------
class VTKPComputeHistogram2DOutliers(Node, BVTK_Node):

    bl_idname = 'VTKPComputeHistogram2DOutliersType'
    bl_label  = 'vtkPComputeHistogram2DOutliers'
    
    m_PreferredNumberOfOutliers: bpy.props.IntProperty( name='PreferredNumberOfOutliers', default=10 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PreferredNumberOfOutliers',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKPComputeHistogram2DOutliers )        
TYPENAMES.append('VTKPComputeHistogram2DOutliersType' )

#--------------------------------------------------------------
class VTKPExtractHistogram2D(Node, BVTK_Node):

    bl_idname = 'VTKPExtractHistogram2DType'
    bl_label  = 'vtkPExtractHistogram2D'
    e_ScalarType_items=[ (x,x,x) for x in ['UnsignedChar', 'UnsignedShort', 'UnsignedInt', 'UnsignedLong', 'Float', 'Double']]
    
    m_AssessOption             : bpy.props.BoolProperty       ( name='AssessOption',              default=False )
    m_DeriveOption             : bpy.props.BoolProperty       ( name='DeriveOption',              default=True )
    m_LearnOption              : bpy.props.BoolProperty       ( name='LearnOption',               default=True )
    m_SwapColumns              : bpy.props.BoolProperty       ( name='SwapColumns',               default=True )
    m_TestOption               : bpy.props.BoolProperty       ( name='TestOption',                default=False )
    m_UseCustomHistogramExtents: bpy.props.BoolProperty       ( name='UseCustomHistogramExtents', default=True )
    m_NumberOfPrimaryTables    : bpy.props.IntProperty        ( name='NumberOfPrimaryTables',     default=1 )
    e_ScalarType               : bpy.props.EnumProperty       ( name='ScalarType',                default="UnsignedInt", items=e_ScalarType_items )
    m_ComponentsToProcess      : bpy.props.IntVectorProperty  ( name='ComponentsToProcess',       default=[0, 0], size=2 )
    m_NumberOfBins             : bpy.props.IntVectorProperty  ( name='NumberOfBins',              default=[0, 0], size=2 )
    m_CustomHistogramExtents   : bpy.props.FloatVectorProperty( name='CustomHistogramExtents',    default=[0.0, 0.0, 0.0, 0.0], size=4 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_SwapColumns','m_TestOption','m_UseCustomHistogramExtents','m_NumberOfPrimaryTables','e_ScalarType','m_ComponentsToProcess','m_NumberOfBins','m_CustomHistogramExtents',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2', 'output 3'], ['RowMask'], []) 
    
add_class( VTKPExtractHistogram2D )        
TYPENAMES.append('VTKPExtractHistogram2DType' )

#--------------------------------------------------------------
class VTKPPairwiseExtractHistogram2D(Node, BVTK_Node):

    bl_idname = 'VTKPPairwiseExtractHistogram2DType'
    bl_label  = 'vtkPPairwiseExtractHistogram2D'
    e_ScalarType_items=[ (x,x,x) for x in ['UnsignedChar', 'UnsignedShort', 'UnsignedInt', 'UnsignedLong']]
    
    m_AssessOption         : bpy.props.BoolProperty     ( name='AssessOption',          default=False )
    m_DeriveOption         : bpy.props.BoolProperty     ( name='DeriveOption',          default=True )
    m_LearnOption          : bpy.props.BoolProperty     ( name='LearnOption',           default=True )
    m_TestOption           : bpy.props.BoolProperty     ( name='TestOption',            default=False )
    m_NumberOfPrimaryTables: bpy.props.IntProperty      ( name='NumberOfPrimaryTables', default=1 )
    e_ScalarType           : bpy.props.EnumProperty     ( name='ScalarType',            default="UnsignedInt", items=e_ScalarType_items )
    m_NumberOfBins         : bpy.props.IntVectorProperty( name='NumberOfBins',          default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_NumberOfPrimaryTables','e_ScalarType','m_NumberOfBins',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2', 'output 3'], [], []) 
    
add_class( VTKPPairwiseExtractHistogram2D )        
TYPENAMES.append('VTKPPairwiseExtractHistogram2DType' )

#--------------------------------------------------------------
class VTKPairwiseExtractHistogram2D(Node, BVTK_Node):

    bl_idname = 'VTKPairwiseExtractHistogram2DType'
    bl_label  = 'vtkPairwiseExtractHistogram2D'
    e_ScalarType_items=[ (x,x,x) for x in ['UnsignedChar', 'UnsignedShort', 'UnsignedInt', 'UnsignedLong']]
    
    m_AssessOption         : bpy.props.BoolProperty     ( name='AssessOption',          default=False )
    m_DeriveOption         : bpy.props.BoolProperty     ( name='DeriveOption',          default=True )
    m_LearnOption          : bpy.props.BoolProperty     ( name='LearnOption',           default=True )
    m_TestOption           : bpy.props.BoolProperty     ( name='TestOption',            default=False )
    m_NumberOfPrimaryTables: bpy.props.IntProperty      ( name='NumberOfPrimaryTables', default=1 )
    e_ScalarType           : bpy.props.EnumProperty     ( name='ScalarType',            default="UnsignedInt", items=e_ScalarType_items )
    m_NumberOfBins         : bpy.props.IntVectorProperty( name='NumberOfBins',          default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_NumberOfPrimaryTables','e_ScalarType','m_NumberOfBins',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2', 'output 3'], [], []) 
    
add_class( VTKPairwiseExtractHistogram2D )        
TYPENAMES.append('VTKPairwiseExtractHistogram2DType' )

#--------------------------------------------------------------
class VTKProgrammableSource(Node, BVTK_Node):

    bl_idname = 'VTKProgrammableSourceType'
    bl_label  = 'vtkProgrammableSource'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], ['output 0', 'output 1', 'output 2', 'output 3', 'output 4'], [], []) 
    
add_class( VTKProgrammableSource )        
TYPENAMES.append('VTKProgrammableSourceType' )

#--------------------------------------------------------------
class VTKRadiusOutlierRemoval(Node, BVTK_Node):

    bl_idname = 'VTKRadiusOutlierRemovalType'
    bl_label  = 'vtkRadiusOutlierRemoval'
    
    m_GenerateOutliers : bpy.props.BoolProperty ( name='GenerateOutliers',  default=False )
    m_GenerateVertices : bpy.props.BoolProperty ( name='GenerateVertices',  default=False )
    m_NumberOfNeighbors: bpy.props.IntProperty  ( name='NumberOfNeighbors', default=2 )
    m_Radius           : bpy.props.FloatProperty( name='Radius',            default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateOutliers','m_GenerateVertices','m_NumberOfNeighbors','m_Radius',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKRadiusOutlierRemoval )        
TYPENAMES.append('VTKRadiusOutlierRemovalType' )

#--------------------------------------------------------------
class VTKResliceCursorPolyDataAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKResliceCursorPolyDataAlgorithmType'
    bl_label  = 'vtkResliceCursorPolyDataAlgorithm'
    e_ReslicePlaneNormal_items=[ (x,x,x) for x in ['XAxis', 'YAxis', 'ZAxis']]
    
    e_ReslicePlaneNormal: bpy.props.EnumProperty       ( name='ReslicePlaneNormal', default="XAxis", items=e_ReslicePlaneNormal_items )
    m_SliceBounds       : bpy.props.FloatVectorProperty( name='SliceBounds',        default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['e_ReslicePlaneNormal','m_SliceBounds',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1', 'output 2', 'output 3'], ['ResliceCursor'], []) 
    
add_class( VTKResliceCursorPolyDataAlgorithm )        
TYPENAMES.append('VTKResliceCursorPolyDataAlgorithmType' )

#--------------------------------------------------------------
class VTKSelectPolyData(Node, BVTK_Node):

    bl_idname = 'VTKSelectPolyDataType'
    bl_label  = 'vtkSelectPolyData'
    e_SelectionMode_items=[ (x,x,x) for x in ['SmallestRegion', 'LargestRegion', 'ClosestPointRegion']]
    
    m_GenerateSelectionScalars: bpy.props.BoolProperty       ( name='GenerateSelectionScalars', default=True )
    m_GenerateUnselectedOutput: bpy.props.BoolProperty       ( name='GenerateUnselectedOutput', default=True )
    m_InsideOut               : bpy.props.BoolProperty       ( name='InsideOut',                default=True )
    e_SelectionMode           : bpy.props.EnumProperty       ( name='SelectionMode',            default="SmallestRegion", items=e_SelectionMode_items )
    m_ClosestPoint            : bpy.props.FloatVectorProperty( name='ClosestPoint',             default=[0.0, 0.0, 0.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateSelectionScalars','m_GenerateUnselectedOutput','m_InsideOut','e_SelectionMode','m_ClosestPoint',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1', 'output 2'], ['Loop'], []) 
    
add_class( VTKSelectPolyData )        
TYPENAMES.append('VTKSelectPolyDataType' )

#--------------------------------------------------------------
class VTKStatisticalOutlierRemoval(Node, BVTK_Node):

    bl_idname = 'VTKStatisticalOutlierRemovalType'
    bl_label  = 'vtkStatisticalOutlierRemoval'
    
    m_GenerateOutliers         : bpy.props.BoolProperty ( name='GenerateOutliers',          default=False )
    m_GenerateVertices         : bpy.props.BoolProperty ( name='GenerateVertices',          default=False )
    m_SampleSize               : bpy.props.IntProperty  ( name='SampleSize',                default=25 )
    m_ComputedMean             : bpy.props.FloatProperty( name='ComputedMean',              default=0.0 )
    m_ComputedStandardDeviation: bpy.props.FloatProperty( name='ComputedStandardDeviation', default=0.0 )
    m_StandardDeviationFactor  : bpy.props.FloatProperty( name='StandardDeviationFactor',   default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateOutliers','m_GenerateVertices','m_SampleSize','m_ComputedMean','m_ComputedStandardDeviation','m_StandardDeviationFactor',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKStatisticalOutlierRemoval )        
TYPENAMES.append('VTKStatisticalOutlierRemovalType' )

#--------------------------------------------------------------
class VTKStreamingStatistics(Node, BVTK_Node):

    bl_idname = 'VTKStreamingStatisticsType'
    bl_label  = 'vtkStreamingStatistics'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKStreamingStatistics )        
TYPENAMES.append('VTKStreamingStatisticsType' )

#--------------------------------------------------------------
class VTKTableBasedClipDataSet(Node, BVTK_Node):

    bl_idname = 'VTKTableBasedClipDataSetType'
    bl_label  = 'vtkTableBasedClipDataSet'
    
    m_GenerateClipScalars  : bpy.props.BoolProperty ( name='GenerateClipScalars',   default=True )
    m_GenerateClippedOutput: bpy.props.BoolProperty ( name='GenerateClippedOutput', default=True )
    m_InsideOut            : bpy.props.BoolProperty ( name='InsideOut',             default=True )
    m_UseValueAsOffset     : bpy.props.BoolProperty ( name='UseValueAsOffset',      default=True )
    m_MergeTolerance       : bpy.props.FloatProperty( name='MergeTolerance',        default=0.01 )
    m_Value                : bpy.props.FloatProperty( name='Value',                 default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateClipScalars','m_GenerateClippedOutput','m_InsideOut','m_UseValueAsOffset','m_MergeTolerance','m_Value',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ClipFunction'], []) 
    
add_class( VTKTableBasedClipDataSet )        
TYPENAMES.append('VTKTableBasedClipDataSetType' )

#--------------------------------------------------------------
class VTKTemporalPathLineFilter(Node, BVTK_Node):

    bl_idname = 'VTKTemporalPathLineFilterType'
    bl_label  = 'vtkTemporalPathLineFilter'
    
    m_IdChannelArray : bpy.props.StringProperty     ( name='IdChannelArray',  default="" )
    m_KeepDeadTrails : bpy.props.IntProperty        ( name='KeepDeadTrails',  default=0 )
    m_MaskPoints     : bpy.props.IntProperty        ( name='MaskPoints',      default=200 )
    m_MaxTrackLength : bpy.props.IntProperty        ( name='MaxTrackLength',  default=10 )
    m_MaxStepDistance: bpy.props.FloatVectorProperty( name='MaxStepDistance', default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_IdChannelArray','m_KeepDeadTrails','m_MaskPoints','m_MaxTrackLength','m_MaxStepDistance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKTemporalPathLineFilter )        
TYPENAMES.append('VTKTemporalPathLineFilterType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( BVTK_NodeCategory( 'Filter', 'Filter', items=menu_items) )