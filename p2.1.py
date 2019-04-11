#!/usr/bin/python3
import sys
import csv
import re
import operator

#diplays a menu to the user which gives them the option to where they would like to go 
def menu():
    print(20*"-","MENU",20*"-")
    print("1. Add Player")
    print("2. Remove Player")
    print("3. Update Player")
    print("4. Sort Players")
    print("5. Exit")
    print(45 * "-")

#checks if the phone number that is enter only contains int and no string 
def inputint(message):
    while True:
        try:
            phone = int(input(message))
        except ValueError:
            print("wrong format please try again")
            continue
        else:
            return phone

#checks if there is an @ symbol in the email as all emails have an @ symbol
def inputcharacter(message):
    a = '@'
    email = input("please enter you email address: ")

    if a in email:
        return email
    else:
        print("wrong format") #HALF DONE
        inputcharacter(message)

#adds each input from the user to the csv file on its own line    
def add():
    name = input("please enter your name: ")
    email = inputcharacter("please enter you email address: ")    
    phone = inputint("please enter your mobile number: ")
    character = input("please enter your characters class: ")       
    group = input("please enter your group name: ")    
    
    with open('info.txt', 'a') as datafile:
        datafilewriter = csv.writer(datafile)
        datafilewriter.writerow([name, email, phone, character, group])

    datafile.close()

#takes user input and searchs for the csv file for that name, if found there is an option to remove the player 
def remove():
    with open ('info.txt', 'r') as datafile:
        name = input("enter name to search")
        datafilereader = csv.reader(datafile)
        for row in datafilereader:
            for field in row:
                if field == name:
                    print(row)
                    a = 'yes'                    
                    inputremove = input("would you like to remove this player, yes or no?")                    
                    if a in inputremove:
                        with open ('info.txt', 'w') as datafile:
                            if field in row:
                                del(row)
                                print("player removed")
                            else:
                                print("please try again")
                                menu()
                                
                        
    datafile.close()

#takes user input and searchs the csv file for that name, if founf there is an option to update that player
def update():
    with open ('info.txt', 'r') as datafile:
        name = input("enter name to search")
        datafilereader = csv.reader(datafile)
        for row in datafilereader:
            for field in row:
                if field == name:
                    print(row)
                    a = 'yes'                    
                    inputremove = input("would you like to update this player, yes or no?")
                    with open('info.txt', 'a') as datafile:
                        if a in inputremove:
                            name = input("please enter your name")
                            email = inputcharacter("please enter you email address")    
                            phone = inputint("please enter your mobile number")
                            character = input("please enter your characters class")       
                            group = input("please enter your group name")
                            with open ('info.txt', 'a') as datafile:
                                datafilewriter = csv.writer(datafile)
                                datafilewriter.writerow([name, email, phone, character, group])
                        else:
                            print("please try again")
                            menu()                        

    datafile.close()
    #info = f.readline()
    # = ["a","b"]
    #finds this person
    #
def sort():
    a = 'yes'
    sortfile = input("would you like to sort the file")
    with open('info.txt', 'r') as datafile:
        if a in sortfile:
            datafilereader = csv.reader(datafile)
            info = []        
            for row in datafilereader:
                info.append(row)
                sortedlist = sorted(info)
                print(sortedlist)
#           split now to get each field           
            
#             sort = sorted(datafile)
#             print(sort)
    
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

