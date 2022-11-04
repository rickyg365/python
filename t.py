import os


@print
@str
def main():
    return "Sample Decorator Print"

if __name__ == '__main__':
    l = [x for (x + 1) in range(10)]
    print(l)

    print_sideeffect = main()

