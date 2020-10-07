import sys
import re
import vtk
#from vtk_patch import vtk

version = vtk.vtkVersion().GetVTKVersion()

BannedNames = (
'vtk', # not a class
'vtkAlgorithm', # abstract
'vtkAbstractInteractionDevice', # abstract
'vtkAbstractRenderDevice',  # abstract
'vtkInteractorStyleTrackball', # deprecated
'vtkStructuredPointsGeometryFilter', # deprecated
'vtkVolumeRayCastCompositeFunction', # deprecated
'vtkVolumeRayCastIsosurfaceFunction', # deprecated
'vtkVolumeRayCastMapper',# deprecated
'vtkVolumeRayCastMIPFunction', # deprecated
'vtkVolumeTextureMapper2D', # deprecated
'vtkVolumeTextureMapper3D',
'vtkOpenGLVolumeTextureMapper2D',# deprecated
'vtkOpenGLVolumeTextureMapper3D',# deprecated
'vtkOpenGLPolyDataMapper',# deprecated ??
'vtkRenderState',
'vtkRendererDelegate',
'vtkRenderWidget', # instantiate internally some deprecated class
'vtkThreadedSynchronizedTemplatesCutter3D', # some exposed feature are no more supported
'vtkSynchronizedTemplates3D', # some exposed feature are no more supported
'vtkNetCDFCAMReader', # got obsolete methods
'vtkQImageToImageSource', # need qt, requires VTK built with SIP support
'vtkThreadedSynchronizedTemplates3D', # give problem
'vtkSynchronizedTemplatesCutter3D',   # give problem

'vtkClipHyperOctree', #deprecated

#'vtkRenderedRepresentation',
#'vtkRenderedGraphRepresentation',
#'vtkRenderedHierarchyRepresentation',
#'vtkRenderedSurfaceRepresentation',
#'vtkRenderedTreeAreaRepresentation',

#'vtkConvexHull2D',        # take a Renderer as  input
#'vtkDistanceToCamera',    # take a Renderer as  input
#'vtkGeoAdaptiveArcs',     # take a Renderer as  input
#'vtkGraphToGlyps',        # take a Renderer as  input
#'vtkLabelPlacer',         # take a Renderer as  input
#'vtkSelectVisiblePoints', # take a Renderer as  input
#'vtkVolumeOutlineSource', # take a VolumeMapper as  input
#'vtkRendererSource',
#'vtkRenderLargeImage',

'vtkAxesActor',         # give problems
'vtkContextMouseEvent', # give problems (crash)
'vtkImageConvolve',     # non standard docs --  SetKernel7x7 ...

# Qt label rendering not supported.
'vtkGeoView'    ,
'vtkGeoView2D',
'vtkGraphLayoutView',
'vtkHierarchicalGraphView',
'vtkIcicleView',
'vtkParallelCoordinatesView',
'vtkRenderedTreeAreaRepresentation',
'vtkRenderView',
'vtkTreeAreaView',
'vtkTreeMapView',
'vtkTreeRingView',

#deprecated
'vtkHyperOctreeAlgorithm',
'vtkHyperOctreeClipCutPointsGrabber',
'vtkHyperOctreeContourFilter',
'vtkHyperOctreeCursor',
'vtkHyperOctreeCutter',
'vtkHyperOctreeDepth',
'vtkHyperOctreeFractalSource',
'vtkHyperOctreeLimiter',
'vtkHyperOctreePointsGrabber',
'vtkHyperOctreeSampleFunction',
'vtkHyperOctreeToUniformGridFilter',
'vtkHyperOctree',
'vtkXMLHyperOctreeReader',
'vtkXMLHyperOctreeWriter',
'vtkUGFacetReader',
'vtkSMPTransform',
'vtkSMPWarpVector',
'vtkSMPContourGridManyPieces',

'vtkInstantiator', # have deprecated methods

'vtkGraph',             # abstract ?
'vtkPiecewiseFunction', # abstract ?

'vtkCompositeDataPipeline' , # give problem
'vtkResliceImageViewer',     # give problem
)

