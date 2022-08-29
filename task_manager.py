# =====importing libraries===========
# ====Login Section====
# used a with open to  open the user.txt file as read mode
# The above code is a program that allows the user to register a new user, add a task, view all tasks,
# view my task, and exit.
# The above code is a program that allows the user to register a new user, add a task, view all tasks,
# view my task, and exit.
with open("user.txt", "r+") as f:
    # created a variable called "my_read1" and assigned it to f.readlines() to read all the lines in the file
    my_read1 = f.readlines()

    # created a variable called "my_read2" and assigned it to read all the lines in the file  my_read1 joined
    my_read2 = " ".join(my_read1)

    # created a variable called "my_read3" and assigned it to my_read2 and used the replace function to to replace the comma to an empty
    my_read3 = my_read2.replace(",", "")

    # created a variable called my_read4 and used the split function to created a list with splited in a string
    my_read4 = my_read3.split()

# created empty lists
list_x1 = []
list_x2 = []

# created a range starting 0 to the length of my_read4 len(my_read4) 
for i in range(0, len(my_read4)):

    # if i % 2 is equal to 0 than the code below should be executed
    if i % 2 == 0:

        # if the above statement is true than, it will append that i to list_x1
        list_x1.append(my_read4[i])

        # else will be the defualt if the above the statement is false
    else:

        # if the above statement is false than, it will append that i to list_x2
        list_x2.append(my_read4[i])

# created a variable called manage_task and to dict(zip(list_x1,list_x2)) the dict and zip function to create a dictionary with all all the list_x1 values as keys and list_x2 as values accordingly  
manage_task = dict(zip(list_x1, list_x2))

# used a while true loop to keep asking the same question over and over again till the condition is met
while True:

    # created a variable called username and assigned it to user input requesting input
    username = input("Enter your username: ")

    # created a variable called userpassword and assigned it to user input requesting input
    userpassword = input("Enter your password: ")

    # if username is in manage_task keys in the diction and is the userpassword is equal to the manage_task at that  username key
    if username in manage_task.keys() and userpassword == manage_task[username]:

        # used a while true loop to keep asking the same question over and over again till the condition is met
        while True:

            # presenting the menu to the user and
            # making sure that the user input is coneverted to lower case.
            menu = input('''Select one of the following Options below:
             r - Registering a user
             a - Adding a task
             va - View all tasks
             vm - view my task
             e - Exit
             : ''').lower()

            #  menu is the following statement is true than the code below will be executed
            if menu == 'r' and username == "admin":

                # created a variable called new_username and assigned it to user input requesting input
                new_username = input("Please enter new username: ")

                # created a variable called new_password and assigned it to user input requesting input
                new_password = input("Please enter new password: ")

                # used a while true loop to keep asking the same question over and over again till the condition is me
                while True:

                    # created a variable called confirm_password and assigned it to user input requesting input
                    confirm_password = input("Please confirm password: ")

                    # if the input of confirm_password is equal to new_passaword  than the the code below will be executed
                    if confirm_password == new_password:

                        # used with open to file user.txt as j in append mode
                        with open("user.txt", "a") as j:

                            # used the write funtion to write on to the file
                            j.write("\n" + f"{new_username}, {confirm_password}")

                            # the break will break the loop when the statment is met
                            break

                    # else will be the defualt if the above the statement is false
                    else:

                        # it will display the string as the output
                        print("Sorry please try again")

                # the break will break the loop when the statment is met
                # break

                #  menu is the following statement is true than the code below will be executed
            elif menu == 'a':

                # created a variable called add_info and assigned it to user input requesting input
                add_info = input("Enter your another username: ")

                # created a variable called title_task and assigned it to user input requesting input
                title_task = input("Enter new title task: ")

                # created a variable called describe_task and assigned it to user input requesting input
                describe_task = input("Enter new description: ")

                # created a variable called due_date and assigned it to user input requesting input
                due_date = input("Enter the due date: ")

                # created a variable called current_date and assigned it to user input requesting input
                current_date = input("Enter current date: ")

                # used with open to file tasks.txt as g in append mode
                with open("tasks.txt", "a") as g:

                    # used the write funtion to write on to the file
                    g.write("\n" + f"{add_info}, {title_task}, {describe_task}, {due_date}, {current_date}, No")

                # the break will break the loop when the statment is met
                # break

            # menu is the following statement is true than the code below will be executed
            elif menu == 'va':

                # used with open to file tasks.txt as t in read mode
                with open("tasks.txt", "r") as t:

                    # used the readlines funtion to read the lines on to the file
                    view_a = t.readlines()

                    # used a for loop to iterate through "view_a"
                    for va in view_a:
                        # the code indented will execute
                        # created a view_a2 and assigned it to va.replace() this will allow the code to replace every newline chraracter  with empty quotation marks
                        view_a2 = va.replace("\n", "")

                        # created a new variable called view_a3 and assinged to view_a3.split() method so that string turns to a list
                        view_a3 = view_a2.split(",")

                        # it will display every 3rd character, 4th character, and 5th characterprint(" " + "Task:" + "\t\t\t\t\t\t" + var_z[1] + "\n", "Assigned to:"+ "\t\t\t\t " + var_z[0] + "\n", "Date assigned:" + "\t\t\t" + var_z[3] + "\n", "Due date:" + "\t\t\t\t\t" + var_z[4] + "\n", "Task Complete?" + "\t\t\t" + var_z[5] + "\n", "Task description:" + "\t\t" + var_z[2] + "\n")
                        print(f"Task:             {view_a3[1]}")
                        print(f"Assigned to:       {view_a3[0]}")
                        print(f"Date assigned:    {view_a3[3]}")
                        print(f"Due date:         {view_a3[4]}")
                        print(f"Task Complete?    {view_a3[5]}")
                        print(f"Task description: {view_a3[2]} \n")


            # menu is the following statement is true than the code below will be executed
            elif menu == 'vm':

             # the code indented will execute
             # created a open_1 and assigned it to vm.replace() this will allow the code to replace every newline chraracter  with empty quotation marks and split at every comma
             with open("tasks.txt","r") as f:
              var_lines = f.readlines()
              for i in var_lines:
               display_vm = i.replace("\n","").split(",")
               if username == display_vm[0]:
                 print(f"User Assigned:     {display_vm[0]}")
                 print(f"Task Title:       {display_vm[1]}")
                 print(f"Task Description: {display_vm[2]}")
                 print(f"Date Assigned:    {display_vm[3]}")
                 print(f"Due Date:         {display_vm[4]}")
                 print(f"Completion:       {display_vm[5]}\n")


            # if the following statement is true than the code below will be executed
            elif menu == 'e':

                # the string will be displayed
                print('Goodbye!!!')

                # the break will break the loop when the statment is met
                break
            else:
                print("incorrect choices")

        # the break will break the loop when the statment is met
        break

        # else will be the defualt if the above the statement is false
    else:

        # the string will be displayed
        print("You have made a wrong choice, Please Try again")