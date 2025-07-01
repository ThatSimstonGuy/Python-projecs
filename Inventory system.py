from pathlib import Path

#Define the file path for the inventory
FILE_PATH = Path('inventory.txt')

#Defining the header for the inventory file
HEADER = 'ID,Name,Category,Quantity,Price\n'

#Sample data to initialize the inventory file if it doesn't exist
SAMPLE_DATA = '''1,Apple,Fruit,50,10
2,Banana,Fruit,30,15
3,Carrot,Vegetable,20,18
4,Detergent,Household,15,10
5,Shampoo,Personal Care,25,35
'''

#Function to initialize the inventory file with sample data
def initialize_inventory():
    with FILE_PATH.open('w') as file:
        file.write(HEADER)
        file.write(SAMPLE_DATA)

#Function to read the inventory from the file
def read_inventory():
    if not FILE_PATH.exists():
        initialize_inventory()
    with FILE_PATH.open('r') as file:
        lines = file.readlines()[1:]  # Skip the header
    inventory = []
    for line in lines:
        id, name, category, quantity, price = line.strip().split(',')
        inventory.append({
            'ID': int(id),
            'Name': name,
            'Category': category,
            'Quantity': int(quantity),
            'Price': float(price)
        })
    return inventory

# Function to write the inventory back to the file
def write_inventory(inventory):
    with FILE_PATH.open('w') as file:
        file.write(HEADER)
        for item in inventory:
            file.write(f"{item['ID']},{item['Name']},{item['Category']},{item['Quantity']},{item['Price']}\n")

# Function to add a new product
def add_product():
    inventory = read_inventory()
    id = max(item['ID'] for item in inventory) + 1 if inventory else 1
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    quantity = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))
    inventory.append({
        'ID': id,
        'Name': name,
        'Category': category,
        'Quantity': quantity,
        'Price': price
    })
    write_inventory(inventory)
    print(f"Product '{name}' added successfully.")

# Function to update an existing product
def update_product():
    inventory = read_inventory()
    id = int(input("Enter product ID to update: "))
    for item in inventory:
        if item['ID'] == id:
            item['Name'] = input(f"Enter new name (current: {item['Name']}): ") or item['Name']
            item['Category'] = input(f"Enter new category (current: {item['Category']}): ") or item['Category']
            item['Quantity'] = int(input(f"Enter new quantity (current: {item['Quantity']}): ") or item['Quantity'])
            item['Price'] = float(input(f"Enter new price (current: {item['Price']}): ") or item['Price'])
            write_inventory(inventory)
            print(f"Product ID {id} updated successfully.")
            return
    print(f"Product ID {id} not found.")

# Function to delete a product
def delete_product():
    inventory = read_inventory()
    id = int(input("Enter product ID to delete: "))
    for item in inventory:
        if item['ID'] == id:
            inventory.remove(item)
            write_inventory(inventory)
            print(f"Product ID {id} deleted successfully.")
            return
    print(f"Product ID {id} not found.")

# Function to sort products by price
def sort_by_price():
    inventory = read_inventory()
    inventory.sort(key=lambda x: x['Price'])
    print("Products sorted by price:")
    for item in inventory:
        print(f"{item['ID']}. {item['Name']} - {item['Price']}")

# Function to filter products by category
def filter_by_category():
    category = input("Enter category to filter by: ")
    inventory = read_inventory()
    filtered = [item for item in inventory if item['Category'].lower() == category.lower()]
    if filtered:
        print(f"Products in category '{category}':")
        for item in filtered:
            print(f"{item['ID']}. {item['Name']} - {item['Price']}")
    else:
        print(f"No products found in category '{category}'.")

# Function to generate an inventory summary report
def generate_inventory_report():
    inventory = read_inventory()
    print("Inventory Summary Report:")
    for item in inventory:
        print(f"ID: {item['ID']}, Name: {item['Name']}, Category: {item['Category']}, Quantity: {item['Quantity']}, Price: {item['Price']}")

# Function to generate a category summary report
def generate_category_report():
    inventory = read_inventory()
    categories = {}
    for item in inventory:
        if item['Category'] not in categories:
            categories[item['Category']] = {'count': 0, 'total_value': 0}
        categories[item['Category']]['count'] += 1
        categories[item['Category']]['total_value'] += item['Quantity'] * item['Price']
    print("Category Summary Report:")
    for category, data in categories.items():
        print(f"Category: {category}, Number of Products: {data['count']}, Total Value: {data['total_value']}")

# Main function to display the menu and handle user input
def main():
    while True:
        print("\n****||SOL.AR Inventory Management System||*****")
        print("1. Add a new product")
        print("2. Update an existing product")
        print("3. Delete a product")
        print("4. Sort products by price")
        print("5. Filter products by category")
        print("6. Generate inventory summary report")
        print("7. Generate category summary report")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_product()
        elif choice == '2':
            update_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            sort_by_price()
        elif choice == '5':
            filter_by_category()
        elif choice == '6':
            generate_inventory_report()
        elif choice == '7':
            generate_category_report()
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
