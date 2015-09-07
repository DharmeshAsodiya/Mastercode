__author__ = 'dharmesh'
class LinkedStack:
    head = None
    # def __init__(self):

    class _Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next

    def _push(self,e):
        if self._is_empty():
            self.head = self._Node(e,None)
        else:
            new_node = self._Node(e,self.head)
            self.head._next = None
            self.head = new_node
        return 'Added'

    def _pop(self):
        if self._is_empty():
            return "Stack is empty"
        pop_element = self.head.element
        self.head = self.head.next
        return pop_element

    def _top(self):
        if self._is_empty():
            return "Stack is empty"
        return self.head.element

    def _elements(self):
        if self._is_empty():
            return "Stack is empty"
        head = self.head
        ele_list = [head.element]
        while head.next is not None:
            ele_list.append(head.next.element)
            head = head.next
        return ele_list

    def length(self):
        if self._is_empty():
            return 0
        return len(self._elements())

    def _is_empty(self):
        return self.head is None