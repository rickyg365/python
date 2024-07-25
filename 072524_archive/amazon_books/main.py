import os
import glob
import pandas as pd

"""
URL, Title, Price, five_star_rating, four_star_rating, three_star_rating, two_star_rating, one_star_rating, overall_rating, No_of_ratings, cover_img_url
"""

# Get Files - Hard Coded
# FILES = [
#     "Reference.csv",
#     "Religion.csv",
#     "Romance.csv",
#     "School_Books.csv",
#     "Science_and_Mathematics.csv",
#     "Sciences_Technology_and_Medicine.csv",
#     "Society_and_Social_Sciences.csv",
#     "Sports.csv",
#     "Textbooks_and_Study_Guides.csv",
#     "Travel.csv",
# ]

# Using glob
FILES = glob.glob("data/*.csv")


def main():
    tables = {}
    for file in FILES:
        new_df = pd.read_csv(file)

        cleaned_filename = file.split('\\')[1].split('.')[0].lower()
        tables[f"{cleaned_filename}"] = new_df
    
    # Display Tables
    print("\n".join(tables.keys()))

    # Choose Table
    CHOSEN_TABLE = "reference"
    CHOSEN_TITLE = "My First Mythology Tale".lower()

    table_df = tables[CHOSEN_TABLE]

    # Search for partial query
    print(table_df[table_df['Title'].str.contains(CHOSEN_TITLE)])

    # Needs both .str if using .lower()
    print(table_df[table_df['Title'].str.lower().str.contains(CHOSEN_TITLE)])
    


if __name__ == "__main__":
    main()