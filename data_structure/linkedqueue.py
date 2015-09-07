__author__ = 'dharmesh'


class LinkedQueue:

    head = None
    tail = None
    size = 0

    class _Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next

    def _is_empty(self):
        return self.head is None

    def enqueue(self, e):
        if self._is_empty():
            self.tail = self._Node(e, None)
            self.head = self.tail
        else:
            self.tail.next = self._Node(e, None)
        self.size += 1
        return "Added"

    def delqueue(self):
        if self._is_empty():
            return "Queue is empty"
        rem_element = self.head.element
        self.head = self.head.next
        self.size -= 1
        return rem_element

    def elements(self):
        head = self.head
        ele_list = [head.element]
        while head.next is not None:
            head = head.next
            ele_list.append(head.element)
        return ele_list

    def length(self):
        return str(self.size)