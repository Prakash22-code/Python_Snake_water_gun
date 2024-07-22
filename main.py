import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([1,0,-1])
yourstr = input("Enter your choice:   ")
youDict = {"s":1, "w": -1, "g": 0}
reverseDict = {1 : "snake", -1 : "water", 0 : "gun"}

you = youDict[yourstr]

# By now we hve 2 numbers(variables) you and computer.

print(f"you chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if(computer == you):
    print("Match is draw!")

'''else:
    if(computer==1 and you ==-1):
        print("you lose!")
!
    elif(computer ==1 and you ==0):
        print("you win!")

    elif(computer ==-1 and you ==1):
        print("you win!")

    elif(computer ==-1 and you ==0):
        print("you lose!")

    elif(computer ==0 and you ==-1):
        print("you win!")

    elif(computer ==0 and you ==1):
        print("you lose!")

    else:
        print("something went woring")

        the below logic is made on basis of computer- you..
'''
if((computer - you) == -1 or (computer - you) == 2):
    print("you win!")
else:
    print("You lose it!")
