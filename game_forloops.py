from random import randint

name = input("Hi! What is your name ")


for guess_number in range(1,6):
    month_number = randint(1,12)
    year_number = randint(1910, 2023)
    print("Guess " , guess_number , " : " , name , " were you born on " , month_number , " / " , year_number , " ?")
    response = input("yes or no? ")
    if response == "yes":
        print("I Knew It")
        exit()
    elif guess_number == 5:
        print("You beat me!")
    else:
        print("Let me try again!!")
