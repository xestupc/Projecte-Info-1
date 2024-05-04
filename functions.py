
class Node():
    def __init__(self, x, y, vecinos_lista):
        self.x = x #X coordinate
        self.y = y #Y coordinate
        self.veins = vecinos_lista 

node1 = Node(100, 200, [])


def addNeighbor(n1, n2):
    if n2 not in n1.veins: 
    #if n2 is not in n1's neighbors list, it will be added. The program will return False
        n1.veins.append(n2) 
        return False 
    #id n2 is already present in n1's neighbors list, the program will return True
    else:
        return True
   

def distance (n1, n2):
    #Calculates the Euclidean distance betwween two nodes
    distance = ((n2.x - n1.x)** 2 + (n2.y - n1.y)**2)**(1/2)
    return distance

#examplee usage
nodo1= Node(2, 4, [])
nodo2= Node(5, 6, [])

print(addNeighbor(nodo1, nodo2))
print(f"\n Distancia =  {distance(nodo1, nodo2)}")


