import os

idx = ['A', 'B', 'C']
cols = ['a', 'b', 'c']


new_data = []
for i, row_label in enumerate(idx):
    new_row = []
    for j, col_label in enumerate(cols):
        data_point = 0
        new_row.append(data_point)
    new_data.append(new_row)

#rint(new_data)



functions = ['n', 'log n']
time_alloted = ['1 second', '1 minute']

def generate_blank_data(row_num, col_num):    
    new_data = []
    for i in range(row_num):
        new_row = []
        for j in range(col_num):
            data_point = 0
            new_row.append(data_point)
        new_data.append(new_row)

    # print(new_data)
    return new_data

d = generate_blank_data(len(functions), len(time_alloted))
print(d)








