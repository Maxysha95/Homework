class QueueNode:
    """ Node: Class for single node of LinkedQueue """

    def __init__(self, elem, nextnode = None):
        """ Initializes new node """
        self.data = elem
        self.next_node = nextnode

class QueueIterator:
    """ QueueIterator: Iterator for LinkedQueue """

    def __init__(self, node, empty_node = None):
        """ Initializes new Iterator """
        self.node = node
        self.empty_node = empty_node

    def __next__(self):
        """ Returns next element of queue: next(iter) """
        if self.node is None:
            raise StopIteration
        else:
            element = self.node.data
            self.node = self.node.next_node
            return element


class LinkedQueue:
    """ LinkedQueue """

    def __init__(self):
        """ Initializes new queue """
        self.__size = 0
        self.head = None
        self.empty_node = QueueNode(None)

    def push(self, elem):
        """ Pushes 'elem' to queue """
        new_node = QueueNode(elem)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            i = 1
            while i < self.__size:
                curr = curr.next_node
                i += 1
            curr.next_node = new_node
        self.__size += 1


    def pop(self):
        """ Removes front of queue and returns it """
        if self.__size != 0:
            first = self.head.data
            self.head = self.head.next_node
            self.__size -= 1
            return first

    def front(self):
        """ Returns front of queue """
        return self.head.data

    def empty(self):
        """ Checks whether queue is empty """
        return self.__size == 0

    def __iter__(self):
        """ Returns Iterator for queue: iter(queue) """
        return QueueIterator(self.head, self.empty_node)

    def __len__(self):
        """ Returns size of queue: len(queue) """
        return self.__size

    def clear(self):
        """ Makes queue empty """
        self.head = None
        self.__size = 0



if __name__ == '__main__':
    qq = LinkedQueue()

    for i in range(55):
        qq.push(i)

    """for x in qq:
        print(qq.pop())"""

    a = qq.pop()
    print(a)

    a = qq.pop()
    print(a)

    print(list(qq))
