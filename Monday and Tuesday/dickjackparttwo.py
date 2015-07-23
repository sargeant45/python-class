import sys
import random

total = ""

while True:
  randomNum1 = str(random.randint(0,10))
  randomNum2 = str(random.randint(0,10))
  
  total += randomNum1 + randomNum2
  
  sys.stdout.write(total)