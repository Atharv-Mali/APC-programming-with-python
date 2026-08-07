cart = ["milk", "bread", "eggs"]

print("Initial cart:", cart)

item_to_add = input("Enter item to add: ")
cart.append(item_to_add)

item_to_remove = input("Enter item to remove: ")
if item_to_remove in cart:
    cart.remove(item_to_remove)
    print("Item removed")
else:
    print("Item not found")

item_to_search = input("Enter item to search: ")
if item_to_search in cart:
    print("Item found in cart")
else:
    print("Item not found in cart")

print("Cart:", cart)
print("Total items:", len(cart))
