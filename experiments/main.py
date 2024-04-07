from functions import get_todos,write_todos
import functions
import time
now = time.strftime("%d/%m/%Y %H:%M:%S")
print("it is")

while True:
    user_action=input("Type add, show ,edit ,complete or exit:")
    user_action=user_action.strip()
    if 'add' in user_action:
        todo=user_action
        todos=get_todos() #call the function,goes back to function and implicitly taking default parameter

        todos.append(todo + "\n")
        write_todos(todos)

    elif 'show' in user_action:
        todos = get_todos() #it will take default parameter implicitly
        #new_todos=[item.strip('\n') for item in todos]
        for index,item in enumerate(todos):
            item=item.strip('\n')
            row=f"{index+1}. {item}" #used to remove spacing before clean in o/p
            print(row)
    elif 'edit' in user_action: #someone want to edit and enter 2 hence int used.
        try:
            number=int(user_action[5:])
            print(number)#convert string to number
            number= number - 1 #if user want to edit 1 but doesnt know indexing
            todos = get_todos() #implicitly take default parameter

            new_todo= input("enter a new todo:") #change old to new
            todos[number]= new_todo #replacing new with old
            print("here is how it will be:", todos)
            write_todos(todos)
        except ValueError:
            print("your command is not valid:")
    elif 'complete' in user_action:
        number=int(input("number of the todo to complete:"))
        todos.pop(number-1)
    elif 'exit' in user_action:
        break
print("Bye!")
