def main():
	add()
	print("{} + {} = {}".format(name, name2, total))
	answer = input("ya done? type yes to exit program").lower().strip()
	while answer != "yes":
		add()
		print("{} + {} = {}".format(name, name2, total))
		answer = input("ya done? type yes to exit program").lower().strip()
	
def add():
	print("gimme two numbers to add")
	global name, name2, total
	name = input("number 1: ").strip()
	name2 = input("numer2: ").strip()
	cheek1()
	total = int(name) + int(name2)

def cheek1():
	try:
		int(name)
		int(name2)
	except: 
		print("That aint a number dawg, try again")
		add()


if __name__ == "__main__":
	main()