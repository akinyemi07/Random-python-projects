contacts = {}

def show_menu():
    print("\n📖 Contact Book Menu")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()
        contacts[name] = phone
        print(f"Contact '{name}' added.")
    
    elif choice == '2':
        if not contacts:
            print("No contacts found.")
        else:
            print("\nAll Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
    
    elif choice == '3':
        search_name = input("Enter name to search: ").strip()
        if search_name in contacts:
            print(f"{search_name}: {contacts[search_name]}")
        else:
            print("Contact not found.")
    
    elif choice == '4':
        delete_name = input("Enter name to delete: ").strip()
        if delete_name in contacts:
            del contacts[delete_name]
            print(f"Deleted contact: {delete_name}")
        else:
            print("Contact not found.")
    
    elif choice == '5':
        print("Goodbye!")
        break
    
    else:
        print("Invalid option. Please choose between 1 and 5.")

