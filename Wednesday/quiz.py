import random

correct_solutions = 0
rounds = 10

for current_round in range(rounds):

  num1 = random.randint(3, 99)
  num2 = random.randint(3, 99)
  
  print (str(num1) + " + " + str(num2))
  print ("what is the sum?")
  sum = float(raw_input())
  
  if sum == num1 + num2:
  	print ("correct")
  	correct_solutions += 1
  else:
  	print ("incorrect")
  
  print ("You got " + str(correct_solutions) + " correct")

if correct_solutions is not 0:
  print ("You got " + str(correct_solutions / rounds) + " percent of the equations correct.")
else:
  print ("You got 0 percent of the equations correct.")