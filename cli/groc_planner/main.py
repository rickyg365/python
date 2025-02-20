import os
from datetime import datetime

from models.grocery_models import Receipt, Item, analyze_receipt_df


RAW_DATA = {
    "store_id": "t1",
    "items": [
        {
            "item_id": "hw01",
            "name": "Command Hook",
            "tag": "hardware",
            "price": 9.99,
        },
        {
            "item_id": "gc01",
            "name": "GM Cereal",
            "tag": "grocery",
            "price": 4.50,
        },
        {
            "item_id": "kn01",
            "name": "Pyrex - Small 3 pack",
            "tag": "kitchen",
            "price": 9.99,
        }
    ],
    "subtotal": 176.45,
    "total": 189.25,
    "datetime": datetime.now()
}


if __name__ == "__main__":
    # r = Receipt(**RAW_DATA)
    # # r.analyze(True)

    receipts = [Receipt(**RAW_DATA)]
    # Create 2 Receipts
    # for _ in range(2):
    #     receipts.append(Receipt.input())


    analyze_receipt_df(receipts, visualize=True)


