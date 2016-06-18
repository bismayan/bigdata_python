
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





class Tree(object):
    """
    Node of a "tree" (more like a list) of type Item
    Attributes:
        item:   The object of type Item forming the node
        left:   The left child node
        right:  The right child node
        parent: The parent node
    """
    def __init__(self,item,left=None,right=None, parent=None):
        self.item=item
        self.left=left
        self.right=right
        self.parent=parent

    def setleft(self,item):
        assert self.left==None, "Left already set"
        self.left=item
        item.setparent(self)
        return True

    def setright(self, item):
        assert self.right == None, "Right already set"
        self.right = item
        item.setparent(self)
        return True

    def setboth(self,leftitem,rightitem):
        assert self.left == None, "Left already set"
        assert self.right == None, "Right already set"
        self.left=leftitem
        self.right=rightitem
        leftitem.setparent(self)
        rightitem.setparent(self)
        return True

    def getitem(self):
        return self.item

    def getright(self):
        return self.right

    def getleft(self):
        return self.left

    def getparent(self):
        return self.parent

    def setparent(self, item):
        assert self.parent==None, "Parent Already Set"
        self.parent = item
        return True

    def __str__(self):
        return self.item.getname()



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
        Itemlist.append(Item(names[i],float(values[i]),float(weights[i])))
    return Itemlist


def keyfunc(Node,**kwargs):
    assert len(kwargs)>0, "Nothing to Check in Keyfunction"
    Item=Node.getitem()
    if kwargs.has_key('name'):
        return (Item.getname()==kwargs['name'])
    if kwargs.has_key('value'):
        return (Item.getvalue() == kwargs['value'])
    elif kwargs.has_key('weight'):
        return (Item.getweight() == kwargs['weight'])
    else:
        raise NameError("No Attribute of type",kwargs.keys())


def TreeCreate(Itmlist):
    TreeContainer = [Tree(item) for item in Itmlist]
    TreeContainer[0].setboth(TreeContainer[1], TreeContainer[2])
    TreeContainer[1].setboth(TreeContainer[3], TreeContainer[4])
    TreeContainer[2].setleft(TreeContainer[5])
    return TreeContainer,TreeContainer[0]

def dfSearch(Root,keyfn,**kwargs):
    print "Looking at Item ", Root.getitem().getname()
    if (keyfn(Root, **kwargs)):
        return True
    else:
        temp = []
        if Root.getright() != None:
            temp.insert(0, Root.getright())
        if Root.getleft() != None:
            temp.insert(0, Root.getleft())
        while (len(temp)>0):
            Current = temp.pop(0)
            print "Looking at Item ", Current.getitem().getname()
            if (keyfn(Current, **kwargs)):
                return True
            if Current.getright() != None:
                temp.insert(0, Current.getright())
            if Current.getleft() != None:
                temp.insert(0, Current.getleft())

        else:
            return False


def bfSearch(Root,keyfn,**kwargs):
    print "Looking at Item ", Root.getitem().getname()
    if (keyfn(Root, **kwargs)):
        return True
    else:
        temp = []
        if Root.getright() != None:
            temp.insert(0, Root.getleft())
        if Root.getleft() != None:
            temp.insert(len(temp), Root.getright())
        while (len(temp)>0):
            Current = temp.pop(0)
            print "Looking at Item ", Current.getitem().getname()
            if (keyfn(Current, **kwargs)):
                return True
            if Current.getleft() != None:
                temp.append(Current.getleft())
            if Current.getright() != None:
                temp.append(Current.getright())

        else:
            return False

if __name__=="__main__":
    nam=["watch","phone","Playstation","Ipad","Kindle","laptop"]
    w=[1.0,2.0,3.0,2.5,1.2,3.5]
    val=[200.0,500.0,300,375,123,1000]
    It_list=createItems(nam,val,w)
    TreeFinal,Root=TreeCreate(It_list)
    if (bfSearch(Root,keyfunc,value=1000)):
        print "Element Found"
    else:
        print "Element Not Found"



