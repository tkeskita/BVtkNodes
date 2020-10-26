# Generated definitions for VTK class group: Reader
# VTK Version: 8.1.2

from ..core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKAMREnzoParticlesReader(Node, BVTK_Node):

    bl_idname = 'VTKAMREnzoParticlesReaderType'
    bl_label  = 'vtkAMREnzoParticlesReader'
    
    m_FilterLocation: bpy.props.BoolProperty  ( name='FilterLocation', default=True )
    m_FileName      : bpy.props.StringProperty( name='FileName',       default="", subtype='FILE_PATH' )
    m_Frequency     : bpy.props.IntProperty   ( name='Frequency',      default=1 )
    m_ParticleType  : bpy.props.IntProperty   ( name='ParticleType',   default=-1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FilterLocation','m_FileName','m_Frequency','m_ParticleType',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKAMREnzoParticlesReader )        
TYPENAMES.append('VTKAMREnzoParticlesReaderType' )

#--------------------------------------------------------------
class VTKAMREnzoReader(Node, BVTK_Node):

    bl_idname = 'VTKAMREnzoReaderType'
    bl_label  = 'vtkAMREnzoReader'
    
    m_ConvertToCGS : bpy.props.BoolProperty  ( name='ConvertToCGS',  default=True )
    m_EnableCaching: bpy.props.BoolProperty  ( name='EnableCaching', default=True )
    m_FileName     : bpy.props.StringProperty( name='FileName',      default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ConvertToCGS','m_EnableCaching','m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKAMREnzoReader )        
TYPENAMES.append('VTKAMREnzoReaderType' )

#--------------------------------------------------------------
class VTKAMRFlashParticlesReader(Node, BVTK_Node):

    bl_idname = 'VTKAMRFlashParticlesReaderType'
    bl_label  = 'vtkAMRFlashParticlesReader'
    
    m_FilterLocation: bpy.props.BoolProperty  ( name='FilterLocation', default=True )
    m_FileName      : bpy.props.StringProperty( name='FileName',       default="", subtype='FILE_PATH' )
    m_Frequency     : bpy.props.IntProperty   ( name='Frequency',      default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FilterLocation','m_FileName','m_Frequency',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKAMRFlashParticlesReader )        
TYPENAMES.append('VTKAMRFlashParticlesReaderType' )

#--------------------------------------------------------------
class VTKAMRFlashReader(Node, BVTK_Node):

    bl_idname = 'VTKAMRFlashReaderType'
    bl_label  = 'vtkAMRFlashReader'
    
    m_EnableCaching: bpy.props.BoolProperty  ( name='EnableCaching', default=True )
    m_FileName     : bpy.props.StringProperty( name='FileName',      default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableCaching','m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKAMRFlashReader )        
TYPENAMES.append('VTKAMRFlashReaderType' )

#--------------------------------------------------------------
class VTKAVSucdReader(Node, BVTK_Node):

    bl_idname = 'VTKAVSucdReaderType'
    bl_label  = 'vtkAVSucdReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_BinaryFile: bpy.props.BoolProperty  ( name='BinaryFile', default=True )
    m_FileName  : bpy.props.StringProperty( name='FileName',   default="", subtype='FILE_PATH' )
    e_ByteOrder : bpy.props.EnumProperty  ( name='ByteOrder',  default="BigEndian", items=e_ByteOrder_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_BinaryFile','m_FileName','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKAVSucdReader )        
TYPENAMES.append('VTKAVSucdReaderType' )

#--------------------------------------------------------------
class VTKArrayDataReader(Node, BVTK_Node):

    bl_idname = 'VTKArrayDataReaderType'
    bl_label  = 'vtkArrayDataReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_InputString        : bpy.props.StringProperty( name='InputString',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_InputString',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKArrayDataReader )        
TYPENAMES.append('VTKArrayDataReaderType' )

#--------------------------------------------------------------
class VTKArrayReader(Node, BVTK_Node):

    bl_idname = 'VTKArrayReaderType'
    bl_label  = 'vtkArrayReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_InputString        : bpy.props.StringProperty( name='InputString',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_InputString',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKArrayReader )        
TYPENAMES.append('VTKArrayReaderType' )

#--------------------------------------------------------------
class VTKBMPReader(Node, BVTK_Node):

    bl_idname = 'VTKBMPReaderType'
    bl_label  = 'vtkBMPReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_Allow8BitBMP            : bpy.props.BoolProperty       ( name='Allow8BitBMP',             default=True )
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_ScalarArrayName         : bpy.props.StringProperty     ( name='ScalarArrayName',          default="ImageFile" )
    m_DataMask                : bpy.props.IntProperty        ( name='DataMask',                 default=1000000000 )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataVOI                 : bpy.props.IntVectorProperty  ( name='DataVOI',                  default=[0, 0, 0, 0, 0, 0], size=6 )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=19, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Allow8BitBMP','m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ScalarArrayName','m_DataMask','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataVOI','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['Transform'], []) 
    
add_class( VTKBMPReader )        
TYPENAMES.append('VTKBMPReaderType' )

