#!/usr/bin/env python
import shelve
import pandas as pd

def get_parameters(object):
	return object.__dict__
def get_methods(object):
	method_list = [func for func in dir(object) if callable(getattr(object, func))]
	return method_list


class Contact:
	def __init__(self, name, address = "", phone = "", email = ""):
		self.name = name
		self.address = address
		self.phone = phone
		self.email = email
	def __str__(self):
		return f"name = {self.name}, address = {self.address}, phone = {self.phone}, email = {self.email}"
	def to_dict(self):
		#return a dict
		return {"name":self.name, "address":self.address, "phone":self.address, "email":self.email}

class Contactlist:
	def __init__(self):
		self.all_contacts = []
		self.names = []
	def add(self, *contacts):
		for contact in contacts:
			if contact.name not in self.names:
				self.names.append(contact.name)
				self.all_contacts.append(contact)
			else:
				print("Name existed already, pls choose different name")
	def __str__(self):
		contacts = []
		for contact in self.all_contacts:
			contacts.append(str(contact))
		return "\n".join(contacts)
	def search(self, name):
		'''
		search contact by name
		print result to terminal
		result list of contact object
		
		'''
		result = []
		for c in self.all_contacts:
			if name.lower() in c.name.lower(): 
				print(c)
				result.append(c)
		return result
	def sort_by_name(self):
		self.all_contacts.sort(key = lambda object:object.name)
	
	def sort_by_phone(self):
		self.all_contacts.sort(key = lambda object:object.phone)
	def delete(self, name):
		for c in self.all_contacts:
			if c.name.lower() == name:
				self.all_contacts.remove(c)
	def save(self, filename):
		'''
		save all contact to database shelve
		'''
		s = shelve.open(filename)
		for contact in self.all_contacts:
			s[contact.name] = contact.to_dict()
		s.close()
		print(f"save successful to {filename}")
	def import_contact_from_file(self, filename):
		s = shelve.open(filename)
		new_list = Contactlist()
		for name in s.keys():
			contact_dict = s[name]
			print(contact_dict)
			new_list.add(Contact(contact_dict['name'], contact_dict['address'], contact_dict['phone'], contact_dict['email']))
		return new_list
	def import_from_csv(self, filename):
		df = pd.read_csv(filename)
		new_list = Contactlist()
		print(df)
		print(df.info())
		df = df.filter(["First Name", "Middle Name", "Last Name", "Phone (Mobile)", "Address (Work)" , "Email (Other)"])
		
		#chuyen doi dinh dang va doi ten
		df['Phone (Mobile)'] = df['Phone (Mobile)'].astype(str)
		df = df.rename(columns={'Phone (Mobile)': 'phone'})
		
		
		df = df.rename(columns={'Address (Work)': 'address'})
		df = df.rename(columns={'Email (Other)': 'email'})
		
		#chuyen doi format to str
		df['First Name'] = df['First Name'].astype(str)
		df['Middle Name'] = df['Middle Name'].astype(str)
		df['Last Name'] = df['Last Name'].astype(str)
		
		#dung de search phone number, nen can chuyen doi sang string
		
		#combine name
		
		df['name'] = df["First Name"] + " " + df['Middle Name'] + " " + df['Last Name']
		
		
		df = df.filter(["name", "phone", "address" , "email"])
		name_col = df['name']
		phone_col = df['phone']
		address_col = df['address']
		email_col = df['email']
		contacts = zip(name_col, phone_col, address_col, email_col)
		for i, contact_data in enumerate(contacts):
			#print(i, contact)
			new_list.add(Contact(contact_data[0], contact_data[1], contact_data[2], contact_data[3]))
		
		#set gia tri, de co the resue ham print, search, get
		self.all_contacts = new_list.all_contacts

c1 = Contact("kid", "vietnam", "0938891234", "abc@gmail.com")
c2 = Contact("tyem", "dongnai", "0928891234", "def@gmail.com")
c3 = Contact("tyem1", "dongnai", "", "zyx@gmail.com")
c4 = Contact("sushi", "kontum", "01234512345", "sushi@gmail.com")
c5 = Contact("bum", "binhduong", "0938812376", "bum@gmail.com")
c6 = Contact("anh", "binhduong", "0938811234", "anhxuan@gmail.com")

print(c1.name)
print(c1)
print(c2)

#all parameter in contac
#print(c.__dict__)
print(get_parameters(c1))
print(get_methods(c1))

clist = Contactlist()
clist.add(c1)
clist.add(c2)
clist.add(c3)
#add many contact at a time, using *arg
clist.add(c4, c5, c6)
#clist.add(c6)
print(clist.all_contacts)

print ("clist.__str__")
print(clist)

print("Test get contact by name")
print ("Get contact with name bob")
print(clist.search("bob"))
print ("Get contact with name sushi")
print(clist.search("sushi"))

print ("Get contact with name SUSHI")
print(clist.search("SUSHI"))

print("contact list before sort:")
print(clist)

print("contact list after sort by name:")
clist.sort_by_name()
print(clist)

print("contact list after sort phone number:")
clist.sort_by_phone()
print(clist)

print("delete contact with name kid")
clist.delete("kid")
clist.delete("me")
print(clist)

print("save contact to database file")
clist.save("mycontact.db")

print("read again contact from file")
new_contact_list = clist.import_contact_from_file("mycontact.db")
print("contact list has just been import")
print(new_contact_list)

my_contact_list = Contactlist()
my_contact_list.import_from_csv("mycontact.csv")
#print(my_contact_list)
#test
print("Test get some data from contact list")

print("All Name: ", len(my_contact_list.names))
my_contact_list.search("xuanbum")
my_contact_list.search("hoang")
my_contact_list.search("sushi")
my_contact_list.search("temp")
