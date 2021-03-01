# Generated definitions for VTK class group: Writer
# VTK version: 9.0.1

from ..core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKArrayDataWriter(Node, BVTK_Node):

    bl_idname = 'VTKArrayDataWriterType'
    bl_label  = 'vtkArrayDataWriter'
    
    m_Binary             : bpy.props.BoolProperty  ( name='Binary',              default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=False )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Binary','m_WriteToOutputString','m_FileName',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKArrayDataWriter )        
TYPENAMES.append('VTKArrayDataWriterType' )

#--------------------------------------------------------------
class VTKArrayWriter(Node, BVTK_Node):

    bl_idname = 'VTKArrayWriterType'
    bl_label  = 'vtkArrayWriter'
    
    m_Binary             : bpy.props.BoolProperty  ( name='Binary',              default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=False )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Binary','m_WriteToOutputString','m_FileName',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKArrayWriter )        
TYPENAMES.append('VTKArrayWriterType' )

#--------------------------------------------------------------
class VTKBMPWriter(Node, BVTK_Node):

    bl_idname = 'VTKBMPWriterType'
    bl_label  = 'vtkBMPWriter'
    
    m_WriteToMemory     : bpy.props.BoolProperty  ( name='WriteToMemory',      default=True )
    m_FileName          : bpy.props.StringProperty( name='FileName',           default="", subtype='FILE_PATH' )
    m_FilePattern       : bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix        : bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality: bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteToMemory','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKBMPWriter )        
TYPENAMES.append('VTKBMPWriterType' )

