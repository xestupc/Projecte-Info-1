from _1_PhaseOne import Segment
from _1_PhaseOne import node

n1 = node.Node("A", 4, 25)
n2 = node.Node("B", 9, 30)
n3 = node.Node("C", 11, 40)

print("The distance between n1 and n2 is: ")
Segment(n1, n2)
print("The distance between n2 and n3 is: ")
Segment(n2, n3)

node.AddNeighbor(n1, n2)
node.AddNeighbor(n2, n3)

print(n1.__dict__)
print(n2.__dict__)
print(n3.__dict__)
