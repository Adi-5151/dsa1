Stack =[]
max = 5 
def push(item):
    if len(Stack)== max:
        print("stack is overflow")
    else:
        Stack.append(item)
        print(item,"inserted")
def pop():
    if len(Stack)== 0:
     print("stack underflow")
    else:
       item = Stack.pop()
       print("deleted element",item)
def peek():
 if len(Stack)== 0:
    print("stack in empty")
 else:
    print("top element",Stack[-1])
def display():
   if len(Stack) == 0:
      print("stack is empty")
   else:
      print("stack elements",Stack[-1])
push(10)
push(20)
push(30)
display()
peek()
pop()
display()


  
    
