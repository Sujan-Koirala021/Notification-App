#Desktop Notification-App
This is a notification app with 20 line of code in python that notifies user to sleep on time.
Module Required: 
1. time: This module works with the time object and is installed by default
2. Plyer: Plyer module is used to access the features of the hardware. This module does not comes built-in with Python. We need to install it externally as:
  pip install plyer
  
 
Approach:

Step 1) Import the notification class from the plyer module i.e from plyer import notification

Step 2) After that it is needed to call the notify method of this class i.e  notification.notify()

Syntaxes:
notification.notify(
        title = "Time to Sleep",
        message = "You are up late night. I recommend sleeping early.",
        app_icon = "sleepy.ico",
        timeout = 2     # Displaying time
    )

Step 3) Add the sleep function to show the notification again.
