import random
import math
def restart():
    print("Do you want to play the game once more (Y/N):")
    c=str(input())
    if not ((c=="Y")or(c=="N")):
        c=str(input("Invalid Input , Enter Again (Y/N):"))
    elif(c=="N"):
        j=0
        print("Your Score is:",m)
        exit()
j=1
m=0
while j==1:
    print("LET THE GUESS GAME BEGIN!")
    l=int(input("Enter your Lower bound:"))
    u=int(input("Enter your Upper bound:"))
    x=random.randint(l , u)
    print("You have 3 chances to guess the number")
    i=0
    for i in range(1,4):
        g=int(input("Enter your guess:"))
        if x==g:
            print("Congrats,You have guessed the number in",i,"tries")
            m=m+1
            restart()
            break
        elif i==3:
            print("The number is",x)
            print("Better Luck Next Time!")
            restart()
            break
        elif x>g:
            print("You have",3-i,"tries,","Your guess was too small")
        elif x<g:
            print("You have",3-i,"tries,","Your guess was too high")