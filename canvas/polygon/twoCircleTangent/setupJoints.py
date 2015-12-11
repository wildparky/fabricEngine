import pymel.core as pm


def loadCanvas(node, distance):
    canvasNode = pm.createNode('canvasNode')
    path = '/Users/johan/Dev/fabricEngine/canvas/polygon/twoCircleTangent/twoCircleTangentXfo.canvas'
    pm.dfgImportJSON(m=canvasNode, f=path)
    
    node.worldMatrix >> canvasNode.parentMatrix
    canvasNode.distance.set(distance)
    #centerRodMesh = pm.createNode('mesh')
    #canvasNode.centerRodMesh >> centerRodMesh.inMesh
    
    loc = pm.createNode('locator')
    canvasNode.dummy >> loc.v
    
    
def relativeRecurse(node):
    
    childList = node.listRelatives()
    
    for child in childList:
        name = child.name()
        distance = (child.tx.get())
        #print('name: {} distance: {}'.format(name, distance))
        loadCanvas(node, distance)
        relativeRecurse(child)
        

root = pm.ls(sl=True)[0]
relativeRecurse(root)

