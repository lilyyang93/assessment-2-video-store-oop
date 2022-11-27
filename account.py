import csv

class Account:

    customers = []

    def __init__(self, id, account_type, first_name, last_name, current_video_rentals=[]):
            self.id = id
            self.account_type = account_type
            self.first_name = first_name
            self.last_name = last_name 
            self.current_video_rentals = current_video_rentals
    
    def __str__(self):
        return f"'id': {self.id}, 'account_type': {self.account_type}, 'first_name': {self.first_name}, 'last_name': {self.last_name}, 'current_video_rentals': {self.current_video_rentals}"
    
    def load_customers():
        with open('./data/customers.csv', 'r') as csv_file:
            customer_csv_data = csv.DictReader(csv_file)
            for c in customer_csv_data:
                Account.customers.append(c)
        for a in Account.customers:
            if a['current_video_rentals']:
                video_log = a['current_video_rentals'].split('/')
                a['current_video_rentals'] = video_log
            else:
                a['current_video_rentals'] = []
        return Account.customers

    def add_new_customer(new_customer):
        Account.customers.append(new_customer)
        return Account.customers

    def view_current_rentals(id):
        for account in Account.customers:
            if account['id'] == id:
                return f"Current rentals: {', '.join(account['current_video_rentals'])}"

    def view_all_customers():
        for account in Account.customers:
            print(f"Account ID: {account['id']}\nAccount Owner: {account['first_name']} {account['last_name']}\n")
        return "You have reached the end of the list."
