#possibility to :
#count chars in file
#count specific charecters
#return sum of all number in the file
#extract NAN to separate file

from libs.fileMod import FileMod 

file1 = FileMod("C:/python_scripts/py3_/read_file/sum.txt")

#file1.count()
file1.count_specific_char("#")

