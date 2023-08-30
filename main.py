application = 'i-Krave'

menu = {
    'sku1': {
        'Name': 'Hamburger',
        'Price': 6.51
    },
    'sku2': {
        'Name': 'Cheeseburger',
        'Price': 7.65
    },
    'sku3': {
        'Name': 'Milkshake',
        'Price': 5.99
    },
    'sku4': {
        'Name': 'Fries',
        'Price': 2.39
    },
    'sku5': {
        'Name': 'Sub',
        'Price': 5.87
    },
    'sku6': {
        'Name': 'Ice Cream',
        'Price': 1.55
    },
    'sku7': {
        'Name': 'Fountain Drink',
        'Price': 3.45
    },
    'sku8': {
        'Name': 'Cookie',
        'Price': 3.15
    },
    'sku9': {
        'Name': 'Brownie',
        'Price': 2.46
    },
    'sku10': {
        'Name': 'Sauce',
        'Price': 0.75
    },
}

actions = {
    '1': 'Add a new menu item to cart',
    '2': 'Remove an item from the cart',
    '3': 'Modify an item from the cart',
    '4': 'View cart',
    '5': 'Checkout',
    '6': 'Exit'
}

sales_tax = 0.05
cart = {}


def display_menu():
    index = 1
    print('\nThis is what we have available on the menu: \n')
    for items in menu.values():
        values = items.values()
        print(f"({index}) {list(values)[0]}: £{list(values)[1]}")
        index += 1


def add_to_cart(sku, quantity=1):
    if sku in menu:
        if sku in cart:
            cart[sku] += quantity
        else:
            cart[sku] = quantity
        print("Added ", quantity, " of ", menu[sku]['Name'], " to the cart.")
    else:
        print('Item not available')


def remove_from_cart(sku):
    if sku in cart:
        cart.pop(sku)
    else:
        print('This item is not in the cart')
    print(f"Removed", menu[sku]['Name'], "from the cart.")


def modify_cart(sku, quantity):
    if sku in cart:
        if quantity > 0:
            cart[sku] = quantity
            print("Modified", menu[sku]['Name'], "quantity to ", quantity, " in the cart.")
        else:
            remove_from_cart(sku)
    else:
        print('This item is not in the cart')


def view_cart():
    print("\n****Cart Contents****\n")
    total_cost = 0
    i = 0
    for items in cart:
        print(f"{list(cart.values())[i]} x {menu[list(cart.keys())[i]]['Name']}")
        total_cost += menu[list(cart.keys())[i]]['Price'] * list(cart.values())[i]
        i += 1
    tax = total_cost * sales_tax
    print(f'\nTotal: £{round(tax + total_cost, 2)}')


def checkout():
    print("\n****Checkout****")
    view_cart()
    print("\nOrder has been submitted\n")


def get_sku_and_quantity(sku_input, quantity_input=None):
    sku_item = sku_input
    sku_item = 'sku' + str(sku_item)
    if quantity_input:
        quantity_amount = quantity_input
        if quantity_amount.isdigit():
            quantity_amount = int(quantity_amount)
        else:
            quantity_amount = 1
        return sku_item, quantity_amount
    else:
        return sku_item


def running_app():
    print(f"\nHello and Welcome to {application}. How can I help you today?")
    is_running = True
    while is_running:
        print('\n****Ordering Actions****\n')
        for item in actions:
            print(f"({item}) {actions[item]}")
        action = input('\nEnter number of action: ')

        if action == '1':
            display_menu()
            sku_item = input('\nPlease enter the SKU number for the menu item you want to order: ')
            quantity_item = input('\nQuantity: ')
            print()
            sku_choice, quantity = get_sku_and_quantity(sku_item, quantity_item)
            add_to_cart(sku_choice, quantity)

        elif action == '2':
            display_menu()
            sku_item = input('\nPlease enter the SKU number for the menu item you want to remove: ')
            print()
            sku_choice = get_sku_and_quantity(sku_item)
            remove_from_cart(sku_choice)

        elif action == '3':
            view_cart()
            display_menu()
            sku_item = input('\nPlease enter the SKU number for the menu item you want to modify: ')
            quantity_item = input('\nQuantity: ')
            print()
            sku_choice, quantity = get_sku_and_quantity(sku_item, quantity_item)
            modify_cart(sku_choice, quantity)

        elif action == '4':
            view_cart()

        elif action == '5':
            checkout()
            is_running = False

        elif action == '6':
            print('Thank you for shopping with us!')
            is_running = False

        else:
            print(f"\nNo such action as {action}. Enter a valid action.\n")


running_app()
