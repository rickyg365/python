from utils.auto_rapper import AutomationHelperFunction
from utils.pushlet import PushBulletNotifier


helper = AutomationHelperFunction()
notifier = PushBulletNotifier('sum.env')

# Play button
notifier.push_note('League Match Finder', "Starting League Match Finder...")
helper.click('images/play.png', search_time=10)

# Gamemode
helper.click('images/aram.png', search_time=30)

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
