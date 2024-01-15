class ContactManagementMemory:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        if name in self.contacts:
            print(f"{name} already exists in contacts. Please use a different name.")
        else:
            self.contacts[name] = number
            print(f"Contact '{name}' added successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contacts:")
            for name, number in self.contacts.items():
                print(f"{name}: {number}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact '{name}': {self.contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

def main():
    contact_manager = ContactManagementMemory()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            contact_manager.add_contact(name, number)
        elif choice == '2':
            contact_manager.display_contacts()
        elif choice == '3':
            name = input("Enter contact name to search: ")
            contact_manager.search_contact(name)
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '5':
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).")

if __name__ == "__main__":
    main()