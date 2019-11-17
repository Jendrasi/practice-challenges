class Node:
    # Constructor, requires amount value.
    # NOTE self.parent is commented out for this implementation because a parent address does not need to be accessed from it's child.
    def __init__(self, amt):
        self.amount = amt
        self.children = []
        #self.parent = None

    # Method to add a child to a Node. No return value.
    def addChild(self, node):
        #node.parent = self
        self.children.append(node)
    
    # Method to answer whether the Node has children. Boolean response.
    def hasChildren(self):
        return len(self.children) > 0

    # Recursive function to get a list of child nodes that represent the shortest leaf from 'self/this' Node.
    def getMinDepth(self):
        if not self.hasChildren():
            return [self.amount]
        depths = []
        for child in self.children:
            d = child.getMinDepth()
            depths.append(d)
        return [self.amount] + min(depths,key=len)
