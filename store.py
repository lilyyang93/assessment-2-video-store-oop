import csv 
from account import Account

class Store(Account):

    video_inventory = []

    def load_videos():
        with open('./data/inventory.csv', 'r') as csv_file:
            video_csv_data = csv.DictReader(csv_file)
            for v in video_csv_data:
                Store.video_inventory.append(v)
        for v in Store.video_inventory:
                video_stock = v['copies_available'] 
                v['copies_available'] = int(video_stock)
        return Store.video_inventory

    def view_current_inventory():
        for video in Store.video_inventory:
            print(f"Title: {video['title']}\nCopies Available: {video['copies_available']}\n")
        return "You have reached the end of the list."

    def rent_video(id, title):
        standard_max = 'Your membership allows a maximum of 1 rental at a time. Please make a return or upgrade your membership to Premium.'
        premium_max = 'Your membership allows a maxium of 3 rentals at a time. Please make a return before requesting a rental.'
        wrong_id = "Sorry, this account ID does not exist. Please try again."

        for account in Account.customers:
            if account['id'] == id:
                if account['account_type'] == 'sx':
                    if account['current_video_rentals'] != []:
                        return f"{standard_max}"
                    else:
                        return Store.search_availability(id, title)
                elif account['account_type'] == 'px':
                    if len(account['current_video_rentals']) == 3:
                        return f"{premium_max}"
                    else:
                        return Store.search_availability(id, title)
                elif account['account_type'] == 'sf':
                    if account['current_video_rentals'] != []:
                        return f"{standard_max}"
                    else:
                        return Store.is_rated_r(id, title)
                elif account['account_type'] == 'pf':
                    if len(account['current_video_rentals']) == 3:
                        return f"{premium_max}"
                    else:
                        return Store.is_rated_r(id, title)
        return f"{wrong_id}"

    def search_availability(id, title):
        title_unavailable = "Sorry, the title you requested is currently unavailable."
        wrong_spelling = "Unable to find the requested title. Please check your spelling and try again."

        for video in Store.video_inventory:
            if video['title'] == title:
                if video['copies_available'] >=1:
                    return Store.process_rental(id, title)
                else:
                    return f"{title_unavailable}"
        return f"{wrong_spelling}"

    def is_rated_r(id, title):
        restricted = "Sorry, this membership does not allow renting titles with restricted ratings."

        for video in Store.video_inventory:
            if video['title'] == title:
                if video['rating'] != 'R':
                    return Store.search_availability(id, title)
                else:
                    return f"{restricted}"

    def process_rental(id, title):
        for video in Store.video_inventory:
            if video['title'] == title:
                video['copies_available'] -= 1
                break
        for account in Account.customers:
            if account['id'] == id:
                account['current_video_rentals'].append(title)
                break
        return f"Your rental request for {title} is complete."

    def return_video(id, title):
        for video in Store.video_inventory:
            if video['title'] == title:
                video['copies_available'] += 1
        for record in Account.customers:
            if record['id'] == id:
                for video in record['current_video_rentals']:
                    if video == title:
                        record['current_video_rentals'].remove(title)
                        return "Your return was successfully processed."
                        


