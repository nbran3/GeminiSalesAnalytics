from faker import Faker
fake = Faker()
import pandas as pd
import random
import string


item_categories = {
    'Food': [
        'Fruits', 'Vegetables', 'Meat', 'Sweets', 'Bread', 'Drinks', 
        'Dairy', 'Seafood', 'Snacks', 'Canned Goods', 'Frozen Foods', 'Grains'
    ],
    'Clothes': [
        'Shirts', 'Pants', 'Shoes', 'Socks', 'Underclothes', 
        'Hats', 'Jackets', 'Sweaters', 'Belts', 'Scarves'
    ],
    'Body and Wellness': [
        'Body Wash', 'Shampoo', 'Makeup', 'Razors', 'Deodorant', 
        'Hand Soap', 'Toothpaste', 'Toothbrush', 'Lotion', 'Vitamins', 'Hair Conditioner'
    ],
    'Electronics': [
        'Smartphones', 'Laptops', 'Tablets', 'Headphones', 'Chargers', 
        'Smartwatches', 'TVs', 'Speakers', 'Keyboards', 'Mice'
    ],
    'Home and Kitchen': [
        'Cookware', 'Utensils', 'Plates', 'Cups', 'Pots', 
        'Bedding', 'Towels', 'Furniture', 'Decor', 'Cleaning Supplies'
    ],
    'Sports and Outdoors': [
        'Bicycles', 'Tennis Rackets', 'Soccer Balls', 'Running Shoes', 
        'Yoga Mats', 'Weights', 'Camping Gear', 'Hiking Boots', 'Water Bottles'
    ],
    'Toys and Games': [
        'Board Games', 'Puzzles', 'Action Figures', 'Dolls', 
        'Building Blocks', 'Card Games', 'Stuffed Animals', 'Video Games'
    ],
    'Books and Stationery': [
        'Fiction', 'Non-Fiction', 'Notebooks', 'Pens', 
        'Calendars', 'Planners', 'Art Supplies', 'Children Books'
    ]
}

item_price_ranges = {
    'Food': {
        'Fruits': (1.0, 5.0),
        'Vegetables': (0.5, 4.0),
        'Meat': (5.0, 20.0),
        'Sweets': (1.0, 6.0),
        'Bread': (1.0, 4.0),
        'Drinks': (0.5, 5.0),
        'Dairy': (1.0, 6.0),
        'Seafood': (7.0, 25.0),
        'Snacks': (0.5, 4.0),
        'Canned Goods': (0.8, 5.0),
        'Frozen Foods': (2.0, 10.0),
        'Grains': (1.0, 8.0)
    },
    'Clothes': {
        'Shirts': (10, 50),
        'Pants': (20, 70),
        'Shoes': (30, 120),
        'Socks': (2, 15),
        'Underclothes': (5, 25),
        'Hats': (5, 30),
        'Jackets': (30, 150),
        'Sweaters': (20, 80),
        'Belts': (5, 40),
        'Scarves': (5, 35)
    },
    'Body and Wellness': {
        'Body Wash': (3, 15),
        'Shampoo': (3, 15),
        'Makeup': (10, 50),
        'Razors': (2, 20),
        'Deodorant': (2, 15),
        'Hand Soap': (1, 6),
        'Toothpaste': (1, 5),
        'Toothbrush': (1, 5),
        'Lotion': (5, 25),
        'Vitamins': (5, 30),
        'Hair Conditioner': (3, 15)
    },
    'Electronics': {
        'Smartphones': (200, 1200),
        'Laptops': (400, 2500),
        'Tablets': (150, 800),
        'Headphones': (20, 300),
        'Chargers': (10, 50),
        'Smartwatches': (150, 500),
        'TVs': (300, 2000),
        'Speakers': (30, 400),
        'Keyboards': (20, 150),
        'Mice': (10, 100)
    },
    'Home and Kitchen': {
        'Cookware': (15, 200),
        'Utensils': (5, 50),
        'Plates': (2, 30),
        'Cups': (1, 25),
        'Pots': (10, 150),
        'Bedding': (20, 250),
        'Towels': (5, 60),
        'Furniture': (50, 1000),
        'Decor': (5, 150),
        'Cleaning Supplies': (2, 40)
    },
    'Sports and Outdoors': {
        'Bicycles': (100, 1500),
        'Tennis Rackets': (30, 200),
        'Soccer Balls': (10, 80),
        'Running Shoes': (50, 200),
        'Yoga Mats': (10, 60),
        'Weights': (20, 300),
        'Camping Gear': (20, 500),
        'Hiking Boots': (50, 250),
        'Water Bottles': (5, 50)
    },
    'Toys and Games': {
        'Board Games': (10, 60),
        'Puzzles': (5, 50),
        'Action Figures': (5, 80),
        'Dolls': (10, 100),
        'Building Blocks': (15, 150),
        'Card Games': (5, 40),
        'Stuffed Animals': (5, 60),
        'Video Games': (20, 70)
    },
    'Books and Stationery': {
        'Fiction': (5, 30),
        'Non-Fiction': (5, 35),
        'Notebooks': (1, 15),
        'Pens': (1, 10),
        'Calendars': (5, 25),
        'Planners': (5, 30),
        'Art Supplies': (5, 80),
        'Children Books': (3, 25)
    }
} 

