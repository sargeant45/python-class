def happyBirthday(person):
	print ("Happy birthday to you")
	print ("Happy birthday dear " + person)
	
happyBirthday("John")
happyBirthday("Alice")
happyBirthday("Pat")
# happyBirthday() error

def happyBirthday2(person=" "):
	print ("Happy Birthday dear " + person)

print("*************")
happyBirthday2()
happyBirthday2("Kelly")