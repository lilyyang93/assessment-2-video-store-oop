from account import Account
from store import Store

Account.load_customers()
Store.load_videos()

selection = input("\n== Welcome to Code Platoon Video! ==\n1. View store video inventory\n2. View store customers\n3. View customer rented videos\n4. Add new customer\n5. Rent video\n6. Return video\n7. Exit\n")

while selection != '7':
    match selection:
        case '1':
            print(Store.view_current_inventory())
        case '2':
            print(Account.view_all_customers())
        case '3':
            id = input("\nPlease enter the customer ID #:\n>>>")
            print(Account.view_current_rentals(id))
        case '4':
            id = input("\nPlease enter a new customer ID #:")
            for a in Account.customers:
                if a['id'] == id:
                    print("That ID # is already in use.")
                    id = input("\nPlease input a different ID #:\n>>>")
            account_type = input("\nPlease enter the membership type (sx, px, sf, pf):\n >>>")
            first_name = input("\n Please enter the account owner's first name:\n>>>")
            last_name = input("\n Please enter the account owner's last name:\n>>>")
            new_customer = {'id': id, 'account_type': account_type, 'first_name': first_name, 'last_name': last_name, 'current_video_rentals':[]}
            print("New account successfully added.")
            Account.add_new_customer(new_customer)
        case'5':
            title = input("\n Please enter the title you would like to rent:\n>>>")
            id = input("\nPlease enter the customer ID #:\n>>>")
            print(Store.rent_video(id, title))
        case '6':
            id = input("\nPlease enter the customer ID #:\n>>>")
            title = input("\n Please enter the title you would like to return:\n>>>")
            print(Store.return_video(id, title))
        case _:
            print("Please enter a valid option.")
    
    selection = input("\n== Welcome to Code Platoon Video! ==\n1. View store video inventory\n2. View store customers\n3. View customer rented videos\n4. Add new customer\n5. Rent video\n6. Return video\n7. Exit\n")
