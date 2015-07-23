import sys
import random
import string

while True:
  letter_or_number = random.randint(0,1)
  if letter_or_number == 0:
    sys.stdout.write(str(random.randint(0,10)))
  elif letter_or_number == 1:
    sys.stdout.write(str(random.choice(string.letters)))
  