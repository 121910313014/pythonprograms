class Stack:
    def __init__(self,size):
        self.size = size
        self.fixed = size
        self.items = [0]*self.size
        print(self.items)

    def push(self, data):
        if self.size>0:
            self.items[self.fixed-self.size] = data
            print(self.items)
            self.size -= 1
            return True
        else:
            print('OVERLOAD!!')
            return False

    def pop(self):
        if self.items!=[]:
            return self.items.pop()
        else:
            print("OVERLOAD!!")
            return False

    def printstack(self):
        print(self.items)


n = int(input("Enter the size of the stack : "))
s = Stack(n)
print("Enter the elements of the stack : ")
pu = True
while pu:
    ele = int(input())
    pu = s.push(ele)
while True:
    ans = input("Do you want to pop the stack (y/n) : ")
    if ans == 'y':
        pp = s.pop()
        if pp==False: break
        else: print(pp)
    elif ans=='n': break
    else: print("Enter a valid input!!")





