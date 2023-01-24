i = 0
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

print("All the odd numbers below 20 printed")


# guessing game
def guess_the_word(guess_word):
    guess_limit = 3
    out_of_guesses = False
    correct_word = False
    while not correct_word and not out_of_guesses:
        your_guess = input("Enter the guess: ")
        if your_guess != guess_word:
            guess_limit -= 1
            if guess_limit == 0:
                out_of_guesses = True
                print("You have exhausted your guesses")
            else:
                print("Wrong! you have " + str(guess_limit) + " more tries")
        else:
            print("You win!")
            correct_word = True


your_word = "cricket"
guess_the_word(your_word)
