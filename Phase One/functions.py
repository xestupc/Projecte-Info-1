
class Nodo():
    def __init__(self, x, y, vecinos_lista):
        self.x = x
        self.y = y
        self.veins = vecinos_lista

node1 = Nodo(100, 200, [])


def addNeighbor(n1, n2):
    n1.veins.append(n2)
    if n2 not in nodo1.veins:
       nodo1.veins.append(n2)


    # while loop 

    
    # for 



# poner condicional si n2 ya está en lista vecinos n1 
# no volver a añadirlo


# pistas: buscar syntax del if 
# vas a tener que jugar con un bucle y los indices de una lista
# ya te doy la lsita de vecinos n1, mirar si n2 lo añado o no.



def distance (n1, n2):
    distance = ((n2.x - n1.x)** 2 + (n2.y - n1.y)**2)**(1/2)
    return distance
nodo1= Nodo(2, 4, [])
nodo2= Nodo(5, 6, [])

nodo1.veins = [nodo3, nodo4, nodo5, nodo6, nodo7, nodo8, nodo9, nodo10]



print(f"\n Distancia =  {distance(nodo1, nodo2)}")


