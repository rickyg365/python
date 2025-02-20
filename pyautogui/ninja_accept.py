from utils.auto_rapper import AutomationHelperFunction


if __name__ == "__main__":
    helper = AutomationHelperFunction()

    # Accept
    iterations = 15
    redundancy = 3

    for _ in range(iterations):
        print(_)
        found_btn = helper.click('images/accept.png', search_time=60)

        if found_btn:
            # If wait time is long notifier can time out
            break


    for _ in range(redundancy):
        print(f"r{_}")
        helper.click('images/accept.png', search_time=30)


