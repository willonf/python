class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_node_value(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.first = None

    def insert_on_start(self, value):
        new_node = Node(value=value)
        new_node.next = self.first
        self.first = new_node

    def show(self):
        current: Node = self.first
        while current is not None:
            print(current.get_node_value())
            current = current.next

    def unshift(self):
        # Remove the first element
        if self.first is None:
            print('The list is empty')
            return None
        current_first = self.first
        self.first = self.first.next
        return current_first

    def search(self, value):
        if self.first is None:
            print('The list is empty')
            return None
        current = self.first
        while current.value != value:
            if current.next is None:
                return None
            current = current.next
        return current

    def exclude(self, value):

        if self.first is None:
            print('The list is empty')
            return None

        current = self.first
        previous = self.first
        while current.value != value:
            if current.next is None:
                return None
            else:
                previous = current
                current = current.next

        if current == self.first:
            self.first = self.unshift()
        else:
            previous.next = current.next

        return current



if __name__ == '__main__':
    node = Node(5)
    linked_list = LinkedList()
    linked_list.insert_on_start(1)
    linked_list.insert_on_start(2)
    linked_list.insert_on_start(3)
    linked_list.insert_on_start(4)

    # my_value = linked_list.search(5)
    # if my_value is None:
    #     print('Does not exist on list')
    # else:
    #     print(my_value.get_node_value())

    exclude_value1 = linked_list.exclude(3)
    print(exclude_value1.value)

    exclude_value2 = linked_list.exclude(9)
    print(exclude_value2)


    linked_list.unshift()
    linked_list.unshift()
    linked_list.unshift()
    # linked_list.unshift()
    # linked_list.show()
