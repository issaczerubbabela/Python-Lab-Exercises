#Rock, Paper, Scissor.
from random import randint
while True:
    print("You Win!") if int(input("do you choose rock, paper or scissors?")) - randint(1,3) == -1 else print("You Loser! Try again")
