def greetings():
	print(" Give me two numbers and I will tell you the largest number!.")
def get_largest(largest, value):
	if largest is None:
		largest = value
	elif value > largest:
		largest = value
	print("The largest value is {}".format(largest))
def main():
	stop_loop = "no"
	greetings()
	while stop_loop != "yes":
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
		get_largest(num1,num2)
		stop_loop = input("Type 'yes' to exit program: ").lower().strip()
if __name__ == "__main__":
	main()
