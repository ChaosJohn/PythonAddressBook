#!/usr/bin/python
# Filename: contact.py

import cPickle as p
import sys
import os

class contact:
	amount = 0	# the amount of all contacts

	def __init__(self, name, Tel = 'Not set', Email = 'Not set', cate = 'Not set'):
		self.name = name
		self.Tel = Tel
		self.Email = Email
		self.cate = cate
		self.__class__.amount += 1
		print 'Contact %s added successfully\
			\nAnd there are(is) %d contacts' % (self.name, self.__class__.amount)

	def modifyName(self, name):	# modify the name
		self.name = name

	def modifyTel(self, Tel):	# modify the telephone number
		self.Tel = Tel

	def modifyEmail(self, Email):	# modify the Email address
		self.Email = Email

	def modifyCate(self, cate):	# modify the category
		self.cate = cate

	def __del__(self):
		print 'Contact %s is removed' % self.name

		self.__class__.amount -= 1

		if self.__class__.amount == 0:
			print 'No contact left'
		else:
			print 'There are(is) %d contacts left' % self.__class__.amount
	
	def display(self):	# display the detail information
		print '%s\n\tTel: \t\t%s\n\tEmail: \t\t%s\n\tCategory: \t%s' % (self.name, self.Tel, self.Email, category[self.cate])

def clr():	# clear the screen
	os.system('clear')

cmdhp = {	# the dictionary about the command and their information
	'help'	:	'To display this help document', 
	'quit'	: 	'To quit.', 
	'add'	:	'To add a contact.', 
	'da'	: 	'To display all contact information in detail.', 
	'dp'	: 	'To display the contact information you specify.', 
	'mn'	: 	'To modify the name of the contact you specify.', 
	'mt'	:	'To modify the telephone number of the contact you specify.', 
	'me'	:	'To modify the Email of the contact you specify.', 
	'mc'	: 	'To modify the category of a contact.', 
	'sort'	: 	'To sort the whole contacts by name', 
	'list'	: 	'To list names of whole contacts'
		}

commands = []
for cmd, info in cmdhp.items():	# make the list of commands from the 'cmdhp'-dictionary
	commands.append(cmd)

def ats(obj):	# return the typeset string of detail information from the contact-object
	msg = '%s\n\tTel: \t\t%s\n\tEmail: \t\t%s\n\tCategory: \t%s' % (obj.name, obj.Tel, obj.Email, category[obj.cate])
	msg += '\n' + '-' * 50 + '\n'
	return msg

contactFile = 'addressBook'	#	the name of the file which is used to save the contacts in
objectStore = '.objectStore'	# the name of the file which is used to store the whole contacts-list in

category = {	# the dictionary about the category and their abbreviation
	'fa'	:	'family', 
	'wm'	: 	'workmate', 
	'fr'	: 	'friend'
}

myContact = []	# the contacts-list
for item in os.listdir(os.getcwd()):	# if the contactStore exists, then load the contacts-list from the contactStore
	if item == objectStore:
		f_object = file(objectStore)
		myContact = p.load(f_object)
		contact.amount = len(myContact)	# get the amount of contacts
		break

while 1:
	command = raw_input("Please Enter command('help' for help-page): ")
	clr()
	if not commands.__contains__(command):	# __contains__() returns the boolean value depending on whether the object is in the list
		print 'No such command!!!'
		continue

	if command == 'help':	# display the help-page
		print '*' * 50 
		print '\t\tHelp Page'
		print '*' * 50
		for cmd, info in cmdhp.items():
			print '\t' + cmd + '\t:\t' + info

		print 
		print '\t!!! Category: '
		for short, detail in category.items():
			print '\t\t' + short + '-->' + detail
		print '*' * 50

	elif command == 'add':	# the block used to add a contact
		name = raw_input('name --> ')
		Tel = raw_input('Tel --> ')
		while (Tel.isdigit() and len(Tel) != 8 and len(Tel) != 11 and len(Tel) != 12) or (not Tel.isdigit()):
			# isdigit() return the boolean value depending on whether the string contains just digits
			Tel = raw_input('The Tel-format is wrong!!! Please reinput\nTel --> ')
		Email = raw_input('Email --> ')
		while Email.find('@') == -1:	# find() search the string you specify
			Email = raw_input('The Email-format is wrong!!! Please reinput\nEmail --> ')
		cate = raw_input('Category --> ')
		while cate != 'fa' and cate != 'wm' and cate != 'fr':
			cate = raw_input('No such category!!! Please reinput\nCategory --> ')
		clr()
		myContact.append(contact(name, Tel, Email, cate))

	elif command == 'da':	# the block used to display all contact information in detail
		print '*' * 50
		print '-' * 50
		for member in myContact:
			member.display()
			print '-' * 50
		print '*' * 50

	elif command == 'sort':	# sort the list depending on the specified attribute of the element
		myContact.sort(key = lambda d:d.name)	

	elif command == 'list':	# list the name of the whole contacts
		for member in myContact:
			print member.name

	elif command == 'quit':	# quit the tool
		# dump the contacts-list into the contactStore
		f_object = file(objectStore, 'w')

		p.dump(myContact, f_object)
		
		# let the user choose whether to save the contacts into a readable file
		confirm = raw_input("Do you want to save to 'addressBook'? (y/n) --> ")
		if confirm == 'y' or confirm == 'Y':
			f_contact = file(contactFile, 'w')
			# create a string contaning all contacts information in detail
			message = '*' * 50 + '\n' + '-' * 50 + '\n'
			for member in myContact:
				message += ats(member)
			message += '*' * 50 + '\n'
			f_contact.write(message)
			f_contact.close()

		f_object.close()
		sys.exit()	

	else:
		conName = raw_input('Please enter the name of contact --> ')	# get the name of the contact you specify
		index = -1	# the index of the contact you specify in the contacts-list
		i = -1
		for member in myContact:
			i += 1
			if member.name == conName:
				index = i
				continue
		if index == -1:
			print 'Can not find the contact\n'
			continue
		
		if command == 'del':	# the block used to delete the contact you specify
			del myContact[index]

		elif command == 'dp':	# the block used to display the detailed information of the contact you specify
			print '*' * 50
			myContact[index].display()
			print '*' * 50
		
		elif command == 'mn':	# the block used to modify the name of the contact you specify
			newName = raw_input('Please enter the new name --> ')
			myContact[index].modifyName(newName)

		elif command == 'mt':	# the block used to modify the telepyhone number of the contact you specify
			newTel = raw_input('Please enter the new Tel-Num --> ')
			while not newTel.isdigit():
				newTel = raw_input('Must be digits!!! Please reinput\nTel --> ')
			while len(newTel) != 8 and len(newTel) != 11 and len(newTel) != 12:
				newTel = raw_input('The Tel-format is wrong!!! Please reinput\nTel --> ')
			myContact[index].modifyTel(newTel)

		elif command == 'me':	# the block used to modify the Email address of the contact you specify
			newEmail = raw_input('Please enter the new Email --> ')
			while newEmail.find('@') == -1:
				newEmail = raw_input('The Email-format is wrong!!! Please reinput\nEmail --> ')
			myContact[index].modifyEmail(newEmail)

		elif command == 'mc':	# the block used to modify the category of the contact you specify
			newCate = raw_input('Please enter the new category --> ')
			while newCate != 'fa' and newCate != 'wm' and newCate != 'fr':
				newCate = raw_input('No such category!!! Please reinput\nCategory --> ')
			myContact[index].modifyCate(newCate)
		else:
			pass	
