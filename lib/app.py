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
    state = CharField()

db.connect()
db.create_tables([Contact])
# Anderson = Contact(firstname='Anderson',lastname='Montilla', phonenumber='2406032924',state='VA')
# Anderson.save()

# class AddressBook():
def Start():
    input(print("AddressBook:\n Type 'list' to show all your contacts\n Type 'del' to delete a contact"))
    if input == "list":
        info()
    elif input == "del":
        delete()
    else:
        exit()




def info():
    contact = contacts.select()
    for contacts in Contact:
        print(f"Name: {contacts.firstname} {contacts.lastname}\n Phone: {contacts.phonenumber}\n State: {contacts.state}\n" )
    list = input("Here is the List of Contacts. Would you like to go back to the home page? y/n: ")
    if list == "y":
        Start()
    else:
        exit()

def delete():
    contact = contacts.select()
    for contacts in Contact:
        print(f"Name: {contacts.firstname} {contacts.lastname}\n")
        ConDel = input("Which one of these contacs you would like to delete?: ")
    if ConDel == contact.firstname:
        contact = Contact.get(Contact.firstname == ConDel)
        contact.delete_instance()
        print("contact has been deleted")
    else:
        Start()





# CREATE TABLE contacts (
#   firstname VARCHAR NOT NULL,
#   lastname VARCHAR NOT NULL,
#   phonenumber VARCHAR NOT NULL,
#   state VARCHAR NOT NULL,
# );