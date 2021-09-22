## Matthew Lewis ##
## Chapter 3 ##
## 21 Sep 2021 ##

## 3.1.1.4 ##

n = int(input("Enter a value for n: ")) ## Asking for a number input from user ##
print(n >= 100) ## Where input above is greater than or equal to 100, will show true or false when either success or failure ##

## 3.1.1.10 ##
 
plant =input("Your plant = ")
if plant=="Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant=="spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", str(plant),"!") ## This line recalls the user input if it doesnt satisfy the 2 previous if else loops to display ##
    
## 3.1.1.11 ##

income =float(input("Enter the annual income: ")) ## user input for income ##

if income <= 85528:
    tax = (0.18 * income) - 556.02 ## If the income is less than 85,528. The tax is worked ut as 18% of the full amount minus the amount for tax relief ##
elif income > 85528:
    tax=(income-85528)*.32 + 14839.02 ## This equation works out the tax if the input was greater than 85,528, the tax is 14,839.02 as a base, then the remainder from income minus that base amount is taxed at 32% ##
if tax < 0:
    tax = 0 ## If this amount was less than 0. Tax is shown as 0 ##
else:
    tax = round(tax, 0) ## If the equation does not return any of these values then tax is 0.0 ##
print("The tax is:", tax, "thalers")

## 3.1.1.12 ##

year = int(input("Enter a year: ")) ## User input for year ##

if year % 4 != 0: ## using != to see if the year is devisable by 4 into 0 ##
        print(year, "is a common year")
elif year % 100 != 0: ## As above but using leap year maths ##
        print(year, "is a Leap year")
elif year % 400 != 0:
        print(year, "is a common year")
else :
        print(year, "is a Leap year") ## Any year outside of these fit in to Leap year calculations
if year < 1582:
    print ("but", year, "is not within Gregorian calendar period.")
    
## 3.2.1.3 ##

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number_guess = int(input("Enter your guess: "))
while number_guess != secret_number: ## Used to determine if the guess is a match for our secret number ##
    print ("Haha, You're stuck in my loop")
    number = int(input("Enter another guess: "))
else:
    print("Well done, muggle! You are free now.")
    
## 3.2.1.6 ##

import time

for n in range (5): # Write a for loop that counts to five.
    print (n+1, "Mississippi" ) # Body of the loop - print the loop iteration number and the word "Mississippi".
    time.sleep(1) # Body of the loop - use: time.sleep(1)

print ("Ready or not, here I come!") # Write a print function with the final message.

## 3.2.1.9 ##

secret_word="" # I entered this as I had to have a base value to go off of, or the loop would initiate straight away.
while True:
    secret_word= input("Incorrect! \n Enter secret word to leave loop: ")
    if secret_word == "chupacabra": ## Secret word is equal to ... ##
        print ("You've successfully left the loop.")
        break
        
## 3.2.1.10 ##        

user_word = input("Enter a word: ")
user_word = user_word.upper() ## Converts word to upper-case ##

for letter in user_word:
    # Complete the body of the for loop.
    if letter == "A": ## passes over if it is equal to input ##
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else: 
        print(letter, end="\n") ## Prints remainder of letters on new lines ##
      
## 3.2.1.11 ##

## Whole code is as previous but with the removal of \n so that it prints on one line ##
user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the for loop.
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else: 
        print(letter, end="")
      
## 3.2.1.15 ##
