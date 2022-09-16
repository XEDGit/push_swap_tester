#!/usr/bin/python
import subprocess
import random
import sys

def generate_values():
	array = []
	dup_map  = {}
	for i in range(int(sys.argv[1])):
		while True:
			new_random = random.randint(-2147483648, 2147483647)
			if dup_map.get(new_random) == True:
				continue
			dup_map[new_random] = True
			array.append(str(new_random))
			break
	return array

def str_to_path(string):
	if not "./" in string[:2] or not "/" in string[:1]:
		string = "./" + string
	return string

def main():
	# Arguments parsing
	noexe = False
	length = len(sys.argv)
	help_msg = "Error: not enough arguments\nUsage:\tpython3 tester.py <values amount>: prints the desired amount of random numbers without duplicates\n\tpython3 tester.py <values amount> <push_swap path> <checker path>: run your push_swap output through the checker"
	if length < 2:
		print(help_msg)
		raise Exception
	elif length < 3:
		noexe = True
	elif length < 4:
		print(help_msg)
		raise Exception
	else:
		push_swap_path = str_to_path(str(sys.argv[2]))
		checker_path = str_to_path(str(sys.argv[3]))
	# Execution
	array = generate_values()
	if noexe:
		args = ""
		for n in array:
			args = args + str(n) + " "
		print(args.rstrip())
	else:
		array.insert(0, push_swap_path)
		out, _ = subprocess.Popen(array, stdout=subprocess.PIPE).communicate()
		array.pop(0)
		array.insert(0, checker_path)
		subprocess.Popen(array, stdin=subprocess.PIPE).communicate(out)

if __name__ == "__main__":
	sys.stderr = open("/dev/null", "w")
	try:
		main()
	except:
		print("\nProcess interrupted")
		exit(0)