HiddenMethods = (
'New',
'NewInstance',
'DeepCopy',
'ShallowCopy',
'GetClassName',
'IsA',
'IsTypeOf',
'SafeDownCast',
'GetErrorCode',
'BreakOnError',
'GetAddressAsString',
#'GetOutputIndex',
#'PrintRevisions',
#'SqueezeInputArray',
#'GetUserTransformMatrixMTime',
#'ApplyProperties',
#'ComputeMatrix',
#'SetRequestedRenderModeToRayCastAndTexture',
#'SetRequestedRenderModeToTexture',
#'ReleaseGraphicsResources',
#'RenderOpaqueGeometry',
#'RenderTranslucentGeometry',

'GetInput',
'SetInputData',
'GetOutput',
'SetOutput',
'GetPolyDataOutput',
'GetImageDataOutput',
'GetRectilinearGridOutput',
'GetStructuredGridOutput',
'GetStructuredPointsOutput',
'GetUnstructuredGridOutput',
)

HideKeywords = (
'__',
'AddInputData',
'Algorithm',
'AbortExecute',
'AsynchronousUpdate',
'AttributeMode',#deprecated  -- in vtkArrayCalculator
'BreakOnError',
'Controller',
'Command',
'Connection',
'Debug',
'DataObject',
'Delete',
'DisplayLists', # deprecated method of vtkGlyph3DMapper
'Executive',
'EndMethod',
'Event',
'ForceCompileOnly', #deprecated
'GetErrorCode',
'GetPolyDataInput',
'Ghost',
'GlobalWarning',
'GraphicsResources',
'ImmediateModeRendering', #deprecated
'Information',
'Initialize',
'InputArrayToProcess',
'MaterialMode', #deprecated
'MTime',
'Modified',
'Observer',
'Port',
'Precision',
'Progress',
'ReferenceCount',
'Register',
'ReleaseData',
'RemoveAll',
'Request',
'StartMethod',
'Update',
'UpdateExtent',
'WholeExtent',
'AAFrames', 'FDFrames','SubFrames','FDOffsets', # deprecated methods of RenderWindow
'MapColorScalarsThroughLookupTable',            # deprecated methods of vtkTexture

#'GetInput',
#'SetInputData'
#'GetOutput'
#'SetOutput'
)



HiddenProp = ( #unused
'DataExtent',
'DataType',
'Executive',
'Information',
#'InputConnection',
#'InputDataObject',
#'Locator',
#'Output', ###
#'OutputPointsPrecision',
'ProgressObserver',
#'ScalarTree',
'UpdateExtent',
#'UseScalarTree',
'WholeExtent',
'ParserErrorObserver',
'Kernel7x7',  # vtkImageConvolve
'Kernel7x7x7', # vtkImageConvolve -- Setter has no doc
'ResolveCoincidentTopologyPointOffsetParameter', # bad getter: Set(float) Get(float) -- is in all the Mapper Classes
'ResolveCoincidentTopologyLineOffsetParameters',
'RelativeCoincidentTopologyPointOffsetParameter', # bad getter: Set(float) Get(float) -- is in all the Mapper Classes
'RelativeCoincidentTopologyLineOffsetParameters',

#'Controller',         # parallel filters
#'SocketController',   # parallel filters
#'Compressor',         # xml writers
#'AssessNames',        # hystogram and statistics
#'Camera',             # cant pass the camera in blender Nodes yet
#'FileNames',          # image readers for volumes on multiple slices with non generable names
#'InformationInput',   # optiona in some image filters
#'LayoutStrategy',     # graph layout --- not addressed yet
#'MemoryBuffer',       # on image readers, allow reading from memory instead of file
#'ReaderErrorObserver' # xml readers
#'Renderer',           # cant pass the renderer in blender Nodes yet
#'VolumeMapper',       # VolumeOutlineSource
#'Result',             # vtkUnsignedCharArray used in PNG and JPEG writer
#'CallbackUserData'    # in ImageImport
#'ImportVoidPointer'   # in ImageImport

)

InterestingClasses = ( #unused
vtk.vtkAlgorithm,                  # sources, reader, writers, filters
vtk.vtkAbstractTransform,          # transform
vtk.vtkImplicitFunction,           # implicti functions
vtk.vtkInitialValueProblemSolver,  # runge kutta
vtk.vtkParametricFunction          # parametric function
)

superclass_name =  "\nSuperclass: ([^\n]*)"

def ancestors(cls):
    if not cls.__doc__:
        return []
    match = re.search( superclass_name, cls.__doc__)
    if match:
        name = match.groups()[0]
        name = name.split('[')[0] # vtkQuaternion[float32]

        superclass = None
        if hasattr( vtk, name ):
            superclass = getattr(vtk, name )

        if superclass:
            values = ancestors(superclass)
            values.append( name )
            return values
        else:
            return [name]
    else:
        return []

