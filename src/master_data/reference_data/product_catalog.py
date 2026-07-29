"""
Master product catalog.

Maps categories and brands to valid product names.
"""

PRODUCT_CATALOG = {
    "CAT001": {  # Electronics
        "Apple": [
            "iPhone 16",
            "iPhone 16 Pro",
            "MacBook Air",
            "MacBook Pro",
            "Apple Watch Series 11",
            "AirPods Pro",
            "iPad Air",
        ],
        "Samsung": [
            "Galaxy S25",
            "Galaxy S25 Ultra",
            "Galaxy Watch",
            "Galaxy Buds",
            "Galaxy Tab",
        ],
        "Sony": [
            "WH-1000XM6 Headphones",
            "PlayStation 6 Controller",
            "Bravia OLED TV",
            "Sony Soundbar",
        ],
        "Dell": [
            "XPS 13",
            "Inspiron 15",
            "Alienware Laptop",
            "Dell Monitor",
        ],
    },

    "CAT002": {  # Fashion
        "Nike": [
            "Air Max Shoes",
            "Running Shorts",
            "Sports Jacket",
            "Training T-Shirt",
        ],
        "Adidas": [
            "Ultraboost Shoes",
            "Football Jersey",
            "Track Pants",
        ],
        "Puma": [
            "Running Shoes",
            "Gym Hoodie",
            "Sports Cap",
        ],
    },

    "CAT003": {  # Home
        "IKEA": [
            "Office Chair",
            "Dining Table",
            "Bookshelf",
            "Wardrobe",
        ],
        "Home Centre": [
            "Sofa",
            "Coffee Table",
            "Bed Frame",
            "Dining Chair",
        ],
    },

    "CAT004": {  # Books
        "Penguin": [
            "Python Programming",
            "Data Engineering Guide",
            "Machine Learning Basics",
        ],
        "HarperCollins": [
            "Cloud Computing",
            "Modern SQL",
            "Distributed Systems",
        ],
    },

    "CAT005": {  # Sports
        "Wilson": [
            "Tennis Racket",
            "Basketball",
            "Football",
        ],
        "Yonex": [
            "Badminton Racket",
            "Shuttlecock Pack",
            "Sports Bag",
        ],
    },

    "CAT006": {  # Beauty
        "L'Oréal": [
            "Face Wash",
            "Hair Serum",
            "Lipstick",
        ],
        "Nivea": [
            "Body Lotion",
            "Face Cream",
            "Sunscreen",
        ],
    },

    "CAT007": {  # Grocery
        "Nestlé": [
            "Coffee",
            "Breakfast Cereal",
            "Chocolate",
        ],
        "Kellogg's": [
            "Corn Flakes",
            "Muesli",
            "Granola",
        ],
    },

    "CAT008": {  # Toys
        "LEGO": [
            "City Set",
            "Technic Car",
            "Star Wars Kit",
        ],
        "Mattel": [
            "Barbie Doll",
            "Hot Wheels Pack",
            "UNO Cards",
        ],
    },
}