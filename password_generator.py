import random

'''
    Author: Dyllon Enos
    Description: This program will create a unique password by using
                 random letters and numbers and symbols. The program
                 will ask the user input for how long the random
                 password could be. If the user input is longer than 73,
                 the default length of the password will be 73 characters. 
                 If the user input is less than 1, the default length of the
                 password will be 1 character. The program will use the
                 sample function from the random class to randomly make a
                 password and store it. Once the password is created, the
                 program will output the password to the user for the user
                 to copy. The sample function will choose random characters
                 from a string and will loop this until the length value is
                 met.
'''

lower_letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
random_symbols = "!@#$%^&*()?"

combination = lower_letters + upper_letters + numbers + random_symbols
length = int(input("Enter length of password (1 - 73)\n"))

if (length < 1):
    length = 1

if (length > 73):
    length = 73

password = "".join(random.sample(combination, length))

print("Your " + str(length) + " password is: \n" + str(password))