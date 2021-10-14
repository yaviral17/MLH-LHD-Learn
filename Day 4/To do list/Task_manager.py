import os

def clear_screen(x=100):
    for i in range(x):
        print(" ")


def display_list(name):
    clear_screen()
    with open("lists\\"+name,'r') as lst:
        r=lst.readlines()
        for lines in r:
            print(lines)
    input()
    return


            

def make_list(name):
    clear_screen()
    with open("lists\\"+name,'a+') as lst:
        ln=len(lst.readlines())
        while 1:
            lst.write(str(ln)+input("Enter your task here\n>>> "))
            display_list(name)
            ch=input("Enter y to enter more task : ")
            if ch!='y':
                return


def remove_list(name):
    try:
        os.remove("lists\\"+name+".txt")
        print("List removed !!")
    except FileNotFoundError:
        print("List does not exist !! ")
    input()


if __name__=="__main__":
    clear_screen()
    while 1:
        print("1- Make new task list")
        print("2- remove an exixting list ")
        print("3- Display a task list ")
        print("E/e- Exit the program ")
        ch=input(">>> ")
        if ch=='1':
            make_list(input("Give a name to the list(Name must be different from existing lists ) : ")+".txt")
        elif ch=='2':
            remove_list(input("Enter the name of the list to be removed : "))
        elif ch=='3':
            display_list(input("Enter the name of the list to be displayed :")+".txt")
        elif ch=='e' or ch=='E':
            exit()
        else:
            print("Worng input!!")
            input()