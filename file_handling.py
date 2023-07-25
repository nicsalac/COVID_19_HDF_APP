import csv
import os

# create class for file handling
class FileHandler:

    def save_contacts_to_file(filename, contacts):
     # Get the directory path 
        script_dir = os.path.dirname(os.path.abspath(__file__))
    # Combine the script directory path with the filename to get the full file path
        full_path = os.path.join(script_dir, filename)
        try:
            #Open the file at the full path for writing in text mode and create CSV writer object
            with open(full_path, 'w', newline= '') as file:
                writer = csv.writer(file)
                # write thhe header row with column names
                writer.writerow(['First Name', 'Last Name', 'Address', 'Contact Number', 'Temperature', 'Symptoms',
                                 'Contact with COVID-19 positive person', 'Traveled to high-risk areas',
                                 'Taken COVID-19 test recently'])
                # iterate over each contact and write its data as row in the CSV file
                for contact in contacts:
                    writer.writerow([contact['First Name'], contact['Last Name'], contact['Address'],
                                     contact['Contact Number'], contact['Temperature'],
                                     contact['COVID-19 Questions']['Symptoms'],
                                     contact['COVID-19 Questions']['Contact with COVID-19 positive person'],
                                     contact['COVID-19 Questions']['Traveled to high-risk areas'],
                                     contact['COVID-19 Questions']['Taken COVID-19 test recently']]) 
        except Exception as e:
            # if an excepetion occurs during the file writing, raise a ValueError with the error message
            raise ValueError(f"Failed to save contacts: {e}")

    def load_contacts_from_file(filename):
        # create an empty list to store the loaded contacts
        contacts = []
        # open the file in read mode and create a CSV reader
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            #iterate over each row in the CSV file
            for row in reader:
            # contact information from the row and conver relevant values to boolean
                contact_info = {
                    'First Name': row['First Name'],
                    'Last Name': row['Last Name'],
                    'Address': row['Address'],
                    'Contact Number': row['Contact Number'],
                    'Temperature': row['Temperature'],
                    'COVID-19 Questions': {
                        'Symptoms': row['Symptoms'] == '1',
                        'Contact with COVID-19 positive person': row['Contact with COVID-19 positive person'] == '1',
                        'Traveled to high-risk areas': row['Traveled to high-risk areas'] == '1',
                        'Taken COVID-19 test recently': row['Taken COVID-19 test recently'] == '1'
                    }
                }
                contacts.append(contact_info)
        return contacts         


