# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)




class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

class WeightedEdge(Edge,object):
    def __init__(self,src,dest,totalDistance=0,outdoorDistance=0):
        Edge.__init__(self,src,dest)
        self.weight=(totalDistance,outdoorDistance)


    def getTotalDistance(self):
        return self.weight[0]

    def getOutdoorDistance(self):
        return self.weight[1]

    def getWeight(self):
        return self.weight

    def __str__(self):
        return "{0}->{1} {2}".format(str(self.src),str(self.dest),str(self.weight))




class WeightedDigraph(Digraph,object):

     def __init__(self):
         Digraph.__init__(self)

     def addEdge(self, weightededge):
         assert (isinstance(weightededge,WeightedEdge)), "Cannot Add anything but a Weighted Edge object"
         src = weightededge.getSource()
         dest = weightededge.getDestination()
         if not (src in self.nodes and dest in self.nodes):
             raise ValueError('Node not in graph')
         self.edges[src].append([dest,tuple(map(int,weightededge.getWeight()))])

     def childrenOf(self, node):
         assert isinstance(node,Node), "What the Fuck!"
         return([i[0] for i in self.edges[node]])

     def getTotdistance(self,node1,node2):
         assert self.hasNode(node1) and self.hasNode(node2), "Nodes do not exist in Graph"
         result=None
         for i in self.edges[node1]:
            if i[0]==node2:
                result=int(i[1][0])
                return result
         if result is None:
            return None

     def getOutdistance(self, node1, node2):
         assert self.hasNode(node1) and self.hasNode(node2), "Nodes do not exist in Graph"
         result = None
         for i in self.edges[node1]:
             if i[0] == node2:

                 print "Debug", int(i[1][1])
                 result = int(i[1][1])
                 return result
         if result is None:
             return None

     def __str__(self):
         res = ''
         for k in self.edges:
             for d in self.edges[k]:
                 res = '{0}{1}->{2} ({3},{4})\n'.format(res, k, d[0], d[1][0], d[1][1])
         return res[:-1]


