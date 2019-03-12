num = input("How many people sitting at your table?\n")
type(num)
#The problem here is that its now a table. 
factorial = 1

if num < 0:
	print "Can't be negative dude!"
elif num == 0:
	print "There's 1 possible arrangement!"
else:
	for i in range(1, num):
#since the equation of table factorial is "(n-1)!,
# 1 is not added to num
		
		factorial = (factorial)*i

	print "There are",factorial,"arrangements", 


