# Import tkinter module for GUI 
# Import pickle module for saving and loading file data
import tkinter as tk
from tkinter import messagebox
import pickle

# Load contacts from a file
def load_contacts():
    # Try to open the file and load data
    try:
        with open('contacts.pickle', 'rb') as contact_file:
            return pickle.load(contact_file)
    # If the file doesn't exist, return an empty dictionary
    except FileNotFoundError:
        return {}

# Save contact to file
def save_contacts(contacts):
    with open('contacts.pickle', 'wb') as contact_file:
        pickle.dump(contacts, contact_file)

#Add a new contact to file
def add_contact():
    # Get name and email from user input fields
    contact_name = name_entry.get()
    contact_email = email_entry.get()
    # Save the contact
    contacts[contact_name] = contact_email
    # Clear user input fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    # Display saved contact message
    messagebox.showinfo("Your contact has been added", "The contact has been added")

# Find and display a contact's email
def look_up():
    contact_name = name_entry.get()
    # IF/Else statement for checing if the contacts email address, if email does not exist display string
    if contact_name in contacts:
        contact_email = contacts[contact_name]
    else:
        contact_email = " Email Not found"
    result_label.config(text="Email: " + contact_email)

# Change a contact's email
def change_email():
    contact_name = name_entry.get()
    new_email = email_entry.get()
    # If/Else statement for updating the contact's email if contact doesnt exist, then display error
    if contact_name in contacts:
        contacts[contact_name] = new_email
        messagebox.showinfo("Your contact email has been changed", "The email address for the contact has been changed")
    else:
        messagebox.showerror("Email address cannot be changed", "This contact is not in the system")
    # Clear user input fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Delete contact
def delete_contact():
    contact_name = name_entry.get()
    # If/Else statement for deleting contacts if contact doesnt exist, then display error
    if contact_name in contacts:
        del contacts[contact_name]
        messagebox.showinfo("The contact deleted", "The contact has been deleted")
    else:
        messagebox.showerror("The contact could not be deleted", "This contact is not in the system")
    # Clear user input fields
    name_entry.delete(0, tk.END)

# Ask user to save file before existing program
def on_closing():
    if messagebox.askyesno("Closing program", "Would you like to save the file before closing"):
        save_contacts(contacts)
    root.destroy()

# Create GUI window
root = tk.Tk()
root.title("Name & Email Rolodex")
root.geometry("250x250")

# Create GUI widgets
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1)

add_button = tk.Button(root, text="Add", command=add_contact)
add_button.grid(row=2, column=0)
lookup_button = tk.Button(root, text="Lookup", command=look_up)
lookup_button.grid(row=2, column=1)

change_button = tk.Button(root, text="Change", command=change_email)
change_button.grid(row=3, column=0)
delete_button = tk.Button(root, text="Delete", command=delete_contact)
delete_button.grid(row=3, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Load ontacts within file
contacts = load_contacts()
# Function for when user closes program, prompt using to save file
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start loop
root.mainloop()
