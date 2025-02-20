import time

from utils.pushlet import PushBulletNotifier
from utils.auto_rapper import AutomationHelperFunction

helper = AutomationHelperFunction()
notifier = PushBulletNotifier('sum.env')


# User Input
wait_time = helper.prompt("Would you like to set a delay?", 0)

time.sleep(int(wait_time))

# Game mode
# gamemode = helper.prompt("What gamemode would you like to play?", default="aram")
gamemode = 'aram'

# Play button
notifier.push_note('League Match Finder', "Starting League Match Finder...")
helper.click('images/play.png', search_time=10)

# Gamemode
match gamemode:
    case 'aram':
        helper.click('images/aram.png', search_time=30)
    case _:
        pass

# Confirm
helper.click('images/confirm.png', search_time=30)

# Find Match
helper.click('images/find_match.png', search_time=30)

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
