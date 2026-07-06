''' Inventory Management Problem Statement: 
Create a dictionary to maintain the stock of
 products in a shop. Example: { 'Laptop': 15, 
 'Mouse': 40, 'Keyboard': 25, 'Monitor': 10 } 
 Implement the following: • Add a new product. 
   • Update the stock of an existing product.  
   • Remove a product from inventory. 
     { 'Rahul': {'Math': 85, 'Science': 90, 'English': 88},
       • Display products having stock less than 20.  
       • Display the total number of items available in the inventory.  '''





'''--------------------------------------------------------------CODING----------------------------------'''







# Inventory Management System

# Create a dictionary with initial stock
inventory = {
    "Laptop": 15,
    "Mouse": 40,
    "Keyboard": 25,
    "Monitor": 10
}

# Display current inventory
print("\nCurrent Inventory")
for product, stock in inventory.items():
    print(product, ":", stock)

# Add a new product
new_product = input("\nEnter New Product Name: ")
new_stock = int(input("Enter Stock: "))
inventory[new_product] = new_stock

print("\nInventory After Adding Product")
for product, stock in inventory.items():
    print(product, ":", stock)

# Update stock of an existing product
update_product = input("\nEnter Product Name to Update: ")

if update_product in inventory:
    stock = int(input("Enter New Stock: "))
    inventory[update_product] = stock
    print("Stock Updated Successfully")
else:
    print("Product Not Found")

# Remove a product
delete_product = input("\nEnter Product Name to Remove: ")

if delete_product in inventory:
    del inventory[delete_product]
    print("Product Removed Successfully")
else:
    print("Product Not Found")

# Display products having stock less than 20
print("\nProducts Having Stock Less Than 20")

for product, stock in inventory.items():
    if stock < 20:
        print(product, ":", stock)

# Display total number of items in inventory
total = 0

for stock in inventory.values():
    total += stock

print("\nTotal Items Available =", total)





'''---------------------output---------------------




Current Inventory
Laptop : 15
Mouse : 40
Keyboard : 25
Monitor : 10

Enter New Product Name: Printer
Enter Stock: 18

Inventory After Adding Product
Laptop : 15
Mouse : 40
Keyboard : 25
Monitor : 10
Printer : 18

Enter Product Name to Update: Mouse
Enter New Stock: 50
Stock Updated Successfully

Enter Product Name to Remove: Keyboard
Product Removed Successfully

Products Having Stock Less Than 20
Laptop : 15
Monitor : 10
Printer : 18

Total Items Available = 93'''