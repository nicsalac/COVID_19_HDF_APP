# importing the FileHandler class
from file_handling import FileHandler

# create and def a HDF class
class HealthDeclarationForm:
    def __init__(self, filename="health_declaration_data.csv"):
        # initialize an empty list to store and set the filename for data storage
        self.contacts = []
        self.filename = filename

        