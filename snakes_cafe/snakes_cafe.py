import textwrap

def print_salutation():
    salutation = '''
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    
    ***********************************
    ** What would you like to order? **
    *********************************** 
    '''
    
    print(textwrap.dedent(salutation))

print_salutation()
menu = ['wings','cookies' ,'spring rolls','salmon','steak','meat mornado','a literal garden','ice cream','cake','pie','coffee','tea','unicorn tears']
custmor_input = input('> ')
orders_counter = [0,0,0,0,0,0,0,0,0,0,0,0,0]
order_counter = 1
while custmor_input != 'quit':
    lowerd = custmor_input.lower() 
    if lowerd in menu:
        index_to_increas = menu.index(f'{lowerd}')
        print(f'\n** {order_counter} order of {lowerd} have been added to your meal **\n')
        order_counter += 1
        orders_counter[index_to_increas] += 1
        custmor_input = input('> ')
    else:
        print(f"\n**{lowerd.title()} !!!, It is not in our menu, pleas select a valid item from the menu above , or you can quit by intering 'quit' **\n")
        custmor_input = input('> ')

if custmor_input == 'quit':
    print('Your oredered meal will be ready in minutes')
    print('\n   #num         item      \n')
    for idx, val in enumerate(orders_counter):
        if val != 0:
            print(f'   {val}      {menu[idx]} \n')
 