import vtk
from vtk.util.vtkAlgorithm import VTKPythonAlgorithmBase

class bvtkSetActiveAttribute(VTKPythonAlgorithmBase):
    """ VTK algorithm for setting active attributes.
    This allows the setting of attibutes for Point or Cell fields
    to be integrated into VTK pipelines and executed on Update().

    Resources:
    https://blog.kitware.com/vtkpythonalgorithm-is-great/
    https://github.com/Kitware/VTK/blob/master/Common/DataModel/Testing/Python/TestPartitionedData.py
    """
    def __init__(self):
        VTKPythonAlgorithmBase.__init__(self,
            nInputPorts=1, inputType='vtkDataSet',
            nOutputPorts=1, outputType='vtkDataObject')

        self.field_types = ["Point", "Cell"]
        # Valid attributes we can set, https://vtk.org/doc/nightly/html/classvtkDataSetAttributes.html
        self.attribute_types = ['Scalars', 'Vectors', 'Normals', 'Tangets', 'TCoords', 'Tensors', \
            'GlobalIds', 'PedigreeIds', 'RationalWeights', 'HigherOrderDegrees']
        self.vtk_field_type = None
        self.vtk_attribute = None
        self.vtk_array_name = None

    def SetFieldType(self, field:str):
        """Set field type
        """
        assert field in self.field_types, "Invalid field type, should be Point or Cell"
        self.vtk_field_type = field

    def SetAttributeType(self, attrib:str):
        """Set attribute type
        """
        assert attrib in self.attribute_types, "Invalid attribute type"
        self.vtk_attribute = attrib

    def SetArrayName(self, name:str):
        """Set data array name
        """
        self.vtk_array_name = name

    def RequestDataObject(self, request, inInfo, outInfo):
        """Will be called before request data, so we can init output here
        """
        inp = vtk.vtkDataObject.GetData(inInfo[0])
        opt = vtk.vtkDataObject.GetData(outInfo)

        if opt and opt.IsA(inp.GetClassName()):
            return 1

        opt = inp.NewInstance()
        outInfo.GetInformationObject(0).Set(vtk.vtkDataObject.DATA_OBJECT(), opt)
        return 1

    def RequestData(self, request, inInfo, outInfo):
        """Called on update request
        """
        # Info inputs are always tuples, length is number of input/output ports
        input0 = vtk.vtkDataObject.GetData(inInfo[0])
        opt = vtk.vtkDataObject.GetData(outInfo)

        # If all necessary parameters have been set, attempt to set active attrib 
        if not self.vtk_field_type is None and not self.vtk_attribute is None and not self.vtk_array_name is None:

            if self.vtk_field_type == 'Point':
                if not hasattr(input0, 'GetPointData'): 
                    return 0
                field_data = input0.GetPointData()
            elif self.vtk_field_type == 'Cell':
                if not hasattr(input0, 'GetCellData'): 
                    return 0
                field_data = input0.GetCellData()
            
            # Data object must inherit vtkDataSetAttributes to have attributes
            if not issubclass(type(field_data), vtk.vtkDataSetAttributes):
                return 0

            # Check given array name is actually in data object
            array_names = []
            narray = field_data.GetNumberOfArrays()
            for i in range(narray):
                data_array = field_data.GetArray(i)
                array_names.append(data_array.GetName())
            if not self.vtk_array_name in array_names:
                return 0

            # Update vtk object active attribute
            cmd = 'field_data.SetActive' + self.vtk_attribute + '( "'+ self.vtk_array_name +'" )'
            exec(cmd, globals(), locals())

        opt.ShallowCopy(input0) # Just copy a pointer
        outInfo.GetInformationObject(0).Set(vtk.vtkDataObject.DATA_OBJECT(), opt)
        return 1
    
    def GetOutput(self, port:int = 0):
        # Not implmeneted in the VTKPythonAlgorithmBase
        # https://github.com/Kitware/VTK/blob/master/Wrapping/Python/vtkmodules/util/vtkAlgorithm.py
        return self.GetOutputDataObject(port)