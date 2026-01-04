new_order = {
    "customer" : "Jhon Smith",
    "item" : "laptop", 
    "price" : 1500, 
    "quantity" : 1
}

new_order["date"] = "2023.12.15"

del new_order["quantity"]

print(f"The update order details are: {new_order}")