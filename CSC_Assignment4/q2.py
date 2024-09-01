class Node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer
    def __str__(self):
        return str(self.element)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __str__(self):
        node = self.head
        print_list = []
        while node:
            print_list.append(node.element)
            node = node.pointer
        return str(print_list)

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
        self.size += 1
    
    def getNode(self, index):
        node = self.head
        count = 0
        while count < index:
            count += 1
            node = node.pointer
        return node
    
    def getLastNode(self):
        node = self.head
        count = 0
        while node.pointer != None:
            count += 1
            node = node.pointer
        return self.getNode(count)
        
    def quick_sort(self, node):
        if self.size == 0:
            return None
        left_list = SinglyLinkedList()
        right_list = SinglyLinkedList()
        pivot_element = self.head.element
        for i in range(1, self.size):
            element = self.getNode(i).element
            if element < pivot_element:
                left_list.insert(element)
            else:
                right_list.insert(element)
        left_list.quick_sort(left_list.head)
        right_list.quick_sort(right_list.head)
        node.pointer = None
        if left_list.size > 0:
            left_list_last = left_list.getLastNode()
            left_list_last.pointer = node
        if right_list.size > 0:
            right_list_first = right_list.head
            node.pointer = right_list_first
        if left_list.size > 0:
            self.head = left_list.head
            return left_list.head
        else:
            self.head = node
            return node      

        
