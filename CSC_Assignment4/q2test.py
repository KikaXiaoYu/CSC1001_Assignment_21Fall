from q2 import *
from random import randint
test11 = SinglyLinkedList()
nums = []
for i in range(999):
    nums.append(randint(0,9999999))
print(nums)
len_nums = len(nums)
for i in range(len_nums):
    test11.insert(nums[i])
test11.quick_sort(test11.head)
node_test = test11.head
print(node_test.element)

while node_test.pointer != None:
    i += 1
    node_test = node_test.pointer
    print(node_test.element)
    