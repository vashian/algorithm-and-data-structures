from platform import node


nums = list(map(int, input().split()))


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def reverse_list(self, head: Node):
        if head == None or head.next == None:
            return node

        current = head
        previous = None
        temp = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous


class Solution:

    def __init__(self, numbers: list) -> None:

        llist = LinkedList()

        for num in numbers:
            llist.append(num)

        llist.print_list()
        llist.reverse_list(llist.head)
        llist.print_list()


Solution(nums)
