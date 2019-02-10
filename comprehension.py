import random  # importing the random module

guesses_taken = 0  # initialize 0 to the variable

print('Hello! What is your name?')  # print function which writes out the given string to console
myName = input()  # assign myName variable as an input function

number = random.randint(1, 20)  # assign a random value(1, 20) to the number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  
# write the given strings to console with the myName variable

while guesses_taken < 6:  # repeat the below code as long as the expression is True
    print('Take a guess.')  # print function to write the given string
    guess = input()  # assign the guess variable as an input function
    guess = int(guess)  # convert the value of guess variable to integer

    guesses_taken += 1  # increase the value of guesses_taken by 1

    if guess < number:  # if guess variable less than the number variable, it executes
        print('Your guess is too low.')  # print function writes out the given string 

    if guess > number:  # if guess variable more than the number variable, it executes
        print('Your guess is too high.')  # print function writes out the given string 

    if guess == number:  # if guess variable equals to the number variable, it executes
        break  # exiting the while loop

if guess == number:  # if guess variable equals to the number variable, it executes
    guesses_taken = str(guesses_taken)  # convert the value of guesses_taken to string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')  
    # write the given strings with the two given values

if guess != number:  # if guess variable equals to the number variable, it executes
    number = str(number)  # convert the value of guesses_taken to string
    print('Nope. The number I was thinking of was ' + number)  # write the given strings with the two given values
