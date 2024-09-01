class Node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert(self, data):
        if isinstance(data, Node):
            node = data
        else:
            node = Node(data, None)
        if self.head == None:
            self.head = node
        else:
            in_node = self.head
            while in_node.pointer:
                in_node = in_node.pointer
            in_node.pointer = node
    
    def recursive_count(self, node):
        if isinstance(node, Node) == 0:
            return "Invalid input!"
        if node.pointer == None:
            return 1
        return self.recursive_count(node.pointer) + 1

        