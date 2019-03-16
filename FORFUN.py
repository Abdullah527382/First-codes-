#password identification excercise 
#Add a new user here everytime
username = 'abdullah527382@gmail.com'
password = 'abdullah123'
username2 = 'harris82@gmail.com'
password2 = 'harris123'
LoL = 'a'
CoD = 'b'
FIFA ='c'
#username = 'slifahh'
#password = 'abdul123'
user = raw_input("Enter your username\n")
type(user)

if user == username: #or username2:

	passw = raw_input("Please enter password\n")
	type(passw)
else:
	user = raw_input("Incorrect username: \nTRY AGAIN\n")
	type(user)
	if user == username: #or username2:
		passw = raw_input("Please enter password\n")
		type(passw) 
	else:
		raw_input("INCORRECT, try again!" )
		type(user)

		if user == username: #or username2:
			passw = raw_input("Please enter password\n")
			type(passw) 

		#end loop here possible? 

if passw == password: #or password2: 
	choice = raw_input("What would you like to do? \n Play: \n a.League Of Legends \n b.Call of Duty \n c.FIFA \n")
	type(choice)
	if choice == LoL:
		print"......Loading LoL....."
	if choice == CoD:
		print"......Loading CoD....."
	if choice == FIFA:
		print"......Loading FIFA....."
	else:
		retry = raw_input("Last chance: ---> Please choose a, b or c\n")
		type(retry)
		if retry == LoL:
			print"......Loading LoL....."
		elif retry == CoD:
			print"......Loading CoD....."
		elif retry == FIFA:
			print"......Loading FIFA....."
		else:
			print"Closing program"

		#this code needs to be repeated 

else:
	passw = raw_input("Incorrect password: \n1 retry left\n")
	type(passw)

	if passw == password: #or password2: 
		#print"Sign in successful"
		choice = raw_input("What would you like to do? \n Play: \n a.League Of Legends \n b.Call of Duty \n c.FIFA \n")
		type(choice)
		if choice == LoL:
			print"......Loading LoL....."
		if choice == CoD:
			print"......Loading CoD....."
		if choice == FIFA:
			print"......Loading FIFA....."
		else:
			retry = raw_input("Last chance: ---> Please choose a, b or c\n")
			type(retry)
			if retry == LoL:
				print"......Loading LoL....."
			elif retry == CoD:
				print"......Loading CoD....."
			elif retry == FIFA:
				print"......Loading FIFA....."
			else:
				print"Closing program"	
	else: 
		print"Account locked for 10 minutes..." 


