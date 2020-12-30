
# Mini-game
print("Guess the number \n")
number = 11
while number < 0 or number > 10:
    try:
        number = int(input("Choose a number between 0 and 10: "))
    except ValueError:
        print("Letters or decimal numbers are not accepted")
    if 0 <= number <= 10:
        print("The number is chose")
        break

print("Now you can guess the number, you have 3 tries ! \n")
tries = 3
userChoice = 12
while userChoice != number and tries > 0:
    print(tries, "tries \n")
    userChoice = int(input("Take a guess: "))
    if 0 <= userChoice <= 10:
        if userChoice < number:
            print("the number is higher")
        if userChoice > number:
            print("the number is lower")
        if userChoice == number:
            break
    else:
        print("The number is between 0 to 10")
    tries = tries - 1

if tries > 0:
    print("You guessed the right number. Congratulations !")
else:
    print("You didn't manage to get the right number, better luck next time...")

