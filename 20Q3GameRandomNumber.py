import random

num = random.randint(1,10)

tries = 0

while True:
    guess = int(input("please guess your number between 1 and 10 :- "))
    if num == guess:
        tries +=1
        print(f"you are right you guessed the number is {tries} tries")
        break

    elif num < guess:
        print("go a little lower")
        tries +=1
    
    elif num > guess:
        print("go a little higher")
        tries +=1

    else:
        tries +=1 
        print("sorry you are wrong")