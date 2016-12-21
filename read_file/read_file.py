#possibility to :
#count chars in file
#count specific charecters
#return sum of all number in the file
#extract NAN to separate file

from libs.fileMod import FileMod 


#fname = "C:/python_scripts/read_file/sum.txt"
summa = 0

#with open(fname) as f:
#    content = f.readlines()

#for i in content:
#	for j in i.split(' '):
#		try: 
#			j = int(j)
#			summa = summa + j			
#		except TypeError:
#			print('Type issue')
#		except ValueError:
#			print('Value issue')
		

#print(summa)	

FileMod.test(summa)	
