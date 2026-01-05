cart = [
    {'item': 'laptop', 'count' : 4, 'price' : 700}, 
    {'item': 'computer', 'count' : 10 , 'price' : 200}, 
    {'item': 'monitor', 'count' : 3, 'price': 120},
    {'item' : 'keyboard', 'count': 9 , 'price' : 50}, 
    {'item': 'mouse', 'count': 30, 'price': 10}
]

total_income = 0 
for item in cart:
    total_income += item['count'] * item['price']

print(f"Venitul total este: {total_income}")