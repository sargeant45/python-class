"""
a practice hangman script in Python
yes, I know its messy but I just started learning the language a few days ago
open source under the MIT license, (c) Ethan Arterberry 2015
heavily commented because my code is messy
"""

import random
import os

# define some functions that are used in the program
def winning(lives, tries): # winning script
  print("You guessed the word after trying " + str(tries) + " times with " + str(lives) + " lives left.")
  
def cls(): # clear console
    os.system(['clear','cls'][os.name == 'nt'])

# define some variables that are used in the program
fname = "dictionary.txt" # filename/path for the dictionary
lives = 5                # lives
tries = 0                # total tries it took to guess the word

with open(fname) as f:                                    # open dictionary
    dictionary = f.readlines()                            # put dictionary into a list
dictionary = [line.rstrip('\n') for line in open(fname)]  # strip newlines from list

random_word = dictionary[random.randint(0, len(dictionary) - 1)]  # grab random word from dictionary list

blanks = "_" * len(random_word) # create obfuscated string of the random word

cls() # clear the console

while lives > 0:
  cls() # clear the console
  print(blanks)                 # print the blanks
  print("guess a letter!")
  print("lives: " + str(lives)) # print the lives you have left
  
  guessed_letter = raw_input()  # get a letter that the player will guess
  
  if guessed_letter in random_word and guessed_letter not in blanks:  # check if the letter is in random word but has not already been guessed
    random_word = list(random_word) # turn random word
    blanks = list(blanks)           # and blanks into a list so they can be indexed as one
    
    for i in range(0, len(random_word)): # loop through the word and add all instances of the letter to the blanks
      if random_word[i] == guessed_letter:
        blanks[i] = guessed_letter
    
    random_word = "".join(random_word) # join random word and blanks back into a string
    blanks = "".join(blanks)
  else:
    lives -= 1  # if the condition isn't true then remove a life
  tries += 1 # add a try to the count

  if blanks == random_word: # check if the player has guessed the word fully
    winning(lives, tries) # run winning function with tries and lives passed
    break
  
if lives <= 0: # check for loss and output losing message
  print("You ran out of lives! Hopefully you'll do better next time!")