# Import the necessary modules 
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox
from health_declaration_form import HealthDeclarationForm

# define the HealthDeclarationApp class responsible for managing the GUI
class HealthDeclarationApp:
    def __init__(self):
# create an instance of the HealthDeclarationForm class to handle health declaration data
        self.health_declaration = HealthDeclarationForm ()
        self.health_declaration.load_contacts_from_file("health_declaration_data.csv")

    def run(self):
# entry  for running the application
        self.create_gui()
        self.root.mainloop()

    def create_gui(self):     
# create the main GUI window
        self.root = tk.Tk()
        self.root.title("HDF(COVID-19)")
        self.root.configure(bg="#fde7ea")   
# create the menu frame at the top of the GUI
        menu_frame = tk.Frame(self.root, bg="#e1ccdd")
        menu_frame.pack(pady=10)
# create the title label and pack it into the menu frames
        lbl_title = tk.Label(menu_frame, text="Health Declaration Form", font=("Helvetica", 16), bg="#fde7ea") 
        lbl_title.pack()
 # create buttons for various actions (Add Contact, Show Saved Contacts, Exit) and pack them into the menu frame  
        btn_add = tk.Button(menu_frame, text= "Add Contact", command= self.open_add_contact_dialog)
        btn_add.pack(pady=5)

        btn_show_contacts = tk.Button(menu_frame, text="Show Saved Contacts", command=self.show_saved_contacts)
        btn_show_contacts.pack(pady=5)

        btn_exit = tk.Button(menu_frame, text="Exit", command=self.on_exit)
        btn_exit.pack(pady=5)
# method called when the application is exited
    def on_exit(self):
        #save the contacts data to the health_declaration_data.csv file
        self.health_declaration.save_contacts_to_file("health_declaration_data.csv")
        # main GUI window to exit the application
        self.root.destroy()

    def open_add_contact_dialog(self):
        # method to open the "Add Contact" dialog window
        if len(self.health_declaration.contacts) >= 1000:
            # error message if the contact lists is full
            messagebox.showerror("Error", "HDF Book is full.")
            return

        dialog = AddContactDialog(self.root, self.health_declaration)
        self.root.wait_window(dialog.top)

    def show_saved_contacts(self):
        #method to display the saved contacts in a new window
        saved_contacts = self.health_declaration.contacts
        if not saved_contacts:
            # If there are no contacts saved, show a message
            messagebox.showinfo("Saved Contacts", "No contacts found.")
            return 
        # create a new window to display the saved contacts
        saved_contacts_window = tk.Toplevel(self.root)
        saved_contacts_window.title("Saved Contacts")
        
        text_area = scrolledtext.ScrolledText(saved_contacts_window, width=80, height=20)
        text_area.pack()
        
         # the saved contacts by iterating through the contacts list
        for contact in saved_contacts:
            # Insert contact details into the text area
            text_area.insert(tk.END, f"First Name: {contact['First Name']}\n")
            text_area.insert(tk.END, f"Last Name: {contact['Last Name']}\n")
            text_area.insert(tk.END, f"Address: {contact['Address']}\n")
            text_area.insert(tk.END, f"Contact Number: {contact['Contact Number']}\n")
            text_area.insert(tk.END, f"Temperature: {contact['Temperature']}\n")
            text_area.insert(tk.END, "COVID-19 Questions:\n")
            text_area.insert(tk.END, f"  Symptoms: {'Yes' if contact['COVID-19 Questions']['Symptoms'] else 'No'}\n")
            text_area.insert(tk.END, f"  Contact with COVID-19 positive person: {'Yes' if contact['COVID-19 Questions']['Contact with COVID-19 positive person'] else 'No'}\n")
            text_area.insert(tk.END, f"  Traveled to high-risk areas: {'Yes' if contact['COVID-19 Questions']['Traveled to high-risk areas'] else 'No'}\n")
            text_area.insert(tk.END, f"  Taken COVID-19 test recently: {'Yes' if contact['COVID-19 Questions']['Taken COVID-19 test recently'] else 'No'}\n")
            text_area.insert(tk.END, "\n")

        # disable the text area to prevent editing
        text_area.configure(state=tk.DISABLED)

class BaseDialog:
    def __init__(self,parent, health_declaration):
        self.top = tk.Toplevel(parent)
        self.health_declaration = health_declaration
        self.create_gui()

    def create_gui(self):
        self.top.grab_set()
        self.top.title(self.dialog_title)

        main_frame = tk.Frame(self.top, bg= "#fde7ea")
        main_frame.pack(pady=10, padx=10)

        self.create_body(main_frame)

        btn_frame = tk.Frame(self.top)
        btn_frame.pack(pady=10)

    def show_message(self,message):
        messagebox.showinfo(self.dialog_title, message)