#-------------------------------------------------
# collect infos
#-------------------------------------------------

infos = []
counter = 0

def inspect_cls( cls_name ):
    global counter, infos

    if not cls_name.startswith('vtk'):
        return

    if '.' in cls_name: # internal classes like vtkCommonCorePython.xxx
        return

    if cls_name in BannedNames:
        #print( 'skipping', name )
        return

    c = getattr(vtk, cls_name, None)
    if c is None:
        return

    try:
        o = c()
    except:
        return

    parents = ancestors(c)
    parents.reverse()

    #interesting = issubclass( c, vtk.vtkAlgorithm )
    #if not interesting : interesting = issubclass(c, vtk.vtkAbstractTransform)
    #if not interesting : interesting = issubclass(c, vtk.vtkImplicitFunction)
    #if not interesting : interesting = issubclass(c, vtk.vtkInitialValueProblemSolver)
    #if not interesting : interesting = issubclass(c, vtk.vtkParametricFunction)
    #if not interesting :
    #    continue

    counter +=1
    #if counter >50:
    #    break

    out_type = None
    get_output = getattr( o, 'GetOutput', None )
    if get_output:
        out_type = get_output.__doc__.split('\n')[0].split('>')[1].strip()

    num_in = 0
    if hasattr(o, "GetNumberOfInputPorts") :
        num_in  = o.GetNumberOfInputPorts()

    num_out = 0
    if hasattr(o, "GetNumberOfOutputPorts") :
        num_out = o.GetNumberOfOutputPorts()

    props   = []
    methods = []

    #print()

    #print(counter, cls_name.ljust(40), num_in, num_out, str(out_type).ljust(20) , parents )

    #if not issubclass(c, vtk.vtkAlgorithm):
    #    print(counter, name.ljust(40), num_in, num_out, out_type)


    # retrieve the interesting methods
    m = [x for x in dir(o) if ( not x.isupper() ) and ( not x in HiddenMethods ) and ( not [1 for y in HideKeywords if y in x ] ) ]

    m.sort()
    other_methods = list(m)

    # scan methods searching for properties
    for x in m:
        if x.startswith('Set') and 'Get'+x[3:] in m : # if method is a Setter and there is a matching Getter
            p = x[3:]
            setter = getattr(o, 'Set'+p )
            getter = getattr(o, 'Get'+p )

            # remove the methods used by this properties from other_methods
            om = list(other_methods) # iterate a copy, to avoid iterating the list being modified
            [ other_methods.remove(y) for y in ['Set'+p, 'Get'+p, p+'On', p+'Off', 'Get'+p+'AsString', 'Get'+p+'MinValue', 'Get'+p+'MaxValue' ] if y in om ]
            [ other_methods.remove(y) for y in om if y.startswith('Set' + p + 'To') ]


            # the first line in the method doc is the python-function-signature --- example: SetXXX(int) -- GetXXX()->int
            setter_doc = setter.__doc__.split('\n')[0]
            getter_doc = getter.__doc__.split('\n')[0]

            # extract the arguments.
            # sometime getter have no '->' - meaning that they return the value in the arguments,
            # in some case these properties are reduntant, so lets ignore them
            setter_arg = setter_doc.split('(')[1].replace(')','').replace(' ','')
            if '>' in getter_doc:
                getter_arg = getter_doc.split('>')[1].replace(')','').replace('(','').replace(' ','')  
            else:
                getter_arg = "none"

            p_value = '0'
            p_items = []  # enum-names ordered by their value --- or nothing
            p_note = ''

            # setter and getter args should match
            if setter_arg != getter_arg:
                setter_doc = setter_doc.replace("V.",'').replace(p, '')
                getter_doc = getter_doc.replace("V.",'').replace(p, '')
                p_note = '# ko: arg mismatch ' + setter_doc + ' ' + getter_doc 
                #print( 'ko ', p.ljust(30), 'args mismatch:', setter_doc, getter_doc)
            else:
                # get the default value by calling the getter.
                # it this property return a vtkObject, which is already created, this is an optional-input-property
                po = 0
                if not ',' in getter_arg:
                    try:
                        po = getter()

                    except:
                        pass

                    if po :
                        if getter_arg.startswith('vtk'):
                            p_value = po.__class__.__name__
                            p_note += '# - optional'
                        else:
                            p_value = str(po)

                if getter_arg == 'string':
                    if p_value is None or p_value == 'None' or p_value == '0':
                        p_value = '""'
                
                # if there are also the methods p+On and p+Off this property is a bool
                if p+'On' in m and p+'Off' in m :
                    setter_arg = 'bool'

                # if there are also methods Set+p+To+xxx this property is an Enum  (WIP)

                if setter_arg == 'int':
                    q = 'Set'+p+'To'
                    names = [ y.replace(q,'') for y in m if y.startswith( q ) ]
                    if len(names):
                        setter_arg = 'enum'
                        # retrieve the numerical value matching the enum-names
                        enum_value_to_name = {}
                        for y in names:
                            getattr(o,q+y)()                     # call Set+p+To+y()
                            enum_value_to_name[ getter() ] = y   # call Get+p()

                        if not int(p_value) in enum_value_to_name:
                            p_value = sorted( names )[0]                  # fallback for weird cases
                        else:
                            p_value = enum_value_to_name[ int(p_value) ]  # translate the default value
                            
                        p_items = [ (x,enum_value_to_name[x]) for x in enum_value_to_name.keys() ]
                        p_items.sort()
                    
            props.append( { 'name':p, 'args':setter_arg, 'value':p_value, 'items':p_items, 'note':p_note, 'doc':setter.__doc__ } )
            if not p_items: p_items='' # just for the printout
            #print( '   ', p.ljust(30), setter_arg, p_value, p_items, p_note )

    for x in other_methods:
        met = getattr( o, x )
        mdoc = met.__doc__
        if not mdoc: mdoc = ''
        methods.append(  { 'name':x, 'doc':mdoc }  )

    # for x in props:
    #     print( '   P:   ', x['name'].ljust(20), x['args'].ljust(20), x['note'] )
    # for x in methods:
    #     print( '   M:   ', x['name'], x['doc'].split('\n')[0] )

    expc = [ x for x in ['vtkAlgorithm', 'vtkImplicitFunction', 'vtkParametricFunction', 'vtkAbstractTransform']  if x in parents ]
    if 'Mapper' in cls_name: expc = False

    infos.append({'name': cls_name[3:], 'parents':parents, 'expc':expc,  'num_in':num_in, 'num_out':num_out, 'out_type':out_type, 'props':props, 'methods':methods, 'docs':c.__doc__})



