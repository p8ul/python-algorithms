#!/bin/python3


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node):
    while node:
        print(str(node.data), end=' ')
        node = node.next


def insertNodeAtPosition(head, data, position):
    llist = SinglyLinkedList()
    index = 0

    while head:
        if index == position:
            llist.insert_node(data)
        else:
            llist.insert_node(head.data)
            head = head.next
        index += 1

    return llist.head


linked_list = SinglyLinkedList()

nodes = [16, 13, 7]

for node in nodes:
    linked_list.insert_node(node)

data = 1
position = 0
linked_list_head = insertNodeAtPosition(linked_list.head, data, position)
print_singly_linked_list(linked_list_head)
