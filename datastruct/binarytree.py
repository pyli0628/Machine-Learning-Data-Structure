class Node(object):

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree(object):
    def __init__(self,root=None):
        self.root = root
        self.myqueue = []
    def is_empty(self):
        return True if self.root is None else False
    def add(self,elem): # add by bst
        node = Node(elem)
        if self.root == None:
            self.root = node
            self.myqueue.append(self.root)
        else:
            treenode = self.myqueue[0]
            if treenode.left == None:
                treenode.left = node
                self.myqueue.append(treenode.left)
            else:
                treenode.right = node
                self.myqueue.append(treenode.right)
                self.myqueue.pop(0)
    def preorder(self,root):
        # 根，左，右
        if root == None:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self,root):

        if root == None:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def postorder(self,root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)

    def bstorder(self,root):
        if not root:
            return
        support = []
        node = root
        support.append(node)
        while support:
            node = support.pop(0)
            print(node.val)
            if node.left:
                support.append(node.left)
            if node.right:
                support.append(node.right)
    def height(self,root):
        if not root:
            return 0
        h = max(self.height(root.left),self.height(root.right))+1
        return h

    def preorder_non_recur(self,root):
        #非递归 中、左、右
        if root is None:
            return None
        node_stack = []
        ret = []
        node = root
        while node or node_stack:
            while node:
                ret.append(node.val)
                node_stack.append(node)
                node = node.left

            node = node_stack.pop()
            node = node.right
        return ret
    def inorder_non_recur(self,root):
        # 左，中，右
        if root is None:
            return
        node_stack = []
        ret = []
        node = root
        while node or node_stack:
            while node:
                node_stack.append(node)
                node = node.left
            node = node_stack.pop()
            ret.append(node.val)
            node = node.right
        return ret

    def postorder_non_recur(self,root):
        if root is None:
            return
        stack1 = [root]
        stack2 = []
        ret = []

        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            ret.append(stack2.pop().val)
        return ret


if __name__ == '__main__':
    tree = Tree()
    for ele in range(1,10):
        tree.add(ele)
    tree.postorder(tree.root)
    print(tree.postorder_non_recur(tree.root))
    #print(tree.height(tree.root))