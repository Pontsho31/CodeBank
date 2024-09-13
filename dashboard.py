'''
After the user has entered valid credentials 
1. Store the credentials in a dictionary called database which has the values 
	database = {
		username : [
		user_balance , username
	]
}

2. we get the username they entered by using the .get method for dictionaries e.g 
	if username!="":
		database.get(username , 'Invalid username') - output [inside of .get the left hand value
														is for getting the key and the right hand
														value if the exception/ error message if the
														user does not exist
																	]
	if their credential checkout then we should get from the dictionary a list with bank balance and their
	username. We can use indexes to get the balance and username for dashboard e.g f"welcome {database.get(username)[0]}"
3.  incase the user is not registred we call out signup() function to make them signup
	after the we call the login() after we have stored the values in the database

4. After the sucessful login we run our while loop until the user chooses to logout 
'''
database: dict = {
	'Juniorzwane' : [5000]
}
def dashboard():
	# Username is not yet defined because we have to recieve it from login()
	print(f'Welcome back to your CodeBank profile {username}\n\n')
	print('Please make a selection below:\n1. View Balance\n2.Withdraw\n3.Deposit\n4.LogOut')
	option_Selection = input('Choose an option above e.g 1 : ')
	while True:
		if option_Selection == 1:
			print(f'Your balance is : {database.get(username)[0]}\n') # on the returned list the 0 index value is balance
			option_Selection = input('Choose an option above e.g 1 : ')
		elif option_Selection == 2:
			withdraw = input('Please enter a withdrawal amount: ')
			print(f'Your remaining balance is : {database.get(username)[0] - withdraw}\n') # on the returned list the 0 index value is balance
			option_Selection = input('Choose an option above e.g 1 : ')
		elif option_Selection == 3:
			deposit = input('Enter deposit amount : ')
			print(f'Your updated balance is : {database.get(username)[0] + deposit}\n')
		elif option_Selection == 4:
			break
dashboard()
