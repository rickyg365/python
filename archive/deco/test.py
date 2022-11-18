import os
from utils.file import compare_date

def test_compare_date():
    date_test_cases = [
        ['2000-05-20', '2000-05-25'],  # day lt
        ['2000-05-20', '2000-05-10'],  # day gt
        ['2000-05-20', '2000-06-20'],  # month lt
        ['2000-05-20', '2000-04-20'],  # month gt
        ['2000-05-20', '2002-05-20'],  # year lt
        ['2000-05-20', '1999-05-20'],  # year gt
        ['2000-05-20', '2020-2-10'],  # random
        ['2000-05-20', '2000-05-20'],  # 0 case        
    ]

    for _, data in enumerate(date_test_cases):
        print(f"\nTest #{_+1}")
        # d1, d2 = data
        compare_date(*data)



def main():
    test_compare_date()
    return

if __name__ == '__main__':
    main()
