import json

online_shop = json.dumps({
    1: { 
        "Name": "Jisu Life Portable Fan",
        "Price": 1_200
    },
    2: {
        "Name": "Miniso Doraemon Keyboard",
        "Price": 1_999
    },
    3: {
        "Name": "Xiaomi 15",
        "Price": 50_000
    },
    4: {
        "Name": "Xiaomi Pad 7 - 256GB",
        "Price": 22_299
    },
    5: {
        "Name": "Orashare 10000mah Powerbank",
        "Price": 1_499
    },
    6: {
        "Name": "Baseus Bowie WM 02",
        "Price": 7_99
    },
    7: {
        "Name": "Ugreen Kinich Powerbank",
        "Price": 2_399
    },
    8: {
        "Name": "Samsung A55",
        "Price": 25_599
    },
    9: {
        "Name": "Lenovo Xiaoxin Pad",
        "Price": 21_299
    },
    10: {
        "Name": "Redmagic Pad",
        "Price": 32_999
    }
})

with open("online_shop_inventory.json", 'r') as file:
    online_shop = json.loads(json.load(file))

for id, product in online_shop.items():
    print(id)
    for column, product_details in product.items():
        print(f'    {column}: {product_details}')
