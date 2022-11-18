

def load(filepath: str):
    with open(filepath, 'r') as in_file:
        headers = []
        for _, line in enumerate(in_file):
            if _ == 0:
                headers = line.split(',')
            
            if _ == 5:
                print(headers)
                break
            print(_, line)

def main():
    return

if __name__ == '__main__':
    main()
