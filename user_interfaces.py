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






