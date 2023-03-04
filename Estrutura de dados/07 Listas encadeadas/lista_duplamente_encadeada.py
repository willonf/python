class Node:
    def __init__(self, value):
        self.__value = value
        self.next = None
        self.previous = None

    @property
    def value(self):
        return self.__value


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __list_is_empty(self):
        return self.head is None

    def insert_on_start(self, value):
        new_node = Node(value)
        if self.__list_is_empty():
            self.tail = new_node
        else:
            self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_on_final(self, value):
        new_node = Node(value)
        if self.__list_is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
        self.tail = new_node

    def exclude_start(self):
        temp = self.head
        if self.head.next is None:
            self.tail = None
        else:
            self.head.next.previous = None
        self.head = self.head.next
        return temp

    def exclude_final(self):
        temp = self.tail
        if self.head.next is None:
            self.head = None
        else:
            self.tail.previous.next = None
        self.tail = self.tail.previous
        return temp

    def exclude_value(self, value):
        current = self.head
        while current.value != value:
            current = current.next
            if current is None:
                return None
        if current == self.head:
            self.head = current.next
        else:
            current.previous.next = current.next

        if current == self.tail:
            self.tail = current.previous
        else:
            current.next.previous = current.previous
        return current

    def show_list(self, reverse=False):
        if reverse:
            current = self.tail
            while current is not None:
                print(current.value)
                current = current.previous
        else:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert_on_start(1)
    doubly_linked_list.insert_on_start(2)
    doubly_linked_list.insert_on_start(3)
    doubly_linked_list.insert_on_start(4)
    doubly_linked_list.insert_on_start(5)
    doubly_linked_list.insert_on_final(6)


    print(30 * '=+')
    # print(doubly_linked_list.head.value)
    # print(doubly_linked_list.tail.value)
    # print(doubly_linked_list.tail.previous.value)
    print(30 * '=+')
    doubly_linked_list.show_list()
    print(30 * '=+')
    # doubly_linked_list.show_list(reverse=True)
    # doubly_linked_list.exclude_start()
    # doubly_linked_list.exclude_final()
    print(30 * '=+')
    doubly_linked_list.exclude_value(0)
    doubly_linked_list.exclude_value(3)
    doubly_linked_list.exclude_value(6)
    doubly_linked_list.show_list()
    print(30 * '=+')
    doubly_linked_list.show_list(reverse=True)
