import sys
import os

extensions = set([ "txt", "csv", "sql" ])

longest = 0
lower = ""

def valid(path):
	global lower
	
	if not os.path.isfile(path) or path.lower() == lower:
		return False
	split = path.split('.')
	
	if split[len(split) - 1] not in extensions:
		return False
	size = os.path.getsize(path)
	
	global longest
	
	if size > longest:
		longest = size
	return True

def main():
	global lower
	
	name = "output.txt" if len(sys.argv) == 1 else sys.argv[1]
	lower = name.lower()
	
	files = list(filter(valid, os.listdir(os.curdir)))
	
	length = len(str(longest)) + 1
	output = open(name, "w")
	
	for file in files:
		size = str(os.path.getsize(file))
		output.write((' ' * (length - len(size))) + size + ' ' + file + '\n')
	output.close()

main()