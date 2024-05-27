class NodeClass:
   def __init__(self, name, x, y):
       self.name = name # nombre
       self.x = x # X coordinate
       self.y = y # Y coordinate
       self.veins = [] # lista nodos directamente connectadoes a self

def NodeConstructor():
    NodeObject = NodeClass("", "", "", [])
    return NodeObject


def addNeighbor(n1, n2):
   if n2 not in n1.veins:
   #if n2 is not in n1's neighbors list, it will be added. The program will return true
       n1.veins.append(n2)
       return True
   #id n2 is already present in n1's neighbors list, the program will return false
   else:
       return False
 
def Distance (n1, n2):
   #Calculates the Euclidean distance betwween two nodes
   distance = ((n2.x - n1.x)** 2 + (n2.y - n1.y)**2)**(1/2)
   return distance

def printNodeChar(node):
    print(f"Node name: {node.name}")
    print(f"Node coordinates (x,y): {node.x}, {node.y}")
    if len(node.veins) == 0:
        print(f"{node.name} does not have any neighbours")
    else: 
        for item in node.veins:
            print(item)
