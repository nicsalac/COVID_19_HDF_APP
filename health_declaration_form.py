# importing the FileHandler class
from file_handling import FileHandler

# create and def a HDF class
class HealthDeclarationForm:
    def __init__(self, filename="health_declaration_data.csv"):
        # initialize an empty list to store and set the filename for data storage
        self.contacts = []
        self.filename = filename

    def add_contact(self, contact_info):
        # method to add new contact to the contacts list
        if len(self.contacts) >= 1000
        #check if the contact list is full (max of 1000 records)
             raise ValueError("HDF Record Book is full. Cannot add more contacts")
        # append the new contact info to the contact list
        self.contacts.append(contact_info)

    def save_contacts_to_file(self, filename):
        FileHandler.save_contacts_to_file(filename, self.contacts)

    def load_contacts_from_file(self, filename):
        self.contacts = FileHandler.load_contacts_from_file(filename)
        

        


