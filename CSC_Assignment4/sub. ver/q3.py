class ListStack(): 
    def __init__(self):
        self.data = list()
    def isEmpty(self):
        return len(self.data) == 0
    def push(self, e):
        self.data.append(e)
    def pop(self):
        if self.isEmpty() == 0:
            return self.data.pop()

def HanoiTower(n):
    position = ["A","B","C"]
    process_stack = ListStack()
    process_stack.push((n,0,2,1))
    while process_stack.isEmpty() == 0:
        next_tuple = process_stack.pop()
        N, I, J, K = next_tuple[0], next_tuple[1], next_tuple[2], next_tuple[3]
        if N > 1:
            process_stack.push((N-1,K,J,I))
            process_stack.push((1,I,J,K))
            process_stack.push((N-1,I,K,J))
        else:
            print("%s --> %s" % (position[I], position[J]))

def main():
    n = input("Please input the number n:")
    try:
        n = int(n)
        if n <= 0:
            print("Invalid input!")
            return
    except:
        print("Invalid input!")
        return
    HanoiTower(n)

main()
