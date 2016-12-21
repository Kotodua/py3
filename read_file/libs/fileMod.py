class FileMod(object):

	'Common base class for all employees'


	def __init__(self):
		self.fCount = 0
		self.fContent = ''
		self.fname = "C:/python_scripts/read_file/sum.txt"

    	#self.fCount = self.fCount + 1
   
	def refresh(self):
		with open(fname) as f:
      		self.fContent = f.readlines()

	def toString(self):
		print (self.fContent)

	def test(self):
		print ("test passed")
