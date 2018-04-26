class LinkedList:
    
    class _Node:
        def __init__(self, element):
            self.element = element
            self.next = None
	
    def __init__(self):
	self.head = None

    def insert(self, e, node=None):
	if self.head is None:
	    self.head = self._Node(e)
	else:
	    if node is None:
	    	node = self.head
	    if node.next:
		self.insert(e, node.next)
	    else:
		node.next = self._Node(e)
	return

    def elements(self):
	node = self.head
	while node is not None:
	    print node.element
	    node = node.next
    



