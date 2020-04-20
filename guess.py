secret_num1 = "2"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_num1 and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter guess: ")
        guess_count +=1
    else:
            out_of_guesses = True
            if out_of_guesses:
                print("out of guesses, You Lose! ")
            else:
                    print("You win! ")


