
def confirmation2():
	answer = input()
	if answer == "questionone":
		print("Alright, let's try questionone again.")
		questionone()
		fullinfo()
		confirmation()
	elif answer == "questiontwo":
		print("Alright, let's try questiontwo again.")
		questiontwo()
		fullinfo()
		confirmation()
	elif answer == "questionthree":
		print("Alright, let's try questionthree again.")
		questionthree()
		fullinfo()
		confirmation()
	else:
		print("Sorry, I couldn't understand that. Please type in 'questionone', 'questiontwo', or 'questionthree'.")
		confirmation2()




def fullinfo():
	print("Let's review. Your name is" + name + ".")
	print("You are currently attending" + college + ".")
	print("And you previously attended" + highschool + ".")
	print("Did I get that right?")
	
def confirmation():
	answer = input()
	if answer == "yes":
		print("Awesome! I really feel like I've gotten to know you a bit better now.")
	elif answer == "no":
		print("I'm so sorry! Can you please tell me which question I got wrong? Was it 'questionone', 'questiontwo', or 'questionthree'?")
		confirmation2()
	else:
		print("Sorry, I couldn't understand that. Please type in 'yes' or 'no'.")
		confirmation()





def questionthree():
	global highschool
	highschool = input("Which high school did you previously attend?")
	print("You're previously attended {}. Is that right? Please type in 'yes' or 'no'." .format(highschool))
	answer = input()
	if answer == "yes":
		print("Great. Let's move on to the next question.")
		
	elif answer == "no":
		print("I'm sorry. Could you please type that one more time for me?")
		questionthree()
	else:
		print("Sorry, I couldn't understand that. Please type in 'yes' or 'no' next time.")
		questionthree()





def questiontwo():
	global college
	college = input("Which college are you currently attending?")
	print("You're currently attending {}. Is that right? Please type in 'yes' or 'no'." .format(college))
	answer = input()
	if answer == "yes":
		print("Great. Let's move on to the next question.")
		
	elif answer == "no":
		print("I'm sorry. Could you please type that one more time for me?")
		questiontwo()
	else:
		print("Sorry, I couldn't understand that. Please type in 'yes' or 'no' next time.")
		questiontwo()


def questionone():
	global name
	name = input("Can I ask what your name is?")
	print("Your name is {}. Did I get that right? Please type in 'yes' or 'no'." .format(name))
	answer = input()
	if answer == "yes":
		print("Great. Let's move on to the next question.")
		
	elif answer == "no":
		print("I'm sorry. Could you please type that one more time for me?")
		questionone()
	else:
		print("Sorry, I couldn't understand that. Please type in 'yes' or 'no' next time.")
		questionone()

def main():
	print("Hello. I'm ranBot. I'm going to be asking you a series of questions in order to get to know you better.")
	print("But first, you need to introduce yourself.")
	questionone()
	questiontwo()
	questionthree()
	fullinfo()
	confirmation()
	print("Thank you so much for conversing with me!")
	print("Ciao!")


if __name__ == "__main__":
	main()		
