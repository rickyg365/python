import os
from datetime import datetime

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from dataclasses import dataclass
from typing import List, Dict, Union


"""
Grocery Models
____________________________
> Item


> Receipt


"""
class Purchase:
    def __init__(self, amount: float, item_id: str, store_id: str, datetime: Union[datetime, str]):
        self.item_id = item_id
        self.store_id = store_id
        self.amount = amount
        self.datetime = datetime

    def __str__(self):
        s = f'{self.amount}'
        return s
    
    @classmethod
    def input(cls):
        item_id = input("Item ID: ")
        store_id = input("Store ID: ")
        amount = input("Amount: ")
        datetime = input("Date of Purchase: ")
        
        # data = {
        #     'name': name,
        #     'item_id': item_id,
        #     'tag': tag,
        #     'price': price
        # }

        # return data
        return cls(item_id=item_id, store_id=store_id, amount=amount, datetime=datetime)
    
    def export(self):
        return {
            "item_id": self.item_id,
            "store_id": self.store_id,
            "amount": self.amount,
            "datetime": self.datetime
        }

class PriceSnapshot:
    def __init__(self, amount: float, store_id: str, datetime: Union[datetime, str]):
        self.store_id = store_id
        self.amount = amount
        self.datetime = datetime

    def __str__(self):
        s = f'{self.amount}'
        return s
    
    @classmethod
    def input(cls):
        store_id = input("Store ID: ")
        amount = input("Amount: ")
        datetime = input("Date of Purchase: ")
        
        # data = {
        #     'name': name,
        #     'tag': tag,
        #     'price': price
        # }

        # return data
        return cls(store_id=store_id, amount=amount, datetime=datetime)
    
    def export(self):
        return {
            "store_id": self.store_id,
            "amount": self.amount,
            "datetime": self.datetime
        }


@dataclass
class Item:
    item_id: str=None
    name: str
    tag: str=None
    price_history: List[PriceSnapshot]=None

    def add_purchase(self, amount: float, store_id: str, datetime: Union[datetime, str]):
        new_purchase = PriceSnapshot(amount=amount, store_id=store_id, datetime=datetime)

        if self.price_history is None:
            self.price_history = list()

        self.price_history.append(new_purchase)


    def export(self):
        return {
            "name": self.name,
            "item_id": self.item_id,
            "tag": self.tag,
            "price_history": [i.export() for i in self.price_history],
        }
    
    @classmethod
    def input(cls, item_id: str=None):
        item_id = item_id if item_id is not None else input("Item ID: ")
        name = input("Name: ")
        tag = input("Tag: ")

        # Add a purchase?
        price = PriceSnapshot.input()
        
        # data = {
        #     'name': name,
        #     'item_id': item_id,
        #     'tag': tag,
        #     'price': price
        # }
                        
        # return data
        return cls(name=name, tag=tag, price_history=price, item_id=item_id)


class Receipt:
    def __init__(self, store_id: str, datetime: Union[str, datetime], subtotal: float, total: float, items: List[Union[Dict, Purchase]]):
        self.store_id = store_id
        self.datetime = datetime
        self.total = total
        self.subtotal = subtotal

        self.data = items

        # Check if data is raw
        if isinstance(items[0], dict):
            self.data = [Purchase(**i) for i in items]

        # Analysis Variables


    def __str__(self):
        txt = f"""[{self.store_id}] {self.datetime}
Subtotal: {self.subtotal}
Taxes: {self.total - self.subtotal}
Total: {self.total}
"""
        return txt
    
    def export(self):
        return {
            "store_id": self.store_id,
            "datetime": self.datetime,
            "total": self.total,
            "subtotal": self.subtotal,
            "items": [i.export() for i in self.data]
        }
    
    @classmethod
    def input(cls):
        # Datetime
        dt = datetime.now()

        # Store Id
        store_id = input("Store ID: ")

        print("Now lets add some items!")
        # Items        
        items = []
        while True:
            new_item = Purchase.input()
            items.append(new_item)

            u_in = input("Input Another? (q to quit): ")
            if u_in == 'q':
                break           
        
        # Subtotal
        subtotal = input("Subtotal: ")

        # Total
        total = input("Total: ")

        # Add to data
        # data = {
        #     'store_id': store_id,
        #     'items': items,
        #     'subtotal': subtotal,
        #     'total': total,
        # }
        # return data
        
        return cls(store_id=store_id, datetime=dt, subtotal=float(subtotal), total=float(total), items=items)
    
    def to_dataframe(self):
        """Dataframe Columns
        Date
        Store
        Name
        Tag
        Price
        """
        d = self.datetime
        s_id = self.store_id

        frame = {
            "date": [],
            "store": [],
            "item": [],
            "tag": [],
            "price": [],
        }

        for item in self.data:
            frame['date'].append(d)
            frame['store'].append(s_id)
            frame['item'].append(item.name)
            frame['tag'].append(item.tag)
            frame['price'].append(item.amount)

        return frame
    
    
    def calculate_taxes(self):
        return

