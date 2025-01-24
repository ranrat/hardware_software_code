def main():
	print("This program adds two numbers. ")
	num1 = input("Enter first number: ")
	num2 = input("Enter second number: ")
	total = int(num1) + int(num2)
	print("{} + {} = {}".format(num1, num2, total))

	print("Are you done adding?")
	answer = input().lower().strip()
	if answer == "yes":
		print("Shutting down program.")
	elif answer == "no":
		main()

if __name__ == "__main__":
	main()