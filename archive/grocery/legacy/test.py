import os

# Test Save
test_path = "data/test.json"

save_data = new_item.to_dict()
save(save_data, test_path)

# Test Load
sample_grocery_data = load(test_path) 

new_item = GroceryItem(**sample_grocery_data)


# Test new item
new_item = GroceryItem(**sample_grocery_data)
new_item_data = new_item.to_dict()

print(new_item)

# Test new item - to_dict
new_item = GroceryItem(**sample_grocery_data)
new_item_data = new_item.to_dict()
print(new_item_data)


# Test new item - cache
# Test new item - config
# Test new item - generate_config
# Test input item


# Test item view
new_item = GroceryItem(**sample_grocery_data)
new_item_data = new_item.to_dict()

new_item_view = SingleRowView(new_item_data)

print(new_item_view)



def main():
    return

if __name__ == '__main__':
    main()
