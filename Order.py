# menu items and their prices
menu = {
    "Coffee": 150,
    "Tea": 100,
    "Sandwich": 250,
    "Burger": 400,
    "Fries": 200,
    "Cake": 500
}

# Cafe class
class Cafe:
    def __init__(self, num_tables):
        self.num_tables = num_tables
        self.tables = [Table(i) for i in range(1, num_tables + 1)]

    def open_table(self, table_number):
        if table_number > self.num_tables:
            print("Table not available")
            return None
        return self.tables[table_number - 1]

# Table class
class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.order = Order()

    def place_order(self, items):
        self.order.add_items(items)

    def close_order(self):
        self.order.calculate_bill(menu)
        print(f"Table {self.table_number} bill: Rs.{self.order.bill:.2f}")

# Order class
class Order:
    def __init__(self):
        self.items = {}

    def add_items(self, items):
        for item, quantity in items.items():
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity

    def calculate_bill(self, menu):
        self.bill = sum([menu[item] * quantity for item, quantity in self.items.items()])

# Main program
cafe = Cafe(6)

while True:
    print("Welcome to Biscotti Cafe!")
    print("1. Open table")
    print("2. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        table_number = int(input("Enter table number (1-6):-"))
        table = cafe.open_table(table_number)
        if table:
            while True:
                print("1. Place order")
                print("2. Close order")
                print("3. Exit")
                choice = input("Choose an option: ")

                if choice == "1":
                    items = {}
                    while True:
                        print(menu)
                        item = input("Enter item (or 'done' to finish): ")
                        if item.lower() == "done":
                            break
                        quantity = int(input("Enter quantity: "))
                        items[item] = quantity
                    table.place_order(items)
                elif choice == "2":
                    table.close_order()
                    break
                elif choice == "3":
                    break
    elif choice == "2":
        break