item_quantity_ranges = {
    'Food': {
        'Fruits': (1, 10),
        'Vegetables': (1, 10),
        'Meat': (1, 5),
        'Sweets': (1, 15),
        'Bread': (1, 10),
        'Drinks': (1, 15),
        'Dairy': (1, 5),
        'Seafood': (1, 5),
        'Snacks': (1, 20),
        'Canned Goods': (1, 20),
        'Frozen Foods': (1, 15),
        'Grains': (1, 8)
    },
    'Clothes': {
        'Shirts': (1, 6),
        'Pants': (1, 5),
        'Shoes': (1, 4),
        'Socks': (1, 20),
        'Underclothes': (1, 8),
        'Hats': (1, 6),
        'Jackets': (1, 4),
        'Sweaters': (1, 4),
        'Belts': (1, 4),
        'Scarves': (1, 3)
    },
    'Body and Wellness': {
        'Body Wash': (1, 4),
        'Shampoo': (1, 4),
        'Makeup': (1, 4),
        'Razors': (1, 10),
        'Deodorant': (1, 10),
        'Hand Soap': (1, 8),
        'Toothpaste': (1, 6),
        'Toothbrush': (1, 8),
        'Lotion': (1, 10),
        'Vitamins': (1, 8),
        'Hair Conditioner': (1, 4)
    },
    'Electronics': {
        'Smartphones': (1, 4),
        'Laptops': (1, 2),
        'Tablets': (1, 2),
        'Headphones': (1, 3),
        'Chargers': (1, 4),
        'Smartwatches': (1, 2),
        'TVs': (1, 3),
        'Speakers': (1, 3),
        'Keyboards': (1, 2),
        'Mice': (1, 2)
    },
    'Home and Kitchen': {
        'Cookware': (1, 2),
        'Utensils': (1, 4),
        'Plates': (1, 4),
        'Cups': (1, 5),
        'Pots': (1, 3),
        'Bedding': (1, 3),
        'Towels': (1, 15),
        'Furniture': (1, 2),
        'Decor': (1, 2),
        'Cleaning Supplies': (1, 5)
    },
    'Sports and Outdoors': {
        'Bicycles': (1, 2),
        'Tennis Rackets': (1, 3),
        'Soccer Balls': (1, 4),
        'Running Shoes': (1, 4),
        'Yoga Mats': (1, 2),
        'Weights': (1, 3),
        'Camping Gear': (1, 3),
        'Hiking Boots': (1, 2),
        'Water Bottles': (1, 5)
    },
    'Toys and Games': {
        'Board Games': (1, 4),
        'Puzzles': (1, 3),
        'Action Figures': (1, 2),
        'Dolls': (1, 3),
        'Building Blocks': (1, 3),
        'Card Games': (1, 4),
        'Stuffed Animals': (1, 3),
        'Video Games': (1, 2)
    },
    'Books and Stationery': {
        'Fiction': (1, 2),
        'Non-Fiction': (1, 2),
        'Notebooks': (1, 5),
        'Pens': (1, 10),
        'Calendars': (1, 4),
        'Planners': (1, 4),
        'Art Supplies': (1, 10),
        'Children Books': (1, 2)
    }
}

def generate_orders(n_rows):
    rows = []
    for _ in range(n_rows):
        transactionID = fake.uuid4()
        payment_type = random.choice(['Credit Card', 'Debit Card', 'Cash', 'Online'])
        order_date = fake.date_between(start_date='-1w', end_date='today')
        category = random.choice(list(item_categories.keys()))
        item = random.choice(item_categories[category])
        price_min, price_max = item_price_ranges[category][item]
        price = round(random.uniform(price_min, price_max), 2)
        qty_min, qty_max = item_quantity_ranges[category][item]
        quantity = random.randint(qty_min, qty_max)
        name = fake.name()
        state = fake.state()
        account = 'NB' + ''.join(random.choices(string.digits, k=7))
        
        rows.append({
            'transactionID':transactionID,
            'order_date':order_date,
            'paymentType':payment_type,
            'category': category,
            'item': item,
            'price': price,
            'quantity': quantity,
            'name':name,
            'state':state,
            'accountID':account
        })
    return rows

n_rows = 100
data = generate_orders(n_rows)
df = pd.DataFrame(data)
df