class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_node_value(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __list_is_empty(self):
        return self.head is None

    def insert_on_start(self, value):
        new = Node(value)
        if self.__list_is_empty():
            self.tail = new
        new.next = self.head
        self.head = new

    def insert_on_final(self, value):
        new = Node(value)
        if self.__list_is_empty():
            self.head = new
        else:
            self.tail.next = new
        self.tail = new

    def show(self):
        if self.__list_is_empty():
            print('The list is empty')
            return
        current: Node = self.head
        while current is not None:
            print(current.get_node_value())
            current = current.next

    def search(self, value):
        if self.head is None:
            print('The list is empty')
            return None
        current = self.head
        while current.value != value:
            if current.next is None:
                return None
            current = current.next
        return current

    def exclude_head(self):
        if self.__list_is_empty():
            print('The list is empty')
            return
        head = self.head
        if self.head.next is None:
            self.tail = None
        self.head = self.head.next
        return head


if __name__ == '__main__':
    linked_list = LinkedList()
    empty_list = LinkedList()
    linked_list.insert_on_final(1)
    linked_list.insert_on_final(2)
    linked_list.insert_on_final(3)
    linked_list.insert_on_final(4)
    linked_list.insert_on_start(0)

    linked_list.show()
    print(15*'=+')
    head = linked_list.exclude_head()
    print(head.value)
    print(15 * '=+')
    linked_list.show()
    print(15 * '=+')
    empty_list.exclude_head()

