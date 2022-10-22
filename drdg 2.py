stack=[]
top=None
while True:
    print('STACK OPERATIONS')
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Exit")
    choice=int(input('enter your choice[1-4]'))
    if choice==1:
        MemberNo=int(input('enter  member no'))
        MemberName=input("enter member name")
        MemberAge=int(input("enter member age"))
        item=[MemberNo,MemberName,MemberAge]                   
        stack.append(item)
    elif choice==2:
        stack.pop()
    elif choice==3:
        print(stack)
    else:
        break
