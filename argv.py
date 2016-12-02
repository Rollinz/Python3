import sys

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print("Necesita por lo menos 1 argumento")
	else:
		if sys.argv[1] == 'help' or 'Help':
			print("Llama a Rollins")
		print(sys.argv)