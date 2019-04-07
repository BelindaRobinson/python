import sys

def menu():     
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Player")
    print("2. Remove Player")
    print("3. Update Player")
    print("4. Sort Players")
    print("5. Exit")
    print(45 * "-")

def add():    
    f = open("info.txt","a")

    name = input("please enter your name")
    f.write("\n")
    f.write(name)    

    email = input("please enter you email address")
    f.write("\n")
    f.write(email)

    phone = input("please enter your mobile number")
    f.write("\n")
    f.write(phone)

    character = input("please enter your characters class")
    f.write("\n")
    f.write(character)

    group = input("please enter your group name")
    f.write("\n")
    f.write(group)

def remove():
    f = open("info.txt","r")
    search = input("please enter the players name you witch to search for")
    flag = index = 0

    for line in f:
        line.strip().split("\n")
        index+=1
        if search in line:
            flag = 1
            break
    if flag == 0:
        print(f"sorry couldnt find {search}")
    else:        
        print(f"found {search} in line {index}")        

def deleteline():
            output = []
            str="belinda"
#            searchinput = (search)
            for line in f:
                if not line.startswitch(searchinput):
                    output.append(line)
            f.close()
            f = open("info.txt","w")
            f.writelines(output)
            f.close()
            deleteline()
        
#    with open ("info.txt", "rt") as in_file:
#        contents = f.read()
#        print(contents)
    
#    playername = list()
#    playeremail = list()
#    playerphone = list()
#    playeravailability = list() put in later alot to write
#    playercharacter = list()
#    playergroup = list()

#    playernameinput = input("Please enter your name")    
#    playername.append(playernameinput)
#    print(playername)

    
    
loop=True      
  
while loop: 
    menu()  
    choice = input("Enter the for where you would like to go?")
     
    if choice=="1":
        add()        
       
    elif choice=="2":
        remove()
        
    elif choice=="3":
        print("Update Player")
        
    elif choice=="4":
        print("Sort Players")

    elif choice == "5":
        sys.exit
       
        loop=False 
    else:
        
        input("Wrong option selection. Enter any key to try again..")

 

        
