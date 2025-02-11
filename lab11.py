def while_loop(num):
	while num > 0:
		print("While count:{}".format(num))
		num += -1
def for_loop(num):
	for count in range(num,-1, -1):
		print("For count:{}".format(count))
def main():
	counter = 10
	while_loop(counter)
	for_loop(counter)
if __name__ == "__main__":
	main()