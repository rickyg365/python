import os

""""""

def handle_dict(item):
    if type(item) is not dict:
        return
    
    for k, v in item:



def handle_list(item):
    if type(item) is not list:
        return

def check_raw_data(item):
    return


def main():
    raw_list = [1, 2, 3]
    raw_dict = {"a": 1, "b": 2, "c": 3}

    handle_dict(raw_dict)
    
    handle_list(raw_list)
    

if __name__ == '__main__':
    main()




