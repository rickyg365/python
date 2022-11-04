import random

from enum import Enum

from utils.trie import Trie
from typing import Dict, Any

from models.user import User, AuthLevel, build_user_data, build_user_str, parse_user_str

# Create List of user data
# users = []
# for i in range(10):
#     id_num = i+1

#     new_data = build_user_data(id_num, f"random user {id_num}")
#     users.append(new_data)
users = [build_user_data(id_num, f"random user {id_num}") for id_num in range(1, 11)]


# Build list of user strings for trie
user_trie = Trie()
user_strings = [build_user_str(x) for x in users]

for user in user_strings:
    user_trie.insert(user)

t1 = user_trie.starts_with("01")
print(t1)


# Build list of User Objects and print
user_objs = [User(**d) for d in users]
for u in user_objs:
    print(u)