#--------------------------------------------------------------
class VTKBYUWriter(Node, BVTK_Node):

    bl_idname = 'VTKBYUWriterType'
    bl_label  = 'vtkBYUWriter'
    
    m_WriteDisplacement   : bpy.props.BoolProperty  ( name='WriteDisplacement',    default=True )
    m_WriteScalar         : bpy.props.BoolProperty  ( name='WriteScalar',          default=True )
    m_WriteTexture        : bpy.props.BoolProperty  ( name='WriteTexture',         default=True )
    m_DisplacementFileName: bpy.props.StringProperty( name='DisplacementFileName', default="", subtype='FILE_PATH' )
    m_GeometryFileName    : bpy.props.StringProperty( name='GeometryFileName',     default="", subtype='FILE_PATH' )
    m_ScalarFileName      : bpy.props.StringProperty( name='ScalarFileName',       default="", subtype='FILE_PATH' )
    m_TextureFileName     : bpy.props.StringProperty( name='TextureFileName',      default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteDisplacement','m_WriteScalar','m_WriteTexture','m_DisplacementFileName','m_GeometryFileName','m_ScalarFileName','m_TextureFileName',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKBYUWriter )        
TYPENAMES.append('VTKBYUWriterType' )

#--------------------------------------------------------------
class VTKCompositeDataWriter(Node, BVTK_Node):

    bl_idname = 'VTKCompositeDataWriterType'
    bl_label  = 'vtkCompositeDataWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKCompositeDataWriter )        
TYPENAMES.append('VTKCompositeDataWriterType' )

#--------------------------------------------------------------
class VTKDIMACSGraphWriter(Node, BVTK_Node):

    bl_idname = 'VTKDIMACSGraphWriterType'
    bl_label  = 'vtkDIMACSGraphWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKDIMACSGraphWriter )        
TYPENAMES.append('VTKDIMACSGraphWriterType' )

#--------------------------------------------------------------
class VTKDataObjectWriter(Node, BVTK_Node):

    bl_idname = 'VTKDataObjectWriterType'
    bl_label  = 'vtkDataObjectWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteToOutputString','m_FieldDataName','m_FileName','m_Header','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKDataObjectWriter )        
TYPENAMES.append('VTKDataObjectWriterType' )

#--------------------------------------------------------------
class VTKDataSetWriter(Node, BVTK_Node):

    bl_idname = 'VTKDataSetWriterType'
    bl_label  = 'vtkDataSetWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKDataSetWriter )        
TYPENAMES.append('VTKDataSetWriterType' )

#--------------------------------------------------------------
class VTKDataWriter(Node, BVTK_Node):

    bl_idname = 'VTKDataWriterType'
    bl_label  = 'vtkDataWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKDataWriter )        
TYPENAMES.append('VTKDataWriterType' )

#--------------------------------------------------------------
class VTKDelimitedTextWriter(Node, BVTK_Node):

    bl_idname = 'VTKDelimitedTextWriterType'
    bl_label  = 'vtkDelimitedTextWriter'
    
    m_UseStringDelimiter : bpy.props.BoolProperty  ( name='UseStringDelimiter',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=False )
    m_FieldDelimiter     : bpy.props.StringProperty( name='FieldDelimiter',      default="," )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_StringDelimiter    : bpy.props.StringProperty( name='StringDelimiter',     default="" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseStringDelimiter','m_WriteToOutputString','m_FieldDelimiter','m_FileName','m_StringDelimiter',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKDelimitedTextWriter )        
TYPENAMES.append('VTKDelimitedTextWriterType' )

#--------------------------------------------------------------
class VTKEnSightWriter(Node, BVTK_Node):

    bl_idname = 'VTKEnSightWriterType'
    bl_label  = 'vtkEnSightWriter'
    
    m_TransientGeometry: bpy.props.BoolProperty  ( name='TransientGeometry', default=False )
    m_BaseName         : bpy.props.StringProperty( name='BaseName',          default="" )
    m_FileName         : bpy.props.StringProperty( name='FileName',          default="", subtype='FILE_PATH' )
    m_Path             : bpy.props.StringProperty( name='Path',              default="" )
    m_GhostLevel       : bpy.props.IntProperty   ( name='GhostLevel',        default=0 )
    m_NumberOfBlocks   : bpy.props.IntProperty   ( name='NumberOfBlocks',    default=0 )
    m_ProcessNumber    : bpy.props.IntProperty   ( name='ProcessNumber',     default=0 )
    m_TimeStep         : bpy.props.IntProperty   ( name='TimeStep',          default=0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_TransientGeometry','m_BaseName','m_FileName','m_Path','m_GhostLevel','m_NumberOfBlocks','m_ProcessNumber','m_TimeStep',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKEnSightWriter )        
TYPENAMES.append('VTKEnSightWriterType' )

#--------------------------------------------------------------
class VTKExodusIIWriter(Node, BVTK_Node):

    bl_idname = 'VTKExodusIIWriterType'
    bl_label  = 'vtkExodusIIWriter'
    
    m_IgnoreMetaDataWarning       : bpy.props.BoolProperty  ( name='IgnoreMetaDataWarning',        default=False )
    m_WriteAllTimeSteps           : bpy.props.BoolProperty  ( name='WriteAllTimeSteps',            default=True )
    m_WriteOutBlockIdArray        : bpy.props.BoolProperty  ( name='WriteOutBlockIdArray',         default=True )
    m_WriteOutGlobalElementIdArray: bpy.props.BoolProperty  ( name='WriteOutGlobalElementIdArray', default=True )
    m_WriteOutGlobalNodeIdArray   : bpy.props.BoolProperty  ( name='WriteOutGlobalNodeIdArray',    default=True )
    m_BlockIdArrayName            : bpy.props.StringProperty( name='BlockIdArrayName',             default="" )
    m_FileName                    : bpy.props.StringProperty( name='FileName',                     default="", subtype='FILE_PATH' )
    m_GhostLevel                  : bpy.props.IntProperty   ( name='GhostLevel',                   default=0 )
    m_StoreDoubles                : bpy.props.IntProperty   ( name='StoreDoubles',                 default=-1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_IgnoreMetaDataWarning','m_WriteAllTimeSteps','m_WriteOutBlockIdArray','m_WriteOutGlobalElementIdArray','m_WriteOutGlobalNodeIdArray','m_BlockIdArrayName','m_FileName','m_GhostLevel','m_StoreDoubles',]
    def m_connections( self ):
        return (['input'], [], ['ModelMetadata'], []) 
    
add_class( VTKExodusIIWriter )        
TYPENAMES.append('VTKExodusIIWriterType' )

#--------------------------------------------------------------
class VTKFacetWriter(Node, BVTK_Node):

    bl_idname = 'VTKFacetWriterType'
    bl_label  = 'vtkFacetWriter'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKFacetWriter )        
TYPENAMES.append('VTKFacetWriterType' )

#--------------------------------------------------------------
class VTKGenericDataObjectWriter(Node, BVTK_Node):

    bl_idname = 'VTKGenericDataObjectWriterType'
    bl_label  = 'vtkGenericDataObjectWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKGenericDataObjectWriter )        
TYPENAMES.append('VTKGenericDataObjectWriterType' )

#--------------------------------------------------------------
class VTKGraphWriter(Node, BVTK_Node):

    bl_idname = 'VTKGraphWriterType'
    bl_label  = 'vtkGraphWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKGraphWriter )        
TYPENAMES.append('VTKGraphWriterType' )

#--------------------------------------------------------------
class VTKHoudiniPolyDataWriter(Node, BVTK_Node):

    bl_idname = 'VTKHoudiniPolyDataWriterType'
    bl_label  = 'vtkHoudiniPolyDataWriter'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKHoudiniPolyDataWriter )        
TYPENAMES.append('VTKHoudiniPolyDataWriterType' )

#--------------------------------------------------------------
class VTKIVWriter(Node, BVTK_Node):

    bl_idname = 'VTKIVWriterType'
    bl_label  = 'vtkIVWriter'
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKIVWriter )        
TYPENAMES.append('VTKIVWriterType' )

#--------------------------------------------------------------
class VTKImageWriter(Node, BVTK_Node):

    bl_idname = 'VTKImageWriterType'
    bl_label  = 'vtkImageWriter'
    
    m_FileName          : bpy.props.StringProperty( name='FileName',           default="", subtype='FILE_PATH' )
    m_FilePattern       : bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix        : bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality: bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKImageWriter )        
TYPENAMES.append('VTKImageWriterType' )

