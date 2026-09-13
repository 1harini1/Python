print("-------------------------------------------")
print("|   WELCOME TO THE NUMBER GUESSING GAME!   |")
print("-------------------------------------------")
import random
while True:
    random_number=random.randint(1,100)
    attempts=0
    while True:
        guess=int(input("Guess a number between 1 and 100: "))
        attempts+=1
        difference=abs(guess-random_number)
        if guess<random_number:
            if difference<=3:
                print("Very close! Try again.")
            elif difference <=10:
                print("Close! Try again.")
            else:
                print("Too low! Try again.")
        elif guess>random_number:
            if difference<=3:
                print("Very close! Try again.")
            elif difference <=10:
                print("Close! Try again.")
            else:
                print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
            break
    Play=input("Do you want to play again? (yes/no): ")
    if Play.lower() == "no":
        print("Thank you for playing!")
        break


