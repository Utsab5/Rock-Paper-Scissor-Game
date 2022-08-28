import sys
import os
import time
from turtle import goto
from ai import AI
from game import Game

os.system("cls") #for cleaning console
moves=['Rock','Paper','Scissor']
ai=AI()
game=Game()

def make_move():
    
    selected_move=input("What is ur move[Rock, Paper, Scissor]").title()
    if selected_move not in moves:
        print("Invalid Input")
        time.sleep(.3)
        return make_move()
    return selected_move

def gameStart():

    pts=int(input("For how much point do u want to play?"))    
    pts_p=0
    pts_ai=0

    while(1):    

        player_move=make_move()
        print(f"You: {player_move}") 
        ai_move=ai.make_move(moves)
        print(f"AI: {ai_move}")     

        w=game.select_winner(player_move,ai_move)

        if w==1:
            pts_p=pts_p+1
        elif w==-1:        
            pts_ai=pts_ai+1   
        
        print(f"You: {pts_p}")
        print(f"AI: {pts_ai}")  
        print("")  

        if pts_p==pts and pts!=pts_ai:
            print("You won 🥳")
            break
        elif  pts_p!=pts and pts==pts_ai:
            print("AI won. Better luck next time 👍")
            break
        elif pts_p==pts and pts==pts_ai:   
            print("Tie")
            break

    ans=input("Do u want to play again(y/n)?") 
    if ans=='y':
        gameStart()
    else:
        time.sleep(.3)
        sys.exit()



gameStart()        
    
        