# Products available in store (Dictionary: product_id → details as Tuple)
products = {
    101: ("Laptop", 50000),
    102: ("Mouse", 800),
    103: ("Keyboard", 1500),
    104: ("Monitor", 10000),
    105: ("Headphones", 2000)
}

# User's shopping cart (List)
cart = []

# Set to track unique users who purchased
unique_users = set()

# Function to display products
def show_products():
    print("\nAvailable Products:")
    for pid, details in products.items():
        print(f"ID: {pid}, Name: {details[0]}, Price: ₹{details[1]}")

# Add product to cart
def add_to_cart(pid):
    if pid in products:
        cart.append(pid)
        print(f"✅ {products[pid][0]} added to cart!")
    else:
        print("❌ Invalid Product ID!")

# Remove product from cart
def remove_from_cart(pid):
    if pid in cart:
        cart.remove(pid)
        print(f"🗑️ {products[pid][0]} removed from cart!")
    else:
        print("❌ Product not in cart!")

# View cart
def view_cart():
    if not cart:
        print("🛒 Cart is empty.")
        return
    print("\nYour Cart:")
    for pid in cart:
        print(f"- {products[pid][0]} : ₹{products[pid][1]}")
    total = sum(products[pid][1] for pid in cart)
    print(f"Total: ₹{total}")

# Checkout
def checkout(username):
    if not cart:
        print("❌ Cart is empty! Add items before checkout.")
        return
    total = sum(products[pid][1] for pid in cart)
    print(f"\n🧾 Bill for {username}:")
    for pid in cart:
        print(f"- {products[pid][0]} : ₹{products[pid][1]}")
    print(f"Total: ₹{total}")
    
    unique_users.add(username)  # add to unique buyers
    cart.clear()  # empty cart after checkout
    print("✅ Checkout successful!")

# ---------------- MAIN PROGRAM ----------------
print("👋 Welcome to Python E-commerce App!")
username = input("Enter your name: ")

while True:
    print("\n========= MENU =========")
    print("1. Show Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        show_products()
    elif choice == "2":
        pid = int(input("Enter Product ID to add: "))
        add_to_cart(pid)
    elif choice == "3":
        pid = int(input("Enter Product ID to remove: "))
        remove_from_cart(pid)
    elif choice == "4":
        view_cart()
    elif choice == "5":
        checkout(username)
    elif choice == "6":
        print("👋 Thanks for visiting! Unique buyers so far:", unique_users)
        break
    else:
        print("❌ Invalid choice! Please select 1-6.")
