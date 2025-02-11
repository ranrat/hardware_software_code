def main():
	print("This program adds two numbers. ")
	num1 = input("Enter first number: ")
	num2 = input("Enter second number: ")
	total = int(num1) + int(num2)
	print("{} + {} = {}".format(num1, num2, total))
	check()

	
def check():
	answer = input("Are you done adding?").lower().strip()
	if answer == "yes":
		print("Thanks for adding!")
	elif answer == "no":
		main()
	else:
		print("Say that again?")
		check()

if __name__ == "__main__":
	main()