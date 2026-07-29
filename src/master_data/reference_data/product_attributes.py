"""
Product attribute rules.

These rules are used to generate realistic product
pricing, inventory and weights.
"""

PRODUCT_ATTRIBUTES = {
    "CAT001": {  # Electronics
        "selling_price": (300.0, 2500.0),
        "cost_ratio": (0.65, 0.80),
        "weight": (0.10, 8.00),
        "stock": (25, 300),
        "reorder_level": (10, 40),
    },
    "CAT002": {  # Fashion
        "selling_price": (20.0, 250.0),
        "cost_ratio": (0.45, 0.70),
        "weight": (0.20, 2.00),
        "stock": (50, 500),
        "reorder_level": (20, 75),
    },
    "CAT003": {  # Home
        "selling_price": (40.0, 1500.0),
        "cost_ratio": (0.55, 0.75),
        "weight": (1.00, 40.00),
        "stock": (10, 150),
        "reorder_level": (5, 25),
    },
    "CAT004": {  # Books
        "selling_price": (10.0, 80.0),
        "cost_ratio": (0.40, 0.60),
        "weight": (0.20, 2.00),
        "stock": (100, 1000),
        "reorder_level": (25, 100),
    },
    "CAT005": {  # Sports
        "selling_price": (25.0, 800.0),
        "cost_ratio": (0.50, 0.70),
        "weight": (0.20, 10.00),
        "stock": (30, 300),
        "reorder_level": (10, 50),
    },
    "CAT006": {  # Beauty
        "selling_price": (8.0, 150.0),
        "cost_ratio": (0.40, 0.60),
        "weight": (0.05, 1.50),
        "stock": (100, 800),
        "reorder_level": (30, 120),
    },
    "CAT007": {  # Grocery
        "selling_price": (2.0, 30.0),
        "cost_ratio": (0.55, 0.80),
        "weight": (0.10, 5.00),
        "stock": (300, 3000),
        "reorder_level": (100, 400),
    },
    "CAT008": {  # Toys
        "selling_price": (10.0, 400.0),
        "cost_ratio": (0.45, 0.70),
        "weight": (0.20, 8.00),
        "stock": (40, 400),
        "reorder_level": (15, 60),
    },
}