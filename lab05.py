def greeting():
	print("I can only stop if you type exit.")
	print("Do you want me to stop")
	print("Type exit then!")
	return input ("I’m waiting!!! ").lower().strip()
def main():
	run_loop = greeting()
	while run_loop != 'exit':
		run_loop = greeting()
if __name__ == "__main__":
	main()