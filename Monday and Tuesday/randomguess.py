import random

rand_num = random.randint(1,50)

guesses = 0

while guesses < 6:
  guesses += 1
  if guesses > 1:
    s = "s"
  else:
    s = ""
  
  print "Enter a number."
  user_num = int(raw_input())
  
  if user_num > rand_num:
    print "Too high!"
  if user_num < rand_num:
    print "Too low!"
  if user_num == rand_num:
    print "You guessed correctly after trying " + str(guesses) + " time" + s + ". Congratulations!"
    break