def main_menu():
	print("""
		Main menu
		1. View Products
		2. Add to Cart
		3. Remove from Cart
		4. View Cart
		5. Checkout
		6. exit
    		""")
	print(f"you have {len(cart[0])} items")
	response = int(input("> "))
	match response:
		case 1: view_products()
		case 2: add_to_cart()
		case 3: remove_from_cart()
		case 4: view_cart()
		case 5: check_out()
		case 6: print("exiting...")
        
        
        
def view_products():
    for index in range(len(products[0])):
        print(f"{index + 1}. {products[0][index]}   {products[1][index]}")
    print("""
	do you want to go back ?
	1. back
    	""")
    response = int(input("> "))
    match response:
        case 1: main_menu()
        

def add_to_cart():
    for index in range(len(products[0])):
        print(f"{index + 1}. {products[0][index]}   {products[1][index]}")
    response = int(input("add to cart\n>"))
    cart[0].append(products[0][response - 1])
    cart[1].append(products[1][response - 1])
    print(f"{products[0][response - 1]} has been added to cart....")
    main_menu()
    
    
    
def check_out():
    total = 0
    for index in range(len(cart[0])):
        total += cart[1][index]
        print(f"{index + 1}. {cart[0][index]}   {cart[1][index]}")
    print(f"the total price is: {total}")
    cart[0].clear()
    cart[1].clear()
    response = input("would you like to go back to main menu? yes/no: ")
    if response.lower() == "yes":
        main_menu()
    else:
        print("thank you for shopping with us...")
    
    
    
def remove_from_cart():
    for index in range(len(cart[0])):
        print(f"{index + 1}. {cart[0][index]}")
    response = int(input("> "))
    
    if len(cart) == 2:
        cart[0].pop([0][response - 1])
        cart[1].pop([0][response - 1])
        main_menu()
    else:
        print("no index")
        
        
def view_cart():
	for index in range(len(cart)):
		print(f"{index + 1}.{cart[0][index]} {cart[1][index]}")
	response = int(input("Would you like to checkout; Press 1 for yes or 2 to go back to main menu: "))
	if response == 1:
		check_out()
	elif response == 2:
		main_menu()
	else:
		print("invalid input, returning to main menu")
		main_menu()
			
		


products = [["laptop", "phone", "headphones"], [1000, 500, 100]]
cart = [[], []]
main_menu()