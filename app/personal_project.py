import requests, json
print('< TITLE > hello world </ TITLE >')
freezer_items = []
fridge_items = []
dry_items = []
inventory_list = []
def sort_cat(if_zone):
    while True:
        print("Updating items")
        if if_zone == '1':
            freezer_items.append(if_zone)
            break
        elif if_zone == '2':
            fridge_items.append(if_zone)
            break
        if if_zone == '3':
            dry_items.append(if_zone)
            break
        else:
            print('That was not valid input')
            break
    return
def select_list(updated_item):
    if updated_item == 'freezer_list':
        selection = (710, 739, 788)
        inventory_list.append(selection)
    elif updated_item == 'fridge_list':
        selection = (510, 539, 588)
        inventory_list.append(selection)
    elif updated_item == 'dry_list':
        selection = (210, 239, 288)
        inventory_list.append(selection)
    return
def weekly_order(items):
    while True:
        item = input("What item is being updated: ")
        add = input(f"How many of {item} per order: ")
    return
def detect_variance(variance):
    last_proj = 0
    last_actual = 0
    surp_defic = last_proj-last_actual
    var2 = 0
    calculate = surp_defic - var2
    with open('results.json', 'r') as f:
        json.load(calculate, f, indent=4)
    return
def notify_party(message):
    distributor = "Big Brand"
    print(f"system: {distributor} this is the current detection ({message})")
    shop = "Small Franchise"
    print(f"system: {shop} this is the current detection ({message})")
    return
def create_save_for_inventory():
    updated_data = inventory_list
    with open('results.json', 'w') as f:
        json.dump(updated_data, f, indent=4)
    return 
def main():
    locate = input("What zone is this in? \n1. Freezer\n2. Fridge\n3. Dry\n(Enter Number Only): ")
    sort_cat(locate)
    updated_item = input("What item is being updated (target_list)?: ")
    select_list(updated_item)
    alert = notify_party("positive")
# Read existing data
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []  # Start with an empty list if file doesn't exist

# Append new data
    data.append(updated_item)

# Write updated data back
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    return 
if __name__ == "__main__":
    main()
