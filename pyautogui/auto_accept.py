from utils.pushlet import PushBulletNotifier
from utils.auto_rapper import AutomationHelperFunction


if __name__ == "__main__":
    helper = AutomationHelperFunction()
    notifier = PushBulletNotifier('sum.env')

    # Accept
    iterations = 15
    redundancy = 3

    notifier.push_note('League Match Finder', 'Waiting to accept Match')
    for _ in range(iterations):
        print(_)
        found_btn = helper.click('images/accept.png', search_time=60)
        print(found_btn)
        if found_btn:
            # If wait time is long notifier can time out
            notifier.push_note('League Match Finder', "Match has been Found!")
            break


    for _ in range(redundancy):
        print(f"r{_}")
        helper.click('images/accept.png', search_time=30)


