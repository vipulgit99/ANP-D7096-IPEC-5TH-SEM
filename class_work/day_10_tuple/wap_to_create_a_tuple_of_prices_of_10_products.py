# WAP to create a tuple of prices of 10 products.
# Display the lowest price, highest price, and count
# the number of products whose price is greater than 4000.


'''--------------------coding--------------------'''
# Create empty lists to store product names and prices
product_name = []
price = []

# Input product name and price
for i in range(5):
    name = input("Enter Product Name: ")
    p = float(input("Enter Product Price: "))

    product_name.append(name)
    price.append(p)

# Convert lists into tuples
product_name = tuple(product_name)
price = tuple(price)

# Display the tuples
print("\nProduct Names:")
print(product_name)

print("\nProduct Prices:")
print(price)

# Find the lowest and highest price
lowest = min(price)
highest = max(price)

# Find the index of lowest and highest price
low_index = price.index(lowest)
high_index = price.index(highest)

# Display the lowest price with product name
print("\nLowest Price Product:")
print(product_name[low_index], "-", lowest)
n   
# Display the highest price with product name
print("\nHighest Price Product:")
print(product_name[high_index], "-", highest)

# Count products whose price is greater than 4000
count = 0

for p in price:
    if p > 4000:
        count = count + 1

# Display the count
print("\nNumber of products having price greater than 4000 =", count)


'''---------------------------output---------------------------

Enter Product Name: monitor 
Enter Product Price: 5000
Enter Product Name: cpu
Enter Product Price: 400
Enter Product Name: laptop
Enter Product Price: 6000
Enter Product Name: phone 
Enter Product Price: 50
Enter Product Name: mouse
Enter Product Price: 500

Product Names:
('monitor ', 'cpu', 'laptop', 'phone ', 'mouse')

Product Prices:
(5000.0, 400.0, 6000.0, 50.0, 500.0)

Lowest Price Product:
phone  - 50.0

Highest Price Product:
laptop - 6000.0

Number of products having price greater than 4000 = 2'''