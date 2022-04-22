"""
Notification app to notify user to sleep on time.
Required modules:
1. time
2. plyer
"""

import time

from plyer import notification

if  __name__ == '__main__':
    notification.notify(
        title = "Time to Sleep",
        message = "You are up late night. I recommend sleeping early.",
        app_icon = "sleepy.ico",
        timeout = 2     # Displaying time
    )

    time.sleep(5)       # Waiting time