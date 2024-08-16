import re
import os

# Initialize contact data storage
contacts = {}

def add_contact():
    """
    Add a new contact to the system
    """
    try:
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email address: ")
        additional_info = input("Enter additional information (optional): ")

# Validate phone number and email address using regular expressions
        if not re.match(r"^\d{3}-\d{3}-\d{4}$", phone):
            raise ValueError("Invalid phone number format. Please use XXX-XXX-XXXX.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address format.")

# Create a new contact
        contact_id = phone
        contacts[contact_id] = {
            "name": name,
            "phone": phone,
            "email": email,
            "additional_info": additional_info
        }
        print("Contact added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

# To edit contact
def edit_contact():
    """
    Edit an existing contact
    """
    try:
        contact_id = input("Enter contact phone number: ")
        if contact_id not in contacts:
            raise KeyError("Contact not found.")

        name = input("Enter new contact name (press Enter to keep current): ")
        phone = input("Enter new contact phone number (press Enter to keep current): ")
        email = input("Enter new contact email address (press Enter to keep current): ")
        additional_info = input("Enter new additional information (press Enter to keep current): ")

        # Validate phone number and email address using regular expressions
        if phone and not re.match(r"^\d{3}-\d{3}-\d{4}$", phone):
            raise ValueError("Invalid phone number format. Please use XXX-XXX-XXXX.")
        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address format.")

        # Update contact information
        if name:
            contacts[contact_id]["name"] = name
        if phone:
            contacts[contact_id]["phone"] = phone
        if email:
            contacts[contact_id]["email"] = email
        if additional_info:
            contacts[contact_id]["additional_info"] = additional_info
        print("Contact updated successfully!")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
# Delete a contact
def delete_contact():
    try:
        contact_id = input("Enter contact phone number: ")
        if contact_id not in contacts:
            raise KeyError("Contact not found.")

        del contacts[contact_id]
        print("Contact deleted successfully!")
    except KeyError as e:
        print(f"Error: {e}")

# Search for a contact
def search_contact():

    try:
        search_term = input("Enter search term (name, phone, email, or additional info): ")
        results = []
        for contact_id, contact in contacts.items():
            if search_term in contact["name"] or search_term in contact["phone"] or search_term in contact["email"] or search_term in contact["additional_info"]:
                results.append(contact)
        if results:
            print("Search results:")
            for result in results:
                print(f"Name: {result['name']}, Phone: {result['phone']}, Email: {result['email']}, Additional Info: {result['additional_info']}")
        else:
            print("No results found.")
    except Exception as e:
        print(f"Error: {e}")

# Display all contacts
def display_contacts():
   
    try:
        if not contacts:
            print("No contacts found.")
            return

        print("Contacts:")
        for contact_id, contact in contacts.items():
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Additional Info: {contact['additional_info']}")
    except Exception as e:
        print(f"Error: {e}")

# Export contacts
def export_contacts():
    
    try:
        with open("contacts.txt", "w") as f:
            for contact_id, contact in contacts.items():
                f.write(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Additional Info: {contact['additional_info']}\n")
        print("Contacts exported to contacts.txt successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Import contacts 
def import_contacts():
   if not os.path.exists("contacts.txt"):
        print("contacts.txt file not found.")
        return

with open("contacts.txt", "r") as f:
        for line in f.readlines():
            contact_info = line.strip().split(", ")
            contact_id = contact_info[1].split(": ")[1]
            contacts[contact_id] = {
                "name": contact_info[0].split(": ")[1],
                "phone": contact_info[1].split(": ")[1],
                "email": contact_info[2].split(": ")[1],
                "additional_info": contact_info[3].split(": ")[1]
            }
print("Contacts imported from contacts.txt successfully!")


# This function will run the CMS
def main():
    while True:
        print("Welcome to the Contact Management System!")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a file")
        print("7. Import contacts from a file")
        print("8. Quit")
        choice = input("Enter your choice: ")
