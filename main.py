import os, sys

class Gisty(object):
	def __init__(self):
		self.home = os.getenv("HOME")+"/.config/gisty"
		if not os.path.exists(self.home):
			os.makedirs(self.home)

	def usage(self):
		print u"Usage: gisty new git"

	def list(self):
		print [filename.split('.')[0] for filename in os.listdir(self.home)]

	def read(self, name):
		filename = self.home + "/" + name + '.md'
		if os.path.isfile(filename):
			for line in open(filename, 'r'):
				print line
		else:
			print u"File does not exist. Maybe you want to create it? try 'gisty new %s'" % (name)

	def create(self, name):
		filename = self.home + "/" + name + '.md'
		if not os.path.isfile(filename):
			file(filename, 'w').close() 
		os.system('open ' + filename)


if __name__ == '__main__':
	params = sys.argv[1:]
	if(len(params) == 2):
		if(params[0] in ['new', 'edit']):
			Gisty().create(params[1])
	elif(len(params) == 1):
		if(params[0] in 'list'):
			Gisty().list()
		else:
			Gisty().read(params[0])
	else:
		Gisty().usage()