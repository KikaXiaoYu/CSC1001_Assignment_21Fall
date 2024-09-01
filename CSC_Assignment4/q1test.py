from q1 import *
test11 = SinglyLinkedList()
for i in range(4):
    test11.insert(i)
print(test11.recursive_count(test11.head))
print(test11.recursive_count(2))