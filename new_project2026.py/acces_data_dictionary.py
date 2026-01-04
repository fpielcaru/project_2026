items = { 1: "laptop", 2: "monitor", 3: "printer", 4: "mouse"}
items[3,] = "keyboard"
items[1] = "tablet"
print(items)


first_production = { 1: "car", 2: "truck", 3: "bus", 4: "motorcycle"}
first_production.update({2: "bicycle", 4: "scooter"})
print(f"Noua productie in acest an este: {first_production}")