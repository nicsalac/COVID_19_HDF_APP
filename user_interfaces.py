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
        

