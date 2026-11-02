
menu = {
    1: ["Pizza", 150],
    2: ["Burger", 100],
    3: ["Momos", 80],
    4: ["Biryani", 180],
    5: ["Cold Drink", 40]
}

cart = []
total = 0

print("       FOOD ORDERING APP")

while True:
    print("\nFOOD MENU ")

    for key, value in menu.items():
        print(key, ".", value[0], "- Rs.", value[1])

    print("6. Checkout")
    print("0. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 0:
        print("Thank you! Visit again.")
        break

    elif choice == 6:
        print("\n======= YOUR BILL =======")

        for item, price in cart:
            print(item, "- Rs.", price)
            total += price

     
        print("Total Amount: Rs.", total)
        print("Order placed successfully!")
        break

    elif choice in menu:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            item = menu[choice][0]
            price = menu[choice][1] * quantity

            cart.append((item + " x " + str(quantity), price))

            print(item, "added to cart!")
        else:
            print("Please enter a valid quantity.")

    else:
        print("Invalid choice! Try again.")
