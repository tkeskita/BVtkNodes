from .core import l # Import logging
import time
import vtk
import bpy
import os
from .core import b_path
from .errors.bvtk_errors import BVTKException

# -----------------------------------------------------------------------------
#  Functions and classes for running BVTK_Nodes internal function queue and
#  other updates
# -----------------------------------------------------------------------------


def SetColor(node, color):
    '''Set color of node to color'''
    node.color = color


def UpdateObj(node, vtkobj):
    '''Update node corresponding to vtkobj by applying properties, inputs
    and call to VTK Update()
    '''
    #time.sleep(1)
    try:
        node.apply_properties(vtkobj)
        node.apply_inputs(vtkobj)
    except AttributeError as err:
        err_msg = ("Encountered an attribute error when trying to apply vtk properties.\n"
                + "This may point to a VTK version mismatch between generated and currently used VTK.")
        raise BVTKException(err_msg, err)
    except Exception as ex:
        err_msg = "Unknown error..."
        raise BVTKException(err_msg, ex)
    
    if hasattr(vtkobj, "Update"):
        vtkobj.Update()


def SetInputConnection(vtkobj, i, input_obj):
    '''Set input connection i of vtkobj to input object'''
    #time.sleep(1)
    vtkobj.SetInputConnection(i, input_obj)


def SetInputObj(vtkobj, name, input_obj):
    '''Run a named Set function on vtkobj with argument input_obj'''
    #time.sleep(1)
    cmd = 'vtkobj.Set' + name + '( input_obj )'
    exec(cmd, globals(), locals())


def Update(node, cb, x=True):
    '''Update the input functions of this node using the function queue.
    Sets color of node to reflect node run status. Finally updates this
    node and queues argument function cb() if argument x is True.
    '''
    l.debug('Processing ' + node.name)
    if x:
        queue.add(log_check)
    ex_color = node.color.copy() # Current color
    inputs_color = 0.84, 0.84, 0.73 # Input color
    execute_color = 0.85, 0.6, 0.2 # Execution color

    vtkobj = node.get_vtkobj()

    # Call update for input nodes
    queue.add(SetColor, node, inputs_color)
    for input_node in node.input_nodes():
        Update(input_node, None, False)
    queue.add(SetColor, node, execute_color)

    # Update VTK object
    if vtkobj:
        queue.add(UpdateObj, node, vtkobj)
    queue.add(SetColor, node, ex_color)

    # For special nodes, run update_cb
    if x:
        queue.add(SetColor, node, execute_color)
        queue.add(log_show)
        if cb:
            queue.add(cb)
        queue.add(SetColor, node, ex_color)
        bpy.ops.node.bvtk_function_queue()


def no_queue_update(node, cb, x=True):
    '''Force the update of all the input connections of this node,
    bypassing the functions queue. Does not update node colors.
    Finally updates this node by calling argument cb() if argument x
    is True, and VTK Update function otherwise.
    '''
    l.debug('Processing ' + node.name)
    vtkobj = node.get_vtkobj()

    # Call update for input nodes
    for input_node in node.input_nodes():
        no_queue_update(input_node, None, False)

    # For special nodes, run update_cb
    if x:
        cb()

    # Update VTK object
    else:
        if vtkobj:
            node.apply_properties(vtkobj)
            node.apply_inputs(vtkobj)
            if hasattr(vtkobj, "Update"):
                vtkobj.Update()




# -----------------------------------------------------------------------------
#  function queue
# -----------------------------------------------------------------------------


class BVTK_FunctionsQueue:
    '''Class for Functions Queue. Used for running a queue system for 
    BVTK_Nodes functions.
    '''
    functions = [] # List of functions in queueus
    executed = [] # Index list of executed functions
    running = False # Queue running state
    i = 0 # Index of function being run

    def add(self, f, *args):
        if not self.running:
            self.functions.append((f, (a for a in args)))

    def next_function(self):
        i = self.i
        if i >= len(self.functions):
            self.running = False
            return
        f = self.functions[i]
        if i not in self.executed:
            f[0](*f[1])
            #try:
            #    f[0](*f[1])
            #except Exception as e:
            #    l.critical("i=" + str(i) + ", f[0] = " + str(f[0]) + \
            #               " got exception: " + str(e))
            self.executed.append(i)
            self.i += 1

    def reset(self):
        self.functions = []
        self.executed = []
        self.running = False
        self.i = 0

# Global functions queue
queue = BVTK_FunctionsQueue()


class BVTK_OT_FunctionQueue(bpy.types.Operator):
    '''Operator to call a function in functions queue. 
    Calls are spaced (separated in time) by 1/100 s.
    '''
    bl_idname = "node.bvtk_function_queue"
    bl_label = "Run a VTK function in queue"

    _timer = None

    def modal(self, context, event):
        global queue
        try:

            if not queue.running:
                self.cancel(context)
                return {'CANCELLED'}
            elif event.type == 'TIMER':
                queue.next_function()
            return {'PASS_THROUGH'}

        except BVTKException as bvtk_ex:
            err_str = "Queue execution (modal) failed with an unexpected error: \n" + str(bvtk_ex)
            l.error(err_str)
            self.report({'ERROR'}, err_str)
            self.cancel(context)
            return {'CANCELLED'}

    def execute(self, context):
        global queue
        try:

            if queue.running:
                return {'CANCELLED'}
            queue.running = True
            wm = context.window_manager
            self._timer = wm.event_timer_add(0.01, window=context.window)
            wm.modal_handler_add(self)
            return {'RUNNING_MODAL'}
            
        except BVTKException as bvtk_ex:
            err_str = "Queue execution (modal) failed with an unexpected error: \n" + str(bvtk_ex)
            l.error(err_str)
            self.report({'ERROR'}, err_str)
            self.cancel(context)
            return {'CANCELLED'}

    def cancel(self, context):
        global queue
        queue.reset()
        wm = context.window_manager
        wm.event_timer_remove(self._timer)

# add_ui_class(BVTK_OT_FunctionQueue) # TODO: Works only if in converters.py?

# -----------------------------------------------------------------------------
# Vtk logs
# -----------------------------------------------------------------------------


out = vtk.vtkFileOutputWindow()
b_dir = b_path.rsplit(os.sep, 1)[0]
logfile = os.path.join(b_dir, 'vtklog.txt')
open(logfile, 'w').write('')
out.SetFileName(logfile)
vtk.vtkOutputWindow.SetInstance(out)

last_log = '' # Current log file contents

def log_check():
    '''Saves current log file contents. This function is to be called
    before executing more code that could generate errors, so that
    only latest error messages can be shown to user
    '''
    global last_log
    last_log = open(logfile, 'r').read()


def log_show():
    '''Shows log text of only latest operation'''
    logs = open(logfile, 'r').read()
    logs = logs.replace(last_log, '', 1) # Remove old log text
    if logs:
        def draw(self, context):
            layout = self.layout
            for line in logs.split('\n'):
                if line:
                    row = layout.row()
                    row.label(text=line)

        bpy.context.window_manager.popup_menu(draw, 'vtk:', 'INFO')

