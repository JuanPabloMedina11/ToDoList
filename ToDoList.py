


toDo = []

print("")
print("Hello this is your to do list")
print("")
a = True
while(a == True):

    answer = input("1:add \n2:remove \n3:close\n")
    print("")

    if answer == "1":
        add = input("Write the task: ")
        toDo.append(add)
        print("")

    elif answer == "2":

        for i in toDo:
            print(i)

        remove = input("Which task do you want to remove: ")
        remove = int(remove) - 1     #Since the list starts from the number 0 the input the person will place will be one higher
        toDo.pop(remove)

        print("")

    elif answer == "3":

        a = False
        
    else:
        print("Invalid Input. Please enter 1,2, or 3.")

for i in toDo:
    print(i)

    