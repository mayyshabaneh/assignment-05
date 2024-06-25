class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.right = None
        self.left = None


class BinTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value):#time comp = O(N) / N : the number of nodes
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if temp.left is None:
                temp.left = node
                break
            else:
                queue.append(temp.left)
            
            if temp.right is None:
                temp.right = node
                break
            else:
                queue.append(temp.right)

    
    def inorder_traversal(self, root):#time comp = O(N) / N : the number of nodes
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.value)
            result = result + self.inorder_traversal(root.right)
        return result
    

    def preorder_traversal(self, root):#time comp = O(N) / N : the number of nodes
        result = []
        if root:
            result.append(root.value)
            result = result + self.preorder_traversal(root.left)
            result = result + self.preorder_traversal(root.right)
        return result
    

    def postorder_traversal(self, root):#time comp = O(N) / N : the number of nodes
        result = []
        if root:
            result = self.postorder_traversal(root.left)
            result = result + self.postorder_traversal(root.right)
            result.append(root.value)
        return result


    def search(self,value):#time comp = O(N) / N : the number of nodes
        if value in self.inorder_traversal(self.root) :
            print ("value exist")
            return True
        else:
            print("value doesnt exist")
            return False


    def find_min(self):#time comp = O(N) / N : the number of nodes
       return min(self.inorder_traversal(self.root))


    def find_max(self):#time comp = O(N) / N : the number of nodes
        return max(self.inorder_traversal(self.root))


    def delete(self,value):
        if self.search(value) is True :
            temp = self.root
            while self.root :
                if temp.value == value:
                    del(temp.value)
                    return
                else :
                    print ("the value dosnt exist or the tree is empty")
                return




tree = BinTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(9)
tree.insert(1)
print("inorder traversal --> ",tree.inorder_traversal(tree.root))
print("postorder traversal --> ",tree.postorder_traversal(tree.root))
print("preorder traversal --> ",tree.preorder_traversal(tree.root))
tree.search(9)
tree.search(10)
print("the minimum value is : " , tree.find_min())
print("the maximum value is : " , tree.find_max())
tree.delete(5)
tree.search(5)
