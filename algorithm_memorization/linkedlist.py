# Linked List
class Node():
    def __init__(self, data, nextn=None):
        self.data = data
        self.nextn = nextn

class LinkedList():
    def __init__(self, data):
        self.head = Node(data)

    def addFirst(self, data):
        new = Node(data)
        new.nextn = self.head
        self.head = new

    def addLast(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            return
        last = self.head
        while last.nextn != None:
            last = last.nextn
        last.nextn = new

    def add(self, mid_node, data): # mid_node가 node 주소일때
        if mid_node == None:
            print("ERROR : the node is absent")
            return

        new = Node(data)
        new.nextn = mid_node.nextn
        mid_node.nextn = new

    def delete(self, remove_data):
        del_node = self.head
        if del_node == None:
            return

        if del_node.data == remove_data:
            self.head = del_node.nextn
            del_node = None # del del_node
            return
        else:
            while del_node.nextn.data != remove_data:
                del_node = del_node.nextn
            temp = del_node.nextn
            del_node.nextn = del_node.nextn.nextn
            temp = None

    def traversal(self):
        next_node = self.head
        while next_node.nextn != None:
            print(next_node.data)
            next_node = next_node.nextn