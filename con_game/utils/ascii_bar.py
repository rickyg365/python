
def create_bar(value: int, max_value: int):
    """
    Bar Styles
    1. ■■■■■■■■■▢ 90%
    2. ▕, █, ▏
    3. ▮ ▯
    """
    size = 15
    fill_char = "■"
    space_char = "▢"

    ratio = value/max_value

    filled_len = int(ratio*size)
    unfilled_len = size - filled_len

    return f"{filled_len*fill_char}{unfilled_len*space_char}"


def main():
    return

if __name__ == '__main__':
    main()
