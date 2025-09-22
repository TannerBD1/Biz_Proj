#   Output some of the main fn into an alt file for simplicity
#   import packages
import json, requests
# import numpy, pandas

#   tmp var
weekday = []
weekend = []
timeframe = []
zone = 'cat'
sys_data = []

#   Create header formatting for design
print('\t<h> Order Trajectory on Timeframe </h>\n')
#   def
def timeframe_adj(season):
    weekday
    weekend
    last_proj = input('Weekday, or Weekend: ')
    period = last_proj
    last_actual = int(input(f'What happened last {period} (variance): '))

    if season == 'winter':
        selection = int(+1, 739, 788)
        timeframe.append(selection)
    elif season == 'spring':
        selection = int(-1, 539, 588)
        timeframe.append(selection)
    elif season == 'summer':
        selection = int(-2, 239, 288)
        timeframe.append(selection)
    elif season == 'fall':
        selection = int(+2, 239, 288)
        timeframe.append(selection)
def detect_variance(stock_order):
    tmp_stock = int(input('what is left in stock?: '))
    surp_defic = stock_order-tmp_stock
    print(f'order {surp_defic}')
    proj_data=int(input('Look ahead how busy will next period be?: '))
    calculate_order = surp_defic - proj_data
    print(calculate_order)
# Read existing data
    try:
        with open("stock.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []  # Start with an empty list if file doesn't exist
    return
def weekly_order(variance):
    item = input('Select an item: ')
    while True:
        add = int(input(f"How many of {item} per order: "))
        break
    return
def place_order(prod, order):
    distributor = "Big Brand"
    print(f"system syn: {distributor} this is the current shipment ({prod}; {order})")
    shop = "Small Franchise"
    print(f"system ack: {shop} this is the current shipment ({prod}; {order})")
    return
#   Main
def main():
    prod = input('What item is being updated; ')
    stock_order = int(input('enter last order amount: '))
    detect_variance(stock_order)
    variance = int(input("lets do some basic calc required(to meet demand) - current(on shelf): "))
    weekly_order(variance)
    season = ('What season are we in?(winter, spring, summer, fall); ')
    timeframe_adj(season)
#   run through timeframe adj
    order = int(stock_order-variance)
    place_order(prod, order)
    sys_data = (f'\n\t<h>{zone}</h>;\n <p>{prod}; {stock_order}</p>')
    print(sys_data)
# Read existing data
    try:
        with open("stock.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []  # Start with an empty list if file doesn't exist

# Append new data
    data.append(sys_data)

# Write updated data back
    with open("stock.json", "w") as file:
        json.dump(data, file, indent=4)
    return 
if __name__ == "__main__":
    main()
