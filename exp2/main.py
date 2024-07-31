from random import randint
actual = randint(1,10)
while True:
    guess = int(input("guess a number between 1 and 9: "))
    print("try higher") if guess < actual else print("try lower") if guess > actual else print("Right Guess!", exit())
