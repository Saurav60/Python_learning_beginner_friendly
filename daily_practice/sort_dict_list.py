# to sort a list of dictionaries containing product details by price in descending order.
products = [
    {"name": "Product A", "price": 25},
    {"name": "Product B", "price": 10},
    {"name": "Product C", "price": 40},
    {"name": "Product D", "price": 30}
]
sorted_products = sorted(products,key = lambda x: x['price'],reverse=True)
print(sorted_products)
