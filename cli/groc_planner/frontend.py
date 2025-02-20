import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



class AppConfig:
    def __init__(self, save_path: str='data/', item_path: str='data/items', receipt_path: str='data/receipts', data_visualization_path: str="data/visualizations"):
        self.save_path = save_path
        self.item_path = item_path
        self.receipt_path = receipt_path
        self.data_visualization_path = data_visualization_path

class App:
    DEFAULT_CONFIG = AppConfig()
    def __init__(self, config:AppConfig=None):
        self.data = None  # List of receipts

        # Config
        self.config = config if config is not None else self.DEFAULT_CONFIG
        
        self.save_path = self.config.save_path
        self.item_path = self.config.item_path
        self.receipt_path = self.config.receipt_path
        self.data_visualization_path = self.config.data_visualization_path

        # Analyzed Data
        self.data_analyzed = False
        self.main_dataframe = None

        self.category_spending = None
        self.average_price_store = None
        self.price_trends = None
        self.best_store = None
        self.spending_over_time = None
        self.category_stats = None

    def __str__(self):
        s = f'{self.name}'
        return s
    
    def add_receipt(self):
        return
    
    def analyze_data(self):
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
        self.main_dataframe = pd.concat([pd.DataFrame(receipt.to_dataframe()) for receipt in receipts])

        # Spending by Category
        self.category_spending = self.main_dataframe.groupby('tag')['price'].sum().reset_index()

        # Average Price by Store
        self.average_price_store = self.main_dataframe.groupby('store')['price'].mean().reset_index()

        # Price Trends over Time
        self.price_trends = self.main_dataframe.groupby(['date', 'item'])['price'].mean().reset_index()

        # Best Store for Each Item
        self.best_store = self.main_dataframe.loc[self.main_dataframe.groupby('item')['price'].idxmin()][['item', 'store', 'price']]

        # Calculate Total Spending Over Time
        self.spending_over_time = self.main_dataframe.groupby('date')['price'].sum().reset_index()

        # Determine Cost Distribution by Category
        self.category_stats = self.main_dataframe.groupby('tag')['price'].describe()

        print(f"""
{self.category_spending=}
{self.average_price_store=}
{self.price_trends=}
{self.best_store=}
{self.spending_over_time=}
{self.category_stats=}
""")
        self.data_analyzed = True
        return
    
    def create_visuals(self):
        if not self.data_analyzed:
            self.analyze_data()
        # Change save filename to have date or be seperated into folders by date

        # Spending by Category
        plt.figure(figsize=(8, 5))
        sns.barplot(x="tag", y="price", data=self.category_spending)
        plt.title("Total Spending by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Spending ($)")

        plt.savefig(f'{self.data_visualization_path}/spend_category.png', dpi=100)
        plt.show()

        # Average Price by Store
        plt.figure(figsize=(8, 5))
        sns.barplot(x="store", y="price", data=self.average_price_store)
        plt.title("Average Price by Store")
        plt.xlabel("Store")
        plt.ylabel("Average Price ($)")

        plt.savefig(f'{self.data_visualization_path}/average_price_store.png', dpi=100)
        plt.show()

        # Price Trends over Time
        plt.figure(figsize=(8, 5))
        sns.lineplot(x="date", y="price", hue="item", data=self.price_trends, marker='o')
        plt.title("Price Trends Over Time")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.xticks(rotation=45)
        plt.legend(title="Item")

        plt.savefig(f'{self.data_visualization_path}/price_trends_time.png', dpi=100)
        plt.show()

        # Determine Cost Distribution by Category
        # Spending Distribution (Pie Chart)
        self.category_spending.set_index('tag')['price'].plot(kind='pie', autopct="%1.1f%%", figsize=(6, 6), title="Spending Distribution by Category")
        plt.ylabel("")  # Remove default y-axis

        plt.savefig(f'{self.data_visualization_path}/spending_pie.png', dpi=100)
        plt.show()

        # Best Store for Each Item
        # Compare Store Performance (Heatmap)
        store_item_prices = self.main_dataframe.pivot_table(index='store', columns='item', values='price', aggfunc="mean")
        plt.figure(figsize=(8, 5))
        sns.heatmap(store_item_prices, annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Average item Prices by Store")

        plt.savefig(f'{self.data_visualization_path}/best_store_heat_map.png', dpi=100)
        plt.show()

        # Spending Over Time (Cumulative Line Chart)
        self.main_dataframe["Cumulative Spending"] = self.main_dataframe['price'].cumsum()
        plt.figure(figsize=(8, 5))
        plt.plot(self.main_dataframe['date'], self.main_dataframe['Cumulative Spending'], marker='o')
        plt.title("Cumulative Spending Over Time")
        plt.xlabel("Date")
        plt.ylabel("Cumulative Spending ($)")
        plt.xticks(rotation=45)

        plt.savefig(f'{self.data_visualization_path}/spend_cumulative_line_chart.png', dpi=100)    
        plt.show()    

        return
    
    def run(self):
        return



if __name__ == "__main__":
    config_data = {
        "save_path": "data/",
        "data_visualization_path": "data/test_visualizations",
         
    }
    new_config = AppConfig(**config_data)
    
    
    app = App(config=new_config)
    app.run()
