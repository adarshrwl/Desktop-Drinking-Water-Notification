
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink WATER NOW!!",
            message="Thousands have lived without love, not one without water",
            app_icon="Glass.ico",
            timeout=10
        )
        time.sleep(60*60)
        # pythonw .\main.py
        #run in background
        # Kill in background terminal
