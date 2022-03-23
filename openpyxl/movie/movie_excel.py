import os
import pandas as pd
from utils.auto_excel import create_workbook

"""
[CSV Keys]
    Index #
    Title	
    Movie Info	
    Distributor	
    Release Date	
    Domestic Sales (in $)	
    International Sales (in $)	
    World Sales (in $)	
    Genre	
    Movie Runtime	
    License

[Sample Entry]
    0	
    Star Wars: Episode VII - The Force Awakens (2015)	
    As a new threat to the galaxy rises, Rey, a desert scavenger, and Finn, an ex-stormtrooper, must join Han Solo and Chewbacca to search for the one hope of restoring peace.	
    Walt Disney Studios Motion Pictures	
    December 16, 2015	
    936662225	
    1132859475	
    2069521700	
    ['Action', 'Adventure', 'Sci-Fi']	
    2 hr 18 min	
    PG-13

"""

# type_map = {
#     "title": str,
#     "movie_info": str,
#     "distributor": str,
#     "release_date": int,
#     "domestic_sales": int,
#     "international_sales": int,
#     "world_sales": int,
#     "genre": object,
#     "movie_runtime": str,
#     "license": str
# }

# set the first column as the index and first row as column titles(header)
# new_movie_df = pd.read_csv("data/raw_highest_holywood_grossing_movies.csv", header=0, index_col=0)


new_movie_df = pd.read_csv("data/highest_holywood_grossing_movies.csv", index_col=0)

# Save DF
# new_movie_df.to_csv("data/highest_holywood_grossing_movies.csv")

print(new_movie_df.head())

movie_financial_info = new_movie_df[["international_sales", "domestic_sales", "world_sales", "movie_runtime"]]

print(movie_financial_info.shape)
print(movie_financial_info.head())

# Movies that made less than a million domestic
less_than_a_mill = new_movie_df[movie_financial_info["domestic_sales"] > 700_000_000]
print(less_than_a_mill.head())

# print(pd.to_numeric(movie_financial_info["domestic_sales"]))
