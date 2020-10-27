class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if s.items!=[]: return self.items.pop()

    def printstack(self):
        print(self.items)

s = Stack()
print("Select a choice :")
print("1. PUSH")
print("2. POP")
print("3. DISPLAY")
print("4. EXIT")
while True:
    choice = int(input("Enter a choice number (1/2/3/4) : "))
    if choice==1:
        data = input("Enter the element you wanna push in the stack : ")
        s.push(data)
    elif choice==2: print("The popped element is", s.pop())
    elif choice==3:
        print("The stack is : ")
        s.printstack()
    elif choice==4:
        print("----The menu is closed----")
        break
    else: print("Enter a valid choice")


