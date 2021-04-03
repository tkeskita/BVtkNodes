import logging
import bpy
import vtk
import functools
from . import bvtk

l = logging.getLogger(__name__)

nodeMaxId:int = 1   # Maximum node id number. 0 means invalid
nodesIdMap:dict = {}  # node_id -> node
treeIdMap:dict = {}  # node_id -> node
vtkCache:dict = {}  # node_id -> vtkobj

persistent_storage = {"nodes": {}}

#It is sometimes not possible to save instance variables in a class, which is why we use this node
class PersistentStorageUser():
    def free(self):
        if self.name in persistent_storage["nodes"]:
            del persistent_storage["nodes"][self.name]

    def get_persistent_storage(self):
        if self.name not in persistent_storage["nodes"]:
            persistent_storage["nodes"][self.name] = {}
        return persistent_storage["nodes"][self.name]

class BVTKCache:
    '''Class for accessing vtkCache and nodemap
    '''

    @classmethod
    def init(cls):
        ''' Initialzed cache/node ids
        '''
        cls.reload()
        cls.check_cache()

    @classmethod
    def reload(cls):
        '''Resets the caches to be recreated from scratch
        '''
        global nodeMaxId, nodesIdMap, vtkCache

        nodeMaxId = 1
        nodesIdMap = {}
        treeIdMap = {}
        vtkCache = {}

    @classmethod
    def check_cache(cls):
        '''Rebuild Node Cache. Called by all operators. Cache is out of sync
        if an operator is called and at the same time NodesMaxId=1.
        This happens after reloading addons. Cache is rebuilt, and the
        operator must be interrupted, but the next operator call will work
        OK.
        '''
        # After F8 or FileOpen VTKCache is empty and NodesMaxId == 1
        # any previous node_id must be invalidated
        if nodeMaxId == 1:
            for nt in bpy.data.node_groups:
                if nt.bl_idname == 'BVTK_NodeTreeType':
                    for n in nt.nodes:
                        n.node_id = 0

        # For each node check if it has a node_id
        # and if it has a vtk_obj associated
        for nt in bpy.data.node_groups:
            if nt.bl_idname == 'BVTK_NodeTreeType':
                for n in nt.nodes:
                    if n.node_id == 0:
                        cls.map_node(n, tree=nt)
                    if cls.get_vtkobj(n) == None:
                        cls.init_vtkobj(n)

    @classmethod
    def init_vtkobj(cls, node):
        '''Instantiate the nodes vtkobj and store it in VTKCache.
        '''
        global vtkCache

        # create the node vtk_obj if needed
        if node.bl_label.startswith('vtk'):
            vtk_class = getattr(vtk, node.bl_label, None)
            if vtk_class is None:
                l.error("bad classname " + node.bl_label)
                return
            vtkCache[node.node_id] = vtk_class()
            l.debug("Created VTK object of type " + node.bl_label + ", id " + str(node.node_id))
        elif node.bl_label.startswith('bvtk'):
            vtk_class = getattr(bvtk, node.bl_label, None)
            if vtk_class is None:
                l.error("bad classname " + node.bl_label)
                return
            vtkCache[node.node_id] = vtk_class()
            l.debug("Created BVTK object of type " + node.bl_label + ", id " + str(node.node_id))
        else:
            vtkCache[node.node_id] = None

    @classmethod
    def map_node(cls, node, tree=None, force=False):
        '''Assigned new node its unique ID and adds node to node map.
        Called when building the cache
        '''
        global nodeMaxId, nodesIdMap, treeIdMap, vtkCache

        if node.node_id == 0 or force:
            node.node_id = nodeMaxId
            l.debug("Initialize new node: %s, id %d" % (node.name, node.node_id))
            vtkCache[node.node_id] = None
            nodesIdMap[node.node_id] = node
            treeIdMap[node.node_id] = tree
            nodeMaxId += 1 # Index node id for next created node

    @classmethod
    def unmap_node(cls, node):
        '''Remove node from cache. To be called from node.free().
        Remove node from NodesMap and its vtkobj from VTKCache
        '''
        global nodesIdMap, vtkCache

        if node.node_id in nodesIdMap:
            del nodesIdMap[node.node_id]

        if node.node_id in vtkCache:
            obj = vtkCache[node.node_id]
            # if obj: 
            #     obj.UnRegister(obj)  # vtkObjects have no Delete in Python -- maybe is not needed
            del vtkCache[node.node_id]
        l.debug("deleted " + node.bl_label + " " + str(node.node_id))

    @classmethod
    def get_node(cls, node_id:int):
        '''Get node corresponding to node_id. Called by BVTK_OT_NodeWrite'''
        global nodesIdMap

        if node_id in nodesIdMap:
            return nodesIdMap[node_id]
        else:
            l.error("not found node_id " + str(node_id))
            return None

    @classmethod
    def get_tree(cls, node_id:int):
        '''Get node tree corresponding to node_id. Called in BVTK_OT_Edit_Custom_Code'''
        global treeIdMap

        if node_id in treeIdMap:
            return treeIdMap[node_id]
        else:
            l.error("not found node_id " + str(node_id))
            return None

    @classmethod
    def get_vtkobj(cls, node):
        '''Get the VTK object associated to a node'''
        global vtkCache
        
        if node is None:
            l.error("bad node " + str(node))
            return None

        if not node.node_id in vtkCache:
            return None

        return vtkCache[node.node_id]