class AddContactDialog(BaseDialog):
    def __init__(self, parent, health_declaration):
        self.dialog_title = "Add Contact"
        super().__init__(parent, health_declaration)

    def create_body(self, frame):
        lbl_first_name = tk.Label(frame, text="First Name:")
        lbl_first_name.grid(row=0, column=0, sticky=tk.E)

        self.entry_first_name = tk.Entry(frame)
        self.entry_first_name.grid(row=0, column=1, pady=5)

        lbl_last_name = tk.Label(frame, text="Last Name:")
        lbl_last_name.grid(row=1, column=0, sticky=tk.E)

        self.entry_last_name = tk.Entry(frame)
        self.entry_last_name.grid(row=1, column=1, pady=5)

        lbl_address = tk.Label(frame, text="Address:")
        lbl_address.grid(row=2, column=0, sticky=tk.E)

        self.entry_address = tk.Entry(frame)
        self.entry_address.grid(row=2, column=1, pady=5)

        lbl_contact_number = tk.Label(frame, text="Contact Number:")
        lbl_contact_number.grid(row=3, column=0, sticky=tk.E)

        self.entry_contact_number = tk.Entry(frame)
        self.entry_contact_number.grid(row=3, column=1, pady=5)

        lbl_temperature = tk.Label(frame, text="Temperature:")
        lbl_temperature.grid(row=4, column=0, sticky=tk.E)

        self.entry_temperature = tk.Entry(frame)
        self.entry_temperature.grid(row=4, column=1, pady=5)
        
        # Additional COVID-19 health-related questions
        lbl_questions = tk.Label(frame, text="COVID-19 Health Questions:", font=("Helvetica", 12))
        lbl_questions.grid(row=5, columnspan=2, pady=10)

        self.question_1_var = tk.IntVar()
        self.question_1_var.set(0)
        self.chk_question_1 = tk.Checkbutton(frame, text="Have you experienced any COVID-19 symptoms?", variable=self.question_1_var)
        self.chk_question_1.grid(row=6, columnspan=2, sticky=tk.W)

        self.question_2_var = tk.IntVar()
        self.question_2_var.set(0)
        self.chk_question_2 = tk.Checkbutton(frame, text="Have you been in contact with a COVID-19 positive person?", variable=self.question_2_var)
        self.chk_question_2.grid(row=7, columnspan=2, sticky=tk.W)

        self.question_3_var = tk.IntVar()
        self.question_3_var.set(0)
        self.chk_question_3 = tk.Checkbutton(frame, text="Have you traveled to any high-risk areas?", variable=self.question_3_var)
        self.chk_question_3.grid(row=8, columnspan=2, sticky=tk.W)

        self.question_4_var = tk.IntVar()
        self.question_4_var.set(0)
        self.chk_question_4 = tk.Checkbutton(frame, text="Have you taken a COVID-19 test recently?", variable=self.question_4_var)
        self.chk_question_4.grid(row=9, columnspan=2, sticky=tk.W)
        
        
        btn_save = tk.Button(frame, text="Save", command=self.save_contact)
        btn_save.grid(row=10, column=1, pady=5)

    def save_contact(self):
        first_name = self.entry_first_name.get().strip()
        last_name = self.entry_last_name.get().strip()
        address = self.entry_address.get().strip()
        contact_number = self.entry_contact_number.get().strip()
        temperature = self.entry_temperature.get().strip()
        
        if not first_name or not last_name or not address or not contact_number or not temperature:
            self.show_message("All fields are required.")
            return

        if any(char.isdigit() or not char.isalpha() for char in first_name) or \
                any(char.isdigit() or not char.isalpha() for char in last_name):
            self.show_message("First Name and Last Name should only contain alphabetic characters.")
            return

        if not contact_number.isdigit() or len(contact_number) != 11:
            self.show_message("Contact Number should be a numeric value with 11 digits.")
            return

        try:
            temperature = float(temperature)
        except ValueError:
            self.show_message("Temperature should be a numeric value.")
            return

        # Gather the selected COVID-19 health-related questions
        questions = {
            'Symptoms': bool(self.question_1_var.get()),
            'Contact with COVID-19 positive person': bool(self.question_2_var.get()),
            'Traveled to high-risk areas': bool(self.question_3_var.get()),
            'Taken COVID-19 test recently': bool(self.question_4_var.get())
        }

        # Add the selected questions to the contact information
        contact_info = {
            'First Name': first_name,
            'Last Name': last_name,
            'Address': address,
            'Contact Number': contact_number,
            'Temperature': temperature,
            'COVID-19 Questions': questions
        }

        self.health_declaration.add_contact(contact_info)
        self.show_message("Your COVID 19-HDF saved sucessfully")
        self.top.destroy()

        







