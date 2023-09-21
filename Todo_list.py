#Todo List
todo_List=[]
def add_Todo():
    n=int(input("Enter the How many items you want add:"))
    for i in range(1,n+1):
        todo_Item=input("Enter the new todo item:")
        todo_List.append(todo_Item)
    return "New item added successfully"
def view_Todo():
    print("Todo List")
    for index,item in enumerate(todo_List,start=1):
        print("{}:{}".format(index,item))

def complete_Todo():
    view_Todo()
    try:
        choice=int(input("Enter the completed Todo_item:"))
        if 1<= choice <=len(todo_List):
            completed=todo_List.pop(choice-1)
            print(f"{completed} marked as completed and removed from the list")
        else:
            print("Enter valid choice")
    except ValueError:
        print("Invalid input")


while True:
    print("Select the operation to perform your Todo_List")
    print("1.Add item to your Todo_List")
    print("2.View items to your Todo_List")
    print("3.Completed and remove the item in a Your Todo_List")
    print("4.Quit")
    try:
        choice=int(input("Enter the choice:"))
        if choice==1:
            add_Todo()
        elif choice==2:
            view_Todo()
        elif choice==3:
            complete_Todo()
        else:
            break
    except:
        print("Invalid Choice")
    
        
    
    
