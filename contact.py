#!/usr/bin/python
# Filename: contact.py

import cPickle as p
import sys
import os

class contact:
	amount = 0
	def __init__(self, name, Tel = 'Not set', Email = 'Not set', cate = 'Not set'):
		self.name = name
		self.Tel = Tel
		self.Email = Email
		self.cate = cate
		self.__class__.amount += 1
		print 'Contact %s added successfully\
			\nAnd there are(is) %d contacts' % (self.name, self.__class__.amount)

	def modifyName(self, name):
		self.name = name

	def modifyTel(self, Tel):
		self.Tel = Tel

	def modifyEmail(self, Email):
		self.Email = Email

	def modifyCate(self, cate):
		self.cate = cate

	def __del__(self):
		print 'Contact %s is removed' % self.name

		self.__class__.amount -= 1

		if self.__class__.amount == 0:
			print 'No contact left'
		else:
			print 'There are(is) %d contacts left' % self.__class__.amount
	
	def display(self):
		print '%s\n\tTel: \t\t%s\n\tEmail: \t\t%s\n\tCategory: \t%s' % (self.name, self.Tel, self.Email, category[self.cate])

def clr():
	os.system('clear')

cmdhp = {
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
for cmd, info in cmdhp.items():
	commands.append(cmd)

def ats(obj):
	msg = '%s\n\tTel: \t\t%s\n\tEmail: \t\t%s\n\tCategory: \t%s' % (obj.name, obj.Tel, obj.Email, category[obj.cate])
	msg += '\n' + '-' * 50 + '\n'
	return msg

contactFile = 'addressBook'
objectStore = '.objectStore'

category = {
	'fa'	:	'family', 
	'wm'	: 	'workmate', 
	'fr'	: 	'friend'
}

myContact = []
for item in os.listdir(os.getcwd()):
	if item == objectStore:
		f_object = file(objectStore)
		myContact = p.load(f_object)
		contact.amount = len(myContact)
		break

# commands = ['help', 'add', 'da', 'quit', 'del', 'dp', 'mn', 'mt', 'me', 'mc']

while 1:
	command = raw_input("Please Enter command('help' for help-page): ")
	clr()
	if not commands.__contains__(command):
		print 'No such command!!!'
		continue

	if command == 'help':
		__print = '''\
	add:	To add a contact.
	del:	To delect a contact.
	da:		To display all contact information in detail
	dp: 	To display the contact information you specify
	mn:		To modify the name of a contact.
	mt:		To modify the telephone of a contact.
	me:		To modify the Email of a contact.
	mc: 	To modify the category of a comtact.

	!!!:	Category: 	'fa' --> family
						'wm' --> workmate
						'fr' --> friend
		'''
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

	elif command == 'add':
		name = raw_input('name --> ')
		Tel = raw_input('Tel --> ')
		while (Tel.isdigit() and len(Tel) != 8 and len(Tel) != 11 and len(Tel) != 12) or (not Tel.isdigit()):
			Tel = raw_input('The Tel-format is wrong!!! Please reinput\nTel --> ')
		Email = raw_input('Email --> ')
		while Email.find('@') == -1:
			Email = raw_input('The Email-format is wrong!!! Please reinput\nEmail --> ')
		cate = raw_input('Category --> ')
		while cate != 'fa' and cate != 'wm' and cate != 'fr':
			cate = raw_input('No such category!!! Please reinput\nCategory --> ')
		clr()
		myContact.append(contact(name, Tel, Email, cate))

	elif command == 'da':
		print '*' * 50
		print '-' * 50
		for member in myContact:
			member.display()
			print '-' * 50
		print '*' * 50

	elif command == 'sort':
		myContact.sort(key = lambda d:d.name)

	elif command == 'list':
		for member in myContact:
			print member.name

	elif command == 'quit':
#		contactFile = 'mycontact.txt'
#		objectStore = 'myObject'
		f_object = file(objectStore, 'w')

		p.dump(myContact, f_object)

		confirm = raw_input("Do you want to save to 'addressBook'? (y/n) --> ")
		if confirm == 'y' or confirm == 'Y':
			f_contact = file(contactFile, 'w')
			message = '*' * 50 + '\n' + '-' * 50 + '\n'
			for member in myContact:
				message += ats(member)
			message += '*' * 50 + '\n'
			f_contact.write(message)
			f_contact.close()

		f_object.close()
		sys.exit()

	else:
		conName = raw_input('Please enter the name of contact --> ')
		__devilcomment = '''
		con = 'NULL'
		for member in myContact:
			if member.name == conName:
				con = member
				continue
		if con == 'NULL':
			print 'Can not find the contact, please try again\n'
			continue

		if command == 'del':
			del con
#			myContact.remove(con)
#			con.__del__()

		elif command == 'dp':
			con.display()

		elif command == 'mn':
			newName = raw_input('Please enter the new name --> ')
			con.modifyName(newName)

		elif command == 'mt':
			newTel = raw_input('Please enter the new Tel-Num --> ')
			con.modifyTel(newTel)

		elif command == 'me':
			newEmail = raw_input('Please enter the new Email --> ')
			con.modifyEmail(newEmail)

		elif command == 'mc':
			newCate = raw_input('Please enter the new category --> ')
			con.modifyCate(newCate)
		else:
			pass
			'''
		index = -1
		i = -1
		for member in myContact:
			i += 1
			if member.name == conName:
				index = i
				continue
		if index == -1:
			print 'Can not find the contact\n'
			continue
		
		if command == 'del':
			del myContact[index]

		elif command == 'dp':
			print '*' * 50
			myContact[index].display()
			print '*' * 50
		
		elif command == 'mn':
			newName = raw_input('Please enter the new name --> ')
			myContact[index].modifyName(newName)

		elif command == 'mt':
			newTel = raw_input('Please enter the new Tel-Num --> ')
			while not newTel.isdigit():
				newTel = raw_input('Must be digits!!! Please reinput\nTel --> ')
			while len(newTel) != 8 and len(newTel) != 11 and len(newTel) != 12:
				newTel = raw_input('The Tel-format is wrong!!! Please reinput\nTel --> ')
			myContact[index].modifyTel(newTel)

		elif command == 'me':
			newEmail = raw_input('Please enter the new Email --> ')
			while newEmail.find('@') == -1:
				newEmail = raw_input('The Email-format is wrong!!! Please reinput\nEmail --> ')
			myContact[index].modifyEmail(newEmail)

		elif command == 'mc':
			newCate = raw_input('Please enter the new category --> ')
			while newCate != 'fa' and newCate != 'wm' and newCate != 'fr':
				newCate = raw_input('No such category!!! Please reinput\nCategory --> ')
			myContact[index].modifyCate(newCate)
		else:
			pass	
