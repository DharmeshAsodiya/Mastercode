__author__ = 'dharmesh'


class BinarySearchTree:

    def __init__(self):
        self.node = {'val':None,
                     'left':None,
                     'right':None}
        self.values = []

    def insert(self, val, insert_at_node=None):

        if self.values:
            node = insert_at_node
            if not node:node = self.values[0]

            if node['val'] is None:
                node['val'] = val
            elif val > node['val']:
                if node['right'] is None:
                    node['right'] = val
                else:
                    insert_on = self.add_node(node['right'])
                    self.insert(val, insert_on)
            elif val < node['val']:
                if node['left'] is None:
                    node['left'] = val
                else:
                    insert_on = self.add_node(node['left'])
                    self.insert(val, insert_on)
            elif node['val'] == str(val):
                return str(val) + ' Already Present'
        else:
            self.add_node(val)
        return str(val) + ' Inserted'

    def add_node(self, root):
        node = self.get_node(root)
        if node is None:
            node = {'val': root,
                    'right': None,
                    'left': None}
            self.values.append(node)
        return node

    def remove(self, val):
        pass

    def get_node(self, node_val):
        for node in self.values:
            if str(node['val']) == str(node_val):
                return node
        return None

    def search(self, val):
        node=self.get_node(val)
        # if val in node.values():
        #     return False, 'Already present'
        if node:
            pass

        return True, ''