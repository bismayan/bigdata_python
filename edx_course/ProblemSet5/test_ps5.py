import graph

def load_map(mapFilename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    dg=graph.WeightedDigraph()
    lines=open(mapFilename,'r').readlines()
    for line in lines:
        data=map(int,line.split())
        source=graph.Node(str(data[0]))
        dst=graph.Node(str(data[1]))
        if not dg.hasNode(source):
            dg.addNode(source)
        if not dg.hasNode(dst):
            dg.addNode(dst)
        ed=graph.WeightedEdge(source,dst,data[2],data[3])
        dg.addEdge(ed)
    print "Loading map from file..."
    return dg


outgraph=load_map("mit_map.txt")
print isinstance(outgraph,graph.WeightedDigraph)
print outgraph.nodes
print outgraph.edges
print outgraph.childrenOf(graph.Node('32'))