""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""
	# if reset or not exists(file_name):
	# 	f = open(file_name,'w')
	# 	f.write("1")
	# 	f.close()

	# else:
	# 	f = open(file_name,'r')
	# 	s = f.read() #should be a string
	# 	f.close()
	# 	f1 = open(file_name,'w')
	# 	f1.write(str(int(s)+1))
	# 	f1.close()

	# read = open(file_name,'r')
	# return int(read.read())

	if reset or not exists(file_name):
		f = open(file_name,'w')
		dump(1, f)
		f.close()

	else:
		f = open(file_name,'r+')
		info = load(f)
		f.close()
		f1 = open(file_name,'w')
		dump(info+1,f1)
		f1.close()

	read = open(file_name,'r')
	info = load(read)
	return info



if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))
