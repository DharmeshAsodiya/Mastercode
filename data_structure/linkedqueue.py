__author__ = 'dharmesh'


class LinkedQueue:

    head = None
    tail = None
    size = 0

    class _Node:
        def __init__(self, element):
            self.element = element
            self.next = None

    def _is_empty(self):
        return self.head is None

    def enqueue(self, e):
        if self._is_empty():
	    self.tail = self._Node(e)
            self.head = self.tail
        else:
            self.tail.next = self._Node(e)
	    self.tail = self.tail.next
	self.size += 1
	return "Added %s" % e

    def delqueue(self):
        if self._is_empty():
            return "Queue is empty"
        rem_element = self.head.element
        self.head = self.head.next
        self.size -= 1
        return rem_element

    def elements(self):
        node = self.head
	ele_list = []
        while node is not None:
            ele_list.append(node.element)
            node = node.next
        return ele_list

    def length(self):
        return str(self.size)
