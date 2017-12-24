import os

path = "/Users/christinechan/Development/AddressBook/"

# Menu 
def menu():
	flag = True
	while flag == True:
		action = input("Welcome to the Address Book. Please select an option below: \n [Press 1] Create new contact \n [Press 2] Search contacts \n [Press 3] Delete contact \n [Press 4] Exit \n")
		if int(action) == 1:
			createContact()
		if int(action) == 2:
			search()
		if int(action) == 3:
			delete()
		if int(action) == 4:
			print("Bye, have a great day!")
			flag = False


# Using OOP to create contacts
class Contact:
	# Initializes an object 
	def __init__(self,name,last,email,phone):
		self.name = name
		self.last = last
		self.email = email 
		self.phone = phone

	# Returns a string representation of an object
	def __str___(self):
		return("\n{0}| {1} | {2} | {3}".format(self.name,self.last, self.email, self.phone))

	# Setters
	def change_name(self,name):
		self.name = name
	def change_name(self,last):
		self.last = last
	def change_email(self, email):
		self.email = email 
	def change_phone(self, phone):
		self.phone = phone 

# Asks user for information (First Name, Last Name, Email, and Phone Number)
def createContact():
	person = []
	print("Please fill in the following information: ")

	first_name = input("First Name: ")
	last_name = input("Last Name: ")
	email = input("Email: ")
	phone = input("Phone: ")

	contact = Contact(first_name,last_name, email, phone)

	output(contact.__str___())
	print("Contact was successfully added")

# Output the existing contacts in the address book text file 
def output(contact):
	if os.path.exists(path):
		with open(path+"AddressBook.txt", "a") as f: f.write(contact)
	else:
		with open(path+"AddressBook.txt", "w+") as f: f.write("# First Name | Last Name | Email | Phone Number \n" + contact)

# Displays current contacts in address book 
def search():
	if os.path.exists(path):
		with open(path+"AddressBook.txt", "r") as f: 
			for line in f: print(line+"\n")	
	else:
		print("Sorry, your address book is empty")

# Deletes a contact
def delete():
	x_person = input("What is the name of the person you would like to remove? \n")
	with open(path+"AddressBook.txt", "r+") as f:
		lines = f.readlines()
		for line in lines: 
			if x_person in line:
				del line
				print("Contact successfully removed \n")
			else:
				print("This person does not exist in the address book")


if __name__ == '__main__':
	menu()

