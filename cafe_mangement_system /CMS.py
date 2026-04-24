# Cafe Management System (Professional Version)

menu = {
    "pizza": 40,
    "pasta": 50,
    "burger": 60,
    "salad": 70,
    "coffee": 80
}

cart = {}
total = 0

print("\n🍽️ Welcome to Python Restaurant 🍽️")
print("\n------ MENU ------")
for item, price in menu.items():
    print(f"{item.title()} : Rs{price}")
print("------------------")

while True:
    item = input("\nEnter item name (or 'exit' to finish): ").lower()

    if item == "exit":
        break

    if item in menu:
        try:
            qty = int(input(f"Enter quantity of {item}: "))
            cart[item] = cart.get(item, 0) + qty
            print(f"{item} x{qty} added to cart")
        except:
            print("Invalid quantity")
    else:
        print("Item not available")

# Bill
print("\n -------- BILL --------")

for item, qty in cart.items():
    price = menu[item] * qty
    total += price
    print(f"{item.title()} x{qty} = Rs{price}")

print("------------------------")
print(f"Subtotal = Rs{total}")

# GST
gst = total * 0.05
print(f"GST (5%) = Rs{gst:.2f}")

# Discount
discount = 0
if total > 200:
    discount = total * 0.10
    print(f"Discount (10%) = -Rs{discount:.2f}")

final_total = total + gst - discount

print("------------------------")
print(f"Final Amount = Rs{final_total:.2f}")
print("------------------------")

print("Thank you! Visit again.")