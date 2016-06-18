__author__="Bismayan Chakrabarti"

"""
This code creates a Binary tree of some items and performs various searcher on them
Each item has a value and a weight
Let's see if this can solve the Knapsack problem
"""

class Item(object):
    """
    class definiing the item which will form the node of the tree
    Attributes:
        value:          The value of the item
        weight:         The weight of the item
        name  :         The name of the item
    """
    def __init__(self,name="Noname",value=0.0,weight=0.0):
        """
        initializes the item with a name, a weight and a value

        """
        usage=""" Items(name,value,weight)
        """
        self.name=name
        self.value=value
        self.weight=weight

    def getvalue(self):
        return self.value

    def getweight(self):
        return self.weight

    def getname(self):
        return self.name

    def __str__(self):
        return "<"+self.name+', weight='+str(self.weight)+",value="+str(self.value)+">"





def createItems(names,values,weights):
    """
    Creates a list of items and returns it
    :param names: list of names
    :param values: list of values
    :param weights: list f weights
    :return: list of objects of type Item with all weights and values converted to float
    """

    assert len(names)==len(values)==len(weights)>0.0, "Names, values and weights don't have equal lengths or are empty"
    assert all(type(name)==str for name in names), "Names must be of type string"
    assert all(type(value)==float  or type(value)==int for value in values), "Value must be of type int/float"
    assert all(type(weight)==float or type(weight)==int for weight in weights), "Value must be of type int/float"
    Itemlist=[]
    for i in range(len(names)):
        Itemlist.insert(0,Item(names[i],float(values[i]),float(weights[i])))
    return Itemlist


def decisionTree(toConsider, avail):
    if toConsider == [] or avail == 0:
        result = (0,0, ())
    elif toConsider[0].getweight() > avail:
        result = decisionTree(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]

        #Explore left branch
        withWeight,withVal, withToTake = decisionTree(toConsider[1:],
                                      avail - nextItem.getweight())
        withVal += nextItem.getvalue()
        withWeight+=nextItem.getweight()
        #Explore right branch
        withoutWeight,withoutVal, withoutToTake = decisionTree(toConsider[1:], avail)

        #Choose better branch
        if withVal > withoutVal:
            result = (withWeight,withVal, withToTake + (nextItem,))
        else:
            result = (withoutWeight,withoutVal, withoutToTake)
    return result


if __name__=="__main__":
    maxweight=4
    nam=["watch","phone","Playstation","Ipad","Kindle"]
    w=[1.0,2.0,3.0,2.5,1.2]
    val=[200.0,500.0,300,375,123]
    It_list=createItems(nam,val,w)
    print "Current List of items"
    print "----------------------"
    for i in It_list:
        print i.__str__()
    weight,val,taken = decisionTree(It_list,maxweight)
    for i in taken:
        print i.getname()
    print val
    print weight


