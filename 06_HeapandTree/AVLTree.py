class TreeNode:
    def __init__(self,key):
       self.key=key
       self.left=None
       self.right=None
       self.height=1

class AVLBST:
    def __init__(self):
        self.root=None
    
    def search(self, key):
        return self.searching(self.root, key)

    def searching(self, currentroot, key):
        if not currentroot:return False
        if currentroot.key == key:
            return True
        if key < currentroot.key:
            return self.searching(currentroot.left, key)
        return self.searching(currentroot.right, key)
    
    def getheight(self,root):
        if root is None:
            return 0 
        return root.height
    
    def avlfactor(self, root):
        if root is None:
            return 0
        return self.getheight(root.left) - self.getheight(root.right)

    def insert(self,key):
        self.root=self.inserting(self.root,key)

    def inserting(self,currentroot,key):
        if currentroot is None:
            return TreeNode(key)
        if key<currentroot.key:
            currentroot.left=self.inserting(currentroot.left,key)
        else: 
            currentroot.right=self.inserting(currentroot.right,key)
        currentroot.height=1+max(self.getheight(currentroot.left),self.getheight(currentroot.right))

        balance=self.avlfactor(currentroot)
        if balance>1 and key<currentroot.left.key:
            return self.rightrotate(currentroot)
        if balance<-1 and key>currentroot.right.key:
            return self.leftrotate(currentroot)
        if balance>1 and key>currentroot.left.key:
            currentroot.left=self.rightrotate(currentroot.left)
            return self.rightrotate(currentroot)
        if balance<-1 and key<currentroot.right.key:
            currentroot.right=self.leftrotate(currentroot.right)
            return self.leftrotate(currentroot)
        
        return currentroot       

    def leftrotate(self,x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.getheight(x.left), self.getheight(x.right))
        y.height = 1 + max(self.getheight(y.left), self.getheight(y.right))
        return y

    def rightrotate(self,x):
        y = x.left
        T2 = y.right
        y.right = x
        x.left = T2
        x.height = 1 + max(self.getheight(x.left), self.getheight(x.right))
        y.height = 1 + max(self.getheight(y.left), self.getheight(y.right))
        return y

    def treeprint(self):
        self.subtreeprint(self.root)
    
    def subtreeprint(self,currentroot):
        if currentroot:
          print("(",end="")
          self.subtreeprint(currentroot.left) 
          print(currentroot.key,end="")
          self.subtreeprint(currentroot.right) 
          print(")",end="")


MyTree=AVLBST()
MyTree.insert(10)
MyTree.insert(20)
MyTree.insert(30)
MyTree.insert(40)
MyTree.insert(50)
MyTree.insert(60)
MyTree.insert(70)
MyTree.treeprint()
x=int(input())
if MyTree.search(x): print(str(x)+" is in the Tree") 
else: print(str(x)+" is in the Tree")