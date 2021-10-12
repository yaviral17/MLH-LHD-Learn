import random

def horror():
    with open("HORROR.txt","r") as f:
        line=f.readlines()
        chh=random.choice(line)
        return chh

def action():
    with open("Action.txt","r") as f:
        line=f.readlines()
        chh=random.choice(line)
        return chh

def romantic():
    with open("romantic.txt","r") as f:
        line=f.readlines()
        chh=random.choice(line)
        return chh

ch=random.choice(["Action","Horror","Romantic"])

if ch == "Action":
    print("Today you should : ",action())
elif ch=="Romantic":
    print("Today you should watch : ",romantic())
else :
    print("Today you should watch : ",horror())
    
