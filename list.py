#=============== list ===============
shopping_list = []

#=============== choice ===============
while True:   
    print("Enter your choice: "
    "\n\t1: Add to shopping list"
    "\n\t2: Remove to shopping list"
    "\n\t3: Print list"
    "\n\t4: Exit")
    print("*-"*30)

    option = int(input("Enter your choise: "))

 #=============== add to list ===============
    if option == 1:
        x = input("add to list(by-->,): ").split(",")
        for i in x :
            shopping_list.append(i)
            print("*-"*30)

 #=============== remove from list ===============    
    elif option == 2:
        r = input("remove to list ").split(",")
        for i in r:
            shopping_list.remove(i)
            print("*-"*30)

 #=============== print list ===============                   
    elif option == 3:
        print("*-"*30)
        if not shopping_list:
            print("empty!")
        for i in shopping_list:
            print(i)
        print("*-"*30)

 #=============== exit ===============           
    elif option == 4:
        print("*-"*30)
        print("Thank you for using my app") 
        exit(0)

 #--------------- when user select option not exist in options list ------------------  
    else:
        print("*-"*30)
        print("WRONG!!!")
        print("*-"*30)
        print("Thank you for using my app") 
        exit(0)
