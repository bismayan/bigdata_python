import graph as gp

g = gp.Digraph()
na = gp.Node('a')
nb = gp.Node('b')
nc = gp.Node('c')
g.addNode(na)
g.addNode(nb)
g.addNode(nc)
e1 = gp.Edge(na, nb)
print e1
e2 = gp.Edge(na, nc)
e3 = gp.Edge(nb, nc)
print e2
print e3
g.addEdge(e1)
g.addEdge(e2)
g.addEdge(e3)
print g