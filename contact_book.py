contacts = {}

while True:
    print('\nContact Book App')
    print('1.Create Contact')
    print('2.view contact')
    print('3.Update contact')
    print('4.Delete contact')
    print('5.search conatct')
    print('6.count contact')
    print('7.Exit')

    choice = input('Enter your choice = ')

    if choice == '1':
        name = input("Enter your name :")
        if name in contacts :
            print(f'Conatct name {name} already exists')
        else:
            age = input('Enter your age = ')
            email = input('Email email = ')
            mobile = input('Enter Mobile number = ')
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
            print(f'Contact name {name} Has been created successfully')

    elif choice == '2':
        name = input("Enter your conatct name to view = ")
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Age:{age}, Mobile Number: {mobile}')
        else:
            print('contact not found')
    
    elif choice == '3':
        name = input("Enter name to update contact = ")
        if name in contacts:
            age = input('Enter update age = ')
            email = input('Email update email = ')
            mobile = input('Enter update Mobile number = ')
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
        else:
            print('Contact not found')

    elif choice == '4':
        name = input("Enter contact name to delete = ")
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} has been deleted sucessfully')
        else:
            print('contact not found')

    elif choice == '5':
        search_name = input("Enter contact name to search = ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name {name}, Age:{age},Mobile Number:{mobile}, Email:{email}')
                found = True
            if not found:
                print('No contact found with that Name')
    
    elif choice == '6':
        print(f"Total contacts in your book: {len(contacts)}")

    elif choice == '7':
        print(f"Good bye...👋")
        break
    else:
        print('Invalid Input ❌')

    