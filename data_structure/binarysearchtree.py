__author__ = 'dharmesh'


class BinarySearchTree:
    base_node = None

    class _Node:

        def __init__(self, val):
            self.parent = None
            self.val = val
            self.left = None
            self.right = None

    def insert(self, val):
        if not self.base_node:
            self.base_node = self._Node(val)
        else:
            retval = self.evaluate_node(self.base_node, val, True)
            if retval:
                return "value already exist"
        return str(val) + " Added to "

    def evaluate_node(self, node, val, add=False):
        if node.val:
            if node.val == val:
                return val
            elif node.val > val:
                return self.check_or_addto_left(node, val, add)
            else:
                return self.check_or_addto_right(node, val, add)
        else:
            return

    def check_or_addto_left(self, node, val ,add):
        if not node.left and add:
            print "Adding to left of node " + str(node.val)
            node.left = self._Node(val)
        else:
            return self.evaluate_node(node.left, val, add)
        return

    def check_or_addto_right(self, node, val, add):
        if not node.right and add:
            print "Adding to right of node " + str(node.val)
            node.right = self._Node(val)
        else:
            return self.evaluate_node(node.right, val, add)
        return

    def remove(self, val):
        node = self.get_node(val)

    def get_node(self, node_val):
        for node in self.values:
            if str(node['val']) == str(node_val):
                return node
        return None

    def search(self, val):
        retval = self.evaluate_node(self.base_node, val)
        if retval:
            return "Exist"
        return "Do exist"


def preorder_recursive(tree, result=[]):
    if not tree:
        return
    result.append(tree.val)
    preorder_recursive(tree.left, result)
    preorder_recursive(tree.right, result)
    return result


def preorder(tree):
    result = []
    stack = []
    stack.append(tree.base_node)
    while stack:
        tree = stack.pop()
        result.append(tree.val)
        if tree.right:
            stack.append(tree.right)
        if tree.left:
            stack.append(tree.left)
    return result


def inorder_recursive(tree, result=[]):
    if not tree:
        return
    inorder_recursive(tree.left, result)
    result.append(tree.val)
    inorder_recursive(tree.right, result)
    return result


def postorder_recursive(tree, result=[]):
    if not tree:
        return
    postorder_recursive(tree.left, result)
    postorder_recursive(tree.right, result)
    result.append(tree.val)
    return result