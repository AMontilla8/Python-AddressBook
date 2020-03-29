from flask import Flask, jsonify, request
from peewee import *
# from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('contacts', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    firstname = CharField()
    lastname = CharField()
    phonenumber = CharField()
    YState = CharField()

db.connect()
db.create_tables([Contact])
db.create_tables([Contact])
# Anderson = Contact(firstname='Anderson',lastname='Montilla', phonenumber='2406032924',state='VA')
# Anderson.save()

def Start():
    print("AddressBook:\n Type 'list' to show all your contacts\n Type 'del' to delete a contact \n Type 'new' to make a new contact \n Type 'update' to update a contac")
    first = input('What Would you like to do: ')
    if first == "list":
        info()
    elif first == "del":
        delete()
    elif first == "new":
        newContact()
    elif first == "update":
        update()
    else:
        exit()


def info():
    contacts = Contact.select()
    for contact in contacts:
        print(f"Name: {contacts.firstname} {contacts.lastname}\n Phone: {contacts.phonenumber}\n State: {contacts.YState}\n" )
    list = input("Here is the List of Contacts. Would you like to go back to the home page? y/n: ")
    if list == "y":
        Start()
    contact = Contact.get(Contact.firstname == show)
    print(f"Name: {contacts.firstname} {contacts.lastname}\n Phone: {contacts.phonenumber}\n State: {contacts.YState}\n" )
    info()
        

def delete():
    contacts = Contact.select()
    for contacts in contacts:
        print(f"Name: {contacts.firstname} {contacts.lastname}\n")
    ConDel = input("Which one of these contacs you would like to delete?: ")
    if ConDel == Contact.firstname:
        contact = Contact.get(Contact.firstname == ConDel)
        contact.delete_instance()
        print("contact has been deleted")
        Start()
    else:
        Start()

def newContact():
    new_firstName = input('Insert First Name: ')
    new_lastName = input('Insert Last Name: ')
    new_phone = input('Insert Phone Number: ')
    new_state = input('Insert State')

    add_contact = Contact(
        firstname = new_firstName,
        lastname = new_lastName,
        phone = new_phone,
        YState = new_state
    )
    add_contact.save()
    Start()

def update():
    contacts = Contact.select()
    for contact in contacts:
        print(contact.firstname)
    frame = input('Enter name of contact to update \nCase Sensitive: ')
    if frame == Contact.firstname:
        print(' 1: First name \n 2: Last name \n 3: Phone number \n 4: State')
        answerOf = input('Enter number of subject to update: ')
        if answerOf == '1':
            contact = Contact.get(Contact.firstname == frame)
            contact.firstname = input('New first name: ')
            contact.save()
            Start()
        elif answerOf == '2':
            contact = Contact.get(Contact.firstname == frame)
            contact.lastname = input('New last name: ')
            contact.save()
            Start()
        elif answerOf == '3':
            contact = Contact.get(Contact.firstname == frame)
            contact.phone = input('New phone number: ')
            contact.save()
            Start()
        elif answerOf == '4':
            contact = Contact.get(Contact.firstname == frame)
            contact.YState = input('New State: ')
            contact.save()
            Start()
        else:
            Start()

Start()

# CREATE TABLE contacts (
#   firstname VARCHAR NOT NULL,
#   lastname VARCHAR NOT NULL,
#   phonenumber VARCHAR NOT NULL,
#   state VARCHAR NOT NULL,
# );