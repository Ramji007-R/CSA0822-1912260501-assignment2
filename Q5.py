
# Q5: Mutable Default Argument Bug and Its Correction

# Global variable
total_items_added = 0


# 1. Function with mutable default argument (BUGGY)
def add_item_buggy(item, cart=[]):
    cart.append(item)
    return cart


print("----- Mutable Default Argument Bug -----")

customer1 = add_item_buggy("Laptop")
customer2 = add_item_buggy("Mobile")
customer3 = add_item_buggy("Tablet")

print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)

# Display the default argument
print("Default values:", add_item_buggy.__defaults__)


# 2. Corrected function using None
def add_item(item, cart=None):
    global total_items_added

    if cart is None:
        cart = []

    cart.append(item)
    total_items_added += 1

    return cart


print("\n----- Corrected Function -----")

# Three customers with separate shopping carts
cart1 = add_item("Laptop")
cart2 = add_item("Mobile")
cart3 = add_item("Tablet")

print("Customer 1 Cart:", cart1)
print("Customer 2 Cart:", cart2)
print("Customer 3 Cart:", cart3)

print("Total Items Added:", total_items_added)


# 3. Function with multiple return values
def customer_summary(name, cart):
    count = len(cart)
    return name, count, cart


print("\n----- Multiple Return Values -----")

name, count, items = customer_summary("Customer 1", cart1)

print("Customer Name:", name)
print("Number of Items:", count)
print("Items:", items)


# 4. Demonstrating local and nonlocal variables
def create_counter():
    count = 0  # Enclosing variable

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


print("\n----- Nonlocal Variable -----")

counter = create_counter()

print("Counter:", counter())
print("Counter:", counter())
print("Counter:", counter())
