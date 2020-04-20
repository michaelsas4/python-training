#Guess Game 2#
secret_num1 = "8"
secret_num2 = "4"
guess_num1 = " "
guess_num2 = " "
guess_count = 0
guess_limit = 4
out_of_guesses = False
while guess_num1 != secret_num1 and not(out_of_guesses):
    if guess_count < guess_limit:
        guess_num1 = input("enter guess_num1: ")
        guess_count +=1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("out of guessess, You Lose! ")
else:
    print("You Win! ")
while guess_num2 != secret_num2 and not(out_of_guesses):
    if guess_count < guess_limit:
        guess_num2 = input("enter guess_num2: ")
        guess_count +=1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("out of guessess, You Lose! ")
else:
    print("You Win")









