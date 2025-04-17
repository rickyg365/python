import ctypes

def get_system_metrics():
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    return screen_width, screen_height


if __name__ == "__main__":
    width, height = get_system_metrics()
    print(f"w{width}  h{height}")

