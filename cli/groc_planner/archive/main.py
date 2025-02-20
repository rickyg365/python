import os
from typing import List, Dict, Union

from dataclasses import dataclass

from datetime import datetime

"""
Objects

Transaction
- store id: str
- Items: List[Item]
- Subtotal: float
- Taxes: float
- Total: float

Item
- item id: str
- name: str
- price: float
- time: str
- store purchased: str
- brand: str
- tag: str

"""
DATETIME_FMT = f""

@dataclass
class Item:
    sort_key: str
    name: str
    price: float
    brand: str
    tag: str
    store_id: str
    time_of_purchase: Union[str, datetime]
    special: bool=False

def export(self):
    return {
        "sort_key": self.sort_key,
        "name": self.name,
        "price": self.price,
        "brand": self.brand,
        "tag": self.tag,
        "store_id": self.store_id,
        "time_of_purchase": self.time_of_purchase,
        "special": self.special,
    }



@dataclass
class Transaction:
    store_id: str
    items: List[Item]
    subtotal: float
    taxes: float
    total: float

    def export(self):
        return {
            "store_id": self.store_id,
            "items": self.items,
            "subtotal": self.subtotal,
            "taxes": self.taxes,
            "total": self.total,
        }

def read_receipt_from_img(img_path: str):
    # Use OCR to read receipt data
    return


def validate_receipt_data(raw_data: int):
    return


if __name__ == "__main__":
    SAMPLE_STORE_ID = ""
    ITEM_1_DATA = {
        "sort_key": "",
        "name": "",
        "price": "",
        "brand": "",
        "tag": "",
        "store_id": "",
        "time_of_purchase": "",
        "special": ""
    }
    ITEM_2_DATA = {
        "sort_key": "",
        "name": "",
        "price": "",
        "brand": "",
        "tag": "",
        "store_id": "",
        "time_of_purchase": "",
        "special": ""
    }
    ITEM_3_DATA = {
        "sort_key": "",
        "name": "",
        "price": "",
        "brand": "",
        "tag": "",
        "store_id": "",
        "time_of_purchase": "",
        "special": ""
    }


    TRANSACTION_DATA = {
        "store_id": "",
        "items": [ITEM_1_DATA, ITEM_2_DATA, ITEM_3_DATA],
        "subtotal": "",
        "taxes": "",
        "total": "",
    }







