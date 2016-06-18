import graph as gp

g = gp.WeightedDigraph()
na = gp.Node('a')
nb = gp.Node('b')
nc = gp.Node('c')
g.addNode(na)
g.addNode(nb)
g.addNode(nc)
e1 = gp.WeightedEdge(na, nb, 15, 10)
print e1
print e1.getTotalDistance()
print e1.getOutdoorDistance()
e2 = gp.WeightedEdge(na, nc, 14, 6)
e3 = gp.WeightedEdge(nb, nc, 3, 1)
print e2
print e3
g.addEdge(e1)
g.addEdge(e2)
g.addEdge(e3)
print g
print g.childrenOf(na)