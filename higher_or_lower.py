from random import randrange
def user_enter_a_number():
        #ask the use to enter a # between 1-10:
        # will need to save it
        saved_input = int(input('Enter a number between 0-10:'))
        return saved_input

def random_number():
    return randrange(10)

def values_random_number():
    #saves input from the methods above
    saved_number = user_enter_a_number()
    ran_number = random_number()
    # == means evaluating
    while saved_number != ran_number:
        if saved_number< ran_number:
            print("You need to guess higher. Try again")
            saved_number = int (input("\n Guess a number between 1 and 10: "))
        else:
            print("You need ro guess lower. Try again")
            guess = int(input("\nGuess a number between 1 and 10: "))
    print('You guessed the number correctly !!!!!!')
    #print(f'The random number was:{ran_number}')


values_random_number()