names = [ x for x in sorted(dir(vtk)) if x.startswith('vtk') and ( not "." in x ) and ( not x.endswith('Python') )]





#------------------ print hierarchy ---------------
#
# parents = [  " - ".join( ancestors( getattr(vtk,x) ) ) + " - " + x  for x in names ]
# parents.sort()
#
# counter = 0
# for p in parents:
#     counter += 1
#     print( counter, p)


#------------------ print properties with args of type vtkObject ---------------------
# #counter = 0
# lst = []
# for c in infos:
#     if c['expc']:
#         for p in c['props']:
#             if p['args'].startswith('vtk'):
#                 counter += 1
#                 #print( str(counter).rjust(4), c['name'].ljust(45),  p['name'].ljust(25),  p['args'] )
#                 lst.append( p['args'].ljust(30) +" "+ p['name'].ljust(25) +" "+ c['name']  )
#
# lst.sort()
# for i in lst:
#     print(i)

def inspect_all():
    for cls_name in names:
        inspect_cls( cls_name )
    print('vtk infos ready')

def print_cls_info(d):
    print(d['name'], '   in:', d['num_in'], '   out:', d['num_out'], '   out_type:', d['out_type'], '   parents:',
          ' -> '.join(d['parents']))
    for x in d['props']:
        print('   P:   ', x['name'].ljust(20), x['args'].ljust(20), x['note'])
    for x in d['methods']:
        print('   M:   ', x['name'], x['doc'].split('\n')[0])

if __name__ == "__main__":
    if len( sys.argv ) > 1 :
        arg = sys.argv[1]
        if arg in names:
            inspect_cls(arg)
            print_cls_info( infos[0] )
        if arg == "conne":
            inspect_all()
            counter = 0
            for x in infos:
                if x['num_in'] > 1 or x['num_out'] > 1:
                    counter +=1
                    print(counter, x['num_in'], x['num_out'], x['name'])

    else:
        inspect_all()
else:
    inspect_all()