#     def analyze(self, generate_visualizations: bool=False):
#         """
#         > Spending by Category
#         > Average Price by Store
#         > Price Trends over Time
#         > Best Store for Each Item
#         > Calculate Total Spending Over Time
#         > Determine Cost Distribution by Category
        
#         TBI
#         Seasonality Analysis
#         > Track price change over months/weeks
        
#         Outlier Detection
#         > Identify unusually high prices for items (using z-scores or interquartile range)

#         Budget Planning
#         > Set budgets and alerts

#         User-Specific Insights 
        
#         """
#         data = self.to_dataframe()
#         df = pd.DataFrame(data)

#         # Spending by Category
#         category_spending = df.groupby('tag')['price'].sum().reset_index()

#         # Average Price by Store
#         average_price_store = df.groupby('store')['price'].mean().reset_index()

#         # Price Trends over Time
#         price_trends = df.groupby(['date', 'item'])['price'].mean().reset_index()

#         # Best Store for Each Item
#         best_store = df.loc[df.groupby('item')['price'].idxmin()][['item', 'store', 'price']]

#         # Calculate Total Spending Over Time
#         spending_over_time = df.groupby('date')['price'].sum().reset_index()

#         # Determine Cost Distribution by Category
#         category_stats = df.groupby('tag')['price'].describe()

#         print(f"""
# {category_spending=}
# {average_price_store=}
# {price_trends=}
# {best_store=}
# {spending_over_time=}
# {category_stats=}
# """)


#         # Generate Visualizations
#         if generate_visualizations:

#             def create_plot(fig_size, x_data, y_data, data, plot_type, title, x_label, y_label):
#                 return
            
#             # Change save filename to have date or be seperated into folders by date
            
#             # Spending by Category
#             plt.figure(figsize=(8, 5))
#             sns.barplot(x="tag", y="price", data=category_spending)
#             plt.title("Total Spending by Category")
#             plt.xlabel("Category")
#             plt.ylabel("Total Spending ($)")
            
#             plt.savefig('data/spend_category.png', dpi=100)
#             plt.show()

#             # Average Price by Store
#             plt.figure(figsize=(8, 5))
#             sns.barplot(x="store", y="price", data=average_price_store)
#             plt.title("Average Price by Store")
#             plt.xlabel("Store")
#             plt.ylabel("Average Price ($)")

#             plt.savefig('data/average_price_store.png', dpi=100)
#             plt.show()

#             # Price Trends over Time
#             plt.figure(figsize=(8, 5))
#             sns.lineplot(x="date", y="price", hue="item", data=price_trends, marker='o')
#             plt.title("Price Trends Over Time")
#             plt.xlabel("Date")
#             plt.ylabel("Price ($)")
#             plt.xticks(rotation=45)
#             plt.legend(title="Item")
            
#             plt.savefig('data/price_trends_time.png', dpi=100)
#             plt.show()

#             # Determine Cost Distribution by Category
#             # Spending Distribution (Pie Chart)
#             category_spending.set_index('tag')['price'].plot(kind='pie', autopct="%1.1f%%", figsize=(6, 6), title="Spending Distribution by Category")
#             plt.ylabel("")  # Remove default y-axis
            
#             plt.savefig('data/spending_pie.png', dpi=100)
#             plt.show()

#             # Best Store for Each Item
#             # Compare Store Performance (Heatmap)
#             store_item_prices = df.pivot_table(index='store', columns='item', values='price', aggfunc="mean")
#             plt.figure(figsize=(8, 5))
#             sns.heatmap(store_item_prices, annot=True, fmt=".2f", cmap="coolwarm")
#             plt.title("Average item Prices by Store")
            
#             plt.savefig('data/best_store_heat_map.png', dpi=100)
#             plt.show()

