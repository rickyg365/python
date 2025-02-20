import time

from utils.pushlet import PushBulletNotifier
from utils.auto_rapper import AutomationHelperFunction

helper = AutomationHelperFunction()
notifier = PushBulletNotifier('sum.env')


def run():
    # User Input
    DELAY = int(helper.prompt("Would you like to set a delay?", 0))
    GAMEMODE = helper.prompt("Would you like to choose a Gamemode?", "aram")
    ITERATIONS = int(helper.prompt("Would you like to set the number of iterations?", 15))
    NOTIFICATIONS_ON = bool(helper.prompt("Receive Notifications?", ''))


    # Delay
    time.sleep(DELAY)

    # Start Program
    if NOTIFICATIONS_ON:
        notifier.push_note('League Match Finder', "Starting League Match Finder...")
    # Play button
    helper.click('images/play.png', search_time=10)

    # Gamemode
    match GAMEMODE.lower():
        case 'aram':
            helper.click('images/aram.png', search_time=30)
        case _:
            pass

    # Confirm
    helper.click('images/confirm.png', search_time=30)

    # Find Match
    helper.click('images/find_match.png', search_time=30)

    # Accept
    redundancy = 3

    if NOTIFICATIONS_ON:
        notifier.push_note('League Match Finder', 'Waiting to accept Match')
    
    for _ in range(ITERATIONS):
        print(_+1)
        found_btn = helper.click('images/accept.png', search_time=60)
        
        if found_btn and NOTIFICATIONS_ON:
            # If wait time is long notifier can time out
            notifier.push_note('League Match Finder', "Match has been Found!")
            break

    for _ in range(redundancy):
        print(f"r{_}")
        helper.click('images/accept.png', search_time=30)


if __name__ == "__main__":
    run()
