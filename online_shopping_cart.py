import os
import json

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def buffer():
    input()

class online_shop:
    def __init__(self):
        self.shop_name = "JOTTEE-BEE"
        self.file_name = "online_shop_inventory.json"
        self.shop_inventory = self.initialize_inventory()
        self.shopping_cart = []
        self.cart_quantity = 0
        self.total_cost = 0

    def shop_menu(self):
        while True:
            clear()
            print(self.shop_name)
            print('\n1. Display available products.')
            print('2. Display Shopping Cart')
            print('3. Add products to cart.')
            print('4. Remove products from cart.')
            print('5. Exit')

            choice = input("\nEnter your choice: ")

            match(choice):
                case '1':
                    clear()
                    self.display_inventory()
                    buffer()

                case '2':
                    clear()
                    self.display_shopping_cart()
                    buffer()

                case '3':
                    clear()
                    self.add_to_cart()

                case '4':
                    clear()
                    self.remove_product()

                case '5':
                    break

    def initialize_inventory(self):
        with open (self.file_name, "r") as file:
            shop_inventory = json.loads(json.load(file))

        return shop_inventory
    
    def display_inventory(self):
        for id, product in self.shop_inventory.items():
            print(f'{id}.')

            for column, information in product.items():
                print(f'    {column}: {information}')

    def add_to_cart(self):
        while True:
            clear()
            self.display_inventory()

            chosen_product_id = input('\nInput product index: ')

            product = self.shop_inventory[chosen_product_id]

            print('\nProduct:\n')
            for column, information in product.items():
                print(f'    {column}: {information}')

            quantity = int(input("\nQuantity: "))

            product['Quantity'] = quantity
            self.shopping_cart.append(product)
            self.cart_quantity += 1

            repeat = input("\nDo you want to add another product again? "
                    "[Yes][No] ").lower()
            
            if repeat != 'yes':
                break

    def remove_product(self):
        while True:
            clear()
            self.display_shopping_cart()
            
            chosen_product_id = input('\nInput product index: ')
            self.shopping_cart.append(self.shop_inventory[chosen_product_id])
            self.cart_quantity -= 1

            repeat = input("\nDo you want to remove another product again? "
                    "[Yes][No] ").lower()
            
            if repeat != 'yes':
                break

    def calculate_total_cost(self):
        for product in self.shopping_cart:
            self.total_cost += product['Price'] * product['Quantity']

    def display_shopping_cart(self):
        self.list_products_in_cart()

        self.calculate_total_cost()

        print('\n[Billing Statement]')
        print(f'\nShopping Cart Quantity: {self.cart_quantity}')
        print(f'\nTotal Cost: {self.total_cost}')

    def list_products_in_cart(self):
        product_index = 1
        print('Shopping Cart\n')

        for product in self.shopping_cart:
            print(f'{product_index}.\n')
            product_index += 1

            for column, information in product.items():
                print(f'    {column}: {information}')

if __name__ == "__main__":
    clear()

    sc = online_shop()

    sc.shop_menu()

