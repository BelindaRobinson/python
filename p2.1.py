import sys
import csv

def menu():
    print(20*"-","MENU",20*"-")
    print("1. Add Player")
    print("2. Remove Player")
    print("3. Update Player")
    print("4. Sort Players")
    print("5. Exit")
    print(45 * "-")
    
def inputint(message):
    while True:
        try:
            phone = int(input(message))
        except ValueError:
            print("wrong format please try again")
            continue
        else:
            return phone
        
def inputcharacter(message):
    a = '@'
    email = input("please enter you email address")

    if a in email:
        return email
    else:
        print("wrong format") #HALF DONE
        inputcharacter(message)
    
def add():
    name = input("please enter your name")
    email = inputcharacter("please enter you email address")    
    phone = inputint("please enter your mobile number")
    character = input("please enter your characters class")       
    group = input("please enter your group name")    
    
    with open('info.txt', 'a') as datafile:
        datafilewriter = csv.writer(datafile)
        datafilewriter.writerow([name, email, phone, character, group])

    datafile.close()

def remove():
##    NEED TO REMOVE SEARCH DATA
    with open ('info.txt', 'r') as datafile:
        name = input("enter name to search")
        datafilereader = csv.reader(datafile)
        for row in datafilereader:
            for field in row:
                if field == name:
                    print(row)                                           
                    delattr(datafile, row)
                    print(row)

    datafile.close()

def update():
    with open ('info.txt', 'r') as datafile:
        name = input("enter name to search")
        datafilereader = csv.reader(datafile)
        for row in datafilereader:
            for field in row:
                if field == name:
                    print(row)
##        with open ('info.txt', 'w') as datafile:
##        replacename = input("what name would you like to replace it with")
##        datafilewrite = csv.write(datafile)
##        for row in datafile:
##            place != row.appened(replacename)
##            print(row)

##def sort():
    
loop=True      
  
while loop: 
    menu()  
    choice = input("Enter the number for what you would like to do?")
     
    if choice=="1":
        add()        
       
    elif choice=="2":
        remove()
        
    elif choice=="3":
        update()
        
    elif choice=="4":
        sort()

    elif choice == "5":
        sys.exit
       
        loop=False 
    else:
        
        input("invaild option! push enter to try again")
