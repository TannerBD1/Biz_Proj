import json
import os
# Inventory storage as dictionary for item zones
inventory = {
    "freezer": [],
    "fridge": [],
    "dry": []
}
def input_items(zone):
    print("\n...Update in Progress...\n")
    while True:
        create_cycle = input('Input an item(y/n): ')
        if create_cycle == 'y':
            list_item = input('What is the item?; ')
            inventory[zone].append(list_item)
        elif create_cycle == 'n' or create_cycle == '':
            break
        else:
            print('invalid input')
    return
def output_items(zone):
    if zone in inventory:
        print(f"\n{zone.title()} items:", inventory[zone])
    elif zone == 'n':
        print("Full inventory:", inventory)
    else:
        print('invalid input')
    return
def select_list(zone):
    if zone in inventory:
        selection = input('Enter 3 numbers: ')
        sys_select = f"{inventory[zone]}; {selection}"
        inventory[zone].append(sys_select)
    else:
        print('invalid zone')
    return
def create_save_for_inventory():
    # Save inventory to JSON file
    try:
        with open("data.json", "w") as file:
            json.dump(inventory, file, indent=4)
        print("Inventory saved.")
    except Exception as e:
        print("Error saving inventory:", e)
def load_inventory():
    # Load inventory from JSON file if exists
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if isinstance(data, dict):
                inventory.update(data)
            else:
                print("Invalid data format in data.json; skipping load.")
    except Exception as e:
        print("Error loading inventory:", e)
def main():
    load_inventory()
    zone_map = {"1": "freezer", "2": "fridge", "3": "dry"}
    chk_zone = input("What zone is this in? \n1. Freezer\n2. Fridge\n3. Dry\n(Enter Number Only): ")
    if chk_zone in zone_map:
        input_items(zone_map[chk_zone])
    updated_zone = input("What zone is being updated?: ")
    if updated_zone in zone_map.values():
        select_list(updated_zone)
    target_zone = input('Specify zone?(1,2,3 or n); ')
    if target_zone in zone_map:
        output_items(zone_map[target_zone])
    elif target_zone == 'n':
        output_items('n')
    create_save_for_inventory()
if __name__ == "__main__":
    main()
