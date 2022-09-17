#!/usr/bin/python
import subprocess
import random
import sys

def generate_values(n):
	array = []
	dup_map  = {}
	for i in range(n):
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
	help_msg = "Not enough arguments\nUsage:\tpython3 tester.py <values amount>: prints the desired amount of random numbers without duplicates\n\tpython3 tester.py <push_swap path> <checker path> <values amount>: run your push_swap output through the checker"
	if length < 2:
		raise Exception(help_msg)
	elif length == 2:
		num = int(sys.argv[1])
		if num <= 0:
			raise ValueError("The value of <values amount> must be positive")
		noexe = True
	elif length < 4:
		raise Exception(help_msg)
	else:
		num = int(sys.argv[3])
		if num <= 0:
			raise ValueError("The value of <values amount> must be positive")
		push_swap_path = str_to_path(str(sys.argv[1]))
		checker_path = str_to_path(str(sys.argv[2]))
	# Execution
	array = generate_values(num)
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
	except Exception as e:
		print("\nProcess interrupted: " + str(e))
		exit(0)