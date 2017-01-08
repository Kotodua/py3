class FileMod(object):
	
	def __init__(self, fpath):
		self.file = fpath
		self.fContent = open(self.file)
		self.summa = 0
		self.char_count = 0

    	#self.fCount = self.fCount + 1
   
	def count(self):
		self.summa = 0				
		for f in self.fContent.readlines():
			for j in f.split(' '):
				try: 
					j = int(j)
					self.summa = self.summa + j			
				except TypeError:
					print('Type issue')
				except ValueError:
					print('Value issue')
		print (self.summa)


	def count_specific_char(self, char):
		print ("Method were called")
		self.char_count = 0
		for f in self.fContent.readlines():
			l = list(f)
			for j in l:
				try:			 
					if j == char:
						self.char_count = self.char_count + 1			
				except TypeError:
					print('Type issue')
				except ValueError:
					print('Value issue')
		print(self.char_count)		


