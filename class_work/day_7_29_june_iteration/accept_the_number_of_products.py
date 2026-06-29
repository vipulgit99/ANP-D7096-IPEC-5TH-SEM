# Accept the number of products
n = int(input("Enter Number of Products: "))

# Read details of the first product
name = input("Enter Product Name: ")
qty = int(input("Enter Quantity: "))
price = float(input("Enter Price per Unit: "))

cost = qty * price
total = cost

highest_cost = cost
lowest_cost = cost
expensive_product = name
cheap_product = name

print(name, "Cost =", cost)

# Read details of remaining products
for i in range(2, n + 1):

    name = input("Enter Product Name: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price per Unit: "))

    cost = qty * price
    total += cost

    print(name, "Cost =", cost)

    if cost > highest_cost:
        highest_cost = cost
        expensive_product = name

    if cost < lowest_cost:
        lowest_cost = cost
        cheap_product = name

# Calculate average product cost
average = total / n

# Display results
print("\nTotal Bill Amount =", total)
print("Most Expensive Product =", expensive_product)
print("Cheapest Product =", cheap_product)
print("Average Product Cost =", average)




'''--------------------------output--------------------------



Enter Number of Products: 2
Enter Product Name: gfdhg
Enter Quantity: 5
Enter Price per Unit: 50
gfdhg Cost = 250.0
Enter Product Name: gjjhf
Enter Quantity: 10
Enter Price per Unit: 40
gjjhf Cost = 400.0

Total Bill Amount = 650.0
Most Expensive Product = gjjhf
Cheapest Product = gfdhg
Average Product Cost = 325.0
'''