#--------------------------------------------------------------
class VTKJPEGWriter(Node, BVTK_Node):

    bl_idname = 'VTKJPEGWriterType'
    bl_label  = 'vtkJPEGWriter'
    
    m_Progressive       : bpy.props.BoolProperty  ( name='Progressive',        default=True )
    m_WriteToMemory     : bpy.props.BoolProperty  ( name='WriteToMemory',      default=True )
    m_FileName          : bpy.props.StringProperty( name='FileName',           default="", subtype='FILE_PATH' )
    m_FilePattern       : bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix        : bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality: bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    m_Quality           : bpy.props.IntProperty   ( name='Quality',            default=95 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Progressive','m_WriteToMemory','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_Quality',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKJPEGWriter )        
TYPENAMES.append('VTKJPEGWriterType' )

#--------------------------------------------------------------
class VTKJSONImageWriter(Node, BVTK_Node):

    bl_idname = 'VTKJSONImageWriterType'
    bl_label  = 'vtkJSONImageWriter'
    
    m_ArrayName: bpy.props.StringProperty( name='ArrayName', default="" )
    m_FileName : bpy.props.StringProperty( name='FileName',  default="", subtype='FILE_PATH' )
    m_Slice    : bpy.props.IntProperty   ( name='Slice',     default=-1 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ArrayName','m_FileName','m_Slice',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKJSONImageWriter )        
TYPENAMES.append('VTKJSONImageWriterType' )

#--------------------------------------------------------------
class VTKJavaScriptDataWriter(Node, BVTK_Node):

    bl_idname = 'VTKJavaScriptDataWriterType'
    bl_label  = 'vtkJavaScriptDataWriter'
    
    m_IncludeFieldNames: bpy.props.BoolProperty  ( name='IncludeFieldNames', default=True )
    m_FileName         : bpy.props.StringProperty( name='FileName',          default="", subtype='FILE_PATH' )
    m_VariableName     : bpy.props.StringProperty( name='VariableName',      default="data" )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_IncludeFieldNames','m_FileName','m_VariableName',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKJavaScriptDataWriter )        
TYPENAMES.append('VTKJavaScriptDataWriterType' )

#--------------------------------------------------------------
class VTKMCubesWriter(Node, BVTK_Node):

    bl_idname = 'VTKMCubesWriterType'
    bl_label  = 'vtkMCubesWriter'
    
    m_FileName      : bpy.props.StringProperty( name='FileName',       default="", subtype='FILE_PATH' )
    m_LimitsFileName: bpy.props.StringProperty( name='LimitsFileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','m_LimitsFileName',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKMCubesWriter )        
TYPENAMES.append('VTKMCubesWriterType' )

#--------------------------------------------------------------
class VTKMINCImageWriter(Node, BVTK_Node):

    bl_idname = 'VTKMINCImageWriterType'
    bl_label  = 'vtkMINCImageWriter'
    
    m_StrictValidation  : bpy.props.BoolProperty  ( name='StrictValidation',   default=True )
    m_FileName          : bpy.props.StringProperty( name='FileName',           default="", subtype='FILE_PATH' )
    m_FilePattern       : bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix        : bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_HistoryAddition   : bpy.props.StringProperty( name='HistoryAddition',    default="" )
    m_FileDimensionality: bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    m_RescaleIntercept  : bpy.props.FloatProperty ( name='RescaleIntercept',   default=0.0 )
    m_RescaleSlope      : bpy.props.FloatProperty ( name='RescaleSlope',       default=0.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_StrictValidation','m_FileName','m_FilePattern','m_FilePrefix','m_HistoryAddition','m_FileDimensionality','m_RescaleIntercept','m_RescaleSlope',]
    def m_connections( self ):
        return (['input'], [], ['DirectionCosines', 'ImageAttributes'], []) 
    
add_class( VTKMINCImageWriter )        
TYPENAMES.append('VTKMINCImageWriterType' )

#--------------------------------------------------------------
class VTKMNIObjectWriter(Node, BVTK_Node):

    bl_idname = 'VTKMNIObjectWriterType'
    bl_label  = 'vtkMNIObjectWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    e_FileType: bpy.props.EnumProperty  ( name='FileType', default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], ['LookupTable', 'Mapper', 'Property'], []) 
    
add_class( VTKMNIObjectWriter )        
TYPENAMES.append('VTKMNIObjectWriterType' )

#--------------------------------------------------------------
class VTKMNITagPointWriter(Node, BVTK_Node):

    bl_idname = 'VTKMNITagPointWriterType'
    bl_label  = 'vtkMNITagPointWriter'
    
    m_Comments: bpy.props.StringProperty( name='Comments', default="" )
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Comments','m_FileName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], [], ['LabelText', 'PatientIds', 'StructureIds', 'Weights'], []) 
    
add_class( VTKMNITagPointWriter )        
TYPENAMES.append('VTKMNITagPointWriterType' )

#--------------------------------------------------------------
class VTKMNITransformWriter(Node, BVTK_Node):

    bl_idname = 'VTKMNITransformWriterType'
    bl_label  = 'vtkMNITransformWriter'
    
    m_Comments: bpy.props.StringProperty( name='Comments', default="" )
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Comments','m_FileName',]
    def m_connections( self ):
        return ([], [], ['Transform'], []) 
    
add_class( VTKMNITransformWriter )        
TYPENAMES.append('VTKMNITransformWriterType' )

#--------------------------------------------------------------
class VTKMetaImageWriter(Node, BVTK_Node):

    bl_idname = 'VTKMetaImageWriterType'
    bl_label  = 'vtkMetaImageWriter'
    
    m_Compression       : bpy.props.BoolProperty  ( name='Compression',        default=True )
    m_FileName          : bpy.props.StringProperty( name='FileName',           default="", subtype='FILE_PATH' )
    m_FilePattern       : bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix        : bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_RAWFileName       : bpy.props.StringProperty( name='RAWFileName',        default="", subtype='FILE_PATH' )
    m_FileDimensionality: bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Compression','m_FileName','m_FilePattern','m_FilePrefix','m_RAWFileName','m_FileDimensionality',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKMetaImageWriter )        
TYPENAMES.append('VTKMetaImageWriterType' )

#--------------------------------------------------------------
class VTKNIFTIImageWriter(Node, BVTK_Node):

    bl_idname = 'VTKNIFTIImageWriterType'
    bl_label  = 'vtkNIFTIImageWriter'
    
    m_PlanarRGB         : bpy.props.BoolProperty  ( name='PlanarRGB',          default=False )
    m_Description       : bpy.props.StringProperty( name='Description',        default="VTK8.1.2" )
    m_FileName          : bpy.props.StringProperty( name='FileName',           default="", subtype='FILE_PATH' )
    m_FilePattern       : bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix        : bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality: bpy.props.IntProperty   ( name='FileDimensionality', default=3 )
    m_NIFTIVersion      : bpy.props.IntProperty   ( name='NIFTIVersion',       default=0 )
    m_TimeDimension     : bpy.props.IntProperty   ( name='TimeDimension',      default=0 )
    m_QFac              : bpy.props.FloatProperty ( name='QFac',               default=0.0 )
    m_RescaleIntercept  : bpy.props.FloatProperty ( name='RescaleIntercept',   default=0.0 )
    m_RescaleSlope      : bpy.props.FloatProperty ( name='RescaleSlope',       default=0.0 )
    m_TimeSpacing       : bpy.props.FloatProperty ( name='TimeSpacing',        default=1.0 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PlanarRGB','m_Description','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_NIFTIVersion','m_TimeDimension','m_QFac','m_RescaleIntercept','m_RescaleSlope','m_TimeSpacing',]
    def m_connections( self ):
        return (['input'], [], ['NIFTIHeader', 'QFormMatrix', 'SFormMatrix'], []) 
    
add_class( VTKNIFTIImageWriter )        
TYPENAMES.append('VTKNIFTIImageWriterType' )

#--------------------------------------------------------------
class VTKNewickTreeWriter(Node, BVTK_Node):

    bl_idname = 'VTKNewickTreeWriterType'
    bl_label  = 'vtkNewickTreeWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_EdgeWeightArrayName: bpy.props.StringProperty( name='EdgeWeightArrayName', default="weight" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NodeNameArrayName  : bpy.props.StringProperty( name='NodeNameArrayName',   default="node name" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_EdgeWeightArrayName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NodeNameArrayName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKNewickTreeWriter )        
TYPENAMES.append('VTKNewickTreeWriterType' )

#--------------------------------------------------------------
class VTKOggTheoraWriter(Node, BVTK_Node):

    bl_idname = 'VTKOggTheoraWriterType'
    bl_label  = 'vtkOggTheoraWriter'
    
    m_Subsampling: bpy.props.BoolProperty  ( name='Subsampling', default=True )
    m_FileName   : bpy.props.StringProperty( name='FileName',    default="", subtype='FILE_PATH' )
    m_Quality    : bpy.props.IntProperty   ( name='Quality',     default=2 )
    m_Rate       : bpy.props.IntProperty   ( name='Rate',        default=25 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Subsampling','m_FileName','m_Quality','m_Rate',]
    def m_connections( self ):
        return (['input'], ['output'], [], []) 
    
add_class( VTKOggTheoraWriter )        
TYPENAMES.append('VTKOggTheoraWriterType' )

#--------------------------------------------------------------
class VTKPDataSetWriter(Node, BVTK_Node):

    bl_idname = 'VTKPDataSetWriterType'
    bl_label  = 'vtkPDataSetWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_UseRelativeFileNames: bpy.props.BoolProperty  ( name='UseRelativeFileNames', default=True )
    m_WriteArrayMetaData  : bpy.props.BoolProperty  ( name='WriteArrayMetaData',   default=True )
    m_WriteToOutputString : bpy.props.BoolProperty  ( name='WriteToOutputString',  default=True )
    m_EdgeFlagsName       : bpy.props.StringProperty( name='EdgeFlagsName',        default="" )
    m_FieldDataName       : bpy.props.StringProperty( name='FieldDataName',        default="FieldData" )
    m_FileName            : bpy.props.StringProperty( name='FileName',             default="", subtype='FILE_PATH' )
    m_FilePattern         : bpy.props.StringProperty( name='FilePattern',          default="%s.%d.vtk" )
    m_GlobalIdsName       : bpy.props.StringProperty( name='GlobalIdsName',        default="" )
    m_Header              : bpy.props.StringProperty( name='Header',               default="vtk output" )
    m_LookupTableName     : bpy.props.StringProperty( name='LookupTableName',      default="lookup_table" )
    m_NormalsName         : bpy.props.StringProperty( name='NormalsName',          default="" )
    m_PedigreeIdsName     : bpy.props.StringProperty( name='PedigreeIdsName',      default="" )
    m_ScalarsName         : bpy.props.StringProperty( name='ScalarsName',          default="" )
    m_TCoordsName         : bpy.props.StringProperty( name='TCoordsName',          default="" )
    m_TensorsName         : bpy.props.StringProperty( name='TensorsName',          default="" )
    m_VectorsName         : bpy.props.StringProperty( name='VectorsName',          default="" )
    m_EndPiece            : bpy.props.IntProperty   ( name='EndPiece',             default=0 )
    m_GhostLevel          : bpy.props.IntProperty   ( name='GhostLevel',           default=0 )
    m_NumberOfPieces      : bpy.props.IntProperty   ( name='NumberOfPieces',       default=1 )
    m_StartPiece          : bpy.props.IntProperty   ( name='StartPiece',           default=0 )
    e_FileType            : bpy.props.EnumProperty  ( name='FileType',             default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=21, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseRelativeFileNames','m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_FilePattern','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_StartPiece','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKPDataSetWriter )        
TYPENAMES.append('VTKPDataSetWriterType' )

#--------------------------------------------------------------
class VTKPImageWriter(Node, BVTK_Node):

    bl_idname = 'VTKPImageWriterType'
    bl_label  = 'vtkPImageWriter'
    
    m_FileName          : bpy.props.StringProperty( name='FileName',           default="", subtype='FILE_PATH' )
    m_FilePattern       : bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix        : bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality: bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    m_MemoryLimit       : bpy.props.IntProperty   ( name='MemoryLimit',        default=1048576 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_MemoryLimit',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKPImageWriter )        
TYPENAMES.append('VTKPImageWriterType' )

#--------------------------------------------------------------
class VTKPLYWriter(Node, BVTK_Node):

    bl_idname = 'VTKPLYWriterType'
    bl_label  = 'vtkPLYWriter'
    e_ColorMode_items=[ (x,x,x) for x in ['Default', 'UniformCellColor', 'UniformPointColor', 'UniformColor', 'Off']]
    e_DataByteOrder_items=[ (x,x,x) for x in ['LittleEndian', 'BigEndian']]
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    e_TextureCoordinatesName_items=[ (x,x,x) for x in ['UV', 'TextureUV']]
    
    m_EnableAlpha           : bpy.props.BoolProperty     ( name='EnableAlpha',            default=False )
    m_ArrayName             : bpy.props.StringProperty   ( name='ArrayName',              default="" )
    m_FileName              : bpy.props.StringProperty   ( name='FileName',               default="", subtype='FILE_PATH' )
    m_Alpha                 : bpy.props.IntProperty      ( name='Alpha',                  default=255 )
    m_Component             : bpy.props.IntProperty      ( name='Component',              default=0 )
    e_ColorMode             : bpy.props.EnumProperty     ( name='ColorMode',              default="Default", items=e_ColorMode_items )
    e_DataByteOrder         : bpy.props.EnumProperty     ( name='DataByteOrder',          default="LittleEndian", items=e_DataByteOrder_items )
    e_FileType              : bpy.props.EnumProperty     ( name='FileType',               default="Binary", items=e_FileType_items )
    e_TextureCoordinatesName: bpy.props.EnumProperty     ( name='TextureCoordinatesName', default="UV", items=e_TextureCoordinatesName_items )
    m_Color                 : bpy.props.IntVectorProperty( name='Color',                  default=[255, 255, 255], size=3 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableAlpha','m_ArrayName','m_FileName','m_Alpha','m_Component','e_ColorMode','e_DataByteOrder','e_FileType','e_TextureCoordinatesName','m_Color',]
    def m_connections( self ):
        return (['input'], [], ['LookupTable'], []) 
    
add_class( VTKPLYWriter )        
TYPENAMES.append('VTKPLYWriterType' )

#--------------------------------------------------------------
class VTKPNGWriter(Node, BVTK_Node):

    bl_idname = 'VTKPNGWriterType'
    bl_label  = 'vtkPNGWriter'
    
    m_WriteToMemory     : bpy.props.BoolProperty  ( name='WriteToMemory',      default=True )
    m_FileName          : bpy.props.StringProperty( name='FileName',           default="", subtype='FILE_PATH' )
    m_FilePattern       : bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix        : bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_CompressionLevel  : bpy.props.IntProperty   ( name='CompressionLevel',   default=5 )
    m_FileDimensionality: bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteToMemory','m_FileName','m_FilePattern','m_FilePrefix','m_CompressionLevel','m_FileDimensionality',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKPNGWriter )        
TYPENAMES.append('VTKPNGWriterType' )

#--------------------------------------------------------------
class VTKPNMWriter(Node, BVTK_Node):

    bl_idname = 'VTKPNMWriterType'
    bl_label  = 'vtkPNMWriter'
    
    m_FileName          : bpy.props.StringProperty( name='FileName',           default="", subtype='FILE_PATH' )
    m_FilePattern       : bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix        : bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality: bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKPNMWriter )        
TYPENAMES.append('VTKPNMWriterType' )

#--------------------------------------------------------------
class VTKPhyloXMLTreeWriter(Node, BVTK_Node):

    bl_idname = 'VTKPhyloXMLTreeWriterType'
    bl_label  = 'vtkPhyloXMLTreeWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeWeightArrayName: bpy.props.StringProperty( name='EdgeWeightArrayName', default="weight" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_NodeNameArrayName  : bpy.props.StringProperty( name='NodeNameArrayName',   default="node name" )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_EdgeWeightArrayName','m_FileName','m_NodeNameArrayName','m_BlockSize','m_NumberOfTimeSteps','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKPhyloXMLTreeWriter )        
TYPENAMES.append('VTKPhyloXMLTreeWriterType' )

#--------------------------------------------------------------
class VTKPolyDataWriter(Node, BVTK_Node):

    bl_idname = 'VTKPolyDataWriterType'
    bl_label  = 'vtkPolyDataWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKPolyDataWriter )        
TYPENAMES.append('VTKPolyDataWriterType' )

#--------------------------------------------------------------
class VTKPostScriptWriter(Node, BVTK_Node):

    bl_idname = 'VTKPostScriptWriterType'
    bl_label  = 'vtkPostScriptWriter'
    
    m_FileName          : bpy.props.StringProperty( name='FileName',           default="", subtype='FILE_PATH' )
    m_FilePattern       : bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix        : bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality: bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKPostScriptWriter )        
TYPENAMES.append('VTKPostScriptWriterType' )

#--------------------------------------------------------------
class VTKRectilinearGridWriter(Node, BVTK_Node):

    bl_idname = 'VTKRectilinearGridWriterType'
    bl_label  = 'vtkRectilinearGridWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteExtent        : bpy.props.BoolProperty  ( name='WriteExtent',         default=False )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteExtent','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKRectilinearGridWriter )        
TYPENAMES.append('VTKRectilinearGridWriterType' )

#--------------------------------------------------------------
class VTKSTLWriter(Node, BVTK_Node):

    bl_idname = 'VTKSTLWriterType'
    bl_label  = 'vtkSTLWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_FileName: bpy.props.StringProperty( name='FileName', default="", subtype='FILE_PATH' )
    m_Header  : bpy.props.StringProperty( name='Header',   default="Visualization Toolkit generated SLA File                                        " )
    e_FileType: bpy.props.EnumProperty  ( name='FileType', default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','m_Header','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKSTLWriter )        
TYPENAMES.append('VTKSTLWriterType' )

#--------------------------------------------------------------
class VTKSimplePointsWriter(Node, BVTK_Node):

    bl_idname = 'VTKSimplePointsWriterType'
    bl_label  = 'vtkSimplePointsWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    m_DecimalPrecision   : bpy.props.IntProperty   ( name='DecimalPrecision',    default=6 )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_DecimalPrecision','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKSimplePointsWriter )        
TYPENAMES.append('VTKSimplePointsWriterType' )

#--------------------------------------------------------------
class VTKStructuredGridWriter(Node, BVTK_Node):

    bl_idname = 'VTKStructuredGridWriterType'
    bl_label  = 'vtkStructuredGridWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteExtent        : bpy.props.BoolProperty  ( name='WriteExtent',         default=False )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteExtent','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKStructuredGridWriter )        
TYPENAMES.append('VTKStructuredGridWriterType' )

#--------------------------------------------------------------
class VTKStructuredPointsWriter(Node, BVTK_Node):

    bl_idname = 'VTKStructuredPointsWriterType'
    bl_label  = 'vtkStructuredPointsWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteExtent        : bpy.props.BoolProperty  ( name='WriteExtent',         default=False )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteExtent','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKStructuredPointsWriter )        
TYPENAMES.append('VTKStructuredPointsWriterType' )

#--------------------------------------------------------------
class VTKTIFFWriter(Node, BVTK_Node):

    bl_idname = 'VTKTIFFWriterType'
    bl_label  = 'vtkTIFFWriter'
    e_Compression_items=[ (x,x,x) for x in ['NoCompression', 'PackBits', 'JPEG', 'Deflate', 'LZW']]
    
    m_FileName          : bpy.props.StringProperty( name='FileName',           default="", subtype='FILE_PATH' )
    m_FilePattern       : bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix        : bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality: bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    e_Compression       : bpy.props.EnumProperty  ( name='Compression',        default="PackBits", items=e_Compression_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','e_Compression',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKTIFFWriter )        
TYPENAMES.append('VTKTIFFWriterType' )

#--------------------------------------------------------------
class VTKTableToSQLiteWriter(Node, BVTK_Node):

    bl_idname = 'VTKTableToSQLiteWriterType'
    bl_label  = 'vtkTableToSQLiteWriter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKTableToSQLiteWriter )        
TYPENAMES.append('VTKTableToSQLiteWriterType' )

#--------------------------------------------------------------
class VTKTableWriter(Node, BVTK_Node):

    bl_idname = 'VTKTableWriterType'
    bl_label  = 'vtkTableWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKTableWriter )        
TYPENAMES.append('VTKTableWriterType' )

#--------------------------------------------------------------
class VTKTreeWriter(Node, BVTK_Node):

    bl_idname = 'VTKTreeWriterType'
    bl_label  = 'vtkTreeWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKTreeWriter )        
TYPENAMES.append('VTKTreeWriterType' )

#--------------------------------------------------------------
class VTKUnstructuredGridWriter(Node, BVTK_Node):

    bl_idname = 'VTKUnstructuredGridWriterType'
    bl_label  = 'vtkUnstructuredGridWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData : bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_EdgeFlagsName      : bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName      : bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_GlobalIdsName      : bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header             : bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName    : bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName        : bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName    : bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName        : bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName        : bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName        : bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName        : bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType           : bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKUnstructuredGridWriter )        
TYPENAMES.append('VTKUnstructuredGridWriterType' )

#--------------------------------------------------------------
class VTKXMLDataObjectWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLDataObjectWriterType'
    bl_label  = 'vtkXMLDataObjectWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_NumberOfTimeSteps','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLDataObjectWriter )        
TYPENAMES.append('VTKXMLDataObjectWriterType' )

#--------------------------------------------------------------
class VTKXMLDataSetWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLDataSetWriterType'
    bl_label  = 'vtkXMLDataSetWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_NumberOfTimeSteps','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLDataSetWriter )        
TYPENAMES.append('VTKXMLDataSetWriterType' )

#--------------------------------------------------------------
class VTKXMLHierarchicalBoxDataWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLHierarchicalBoxDataWriterType'
    bl_label  = 'vtkXMLHierarchicalBoxDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WriteMetaFile      : bpy.props.IntProperty   ( name='WriteMetaFile',       default=1 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLHierarchicalBoxDataWriter )        
TYPENAMES.append('VTKXMLHierarchicalBoxDataWriterType' )

#--------------------------------------------------------------
class VTKXMLHyperOctreeWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLHyperOctreeWriterType'
    bl_label  = 'vtkXMLHyperOctreeWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_NumberOfTimeSteps','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLHyperOctreeWriter )        
TYPENAMES.append('VTKXMLHyperOctreeWriterType' )

#--------------------------------------------------------------
class VTKXMLImageDataWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLImageDataWriterType'
    bl_label  = 'vtkXMLImageDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty     ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty     ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty      ( name='BlockSize',           default=32768 )
    m_GhostLevel         : bpy.props.IntProperty      ( name='GhostLevel',          default=0 )
    m_NumberOfPieces     : bpy.props.IntProperty      ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty      ( name='NumberOfTimeSteps',   default=1 )
    m_WritePiece         : bpy.props.IntProperty      ( name='WritePiece',          default=-1 )
    e_ByteOrder          : bpy.props.EnumProperty     ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty     ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty     ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty     ( name='IdType',              default="Int64", items=e_IdType_items )
    m_WriteExtent        : bpy.props.IntVectorProperty( name='WriteExtent',         default=[0, -1, 0, -1, 0, -1], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType','m_WriteExtent',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLImageDataWriter )        
TYPENAMES.append('VTKXMLImageDataWriterType' )

#--------------------------------------------------------------
class VTKXMLMultiBlockDataWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLMultiBlockDataWriterType'
    bl_label  = 'vtkXMLMultiBlockDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WriteMetaFile      : bpy.props.IntProperty   ( name='WriteMetaFile',       default=1 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLMultiBlockDataWriter )        
TYPENAMES.append('VTKXMLMultiBlockDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPDataSetWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLPDataSetWriterType'
    bl_label  = 'vtkXMLPDataSetWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_UseSubdirectory    : bpy.props.BoolProperty  ( name='UseSubdirectory',     default=False )
    m_WriteSummaryFile   : bpy.props.BoolProperty  ( name='WriteSummaryFile',    default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_EndPiece           : bpy.props.IntProperty   ( name='EndPiece',            default=0 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces     : bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece         : bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteToOutputString','m_FileName','m_BlockSize','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLPDataSetWriter )        
TYPENAMES.append('VTKXMLPDataSetWriterType' )

#--------------------------------------------------------------
class VTKXMLPHierarchicalBoxDataWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLPHierarchicalBoxDataWriterType'
    bl_label  = 'vtkXMLPHierarchicalBoxDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WriteMetaFile      : bpy.props.IntProperty   ( name='WriteMetaFile',       default=1 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLPHierarchicalBoxDataWriter )        
TYPENAMES.append('VTKXMLPHierarchicalBoxDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPImageDataWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLPImageDataWriterType'
    bl_label  = 'vtkXMLPImageDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_UseSubdirectory    : bpy.props.BoolProperty  ( name='UseSubdirectory',     default=False )
    m_WriteSummaryFile   : bpy.props.BoolProperty  ( name='WriteSummaryFile',    default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_EndPiece           : bpy.props.IntProperty   ( name='EndPiece',            default=0 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces     : bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece         : bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteToOutputString','m_FileName','m_BlockSize','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLPImageDataWriter )        
TYPENAMES.append('VTKXMLPImageDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPMultiBlockDataWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLPMultiBlockDataWriterType'
    bl_label  = 'vtkXMLPMultiBlockDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces     : bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece         : bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    m_WriteMetaFile      : bpy.props.IntProperty   ( name='WriteMetaFile',       default=1 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLPMultiBlockDataWriter )        
TYPENAMES.append('VTKXMLPMultiBlockDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPPolyDataWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLPPolyDataWriterType'
    bl_label  = 'vtkXMLPPolyDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_UseSubdirectory    : bpy.props.BoolProperty  ( name='UseSubdirectory',     default=False )
    m_WriteSummaryFile   : bpy.props.BoolProperty  ( name='WriteSummaryFile',    default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_EndPiece           : bpy.props.IntProperty   ( name='EndPiece',            default=0 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces     : bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece         : bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteToOutputString','m_FileName','m_BlockSize','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLPPolyDataWriter )        
TYPENAMES.append('VTKXMLPPolyDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPRectilinearGridWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLPRectilinearGridWriterType'
    bl_label  = 'vtkXMLPRectilinearGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_UseSubdirectory    : bpy.props.BoolProperty  ( name='UseSubdirectory',     default=False )
    m_WriteSummaryFile   : bpy.props.BoolProperty  ( name='WriteSummaryFile',    default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_EndPiece           : bpy.props.IntProperty   ( name='EndPiece',            default=0 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces     : bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece         : bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteToOutputString','m_FileName','m_BlockSize','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLPRectilinearGridWriter )        
TYPENAMES.append('VTKXMLPRectilinearGridWriterType' )

#--------------------------------------------------------------
class VTKXMLPStructuredGridWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLPStructuredGridWriterType'
    bl_label  = 'vtkXMLPStructuredGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_UseSubdirectory    : bpy.props.BoolProperty  ( name='UseSubdirectory',     default=False )
    m_WriteSummaryFile   : bpy.props.BoolProperty  ( name='WriteSummaryFile',    default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_EndPiece           : bpy.props.IntProperty   ( name='EndPiece',            default=0 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces     : bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece         : bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteToOutputString','m_FileName','m_BlockSize','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLPStructuredGridWriter )        
TYPENAMES.append('VTKXMLPStructuredGridWriterType' )

#--------------------------------------------------------------
class VTKXMLPTableWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLPTableWriterType'
    bl_label  = 'vtkXMLPTableWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_UseSubdirectory    : bpy.props.BoolProperty  ( name='UseSubdirectory',     default=False )
    m_WriteSummaryFile   : bpy.props.BoolProperty  ( name='WriteSummaryFile',    default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_EndPiece           : bpy.props.IntProperty   ( name='EndPiece',            default=0 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces     : bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece         : bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteToOutputString','m_FileName','m_BlockSize','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLPTableWriter )        
TYPENAMES.append('VTKXMLPTableWriterType' )

#--------------------------------------------------------------
class VTKXMLPUniformGridAMRWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLPUniformGridAMRWriterType'
    bl_label  = 'vtkXMLPUniformGridAMRWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WriteMetaFile      : bpy.props.IntProperty   ( name='WriteMetaFile',       default=1 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLPUniformGridAMRWriter )        
TYPENAMES.append('VTKXMLPUniformGridAMRWriterType' )

#--------------------------------------------------------------
class VTKXMLPUnstructuredGridWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLPUnstructuredGridWriterType'
    bl_label  = 'vtkXMLPUnstructuredGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_UseSubdirectory    : bpy.props.BoolProperty  ( name='UseSubdirectory',     default=False )
    m_WriteSummaryFile   : bpy.props.BoolProperty  ( name='WriteSummaryFile',    default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_EndPiece           : bpy.props.IntProperty   ( name='EndPiece',            default=0 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces     : bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece         : bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteToOutputString','m_FileName','m_BlockSize','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLPUnstructuredGridWriter )        
TYPENAMES.append('VTKXMLPUnstructuredGridWriterType' )

#--------------------------------------------------------------
class VTKXMLPolyDataWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLPolyDataWriterType'
    bl_label  = 'vtkXMLPolyDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces     : bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WritePiece         : bpy.props.IntProperty   ( name='WritePiece',          default=-1 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLPolyDataWriter )        
TYPENAMES.append('VTKXMLPolyDataWriterType' )

#--------------------------------------------------------------
class VTKXMLRectilinearGridWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLRectilinearGridWriterType'
    bl_label  = 'vtkXMLRectilinearGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty     ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty     ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty      ( name='BlockSize',           default=32768 )
    m_GhostLevel         : bpy.props.IntProperty      ( name='GhostLevel',          default=0 )
    m_NumberOfPieces     : bpy.props.IntProperty      ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty      ( name='NumberOfTimeSteps',   default=1 )
    m_WritePiece         : bpy.props.IntProperty      ( name='WritePiece',          default=-1 )
    e_ByteOrder          : bpy.props.EnumProperty     ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty     ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty     ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty     ( name='IdType',              default="Int64", items=e_IdType_items )
    m_WriteExtent        : bpy.props.IntVectorProperty( name='WriteExtent',         default=[0, -1, 0, -1, 0, -1], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType','m_WriteExtent',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLRectilinearGridWriter )        
TYPENAMES.append('VTKXMLRectilinearGridWriterType' )

#--------------------------------------------------------------
class VTKXMLStructuredGridWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLStructuredGridWriterType'
    bl_label  = 'vtkXMLStructuredGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty     ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty     ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty   ( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty      ( name='BlockSize',           default=32768 )
    m_GhostLevel         : bpy.props.IntProperty      ( name='GhostLevel',          default=0 )
    m_NumberOfPieces     : bpy.props.IntProperty      ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty      ( name='NumberOfTimeSteps',   default=1 )
    m_WritePiece         : bpy.props.IntProperty      ( name='WritePiece',          default=-1 )
    e_ByteOrder          : bpy.props.EnumProperty     ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty     ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty     ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty     ( name='IdType',              default="Int64", items=e_IdType_items )
    m_WriteExtent        : bpy.props.IntVectorProperty( name='WriteExtent',         default=[0, -1, 0, -1, 0, -1], size=6 )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType','m_WriteExtent',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLStructuredGridWriter )        
TYPENAMES.append('VTKXMLStructuredGridWriterType' )

#--------------------------------------------------------------
class VTKXMLTableWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLTableWriterType'
    bl_label  = 'vtkXMLTableWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_NumberOfPieces     : bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WritePiece         : bpy.props.IntProperty   ( name='WritePiece',          default=-1 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLTableWriter )        
TYPENAMES.append('VTKXMLTableWriterType' )

#--------------------------------------------------------------
class VTKXMLUniformGridAMRWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLUniformGridAMRWriterType'
    bl_label  = 'vtkXMLUniformGridAMRWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WriteMetaFile      : bpy.props.IntProperty   ( name='WriteMetaFile',       default=1 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLUniformGridAMRWriter )        
TYPENAMES.append('VTKXMLUniformGridAMRWriterType' )

#--------------------------------------------------------------
class VTKXMLUnstructuredGridWriter(Node, BVTK_Node):

    bl_idname = 'VTKXMLUnstructuredGridWriterType'
    bl_label  = 'vtkXMLUnstructuredGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData : bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=True )
    m_WriteToOutputString: bpy.props.BoolProperty  ( name='WriteToOutputString', default=True )
    m_FileName           : bpy.props.StringProperty( name='FileName',            default="", subtype='FILE_PATH' )
    m_BlockSize          : bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel         : bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces     : bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps  : bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WritePiece         : bpy.props.IntProperty   ( name='WritePiece',          default=-1 )
    e_ByteOrder          : bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode           : bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType         : bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType             : bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['input'], [], [], []) 
    
add_class( VTKXMLUnstructuredGridWriter )        
TYPENAMES.append('VTKXMLUnstructuredGridWriterType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( BVTK_NodeCategory( 'Writer', 'Writer', items=menu_items) )