#--------------------------------------------------------------
class VTKBYUReader(Node, BVTK_Node):

    bl_idname = 'VTKBYUReaderType'
    bl_label  = 'vtkBYUReader'
    
    m_ReadDisplacement    : bpy.props.BoolProperty  ( name='ReadDisplacement',     default=True )
    m_ReadScalar          : bpy.props.BoolProperty  ( name='ReadScalar',           default=True )
    m_ReadTexture         : bpy.props.BoolProperty  ( name='ReadTexture',          default=True )
    m_DisplacementFileName: bpy.props.StringProperty( name='DisplacementFileName', default="", subtype='FILE_PATH' )
    m_FileName            : bpy.props.StringProperty( name='FileName',             default="", subtype='FILE_PATH' )
    m_GeometryFileName    : bpy.props.StringProperty( name='GeometryFileName',     default="", subtype='FILE_PATH' )
    m_ScalarFileName      : bpy.props.StringProperty( name='ScalarFileName',       default="", subtype='FILE_PATH' )
    m_TextureFileName     : bpy.props.StringProperty( name='TextureFileName',      default="", subtype='FILE_PATH' )
    m_PartNumber          : bpy.props.IntProperty   ( name='PartNumber',           default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadDisplacement','m_ReadScalar','m_ReadTexture','m_DisplacementFileName','m_FileName','m_GeometryFileName','m_ScalarFileName','m_TextureFileName','m_PartNumber',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKBYUReader )        
TYPENAMES.append('VTKBYUReaderType' )

#--------------------------------------------------------------
class VTKBiomTableReader(Node, BVTK_Node):

    bl_idname = 'VTKBiomTableReaderType'
    bl_label  = 'vtkBiomTableReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKBiomTableReader )        
TYPENAMES.append('VTKBiomTableReaderType' )

#--------------------------------------------------------------
class VTKCMLMoleculeReader(Node, BVTK_Node):

    bl_idname = 'VTKCMLMoleculeReaderType'
    bl_label  = 'vtkCMLMoleculeReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKCMLMoleculeReader )        
TYPENAMES.append('VTKCMLMoleculeReaderType' )

#--------------------------------------------------------------
class VTKCPExodusIIInSituReader(Node, BVTK_Node):

    bl_idname = 'VTKCPExodusIIInSituReaderType'
    bl_label  = 'vtkCPExodusIIInSituReader'
    
    m_FileName       : bpy.props.StringProperty( name='FileName',        default="", subtype='FILE_PATH' )
    m_CurrentTimeStep: bpy.props.IntProperty   ( name='CurrentTimeStep', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','m_CurrentTimeStep',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKCPExodusIIInSituReader )        
TYPENAMES.append('VTKCPExodusIIInSituReaderType' )

#--------------------------------------------------------------
class VTKChacoGraphReader(Node, BVTK_Node):

    bl_idname = 'VTKChacoGraphReaderType'
    bl_label  = 'vtkChacoGraphReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKChacoGraphReader )        
TYPENAMES.append('VTKChacoGraphReaderType' )

#--------------------------------------------------------------
class VTKChacoReader(Node, BVTK_Node):

    bl_idname = 'VTKChacoReaderType'
    bl_label  = 'vtkChacoReader'
    
    m_GenerateEdgeWeightArrays    : bpy.props.BoolProperty  ( name='GenerateEdgeWeightArrays',     default=True )
    m_GenerateGlobalElementIdArray: bpy.props.BoolProperty  ( name='GenerateGlobalElementIdArray', default=True )
    m_GenerateGlobalNodeIdArray   : bpy.props.BoolProperty  ( name='GenerateGlobalNodeIdArray',    default=True )
    m_GenerateVertexWeightArrays  : bpy.props.BoolProperty  ( name='GenerateVertexWeightArrays',   default=True )
    m_BaseName                    : bpy.props.StringProperty( name='BaseName',                     default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateEdgeWeightArrays','m_GenerateGlobalElementIdArray','m_GenerateGlobalNodeIdArray','m_GenerateVertexWeightArrays','m_BaseName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKChacoReader )        
TYPENAMES.append('VTKChacoReaderType' )

#--------------------------------------------------------------
class VTKCompositeDataReader(Node, BVTK_Node):

    bl_idname = 'VTKCompositeDataReaderType'
    bl_label  = 'vtkCompositeDataReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKCompositeDataReader )        
TYPENAMES.append('VTKCompositeDataReaderType' )

#--------------------------------------------------------------
class VTKDEMReader(Node, BVTK_Node):

    bl_idname = 'VTKDEMReaderType'
    bl_label  = 'vtkDEMReader'
    e_ElevationReference_items=[ (x,x,x) for x in ['SeaLevel', 'ElevationBounds']]
    
    m_FileName          : bpy.props.StringProperty( name='FileName',           default="", subtype='FILE_PATH' )
    e_ElevationReference: bpy.props.EnumProperty  ( name='ElevationReference', default="ElevationBounds", items=e_ElevationReference_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','e_ElevationReference',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKDEMReader )        
TYPENAMES.append('VTKDEMReaderType' )

#--------------------------------------------------------------
class VTKDICOMImageReader(Node, BVTK_Node):

    bl_idname = 'VTKDICOMImageReaderType'
    bl_label  = 'vtkDICOMImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_DirectoryName           : bpy.props.StringProperty     ( name='DirectoryName',            default="" )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_DirectoryName','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKDICOMImageReader )        
TYPENAMES.append('VTKDICOMImageReaderType' )

#--------------------------------------------------------------
class VTKDIMACSGraphReader(Node, BVTK_Node):

    bl_idname = 'VTKDIMACSGraphReaderType'
    bl_label  = 'vtkDIMACSGraphReader'
    
    m_EdgeAttributeArrayName  : bpy.props.StringProperty( name='EdgeAttributeArrayName',   default="" )
    m_FileName                : bpy.props.StringProperty( name='FileName',                 default="", subtype='FILE_PATH' )
    m_VertexAttributeArrayName: bpy.props.StringProperty( name='VertexAttributeArrayName', default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EdgeAttributeArrayName','m_FileName','m_VertexAttributeArrayName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKDIMACSGraphReader )        
TYPENAMES.append('VTKDIMACSGraphReaderType' )

#--------------------------------------------------------------
class VTKDataObjectReader(Node, BVTK_Node):

    bl_idname = 'VTKDataObjectReaderType'
    bl_label  = 'vtkDataObjectReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKDataObjectReader )        
TYPENAMES.append('VTKDataObjectReaderType' )

#--------------------------------------------------------------
class VTKDataReader(Node, BVTK_Node):

    bl_idname = 'VTKDataReaderType'
    bl_label  = 'vtkDataReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKDataReader )        
TYPENAMES.append('VTKDataReaderType' )

#--------------------------------------------------------------
class VTKDataSetReader(Node, BVTK_Node):

    bl_idname = 'VTKDataSetReaderType'
    bl_label  = 'vtkDataSetReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKDataSetReader )        
TYPENAMES.append('VTKDataSetReaderType' )

#--------------------------------------------------------------
class VTKDelimitedTextReader(Node, BVTK_Node):

    bl_idname = 'VTKDelimitedTextReaderType'
    bl_label  = 'vtkDelimitedTextReader'
    
    m_AddTabFieldDelimiter                  : bpy.props.BoolProperty  ( name='AddTabFieldDelimiter',                   default=False )
    m_DetectNumericColumns                  : bpy.props.BoolProperty  ( name='DetectNumericColumns',                   default=False )
    m_ForceDouble                           : bpy.props.BoolProperty  ( name='ForceDouble',                            default=False )
    m_GeneratePedigreeIds                   : bpy.props.BoolProperty  ( name='GeneratePedigreeIds',                    default=True )
    m_HaveHeaders                           : bpy.props.BoolProperty  ( name='HaveHeaders',                            default=False )
    m_MergeConsecutiveDelimiters            : bpy.props.BoolProperty  ( name='MergeConsecutiveDelimiters',             default=False )
    m_OutputPedigreeIds                     : bpy.props.BoolProperty  ( name='OutputPedigreeIds',                      default=False )
    m_ReadFromInputString                   : bpy.props.BoolProperty  ( name='ReadFromInputString',                    default=False )
    m_TrimWhitespacePriorToNumericConversion: bpy.props.BoolProperty  ( name='TrimWhitespacePriorToNumericConversion', default=False )
    m_UseStringDelimiter                    : bpy.props.BoolProperty  ( name='UseStringDelimiter',                     default=True )
    m_FieldDelimiterCharacters              : bpy.props.StringProperty( name='FieldDelimiterCharacters',               default="," )
    m_FileName                              : bpy.props.StringProperty( name='FileName',                               default="", subtype='FILE_PATH' )
    m_PedigreeIdArrayName                   : bpy.props.StringProperty( name='PedigreeIdArrayName',                    default="id" )
    m_UTF8FieldDelimiters                   : bpy.props.StringProperty( name='UTF8FieldDelimiters',                    default="," )
    m_UTF8RecordDelimiters                  : bpy.props.StringProperty( name='UTF8RecordDelimiters',                   default="\n" )
    m_UTF8StringDelimiters                  : bpy.props.StringProperty( name='UTF8StringDelimiters',                   default="" )
    m_UnicodeCharacterSet                   : bpy.props.StringProperty( name='UnicodeCharacterSet',                    default="" )
    m_DefaultIntegerValue                   : bpy.props.IntProperty   ( name='DefaultIntegerValue',                    default=0 )
    m_MaxRecords                            : bpy.props.IntProperty   ( name='MaxRecords',                             default=0 )
    m_ReplacementCharacter                  : bpy.props.IntProperty   ( name='ReplacementCharacter',                   default=120 )
    m_DefaultDoubleValue                    : bpy.props.FloatProperty ( name='DefaultDoubleValue',                     default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=21, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AddTabFieldDelimiter','m_DetectNumericColumns','m_ForceDouble','m_GeneratePedigreeIds','m_HaveHeaders','m_MergeConsecutiveDelimiters','m_OutputPedigreeIds','m_ReadFromInputString','m_TrimWhitespacePriorToNumericConversion','m_UseStringDelimiter','m_FieldDelimiterCharacters','m_FileName','m_PedigreeIdArrayName','m_UTF8FieldDelimiters','m_UTF8RecordDelimiters','m_UTF8StringDelimiters','m_UnicodeCharacterSet','m_DefaultIntegerValue','m_MaxRecords','m_ReplacementCharacter','m_DefaultDoubleValue',]
    def m_connections( self ):
        return ([], ['output'], ['StringDelimiter', 'UnicodeFieldDelimiters', 'UnicodeRecordDelimiters', 'UnicodeStringDelimiters'], []) 
    
add_class( VTKDelimitedTextReader )        
TYPENAMES.append('VTKDelimitedTextReaderType' )

#--------------------------------------------------------------
class VTKEnSight6BinaryReader(Node, BVTK_Node):

    bl_idname = 'VTKEnSight6BinaryReaderType'
    bl_label  = 'vtkEnSight6BinaryReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_ParticleCoordinatesByIndex: bpy.props.BoolProperty  ( name='ParticleCoordinatesByIndex', default=True )
    m_ReadAllVariables          : bpy.props.BoolProperty  ( name='ReadAllVariables',           default=True )
    m_CaseFileName              : bpy.props.StringProperty( name='CaseFileName',               default="", subtype='FILE_PATH' )
    m_FilePath                  : bpy.props.StringProperty( name='FilePath',                   default="" )
    m_TimeValue                 : bpy.props.FloatProperty ( name='TimeValue',                  default=0.0 )
    e_ByteOrder                 : bpy.props.EnumProperty  ( name='ByteOrder',                  default="BigEndian", items=e_ByteOrder_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ParticleCoordinatesByIndex','m_ReadAllVariables','m_CaseFileName','m_FilePath','m_TimeValue','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKEnSight6BinaryReader )        
TYPENAMES.append('VTKEnSight6BinaryReaderType' )

#--------------------------------------------------------------
class VTKEnSight6Reader(Node, BVTK_Node):

    bl_idname = 'VTKEnSight6ReaderType'
    bl_label  = 'vtkEnSight6Reader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_ParticleCoordinatesByIndex: bpy.props.BoolProperty  ( name='ParticleCoordinatesByIndex', default=True )
    m_ReadAllVariables          : bpy.props.BoolProperty  ( name='ReadAllVariables',           default=True )
    m_CaseFileName              : bpy.props.StringProperty( name='CaseFileName',               default="", subtype='FILE_PATH' )
    m_FilePath                  : bpy.props.StringProperty( name='FilePath',                   default="" )
    m_TimeValue                 : bpy.props.FloatProperty ( name='TimeValue',                  default=0.0 )
    e_ByteOrder                 : bpy.props.EnumProperty  ( name='ByteOrder',                  default="BigEndian", items=e_ByteOrder_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ParticleCoordinatesByIndex','m_ReadAllVariables','m_CaseFileName','m_FilePath','m_TimeValue','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKEnSight6Reader )        
TYPENAMES.append('VTKEnSight6ReaderType' )

#--------------------------------------------------------------
class VTKEnSightGoldBinaryReader(Node, BVTK_Node):

    bl_idname = 'VTKEnSightGoldBinaryReaderType'
    bl_label  = 'vtkEnSightGoldBinaryReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_ParticleCoordinatesByIndex: bpy.props.BoolProperty  ( name='ParticleCoordinatesByIndex', default=True )
    m_ReadAllVariables          : bpy.props.BoolProperty  ( name='ReadAllVariables',           default=True )
    m_CaseFileName              : bpy.props.StringProperty( name='CaseFileName',               default="", subtype='FILE_PATH' )
    m_FilePath                  : bpy.props.StringProperty( name='FilePath',                   default="" )
    m_TimeValue                 : bpy.props.FloatProperty ( name='TimeValue',                  default=0.0 )
    e_ByteOrder                 : bpy.props.EnumProperty  ( name='ByteOrder',                  default="BigEndian", items=e_ByteOrder_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ParticleCoordinatesByIndex','m_ReadAllVariables','m_CaseFileName','m_FilePath','m_TimeValue','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKEnSightGoldBinaryReader )        
TYPENAMES.append('VTKEnSightGoldBinaryReaderType' )

#--------------------------------------------------------------
class VTKEnSightGoldReader(Node, BVTK_Node):

    bl_idname = 'VTKEnSightGoldReaderType'
    bl_label  = 'vtkEnSightGoldReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_ParticleCoordinatesByIndex: bpy.props.BoolProperty  ( name='ParticleCoordinatesByIndex', default=True )
    m_ReadAllVariables          : bpy.props.BoolProperty  ( name='ReadAllVariables',           default=True )
    m_CaseFileName              : bpy.props.StringProperty( name='CaseFileName',               default="", subtype='FILE_PATH' )
    m_FilePath                  : bpy.props.StringProperty( name='FilePath',                   default="" )
    m_TimeValue                 : bpy.props.FloatProperty ( name='TimeValue',                  default=0.0 )
    e_ByteOrder                 : bpy.props.EnumProperty  ( name='ByteOrder',                  default="BigEndian", items=e_ByteOrder_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ParticleCoordinatesByIndex','m_ReadAllVariables','m_CaseFileName','m_FilePath','m_TimeValue','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKEnSightGoldReader )        
TYPENAMES.append('VTKEnSightGoldReaderType' )

#--------------------------------------------------------------
class VTKEnSightMasterServerReader(Node, BVTK_Node):

    bl_idname = 'VTKEnSightMasterServerReaderType'
    bl_label  = 'vtkEnSightMasterServerReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_ParticleCoordinatesByIndex: bpy.props.BoolProperty  ( name='ParticleCoordinatesByIndex', default=True )
    m_ReadAllVariables          : bpy.props.BoolProperty  ( name='ReadAllVariables',           default=True )
    m_CaseFileName              : bpy.props.StringProperty( name='CaseFileName',               default="", subtype='FILE_PATH' )
    m_FilePath                  : bpy.props.StringProperty( name='FilePath',                   default="" )
    m_CurrentPiece              : bpy.props.IntProperty   ( name='CurrentPiece',               default=-1 )
    m_TimeValue                 : bpy.props.FloatProperty ( name='TimeValue',                  default=0.0 )
    e_ByteOrder                 : bpy.props.EnumProperty  ( name='ByteOrder',                  default="BigEndian", items=e_ByteOrder_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ParticleCoordinatesByIndex','m_ReadAllVariables','m_CaseFileName','m_FilePath','m_CurrentPiece','m_TimeValue','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKEnSightMasterServerReader )        
TYPENAMES.append('VTKEnSightMasterServerReaderType' )

#--------------------------------------------------------------
class VTKExodusIIReader(Node, BVTK_Node):

    bl_idname = 'VTKExodusIIReaderType'
    bl_label  = 'vtkExodusIIReader'
    
    m_AnimateModeShapes             : bpy.props.BoolProperty  ( name='AnimateModeShapes',              default=True )
    m_ApplyDisplacements            : bpy.props.BoolProperty  ( name='ApplyDisplacements',             default=True )
    m_GenerateFileIdArray           : bpy.props.BoolProperty  ( name='GenerateFileIdArray',            default=True )
    m_GenerateGlobalElementIdArray  : bpy.props.BoolProperty  ( name='GenerateGlobalElementIdArray',   default=True )
    m_GenerateGlobalNodeIdArray     : bpy.props.BoolProperty  ( name='GenerateGlobalNodeIdArray',      default=True )
    m_GenerateImplicitElementIdArray: bpy.props.BoolProperty  ( name='GenerateImplicitElementIdArray', default=True )
    m_GenerateImplicitNodeIdArray   : bpy.props.BoolProperty  ( name='GenerateImplicitNodeIdArray',    default=True )
    m_GenerateObjectIdCellArray     : bpy.props.BoolProperty  ( name='GenerateObjectIdCellArray',      default=True )
    m_HasModeShapes                 : bpy.props.BoolProperty  ( name='HasModeShapes',                  default=True )
    m_SqueezePoints                 : bpy.props.BoolProperty  ( name='SqueezePoints',                  default=True )
    m_FileName                      : bpy.props.StringProperty( name='FileName',                       default="", subtype='FILE_PATH' )
    m_XMLFileName                   : bpy.props.StringProperty( name='XMLFileName',                    default="", subtype='FILE_PATH' )
    m_DisplayType                   : bpy.props.IntProperty   ( name='DisplayType',                    default=0 )
    m_FileId                        : bpy.props.IntProperty   ( name='FileId',                         default=0 )
    m_TimeStep                      : bpy.props.IntProperty   ( name='TimeStep',                       default=0 )
    m_CacheSize                     : bpy.props.FloatProperty ( name='CacheSize',                      default=0.0 )
    m_DisplacementMagnitude         : bpy.props.FloatProperty ( name='DisplacementMagnitude',          default=1.0 )
    m_ModeShapeTime                 : bpy.props.FloatProperty ( name='ModeShapeTime',                  default=-1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AnimateModeShapes','m_ApplyDisplacements','m_GenerateFileIdArray','m_GenerateGlobalElementIdArray','m_GenerateGlobalNodeIdArray','m_GenerateImplicitElementIdArray','m_GenerateImplicitNodeIdArray','m_GenerateObjectIdCellArray','m_HasModeShapes','m_SqueezePoints','m_FileName','m_XMLFileName','m_DisplayType','m_FileId','m_TimeStep','m_CacheSize','m_DisplacementMagnitude','m_ModeShapeTime',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKExodusIIReader )        
TYPENAMES.append('VTKExodusIIReaderType' )

#--------------------------------------------------------------
class VTKFLUENTReader(Node, BVTK_Node):

    bl_idname = 'VTKFLUENTReaderType'
    bl_label  = 'vtkFLUENTReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_FileName     : bpy.props.StringProperty( name='FileName',      default="", subtype='FILE_PATH' )
    e_DataByteOrder: bpy.props.EnumProperty  ( name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','e_DataByteOrder',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKFLUENTReader )        
TYPENAMES.append('VTKFLUENTReaderType' )

#--------------------------------------------------------------
class VTKFacetReader(Node, BVTK_Node):

    bl_idname = 'VTKFacetReaderType'
    bl_label  = 'vtkFacetReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKFacetReader )        
TYPENAMES.append('VTKFacetReaderType' )

#--------------------------------------------------------------
class VTKFixedWidthTextReader(Node, BVTK_Node):

    bl_idname = 'VTKFixedWidthTextReaderType'
    bl_label  = 'vtkFixedWidthTextReader'
    
    m_HaveHeaders    : bpy.props.BoolProperty  ( name='HaveHeaders',     default=False )
    m_StripWhiteSpace: bpy.props.BoolProperty  ( name='StripWhiteSpace', default=False )
    m_FileName       : bpy.props.StringProperty( name='FileName',        default="", subtype='FILE_PATH' )
    m_FieldWidth     : bpy.props.IntProperty   ( name='FieldWidth',      default=10 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_HaveHeaders','m_StripWhiteSpace','m_FileName','m_FieldWidth',]
    def m_connections( self ):
        return ([], ['output'], ['TableErrorObserver'], []) 
    
add_class( VTKFixedWidthTextReader )        
TYPENAMES.append('VTKFixedWidthTextReaderType' )

#--------------------------------------------------------------
class VTKGAMBITReader(Node, BVTK_Node):

    bl_idname = 'VTKGAMBITReaderType'
    bl_label  = 'vtkGAMBITReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKGAMBITReader )        
TYPENAMES.append('VTKGAMBITReaderType' )

#--------------------------------------------------------------
class VTKGESignaReader(Node, BVTK_Node):

    bl_idname = 'VTKGESignaReaderType'
    bl_label  = 'vtkGESignaReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_Date                    : bpy.props.StringProperty     ( name='Date',                     default="" )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_ImageNumber             : bpy.props.StringProperty     ( name='ImageNumber',              default="" )
    m_Modality                : bpy.props.StringProperty     ( name='Modality',                 default="" )
    m_PatientID               : bpy.props.StringProperty     ( name='PatientID',                default="" )
    m_PatientName             : bpy.props.StringProperty     ( name='PatientName',              default="" )
    m_Series                  : bpy.props.StringProperty     ( name='Series',                   default="" )
    m_Study                   : bpy.props.StringProperty     ( name='Study',                    default="" )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=22, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_Date','m_FileName','m_FilePattern','m_FilePrefix','m_ImageNumber','m_Modality','m_PatientID','m_PatientName','m_Series','m_Study','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKGESignaReader )        
TYPENAMES.append('VTKGESignaReaderType' )

#--------------------------------------------------------------
class VTKGaussianCubeReader(Node, BVTK_Node):

    bl_idname = 'VTKGaussianCubeReaderType'
    bl_label  = 'vtkGaussianCubeReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    m_BScale  : bpy.props.FloatProperty ( name='BScale',   default=1.0 )
    m_HBScale : bpy.props.FloatProperty ( name='HBScale',  default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','m_BScale','m_HBScale',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], [], []) 
    
add_class( VTKGaussianCubeReader )        
TYPENAMES.append('VTKGaussianCubeReaderType' )

#--------------------------------------------------------------
class VTKGaussianCubeReader2(Node, BVTK_Node):

    bl_idname = 'VTKGaussianCubeReader2Type'
    bl_label  = 'vtkGaussianCubeReader2'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], [], []) 
    
add_class( VTKGaussianCubeReader2 )        
TYPENAMES.append('VTKGaussianCubeReader2Type' )

#--------------------------------------------------------------
class VTKGenericDataObjectReader(Node, BVTK_Node):

    bl_idname = 'VTKGenericDataObjectReaderType'
    bl_label  = 'vtkGenericDataObjectReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKGenericDataObjectReader )        
TYPENAMES.append('VTKGenericDataObjectReaderType' )

#--------------------------------------------------------------
class VTKGenericEnSightReader(Node, BVTK_Node):

    bl_idname = 'VTKGenericEnSightReaderType'
    bl_label  = 'vtkGenericEnSightReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_ParticleCoordinatesByIndex: bpy.props.BoolProperty  ( name='ParticleCoordinatesByIndex', default=True )
    m_ReadAllVariables          : bpy.props.BoolProperty  ( name='ReadAllVariables',           default=True )
    m_CaseFileName              : bpy.props.StringProperty( name='CaseFileName',               default="", subtype='FILE_PATH' )
    m_FilePath                  : bpy.props.StringProperty( name='FilePath',                   default="" )
    m_TimeValue                 : bpy.props.FloatProperty ( name='TimeValue',                  default=0.0 )
    e_ByteOrder                 : bpy.props.EnumProperty  ( name='ByteOrder',                  default="BigEndian", items=e_ByteOrder_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ParticleCoordinatesByIndex','m_ReadAllVariables','m_CaseFileName','m_FilePath','m_TimeValue','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKGenericEnSightReader )        
TYPENAMES.append('VTKGenericEnSightReaderType' )

#--------------------------------------------------------------
class VTKGraphReader(Node, BVTK_Node):

    bl_idname = 'VTKGraphReaderType'
    bl_label  = 'vtkGraphReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKGraphReader )        
TYPENAMES.append('VTKGraphReaderType' )

#--------------------------------------------------------------
class VTKISIReader(Node, BVTK_Node):

    bl_idname = 'VTKISIReaderType'
    bl_label  = 'vtkISIReader'
    
    m_Delimiter : bpy.props.StringProperty( name='Delimiter',  default=";" )
    m_FileName  : bpy.props.StringProperty( name='FileName',   default="", subtype='FILE_PATH' )
    m_MaxRecords: bpy.props.IntProperty   ( name='MaxRecords', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Delimiter','m_FileName','m_MaxRecords',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKISIReader )        
TYPENAMES.append('VTKISIReaderType' )

#--------------------------------------------------------------
class VTKImageReader(Node, BVTK_Node):

    bl_idname = 'VTKImageReaderType'
    bl_label  = 'vtkImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_ScalarArrayName         : bpy.props.StringProperty     ( name='ScalarArrayName',          default="ImageFile" )
    m_DataMask                : bpy.props.IntProperty        ( name='DataMask',                 default=1000000000 )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataVOI                 : bpy.props.IntVectorProperty  ( name='DataVOI',                  default=[0, 0, 0, 0, 0, 0], size=6 )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ScalarArrayName','m_DataMask','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataVOI','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['Transform'], []) 
    
add_class( VTKImageReader )        
TYPENAMES.append('VTKImageReaderType' )

#--------------------------------------------------------------
class VTKImageReader2(Node, BVTK_Node):

    bl_idname = 'VTKImageReader2Type'
    bl_label  = 'vtkImageReader2'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKImageReader2 )        
TYPENAMES.append('VTKImageReader2Type' )

#--------------------------------------------------------------
class VTKJPEGReader(Node, BVTK_Node):

    bl_idname = 'VTKJPEGReaderType'
    bl_label  = 'vtkJPEGReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKJPEGReader )        
TYPENAMES.append('VTKJPEGReaderType' )

#--------------------------------------------------------------
class VTKLSDynaReader(Node, BVTK_Node):

    bl_idname = 'VTKLSDynaReaderType'
    bl_label  = 'vtkLSDynaReader'
    
    m_DeformedMesh            : bpy.props.BoolProperty     ( name='DeformedMesh',             default=True )
    m_DeletedCellsAsGhostArray: bpy.props.BoolProperty     ( name='DeletedCellsAsGhostArray', default=True )
    m_RemoveDeletedCells      : bpy.props.BoolProperty     ( name='RemoveDeletedCells',       default=True )
    m_DatabaseDirectory       : bpy.props.StringProperty   ( name='DatabaseDirectory',        default="" )
    m_FileName                : bpy.props.StringProperty   ( name='FileName',                 default="/d3plot", subtype='FILE_PATH' )
    m_InputDeck               : bpy.props.StringProperty   ( name='InputDeck',                default="" )
    m_TimeStep                : bpy.props.IntProperty      ( name='TimeStep',                 default=0 )
    m_TimeStepRange           : bpy.props.IntVectorProperty( name='TimeStepRange',            default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_DeformedMesh','m_DeletedCellsAsGhostArray','m_RemoveDeletedCells','m_DatabaseDirectory','m_FileName','m_InputDeck','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKLSDynaReader )        
TYPENAMES.append('VTKLSDynaReaderType' )

#--------------------------------------------------------------
class VTKMCubesReader(Node, BVTK_Node):

    bl_idname = 'VTKMCubesReaderType'
    bl_label  = 'vtkMCubesReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_FlipNormals   : bpy.props.BoolProperty  ( name='FlipNormals',    default=True )
    m_Normals       : bpy.props.BoolProperty  ( name='Normals',        default=True )
    m_SwapBytes     : bpy.props.BoolProperty  ( name='SwapBytes',      default=True )
    m_FileName      : bpy.props.StringProperty( name='FileName',       default="", subtype='FILE_PATH' )
    m_LimitsFileName: bpy.props.StringProperty( name='LimitsFileName', default="", subtype='FILE_PATH' )
    m_HeaderSize    : bpy.props.IntProperty   ( name='HeaderSize',     default=0 )
    e_DataByteOrder : bpy.props.EnumProperty  ( name='DataByteOrder',  default="BigEndian", items=e_DataByteOrder_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FlipNormals','m_Normals','m_SwapBytes','m_FileName','m_LimitsFileName','m_HeaderSize','e_DataByteOrder',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKMCubesReader )        
TYPENAMES.append('VTKMCubesReaderType' )

#--------------------------------------------------------------
class VTKMFIXReader(Node, BVTK_Node):

    bl_idname = 'VTKMFIXReaderType'
    bl_label  = 'vtkMFIXReader'
    
    m_FileName     : bpy.props.StringProperty   ( name='FileName',      default="", subtype='FILE_PATH' )
    m_TimeStep     : bpy.props.IntProperty      ( name='TimeStep',      default=0 )
    m_TimeStepRange: bpy.props.IntVectorProperty( name='TimeStepRange', default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKMFIXReader )        
TYPENAMES.append('VTKMFIXReaderType' )

#--------------------------------------------------------------
class VTKMINCImageReader(Node, BVTK_Node):

    bl_idname = 'VTKMINCImageReaderType'
    bl_label  = 'vtkMINCImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_RescaleRealValues       : bpy.props.BoolProperty       ( name='RescaleRealValues',        default=True )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    m_TimeStep                : bpy.props.IntProperty        ( name='TimeStep',                 default=0 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileLowerLeft','m_RescaleRealValues','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','m_TimeStep','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKMINCImageReader )        
TYPENAMES.append('VTKMINCImageReaderType' )

#--------------------------------------------------------------
class VTKMNIObjectReader(Node, BVTK_Node):

    bl_idname = 'VTKMNIObjectReaderType'
    bl_label  = 'vtkMNIObjectReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKMNIObjectReader )        
TYPENAMES.append('VTKMNIObjectReaderType' )

#--------------------------------------------------------------
class VTKMNITagPointReader(Node, BVTK_Node):

    bl_idname = 'VTKMNITagPointReaderType'
    bl_label  = 'vtkMNITagPointReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], [], []) 
    
add_class( VTKMNITagPointReader )        
TYPENAMES.append('VTKMNITagPointReaderType' )

#--------------------------------------------------------------
class VTKMNITransformReader(Node, BVTK_Node):

    bl_idname = 'VTKMNITransformReaderType'
    bl_label  = 'vtkMNITransformReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], [], [], []) 
    
add_class( VTKMNITransformReader )        
TYPENAMES.append('VTKMNITransformReaderType' )

#--------------------------------------------------------------
class VTKMPASReader(Node, BVTK_Node):

    bl_idname = 'VTKMPASReaderType'
    bl_label  = 'vtkMPASReader'
    
    m_IsAtmosphere            : bpy.props.BoolProperty  ( name='IsAtmosphere',             default=False )
    m_IsZeroCentered          : bpy.props.BoolProperty  ( name='IsZeroCentered',           default=False )
    m_ProjectLatLon           : bpy.props.BoolProperty  ( name='ProjectLatLon',            default=False )
    m_ShowMultilayerView      : bpy.props.BoolProperty  ( name='ShowMultilayerView',       default=False )
    m_UseDimensionedArrayNames: bpy.props.BoolProperty  ( name='UseDimensionedArrayNames', default=False )
    m_FileName                : bpy.props.StringProperty( name='FileName',                 default="", subtype='FILE_PATH' )
    m_VerticalDimension       : bpy.props.StringProperty( name='VerticalDimension',        default="nVertLevels" )
    m_LayerThickness          : bpy.props.IntProperty   ( name='LayerThickness',           default=10000 )
    m_VerticalLevel           : bpy.props.IntProperty   ( name='VerticalLevel',            default=-1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_IsAtmosphere','m_IsZeroCentered','m_ProjectLatLon','m_ShowMultilayerView','m_UseDimensionedArrayNames','m_FileName','m_VerticalDimension','m_LayerThickness','m_VerticalLevel',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKMPASReader )        
TYPENAMES.append('VTKMPASReaderType' )

#--------------------------------------------------------------
class VTKMRCReader(Node, BVTK_Node):

    bl_idname = 'VTKMRCReaderType'
    bl_label  = 'vtkMRCReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKMRCReader )        
TYPENAMES.append('VTKMRCReaderType' )

#--------------------------------------------------------------
class VTKMedicalImageReader2(Node, BVTK_Node):

    bl_idname = 'VTKMedicalImageReader2Type'
    bl_label  = 'vtkMedicalImageReader2'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_Date                    : bpy.props.StringProperty     ( name='Date',                     default="" )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_ImageNumber             : bpy.props.StringProperty     ( name='ImageNumber',              default="" )
    m_Modality                : bpy.props.StringProperty     ( name='Modality',                 default="" )
    m_PatientID               : bpy.props.StringProperty     ( name='PatientID',                default="" )
    m_PatientName             : bpy.props.StringProperty     ( name='PatientName',              default="" )
    m_Series                  : bpy.props.StringProperty     ( name='Series',                   default="" )
    m_Study                   : bpy.props.StringProperty     ( name='Study',                    default="" )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=22, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_Date','m_FileName','m_FilePattern','m_FilePrefix','m_ImageNumber','m_Modality','m_PatientID','m_PatientName','m_Series','m_Study','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKMedicalImageReader2 )        
TYPENAMES.append('VTKMedicalImageReader2Type' )

#--------------------------------------------------------------
class VTKMetaImageReader(Node, BVTK_Node):

    bl_idname = 'VTKMetaImageReaderType'
    bl_label  = 'vtkMetaImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKMetaImageReader )        
TYPENAMES.append('VTKMetaImageReaderType' )

#--------------------------------------------------------------
class VTKMultiBlockPLOT3DReader(Node, BVTK_Node):

    bl_idname = 'VTKMultiBlockPLOT3DReaderType'
    bl_label  = 'vtkMultiBlockPLOT3DReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_AutoDetectFormat             : bpy.props.BoolProperty  ( name='AutoDetectFormat',              default=True )
    m_BinaryFile                   : bpy.props.BoolProperty  ( name='BinaryFile',                    default=True )
    m_DoublePrecision              : bpy.props.BoolProperty  ( name='DoublePrecision',               default=True )
    m_ForceRead                    : bpy.props.BoolProperty  ( name='ForceRead',                     default=True )
    m_HasByteCount                 : bpy.props.BoolProperty  ( name='HasByteCount',                  default=True )
    m_IBlanking                    : bpy.props.BoolProperty  ( name='IBlanking',                     default=True )
    m_MultiGrid                    : bpy.props.BoolProperty  ( name='MultiGrid',                     default=True )
    m_PreserveIntermediateFunctions: bpy.props.BoolProperty  ( name='PreserveIntermediateFunctions', default=True )
    m_TwoDimensionalGeometry       : bpy.props.BoolProperty  ( name='TwoDimensionalGeometry',        default=True )
    m_FileName                     : bpy.props.StringProperty( name='FileName',                      default="", subtype='FILE_PATH' )
    m_FunctionFileName             : bpy.props.StringProperty( name='FunctionFileName',              default="", subtype='FILE_PATH' )
    m_QFileName                    : bpy.props.StringProperty( name='QFileName',                     default="", subtype='FILE_PATH' )
    m_XYZFileName                  : bpy.props.StringProperty( name='XYZFileName',                   default="", subtype='FILE_PATH' )
    m_ScalarFunctionNumber         : bpy.props.IntProperty   ( name='ScalarFunctionNumber',          default=100 )
    m_VectorFunctionNumber         : bpy.props.IntProperty   ( name='VectorFunctionNumber',          default=202 )
    m_Gamma                        : bpy.props.FloatProperty ( name='Gamma',                         default=1.4 )
    m_R                            : bpy.props.FloatProperty ( name='R',                             default=1.0 )
    e_ByteOrder                    : bpy.props.EnumProperty  ( name='ByteOrder',                     default="BigEndian", items=e_ByteOrder_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutoDetectFormat','m_BinaryFile','m_DoublePrecision','m_ForceRead','m_HasByteCount','m_IBlanking','m_MultiGrid','m_PreserveIntermediateFunctions','m_TwoDimensionalGeometry','m_FileName','m_FunctionFileName','m_QFileName','m_XYZFileName','m_ScalarFunctionNumber','m_VectorFunctionNumber','m_Gamma','m_R','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKMultiBlockPLOT3DReader )        
TYPENAMES.append('VTKMultiBlockPLOT3DReaderType' )

#--------------------------------------------------------------
class VTKMultiNewickTreeReader(Node, BVTK_Node):

    bl_idname = 'VTKMultiNewickTreeReaderType'
    bl_label  = 'vtkMultiNewickTreeReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKMultiNewickTreeReader )        
TYPENAMES.append('VTKMultiNewickTreeReaderType' )

#--------------------------------------------------------------
class VTKNIFTIImageReader(Node, BVTK_Node):

    bl_idname = 'VTKNIFTIImageReaderType'
    bl_label  = 'vtkNIFTIImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_PlanarRGB               : bpy.props.BoolProperty       ( name='PlanarRGB',                default=False )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_TimeAsVector            : bpy.props.BoolProperty       ( name='TimeAsVector',             default=False )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileLowerLeft','m_PlanarRGB','m_SwapBytes','m_TimeAsVector','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKNIFTIImageReader )        
TYPENAMES.append('VTKNIFTIImageReaderType' )

#--------------------------------------------------------------
class VTKNetCDFCFReader(Node, BVTK_Node):

    bl_idname = 'VTKNetCDFCFReaderType'
    bl_label  = 'vtkNetCDFCFReader'
    e_OutputType_items=[ (x,x,x) for x in ['Automatic', 'Structured', 'Rectilinear', 'Unstructured', 'Image']]
    
    m_ReplaceFillValueWithNan: bpy.props.BoolProperty  ( name='ReplaceFillValueWithNan', default=True )
    m_SphericalCoordinates   : bpy.props.BoolProperty  ( name='SphericalCoordinates',    default=True )
    m_FileName               : bpy.props.StringProperty( name='FileName',                default="", subtype='FILE_PATH' )
    m_VerticalBias           : bpy.props.FloatProperty ( name='VerticalBias',            default=0.0 )
    m_VerticalScale          : bpy.props.FloatProperty ( name='VerticalScale',           default=1.0 )
    e_OutputType             : bpy.props.EnumProperty  ( name='OutputType',              default="Automatic", items=e_OutputType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReplaceFillValueWithNan','m_SphericalCoordinates','m_FileName','m_VerticalBias','m_VerticalScale','e_OutputType',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKNetCDFCFReader )        
TYPENAMES.append('VTKNetCDFCFReaderType' )

#--------------------------------------------------------------
class VTKNetCDFPOPReader(Node, BVTK_Node):

    bl_idname = 'VTKNetCDFPOPReaderType'
    bl_label  = 'vtkNetCDFPOPReader'
    
    m_FileName: bpy.props.StringProperty   ( name='FileName', default="", subtype='FILE_PATH' )
    m_Stride  : bpy.props.IntVectorProperty( name='Stride',   default=[1, 1, 1], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','m_Stride',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKNetCDFPOPReader )        
TYPENAMES.append('VTKNetCDFPOPReaderType' )

#--------------------------------------------------------------
class VTKNetCDFReader(Node, BVTK_Node):

    bl_idname = 'VTKNetCDFReaderType'
    bl_label  = 'vtkNetCDFReader'
    
    m_ReplaceFillValueWithNan: bpy.props.BoolProperty  ( name='ReplaceFillValueWithNan', default=True )
    m_FileName               : bpy.props.StringProperty( name='FileName',                default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReplaceFillValueWithNan','m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKNetCDFReader )        
TYPENAMES.append('VTKNetCDFReaderType' )

#--------------------------------------------------------------
class VTKNewickTreeReader(Node, BVTK_Node):

    bl_idname = 'VTKNewickTreeReaderType'
    bl_label  = 'vtkNewickTreeReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKNewickTreeReader )        
TYPENAMES.append('VTKNewickTreeReaderType' )

#--------------------------------------------------------------
class VTKNrrdReader(Node, BVTK_Node):

    bl_idname = 'VTKNrrdReaderType'
    bl_label  = 'vtkNrrdReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_ScalarArrayName         : bpy.props.StringProperty     ( name='ScalarArrayName',          default="ImageFile" )
    m_DataMask                : bpy.props.IntProperty        ( name='DataMask',                 default=1000000000 )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataVOI                 : bpy.props.IntVectorProperty  ( name='DataVOI',                  default=[0, 0, 0, 0, 0, 0], size=6 )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ScalarArrayName','m_DataMask','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataVOI','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['Transform'], []) 
    
add_class( VTKNrrdReader )        
TYPENAMES.append('VTKNrrdReaderType' )

#--------------------------------------------------------------
class VTKOBJReader(Node, BVTK_Node):

    bl_idname = 'VTKOBJReaderType'
    bl_label  = 'vtkOBJReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKOBJReader )        
TYPENAMES.append('VTKOBJReaderType' )

#--------------------------------------------------------------
class VTKOpenFOAMReader(Node, BVTK_Node):

    bl_idname = 'VTKOpenFOAMReaderType'
    bl_label  = 'vtkOpenFOAMReader'
    
    m_AddDimensionsToArrayNames : bpy.props.BoolProperty  ( name='AddDimensionsToArrayNames',  default=True )
    m_CacheMesh                 : bpy.props.BoolProperty  ( name='CacheMesh',                  default=True )
    m_CreateCellToPoint         : bpy.props.BoolProperty  ( name='CreateCellToPoint',          default=True )
    m_DecomposePolyhedra        : bpy.props.BoolProperty  ( name='DecomposePolyhedra',         default=True )
    m_ListTimeStepsByControlDict: bpy.props.BoolProperty  ( name='ListTimeStepsByControlDict', default=True )
    m_PositionsIsIn13Format     : bpy.props.BoolProperty  ( name='PositionsIsIn13Format',      default=True )
    m_ReadZones                 : bpy.props.BoolProperty  ( name='ReadZones',                  default=True )
    m_SkipZeroTime              : bpy.props.BoolProperty  ( name='SkipZeroTime',               default=False )
    m_Use64BitFloats            : bpy.props.BoolProperty  ( name='Use64BitFloats',             default=True )
    m_Use64BitLabels            : bpy.props.BoolProperty  ( name='Use64BitLabels',             default=False )
    m_FileName                  : bpy.props.StringProperty( name='FileName',                   default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AddDimensionsToArrayNames','m_CacheMesh','m_CreateCellToPoint','m_DecomposePolyhedra','m_ListTimeStepsByControlDict','m_PositionsIsIn13Format','m_ReadZones','m_SkipZeroTime','m_Use64BitFloats','m_Use64BitLabels','m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKOpenFOAMReader )        
TYPENAMES.append('VTKOpenFOAMReaderType' )

#--------------------------------------------------------------
class VTKPChacoReader(Node, BVTK_Node):

    bl_idname = 'VTKPChacoReaderType'
    bl_label  = 'vtkPChacoReader'
    
    m_GenerateEdgeWeightArrays    : bpy.props.BoolProperty  ( name='GenerateEdgeWeightArrays',     default=True )
    m_GenerateGlobalElementIdArray: bpy.props.BoolProperty  ( name='GenerateGlobalElementIdArray', default=True )
    m_GenerateGlobalNodeIdArray   : bpy.props.BoolProperty  ( name='GenerateGlobalNodeIdArray',    default=True )
    m_GenerateVertexWeightArrays  : bpy.props.BoolProperty  ( name='GenerateVertexWeightArrays',   default=True )
    m_BaseName                    : bpy.props.StringProperty( name='BaseName',                     default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateEdgeWeightArrays','m_GenerateGlobalElementIdArray','m_GenerateGlobalNodeIdArray','m_GenerateVertexWeightArrays','m_BaseName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKPChacoReader )        
TYPENAMES.append('VTKPChacoReaderType' )

#--------------------------------------------------------------
class VTKPDBReader(Node, BVTK_Node):

    bl_idname = 'VTKPDBReaderType'
    bl_label  = 'vtkPDBReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    m_BScale  : bpy.props.FloatProperty ( name='BScale',   default=1.0 )
    m_HBScale : bpy.props.FloatProperty ( name='HBScale',  default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','m_BScale','m_HBScale',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], [], []) 
    
add_class( VTKPDBReader )        
TYPENAMES.append('VTKPDBReaderType' )

#--------------------------------------------------------------
class VTKPDataSetReader(Node, BVTK_Node):

    bl_idname = 'VTKPDataSetReaderType'
    bl_label  = 'vtkPDataSetReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKPDataSetReader )        
TYPENAMES.append('VTKPDataSetReaderType' )

#--------------------------------------------------------------
class VTKPLYReader(Node, BVTK_Node):

    bl_idname = 'VTKPLYReaderType'
    bl_label  = 'vtkPLYReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKPLYReader )        
TYPENAMES.append('VTKPLYReaderType' )

#--------------------------------------------------------------
class VTKPNGReader(Node, BVTK_Node):

    bl_idname = 'VTKPNGReaderType'
    bl_label  = 'vtkPNGReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_ReadSpacingFromFile     : bpy.props.BoolProperty       ( name='ReadSpacingFromFile',      default=False )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileLowerLeft','m_ReadSpacingFromFile','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKPNGReader )        
TYPENAMES.append('VTKPNGReaderType' )

#--------------------------------------------------------------
class VTKPNMReader(Node, BVTK_Node):

    bl_idname = 'VTKPNMReaderType'
    bl_label  = 'vtkPNMReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_ScalarArrayName         : bpy.props.StringProperty     ( name='ScalarArrayName',          default="ImageFile" )
    m_DataMask                : bpy.props.IntProperty        ( name='DataMask',                 default=1000000000 )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataVOI                 : bpy.props.IntVectorProperty  ( name='DataVOI',                  default=[0, 0, 0, 0, 0, 0], size=6 )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ScalarArrayName','m_DataMask','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataVOI','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['Transform'], []) 
    
add_class( VTKPNMReader )        
TYPENAMES.append('VTKPNMReaderType' )

#--------------------------------------------------------------
class VTKPOpenFOAMReader(Node, BVTK_Node):

    bl_idname = 'VTKPOpenFOAMReaderType'
    bl_label  = 'vtkPOpenFOAMReader'
    
    m_AddDimensionsToArrayNames : bpy.props.BoolProperty  ( name='AddDimensionsToArrayNames',  default=True )
    m_CacheMesh                 : bpy.props.BoolProperty  ( name='CacheMesh',                  default=True )
    m_CreateCellToPoint         : bpy.props.BoolProperty  ( name='CreateCellToPoint',          default=True )
    m_DecomposePolyhedra        : bpy.props.BoolProperty  ( name='DecomposePolyhedra',         default=True )
    m_ListTimeStepsByControlDict: bpy.props.BoolProperty  ( name='ListTimeStepsByControlDict', default=True )
    m_PositionsIsIn13Format     : bpy.props.BoolProperty  ( name='PositionsIsIn13Format',      default=True )
    m_ReadZones                 : bpy.props.BoolProperty  ( name='ReadZones',                  default=True )
    m_SkipZeroTime              : bpy.props.BoolProperty  ( name='SkipZeroTime',               default=False )
    m_Use64BitFloats            : bpy.props.BoolProperty  ( name='Use64BitFloats',             default=True )
    m_Use64BitLabels            : bpy.props.BoolProperty  ( name='Use64BitLabels',             default=False )
    m_FileName                  : bpy.props.StringProperty( name='FileName',                   default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AddDimensionsToArrayNames','m_CacheMesh','m_CreateCellToPoint','m_DecomposePolyhedra','m_ListTimeStepsByControlDict','m_PositionsIsIn13Format','m_ReadZones','m_SkipZeroTime','m_Use64BitFloats','m_Use64BitLabels','m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKPOpenFOAMReader )        
TYPENAMES.append('VTKPOpenFOAMReaderType' )

#--------------------------------------------------------------
class VTKPSLACReader(Node, BVTK_Node):

    bl_idname = 'VTKPSLACReaderType'
    bl_label  = 'vtkPSLACReader'
    
    m_ReadExternalSurface: bpy.props.BoolProperty  ( name='ReadExternalSurface', default=True )
    m_ReadInternalVolume : bpy.props.BoolProperty  ( name='ReadInternalVolume',  default=True )
    m_ReadMidpoints      : bpy.props.BoolProperty  ( name='ReadMidpoints',       default=True )
    m_MeshFileName       : bpy.props.StringProperty( name='MeshFileName',        default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadExternalSurface','m_ReadInternalVolume','m_ReadMidpoints','m_MeshFileName',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], [], []) 
    
add_class( VTKPSLACReader )        
TYPENAMES.append('VTKPSLACReaderType' )

#--------------------------------------------------------------
class VTKPTSReader(Node, BVTK_Node):

    bl_idname = 'VTKPTSReaderType'
    bl_label  = 'vtkPTSReader'
    
    m_CreateCells             : bpy.props.BoolProperty       ( name='CreateCells',              default=True )
    m_IncludeColorAndLuminance: bpy.props.BoolProperty       ( name='IncludeColorAndLuminance', default=True )
    m_LimitReadToBounds       : bpy.props.BoolProperty       ( name='LimitReadToBounds',        default=False )
    m_LimitToMaxNumberOfPoints: bpy.props.BoolProperty       ( name='LimitToMaxNumberOfPoints', default=False )
    m_OutputDataTypeIsDouble  : bpy.props.BoolProperty       ( name='OutputDataTypeIsDouble',   default=False )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_MaxNumberOfPoints       : bpy.props.IntProperty        ( name='MaxNumberOfPoints',        default=1000000 )
    m_ReadBounds              : bpy.props.FloatVectorProperty( name='ReadBounds',               default=[1e+30, -1e+30, 1e+30, -1e+30, 1e+30, -1e+30], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CreateCells','m_IncludeColorAndLuminance','m_LimitReadToBounds','m_LimitToMaxNumberOfPoints','m_OutputDataTypeIsDouble','m_FileName','m_MaxNumberOfPoints','m_ReadBounds',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKPTSReader )        
TYPENAMES.append('VTKPTSReaderType' )

#--------------------------------------------------------------
class VTKParticleReader(Node, BVTK_Node):

    bl_idname = 'VTKParticleReaderType'
    bl_label  = 'vtkParticleReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_FileType_items=[ (x,x,x) for x in ['Unknown', 'Text', 'Binary']]
    
    m_HasScalar    : bpy.props.BoolProperty  ( name='HasScalar',     default=True )
    m_SwapBytes    : bpy.props.BoolProperty  ( name='SwapBytes',     default=True )
    m_FileName     : bpy.props.StringProperty( name='FileName',      default="", subtype='FILE_PATH' )
    e_DataByteOrder: bpy.props.EnumProperty  ( name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items )
    e_FileType     : bpy.props.EnumProperty  ( name='FileType',      default="Unknown", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_HasScalar','m_SwapBytes','m_FileName','e_DataByteOrder','e_FileType',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKParticleReader )        
TYPENAMES.append('VTKParticleReaderType' )

#--------------------------------------------------------------
class VTKPhyloXMLTreeReader(Node, BVTK_Node):

    bl_idname = 'VTKPhyloXMLTreeReaderType'
    bl_label  = 'vtkPhyloXMLTreeReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKPhyloXMLTreeReader )        
TYPENAMES.append('VTKPhyloXMLTreeReaderType' )

#--------------------------------------------------------------
class VTKPlot3DMetaReader(Node, BVTK_Node):

    bl_idname = 'VTKPlot3DMetaReaderType'
    bl_label  = 'vtkPlot3DMetaReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKPlot3DMetaReader )        
TYPENAMES.append('VTKPlot3DMetaReaderType' )

#--------------------------------------------------------------
class VTKPolyDataReader(Node, BVTK_Node):

    bl_idname = 'VTKPolyDataReaderType'
    bl_label  = 'vtkPolyDataReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKPolyDataReader )        
TYPENAMES.append('VTKPolyDataReaderType' )

#--------------------------------------------------------------
class VTKProStarReader(Node, BVTK_Node):

    bl_idname = 'VTKProStarReaderType'
    bl_label  = 'vtkProStarReader'
    
    m_FileName   : bpy.props.StringProperty( name='FileName',    default="", subtype='FILE_PATH' )
    m_ScaleFactor: bpy.props.FloatProperty ( name='ScaleFactor', default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','m_ScaleFactor',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKProStarReader )        
TYPENAMES.append('VTKProStarReaderType' )

#--------------------------------------------------------------
class VTKRISReader(Node, BVTK_Node):

    bl_idname = 'VTKRISReaderType'
    bl_label  = 'vtkRISReader'
    
    m_Delimiter : bpy.props.StringProperty( name='Delimiter',  default=";" )
    m_FileName  : bpy.props.StringProperty( name='FileName',   default="", subtype='FILE_PATH' )
    m_MaxRecords: bpy.props.IntProperty   ( name='MaxRecords', default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Delimiter','m_FileName','m_MaxRecords',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKRISReader )        
TYPENAMES.append('VTKRISReaderType' )

#--------------------------------------------------------------
class VTKRTXMLPolyDataReader(Node, BVTK_Node):

    bl_idname = 'VTKRTXMLPolyDataReaderType'
    bl_label  = 'vtkRTXMLPolyDataReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKRTXMLPolyDataReader )        
TYPENAMES.append('VTKRTXMLPolyDataReaderType' )

#--------------------------------------------------------------
class VTKRectilinearGridReader(Node, BVTK_Node):

    bl_idname = 'VTKRectilinearGridReaderType'
    bl_label  = 'vtkRectilinearGridReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKRectilinearGridReader )        
TYPENAMES.append('VTKRectilinearGridReaderType' )

#--------------------------------------------------------------
class VTKSLACParticleReader(Node, BVTK_Node):

    bl_idname = 'VTKSLACParticleReaderType'
    bl_label  = 'vtkSLACParticleReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKSLACParticleReader )        
TYPENAMES.append('VTKSLACParticleReaderType' )

#--------------------------------------------------------------
class VTKSLACReader(Node, BVTK_Node):

    bl_idname = 'VTKSLACReaderType'
    bl_label  = 'vtkSLACReader'
    
    m_ReadExternalSurface: bpy.props.BoolProperty  ( name='ReadExternalSurface', default=True )
    m_ReadInternalVolume : bpy.props.BoolProperty  ( name='ReadInternalVolume',  default=True )
    m_ReadMidpoints      : bpy.props.BoolProperty  ( name='ReadMidpoints',       default=True )
    m_MeshFileName       : bpy.props.StringProperty( name='MeshFileName',        default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadExternalSurface','m_ReadInternalVolume','m_ReadMidpoints','m_MeshFileName',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], [], []) 
    
add_class( VTKSLACReader )        
TYPENAMES.append('VTKSLACReaderType' )

#--------------------------------------------------------------
class VTKSLCReader(Node, BVTK_Node):

    bl_idname = 'VTKSLCReaderType'
    bl_label  = 'vtkSLCReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKSLCReader )        
TYPENAMES.append('VTKSLCReaderType' )

#--------------------------------------------------------------
class VTKSQLiteToTableReader(Node, BVTK_Node):

    bl_idname = 'VTKSQLiteToTableReaderType'
    bl_label  = 'vtkSQLiteToTableReader'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKSQLiteToTableReader )        
TYPENAMES.append('VTKSQLiteToTableReaderType' )

#--------------------------------------------------------------
class VTKSTLReader(Node, BVTK_Node):

    bl_idname = 'VTKSTLReaderType'
    bl_label  = 'vtkSTLReader'
    
    m_Merging   : bpy.props.BoolProperty  ( name='Merging',    default=True )
    m_ScalarTags: bpy.props.BoolProperty  ( name='ScalarTags', default=True )
    m_FileName  : bpy.props.StringProperty( name='FileName',   default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Merging','m_ScalarTags','m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKSTLReader )        
TYPENAMES.append('VTKSTLReaderType' )

#--------------------------------------------------------------
class VTKSimplePointsReader(Node, BVTK_Node):

    bl_idname = 'VTKSimplePointsReaderType'
    bl_label  = 'vtkSimplePointsReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKSimplePointsReader )        
TYPENAMES.append('VTKSimplePointsReaderType' )

#--------------------------------------------------------------
class VTKStructuredGridReader(Node, BVTK_Node):

    bl_idname = 'VTKStructuredGridReaderType'
    bl_label  = 'vtkStructuredGridReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKStructuredGridReader )        
TYPENAMES.append('VTKStructuredGridReaderType' )

#--------------------------------------------------------------
class VTKStructuredPointsReader(Node, BVTK_Node):

    bl_idname = 'VTKStructuredPointsReaderType'
    bl_label  = 'vtkStructuredPointsReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKStructuredPointsReader )        
TYPENAMES.append('VTKStructuredPointsReaderType' )

#--------------------------------------------------------------
class VTKTIFFReader(Node, BVTK_Node):

    bl_idname = 'VTKTIFFReaderType'
    bl_label  = 'vtkTIFFReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft           : bpy.props.BoolProperty       ( name='FileLowerLeft',            default=True )
    m_OriginSpecifiedFlag     : bpy.props.BoolProperty       ( name='OriginSpecifiedFlag',      default=False )
    m_SpacingSpecifiedFlag    : bpy.props.BoolProperty       ( name='SpacingSpecifiedFlag',     default=False )
    m_SwapBytes               : bpy.props.BoolProperty       ( name='SwapBytes',                default=True )
    m_FileName                : bpy.props.StringProperty     ( name='FileName',                 default="", subtype='FILE_PATH' )
    m_FilePattern             : bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix              : bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality      : bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset     : bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing    : bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize              : bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength      : bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents: bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    m_OrientationType         : bpy.props.IntProperty        ( name='OrientationType',          default=4 )
    e_DataByteOrder           : bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType          : bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin              : bpy.props.FloatVectorProperty( name='DataOrigin',               default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing             : bpy.props.FloatVectorProperty( name='DataSpacing',              default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileLowerLeft','m_OriginSpecifiedFlag','m_SpacingSpecifiedFlag','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','m_OrientationType','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKTIFFReader )        
TYPENAMES.append('VTKTIFFReaderType' )

#--------------------------------------------------------------
class VTKTableReader(Node, BVTK_Node):

    bl_idname = 'VTKTableReaderType'
    bl_label  = 'vtkTableReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKTableReader )        
TYPENAMES.append('VTKTableReaderType' )

#--------------------------------------------------------------
class VTKTecplotReader(Node, BVTK_Node):

    bl_idname = 'VTKTecplotReaderType'
    bl_label  = 'vtkTecplotReader'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKTecplotReader )        
TYPENAMES.append('VTKTecplotReaderType' )

#--------------------------------------------------------------
class VTKTecplotTableReader(Node, BVTK_Node):

    bl_idname = 'VTKTecplotTableReaderType'
    bl_label  = 'vtkTecplotTableReader'
    
    m_GeneratePedigreeIds: bpy.props.BoolProperty  ( name='GeneratePedigreeIds', default=False )
    m_OutputPedigreeIds  : bpy.props.BoolProperty  ( name='OutputPedigreeIds',   default=False )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_PedigreeIdArrayName: bpy.props.StringProperty( name='PedigreeIdArrayName', default="id" )
    m_ColumnNamesOnLine  : bpy.props.IntProperty   ( name='ColumnNamesOnLine',   default=1 )
    m_HeaderLines        : bpy.props.IntProperty   ( name='HeaderLines',         default=2 )
    m_MaxRecords         : bpy.props.IntProperty   ( name='MaxRecords',          default=0 )
    m_SkipColumnNames    : bpy.props.IntProperty   ( name='SkipColumnNames',     default=1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GeneratePedigreeIds','m_OutputPedigreeIds','m_FileName','m_PedigreeIdArrayName','m_ColumnNamesOnLine','m_HeaderLines','m_MaxRecords','m_SkipColumnNames',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKTecplotTableReader )        
TYPENAMES.append('VTKTecplotTableReaderType' )

#--------------------------------------------------------------
class VTKTreeReader(Node, BVTK_Node):

    bl_idname = 'VTKTreeReaderType'
    bl_label  = 'vtkTreeReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKTreeReader )        
TYPENAMES.append('VTKTreeReaderType' )

#--------------------------------------------------------------
class VTKTulipReader(Node, BVTK_Node):

    bl_idname = 'VTKTulipReaderType'
    bl_label  = 'vtkTulipReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], [], []) 
    
add_class( VTKTulipReader )        
TYPENAMES.append('VTKTulipReaderType' )

#--------------------------------------------------------------
class VTKUGFacetReader(Node, BVTK_Node):

    bl_idname = 'VTKUGFacetReaderType'
    bl_label  = 'vtkUGFacetReader'
    
    m_Merging   : bpy.props.BoolProperty  ( name='Merging',    default=True )
    m_FileName  : bpy.props.StringProperty( name='FileName',   default="", subtype='FILE_PATH' )
    m_PartNumber: bpy.props.IntProperty   ( name='PartNumber', default=-1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Merging','m_FileName','m_PartNumber',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKUGFacetReader )        
TYPENAMES.append('VTKUGFacetReaderType' )

#--------------------------------------------------------------
class VTKUnstructuredGridReader(Node, BVTK_Node):

    bl_idname = 'VTKUnstructuredGridReaderType'
    bl_label  = 'vtkUnstructuredGridReader'
    
    m_ReadAllColorScalars: bpy.props.BoolProperty  ( name='ReadAllColorScalars', default=True )
    m_ReadAllFields      : bpy.props.BoolProperty  ( name='ReadAllFields',       default=True )
    m_ReadAllNormals     : bpy.props.BoolProperty  ( name='ReadAllNormals',      default=True )
    m_ReadAllScalars     : bpy.props.BoolProperty  ( name='ReadAllScalars',      default=True )
    m_ReadAllTCoords     : bpy.props.BoolProperty  ( name='ReadAllTCoords',      default=True )
    m_ReadAllTensors     : bpy.props.BoolProperty  ( name='ReadAllTensors',      default=True )
    m_ReadAllVectors     : bpy.props.BoolProperty  ( name='ReadAllVectors',      default=True )
    m_ReadFromInputString: bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['InputArray'], []) 
    
add_class( VTKUnstructuredGridReader )        
TYPENAMES.append('VTKUnstructuredGridReaderType' )

#--------------------------------------------------------------
class VTKVASPAnimationReader(Node, BVTK_Node):

    bl_idname = 'VTKVASPAnimationReaderType'
    bl_label  = 'vtkVASPAnimationReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKVASPAnimationReader )        
TYPENAMES.append('VTKVASPAnimationReaderType' )

#--------------------------------------------------------------
class VTKVASPTessellationReader(Node, BVTK_Node):

    bl_idname = 'VTKVASPTessellationReaderType'
    bl_label  = 'vtkVASPTessellationReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], [], []) 
    
add_class( VTKVASPTessellationReader )        
TYPENAMES.append('VTKVASPTessellationReaderType' )

#--------------------------------------------------------------
class VTKVolume16Reader(Node, BVTK_Node):

    bl_idname = 'VTKVolume16ReaderType'
    bl_label  = 'vtkVolume16Reader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_SwapBytes     : bpy.props.BoolProperty       ( name='SwapBytes',      default=True )
    m_FilePattern   : bpy.props.StringProperty     ( name='FilePattern',    default="%s.%d" )
    m_FilePrefix    : bpy.props.StringProperty     ( name='FilePrefix',     default="" )
    m_DataMask      : bpy.props.IntProperty        ( name='DataMask',       default=0 )
    m_HeaderSize    : bpy.props.IntProperty        ( name='HeaderSize',     default=0 )
    e_DataByteOrder : bpy.props.EnumProperty       ( name='DataByteOrder',  default="LittleEndian", items=e_DataByteOrder_items )
    m_DataDimensions: bpy.props.IntVectorProperty  ( name='DataDimensions', default=[0, 0], size=2 )
    m_ImageRange    : bpy.props.IntVectorProperty  ( name='ImageRange',     default=[1, 1], size=2 )
    m_DataOrigin    : bpy.props.FloatVectorProperty( name='DataOrigin',     default=[0.0, 0.0, 0.0], size=3 )
    m_DataSpacing   : bpy.props.FloatVectorProperty( name='DataSpacing',    default=[1.0, 1.0, 1.0], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_SwapBytes','m_FilePattern','m_FilePrefix','m_DataMask','m_HeaderSize','e_DataByteOrder','m_DataDimensions','m_ImageRange','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['Transform'], []) 
    
add_class( VTKVolume16Reader )        
TYPENAMES.append('VTKVolume16ReaderType' )

#--------------------------------------------------------------
class VTKWindBladeReader(Node, BVTK_Node):

    bl_idname = 'VTKWindBladeReaderType'
    bl_label  = 'vtkWindBladeReader'
    
    m_Filename : bpy.props.StringProperty   ( name='Filename',  default="" )
    m_SubExtent: bpy.props.IntVectorProperty( name='SubExtent', default=[0, 0, 1, 0, 0, 0], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Filename','m_SubExtent',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKWindBladeReader )        
TYPENAMES.append('VTKWindBladeReaderType' )

#--------------------------------------------------------------
class VTKXGMLReader(Node, BVTK_Node):

    bl_idname = 'VTKXGMLReaderType'
    bl_label  = 'vtkXGMLReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKXGMLReader )        
TYPENAMES.append('VTKXGMLReaderType' )

#--------------------------------------------------------------
class VTKXMLGenericDataObjectReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLGenericDataObjectReaderType'
    bl_label  = 'vtkXMLGenericDataObjectReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLGenericDataObjectReader )        
TYPENAMES.append('VTKXMLGenericDataObjectReaderType' )

#--------------------------------------------------------------
class VTKXMLHierarchicalBoxDataReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLHierarchicalBoxDataReaderType'
    bl_label  = 'vtkXMLHierarchicalBoxDataReader'
    
    m_ReadFromInputString         : bpy.props.BoolProperty     ( name='ReadFromInputString',          default=False )
    m_FileName                    : bpy.props.StringProperty   ( name='FileName',                     default="", subtype='FILE_PATH' )
    m_MaximumLevelsToReadByDefault: bpy.props.IntProperty      ( name='MaximumLevelsToReadByDefault', default=1 )
    m_PieceDistribution           : bpy.props.IntProperty      ( name='PieceDistribution',            default=0 )
    m_TimeStep                    : bpy.props.IntProperty      ( name='TimeStep',                     default=0 )
    m_TimeStepRange               : bpy.props.IntVectorProperty( name='TimeStepRange',                default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_MaximumLevelsToReadByDefault','m_PieceDistribution','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLHierarchicalBoxDataReader )        
TYPENAMES.append('VTKXMLHierarchicalBoxDataReaderType' )

#--------------------------------------------------------------
class VTKXMLHierarchicalDataReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLHierarchicalDataReaderType'
    bl_label  = 'vtkXMLHierarchicalDataReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_PieceDistribution  : bpy.props.IntProperty      ( name='PieceDistribution',   default=0 )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_PieceDistribution','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLHierarchicalDataReader )        
TYPENAMES.append('VTKXMLHierarchicalDataReaderType' )

#--------------------------------------------------------------
class VTKXMLHyperOctreeReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLHyperOctreeReaderType'
    bl_label  = 'vtkXMLHyperOctreeReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLHyperOctreeReader )        
TYPENAMES.append('VTKXMLHyperOctreeReaderType' )

#--------------------------------------------------------------
class VTKXMLImageDataReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLImageDataReaderType'
    bl_label  = 'vtkXMLImageDataReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_WholeSlices        : bpy.props.BoolProperty     ( name='WholeSlices',         default=True )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_WholeSlices','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLImageDataReader )        
TYPENAMES.append('VTKXMLImageDataReaderType' )

#--------------------------------------------------------------
class VTKXMLMultiBlockDataReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLMultiBlockDataReaderType'
    bl_label  = 'vtkXMLMultiBlockDataReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_PieceDistribution  : bpy.props.IntProperty      ( name='PieceDistribution',   default=0 )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_PieceDistribution','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLMultiBlockDataReader )        
TYPENAMES.append('VTKXMLMultiBlockDataReaderType' )

#--------------------------------------------------------------
class VTKXMLMultiGroupDataReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLMultiGroupDataReaderType'
    bl_label  = 'vtkXMLMultiGroupDataReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_PieceDistribution  : bpy.props.IntProperty      ( name='PieceDistribution',   default=0 )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_PieceDistribution','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLMultiGroupDataReader )        
TYPENAMES.append('VTKXMLMultiGroupDataReaderType' )

#--------------------------------------------------------------
class VTKXMLPImageDataReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLPImageDataReaderType'
    bl_label  = 'vtkXMLPImageDataReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLPImageDataReader )        
TYPENAMES.append('VTKXMLPImageDataReaderType' )

#--------------------------------------------------------------
class VTKXMLPPolyDataReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLPPolyDataReaderType'
    bl_label  = 'vtkXMLPPolyDataReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLPPolyDataReader )        
TYPENAMES.append('VTKXMLPPolyDataReaderType' )

#--------------------------------------------------------------
class VTKXMLPRectilinearGridReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLPRectilinearGridReaderType'
    bl_label  = 'vtkXMLPRectilinearGridReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLPRectilinearGridReader )        
TYPENAMES.append('VTKXMLPRectilinearGridReaderType' )

#--------------------------------------------------------------
class VTKXMLPStructuredGridReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLPStructuredGridReaderType'
    bl_label  = 'vtkXMLPStructuredGridReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLPStructuredGridReader )        
TYPENAMES.append('VTKXMLPStructuredGridReaderType' )

#--------------------------------------------------------------
class VTKXMLPTableReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLPTableReaderType'
    bl_label  = 'vtkXMLPTableReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLPTableReader )        
TYPENAMES.append('VTKXMLPTableReaderType' )

#--------------------------------------------------------------
class VTKXMLPUnstructuredGridReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLPUnstructuredGridReaderType'
    bl_label  = 'vtkXMLPUnstructuredGridReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLPUnstructuredGridReader )        
TYPENAMES.append('VTKXMLPUnstructuredGridReaderType' )

#--------------------------------------------------------------
class VTKXMLPolyDataReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLPolyDataReaderType'
    bl_label  = 'vtkXMLPolyDataReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLPolyDataReader )        
TYPENAMES.append('VTKXMLPolyDataReaderType' )

#--------------------------------------------------------------
class VTKXMLRectilinearGridReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLRectilinearGridReaderType'
    bl_label  = 'vtkXMLRectilinearGridReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_WholeSlices        : bpy.props.BoolProperty     ( name='WholeSlices',         default=True )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_WholeSlices','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLRectilinearGridReader )        
TYPENAMES.append('VTKXMLRectilinearGridReaderType' )

#--------------------------------------------------------------
class VTKXMLStructuredGridReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLStructuredGridReaderType'
    bl_label  = 'vtkXMLStructuredGridReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_WholeSlices        : bpy.props.BoolProperty     ( name='WholeSlices',         default=True )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_WholeSlices','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLStructuredGridReader )        
TYPENAMES.append('VTKXMLStructuredGridReaderType' )

#--------------------------------------------------------------
class VTKXMLTableReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLTableReaderType'
    bl_label  = 'vtkXMLTableReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLTableReader )        
TYPENAMES.append('VTKXMLTableReaderType' )

#--------------------------------------------------------------
class VTKXMLTreeReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLTreeReaderType'
    bl_label  = 'vtkXMLTreeReader'
    
    m_GenerateEdgePedigreeIds  : bpy.props.BoolProperty  ( name='GenerateEdgePedigreeIds',   default=True )
    m_GenerateVertexPedigreeIds: bpy.props.BoolProperty  ( name='GenerateVertexPedigreeIds', default=True )
    m_MaskArrays               : bpy.props.BoolProperty  ( name='MaskArrays',                default=False )
    m_ReadCharData             : bpy.props.BoolProperty  ( name='ReadCharData',              default=False )
    m_ReadTagName              : bpy.props.BoolProperty  ( name='ReadTagName',               default=True )
    m_EdgePedigreeIdArrayName  : bpy.props.StringProperty( name='EdgePedigreeIdArrayName',   default="edge id" )
    m_FileName                 : bpy.props.StringProperty( name='FileName',                  default="", subtype='FILE_PATH' )
    m_VertexPedigreeIdArrayName: bpy.props.StringProperty( name='VertexPedigreeIdArrayName', default="vertex id" )
    m_XMLString                : bpy.props.StringProperty( name='XMLString',                 default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateEdgePedigreeIds','m_GenerateVertexPedigreeIds','m_MaskArrays','m_ReadCharData','m_ReadTagName','m_EdgePedigreeIdArrayName','m_FileName','m_VertexPedigreeIdArrayName','m_XMLString',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKXMLTreeReader )        
TYPENAMES.append('VTKXMLTreeReaderType' )

#--------------------------------------------------------------
class VTKXMLUniformGridAMRReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLUniformGridAMRReaderType'
    bl_label  = 'vtkXMLUniformGridAMRReader'
    
    m_ReadFromInputString         : bpy.props.BoolProperty     ( name='ReadFromInputString',          default=False )
    m_FileName                    : bpy.props.StringProperty   ( name='FileName',                     default="", subtype='FILE_PATH' )
    m_MaximumLevelsToReadByDefault: bpy.props.IntProperty      ( name='MaximumLevelsToReadByDefault', default=1 )
    m_PieceDistribution           : bpy.props.IntProperty      ( name='PieceDistribution',            default=0 )
    m_TimeStep                    : bpy.props.IntProperty      ( name='TimeStep',                     default=0 )
    m_TimeStepRange               : bpy.props.IntVectorProperty( name='TimeStepRange',                default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_MaximumLevelsToReadByDefault','m_PieceDistribution','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLUniformGridAMRReader )        
TYPENAMES.append('VTKXMLUniformGridAMRReaderType' )

#--------------------------------------------------------------
class VTKXMLUnstructuredGridReader(Node, BVTK_Node):

    bl_idname = 'VTKXMLUnstructuredGridReaderType'
    bl_label  = 'vtkXMLUnstructuredGridReader'
    
    m_ReadFromInputString: bpy.props.BoolProperty     ( name='ReadFromInputString', default=False )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_TimeStep           : bpy.props.IntProperty      ( name='TimeStep',            default=0 )
    m_TimeStepRange      : bpy.props.IntVectorProperty( name='TimeStepRange',       default=[0, 0], size=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ReaderErrorObserver'], []) 
    
add_class( VTKXMLUnstructuredGridReader )        
TYPENAMES.append('VTKXMLUnstructuredGridReaderType' )

#--------------------------------------------------------------
class VTKXYZMolReader(Node, BVTK_Node):

    bl_idname = 'VTKXYZMolReaderType'
    bl_label  = 'vtkXYZMolReader'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    m_TimeStep: bpy.props.IntProperty   ( name='TimeStep', default=0 )
    m_BScale  : bpy.props.FloatProperty ( name='BScale',   default=1.0 )
    m_HBScale : bpy.props.FloatProperty ( name='HBScale',  default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','m_TimeStep','m_BScale','m_HBScale',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], [], []) 
    
add_class( VTKXYZMolReader )        
TYPENAMES.append('VTKXYZMolReaderType' )

#--------------------------------------------------------------
class VTKXYZMolReader2(Node, BVTK_Node):

    bl_idname = 'VTKXYZMolReader2Type'
    bl_label  = 'vtkXYZMolReader2'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return ([], ['output'], [], []) 
    
add_class( VTKXYZMolReader2 )        
TYPENAMES.append('VTKXYZMolReader2Type' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( BVTK_NodeCategory( 'Reader', 'Reader', items=menu_items) )