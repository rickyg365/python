import os
import sqlite3

from dataclasses import dataclass

from pushlet import PushBulletNotifier


@dataclass
class Transaction:
    date: str
    amount: float
    category: str
    expense: bool=True
    description: str=None

def transaction_adapter():
    return




class BudgetTracker:
    NOTIFIER_ENV_FILE = 'sum.env'

    def __init__(self, database_filename: str='budget_tracker.db'):
        # User Profile
        self.user_profile = {
            'name': '',
        }
        
        # Data
        self.categories = ['food', 'travel', 'bill', 'entertainment']
        self.transactions = []
        self.budgets = {}

        # Metadata
        self.database = sqlite3.connect(database_filename)
        self.notifier = PushBulletNotifier(self.NOTIFIER_ENV_FILE)
        

    def add_transaction(self, t: Transaction=None):
        self.notifier.push_note("New Transaction", "This is the main body content...")
                
        # Get cursor
        cur = self.database.cursor()
        
        return

    def set_budget(self, category: str):
        self.notifier.push_note(f"New Budget: {category}", "This is the main body content...")
  
        # Get cursor
        cur = self.database.cursor()
        
        return
    
    def view_balance(self):
        # Get cursor
        cur = self.database.cursor()
        
        return
    
    def generate_report(self):
        self.notifier.push_note("Report Generated", "This is the main body content...")
          
        # Get cursor
        cur = self.database.cursor()
        
        return
    

    """
    TBI
    - Visualizations (matplotlib...)
    - Alerts and Notifications    
    """

    


if __name__ == "__main__":
    DATABASE = "budget_tracker.db"
    btracker = BudgetTracker(DATABASE)

    btracker.add_transaction()
    btracker.set_budget('pokemon')
    btracker.view_balance()
    btracker.generate_report()





