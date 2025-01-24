def main():
	f = open("text.txt")
	print(f.readline())
	myfunction()
	myfunction()
	print(myfunction.counter)
def myfunction():
    myfunction.counter += 1

myfunction.counter = 0

if __name__ == "__main__":
	main()