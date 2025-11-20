# lab8Strings.py
# Ira Goldstein

# Demo of string manipulation

def sayHello():
#A function that greets people

  #Ask the user for their name.
  theirName =  input("What is your name? ")

  #Create and display the greeting
  greeting = "Hello " + theirName + "."
  print ( greeting )


def eachCharacter(myString):
#A function that prints each character in the string on its own line.

  #Iterate through each character in myString
  for myCharacter in myString:

    #Display the character
    print ( myCharacter )


def eachCharacter2(myString):
#A function that prints each character in the string on its own line using indecies.

  #Iterate through each character in myString
  for index in range ( len(myString) ):

    #Display the character
    print ( myString[index] )

#  Define functions above
#  Call functions below

sayHello()
