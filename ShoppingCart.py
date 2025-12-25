menu =   {"Popcorn" : 5,
         "Soda" : 2,
         "Chips" : 1,
         "Icecream" : 3}
cart = []
total = 0
print("Item------TODAY'S MENU--------Price")
for key, value in menu.items():
    print(f"{key:10}: ${value: 20}")
while True:
    food = input("Enter the items you wish to buy (press q to exit !): ")
    if food == "q":
       break
    elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total +=  menu.get(food)
print(f"The items that you bought are {cart}, Your total bill is: ${total}", end= " ")
print("Thank You for choosing us !")