#             # Spending Over Time (Cumulative Line Chart)
#             df["Cumulative Spending"] = df['price'].cumsum()
#             plt.figure(figsize=(8, 5))
#             plt.plot(df['date'], df['Cumulative Spending'], marker='o')
#             plt.title("Cumulative Spending Over Time")
#             plt.xlabel("Date")
#             plt.ylabel("Cumulative Spending ($)")
#             plt.xticks(rotation=45)

#             plt.savefig('data/spend_cumulative_line_chart.png', dpi=100)    
#             plt.show()            
        # return


def analyze_receipt_df(receipts: List[Receipt], visualize: bool=False):
    """
        > Spending by Category
        > Average Price by Store
        > Price Trends over Time
        > Best Store for Each Item
        > Calculate Total Spending Over Time
        > Determine Cost Distribution by Category
        
        TBI
        Seasonality Analysis
        > Track price change over months/weeks
        
        Outlier Detection
        > Identify unusually high prices for items (using z-scores or interquartile range)

        Budget Planning
        > Set budgets and alerts

        User-Specific Insights 
        
    """
    df = pd.concat([pd.DataFrame(receipt.to_dataframe()) for receipt in receipts])

    # Spending by Category
    category_spending = df.groupby('tag')['price'].sum().reset_index()

    # Average Price by Store
    average_price_store = df.groupby('store')['price'].mean().reset_index()

    # Price Trends over Time
    price_trends = df.groupby(['date', 'item'])['price'].mean().reset_index()

    # Best Store for Each Item
    best_store = df.loc[df.groupby('item')['price'].idxmin()][['item', 'store', 'price']]

    # Calculate Total Spending Over Time
    spending_over_time = df.groupby('date')['price'].sum().reset_index()

    # Determine Cost Distribution by Category
    category_stats = df.groupby('tag')['price'].describe()

    print(f"""
{category_spending=}
{average_price_store=}
{price_trends=}
{best_store=}
{spending_over_time=}
{category_stats=}
""")


    # Generate Visualizations
    if visualize:

        def create_plot(fig_size, x_data, y_data, data, plot_type, title, x_label, y_label):
            return
        
        # Change save filename to have date or be seperated into folders by date
        
        # Spending by Category
        plt.figure(figsize=(8, 5))
        sns.barplot(x="tag", y="price", data=category_spending)
        plt.title("Total Spending by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Spending ($)")
        
        plt.savefig('data/spend_category.png', dpi=100)
        plt.show()

        # Average Price by Store
        plt.figure(figsize=(8, 5))
        sns.barplot(x="store", y="price", data=average_price_store)
        plt.title("Average Price by Store")
        plt.xlabel("Store")
        plt.ylabel("Average Price ($)")

        plt.savefig('data/average_price_store.png', dpi=100)
        plt.show()

        # Price Trends over Time
        plt.figure(figsize=(8, 5))
        sns.lineplot(x="date", y="price", hue="item", data=price_trends, marker='o')
        plt.title("Price Trends Over Time")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.xticks(rotation=45)
        plt.legend(title="Item")
        
        plt.savefig('data/price_trends_time.png', dpi=100)
        plt.show()

        # Determine Cost Distribution by Category
        # Spending Distribution (Pie Chart)
        category_spending.set_index('tag')['price'].plot(kind='pie', autopct="%1.1f%%", figsize=(6, 6), title="Spending Distribution by Category")
        plt.ylabel("")  # Remove default y-axis
        
        plt.savefig('data/spending_pie.png', dpi=100)
        plt.show()

        # Best Store for Each Item
        # Compare Store Performance (Heatmap)
        store_item_prices = df.pivot_table(index='store', columns='item', values='price', aggfunc="mean")
        plt.figure(figsize=(8, 5))
        sns.heatmap(store_item_prices, annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Average item Prices by Store")
        
        plt.savefig('data/best_store_heat_map.png', dpi=100)
        plt.show()

        # Spending Over Time (Cumulative Line Chart)
        df["Cumulative Spending"] = df['price'].cumsum()
        plt.figure(figsize=(8, 5))
        plt.plot(df['date'], df['Cumulative Spending'], marker='o')
        plt.title("Cumulative Spending Over Time")
        plt.xlabel("Date")
        plt.ylabel("Cumulative Spending ($)")
        plt.xticks(rotation=45)

        plt.savefig('data/spend_cumulative_line_chart.png', dpi=100)    
        plt.show()    



