#Define the menu of hotel
menu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80,
 }

print(menu)

#Great 
print("WELCOME TO SHRUTZZ RESTAURANT")
print("pizza: Rs40\npasta: Rs50\nburger: Rs60\nsalad: Rs70\ncoffee: Rs80")

order_total = 0
#80 + 70 = 150

#user input
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu [item_1] #0 + 50
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (yes/no) ")
if another_order == "yes":
    item_2 = input("Enter the name  of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to Order")
    else:
        print(f"ordered item {item_2} is not available!")
print(f"The total amount of items to pay is {order_total}")
