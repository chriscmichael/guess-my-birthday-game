from random import randint

name = input("Hi! What is your name ")

#guess 1

guess_number = 1

month_number = randint(1,12)
year_number = randint(1910, 2023)

print("Guess " , guess_number , " : " , name , " were you born on " , month_number , " / " , year_number , " ?")

response = input("yes of no? ")

if response == "yes":
    print("I Knew It")
    exit()

else:
    print("OK let me try again!")

#guess 2

guess_number = 2

month_number = randint(1,12)
year_number = randint(1910, 2023)

print("Guess " , guess_number , " : " , name , " were you born on " , month_number , " / " , year_number , " ?")

response = input("yes of no? ")

if response == "yes":
    print("I Knew It")
    exit()

else:
    print("OK let me try again!")

#guess #3

guess_number = 3

month_number = randint(1,12)
year_number = randint(1910, 2023)

print("Guess " , guess_number , " : " , name ," were you born on " , month_number , " / " , year_number , " ?")

response = input("yes of no? ")

if response == "yes":
    print("I Knew It")
    exit()

else:
    print("OK let me try again!")

#guess number 4

guess_number = 4

month_number = randint(1,12)
year_number = randint(1910, 2023)

print("Guess " , guess_number , " : " , name ," were you born on " , month_number , " / " , year_number , " ?")

response = input("yes of no? ")

if response == "yes":
    print("I Knew It")
    exit()

else:
    print("You beat me!!!!")
    exit()
