print("Enter your name: ")
name = raw_input()
print("Hello, " + name + "!\nPlease enter 4 character passcode: ")
passcode = str(raw_input()) # store passcode and do some cool shit with it
if len(passcode) == 4:
  print("Please enter the passcode you created: ")
  passcode_request = raw_input()
  if passcode == str(passcode_request):
    print("correct")
  else:
    print("incorrect")
else:
  print("Your passcode is not 4 characters long.")