import os

class Series:
    def __init__(self):
        pass

    def __str__(self) -> str:
        txt = ""
        return txt
    

def series(formula, start: int = 1, end: int = 100):

    return


def reimann_zeta_function(s, start: int=1, end: int=100):
    return sum([1/x**s for x in range(start, end)])

pi = 3.14159

def main():

    z_2 = reimann_zeta_function(2, 1, 100_000)
    estimate = (pi**2)/6

    print(f"""
Zeta(2): {z_2}    
Estimate [(pi^2)/6]: {estimate}

Error: {(z_2 - estimate)/z_2:.4f}
    
""")

    return

if __name__ == '__main__':
    main()
