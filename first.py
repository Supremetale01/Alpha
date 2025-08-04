import random

def guess_number_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randrange(1, 100)
    
    attempts = 0

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low. Try again.")

            elif guess > secret_number:
                print("Too high. Try again.")
                #this is just a testrun on comments. It works sharp 

            else:
                print(f"✨🎉 Congratulations! You guessed it in {attempts} attempts.")
                break
            
        except ValueError:
            print("Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    guess_number_game() 


