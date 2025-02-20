import pyperclip


def get_clipboard():
    data = None
    try:
        data = pyperclip.paste()

    except pyperclip.PyperclipException:
        print("Error: pyperclip missing or no keyboard access")
    except Exception as e:
        print(f"Error: {e}")

    return data


if __name__ == "__main__":
    d = get_clipboard()
    with open("sample.txt", 'a') as save_buf:
        save_buf.write(f">=<\n{d}\n")
    