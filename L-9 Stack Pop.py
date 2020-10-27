class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def popspecific(self,data):
        if data in self.items:
            self.items.remove(data)
            print("Element popped!")
        else: print("Element not found")

    def printstack(self):
        print(self.items)


s = Stack()
for i in range(11): s.push(i)
print("The elements of the stack : ")
s.printstack()
d = int(input("Enter the element you want to pop : "))
s.popspecific(d)

