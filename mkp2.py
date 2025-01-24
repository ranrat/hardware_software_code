
import random 
    
def nextmain():
	answer = input().lower().strip()
	if answer == "exit":
		print("I guess that's all for today. Goodbye.")
		print("You answered a total of {} questions." .format(random_question.counter))
	else:
		random_question()

def random_question():
	f = open("text.txt")
	lines = f.readlines()
	print(lines[random.randint(0, 48)])
	random_question.counter += 1
	
	nextmain()
random_question.counter = 0

def main():
	print("I'm going to be asking you a series of questions; if at any time you wish to stop answering, please type exit.")
	nextmain()




if __name__ == "__main__":
	main()