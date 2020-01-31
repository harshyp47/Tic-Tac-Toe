import random
import time
#@Harsh Parmar
co=[[1,2,3],[4,5,6],[7,8,9]]
bo=[[" "," "," "],[" "," "," "],[" "," "," "]]
used={0}
def board(bo):
    for i in range(0,3):
        for j in range(0,3):
            if j==1 or j==2:
                print(" | ",end="")
            if j!=2:
                print(bo[i][j],end="")
            else:
                print(bo[i][j])
    print("===========")
def userinput():
    a=int(input("Enter Command:"))
    used.add(a)
    if a==1 or a==2 or a==3:
        bo[0][a-1]="X"
    if a==4 or a==5 or a==6:
        bo[1][a-4]="X"
    if a==7 or a==8 or a==9:
        bo[2][a-7]="X"
def computer():
    b=random.choice([1,2,3,4,5,6,7,8,9])
    while(b in used):
        b = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    used.add(b)
    if b==1 or b==2 or b==3:
        bo[0][b-1]="O"
    if b==4 or b==5 or b==6:
        bo[1][b-4]="O"
    if b==7 or b==8 or b==9:
        bo[2][b-7]="O"
def Check():
    if (bo[0][0]=="X" and bo[0][1]=="X" and bo[0][2]=="X") or (bo[0][0]=="O" and bo[0][1]=="O" and bo[0][2]=="O"):
        return True
    if (bo[1][0]=="X" and bo[1][1]=="X" and bo[1][2]=="X") or (bo[1][0]=="O" and bo[1][1]=="O" and bo[1][2]=="O"):
        return True
    if (bo[2][0]=="X" and bo[2][1]=="X" and bo[2][2]=="X") or (bo[2][0]=="O" and bo[2][1]=="O" and bo[2][2]=="O"):
        return True
    if (bo[0][0]=="X" and bo[1][0]=="X" and bo[2][0]=="X") or (bo[0][0]=="O" and bo[1][0]=="O" and bo[2][0]=="O"):
        return True
    if (bo[0][1]=="X" and bo[1][1]=="X" and bo[2][1]=="X") or (bo[0][1]=="O" and bo[1][1]=="O" and bo[2][1]=="O"):
        return True
    if (bo[0][2]=="X" and bo[1][2]=="X" and bo[2][2]=="X") or (bo[0][2]=="O" and bo[1][2]=="O" and bo[2][2]=="O"):
        return True
    if (bo[0][0]=="X" and bo[1][1]=="X" and bo[2][2]=="X") or (bo[0][0]=="O" and bo[1][1]=="O" and bo[2][2]=="O"):
        return True
    if (bo[0][2]=="X" and bo[1][1]=="X" and bo[2][0]=="X") or (bo[0][2]=="O" and bo[1][1]=="O" and bo[2][0]=="O"):
        return True
    else:
        return False
count=0
board(co)
print("Numbers are mapped in following position. Enter Accordingly. Do not enter if already Filled.\n""Bugs are not Fixed ;)")
board(bo)
inp=input("Enter Y to begin the game.")
if inp=="Y" or inp=="y":
    while (True):
        userinput()
        board(bo)
        print("Thinking...")
        time.sleep(2)
        if Check():
            print("You Won!")
            break
        if count==4:
            print("Game Tied :)")
        computer()
        board(bo)
        if Check():
            print("Computer Won!")
            break
        count = count + 1





