import os
from random import choice
import playsound as ps

elm=['stone','paper','scissor']

def clear_screen(n=100):
    for i in range(n):
        print(" ")

def take_input():
    clear_screen()
    while 1:
        ps.playsound("audio\input.m4a")
        ch=int(input("1- Stone\n2- Paper\n3- Scissors\n>>> ")) 
        if ch in [1,2,3]:
            break
        else:
            print("Wrong input try again : ")
    return ch

def Result(ch,ai):
    clear_screen()
    if((ai==1 and ch ==3) or (ai==2 and ch ==1) or (ai == 3 and ch == 2) ):
        ps.playsound("audio\you lose.m4a")
        return f"Computer Chose : {elm[ai-1]}\nYou Lose ! "
    elif ai==ch:
        return f"Computer Chose : {elm[ai-1]}\nDraw ! "
    else:
        ps.playsound("audio\you win.m4a")
        return f"Cpomputer chose : {elm[ai-1]}\nYou win !"


if __name__=="__main__":
    while 1:
        print(Result(take_input(),ai=choice([1,2,3])))
        c=input("\nEnter 'e' to exit")
        if c=='e':
            break
