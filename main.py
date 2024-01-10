from classes import Resetter, Reminder
import schedule
import time

resetter = Resetter()
reminder = Reminder()

schedule.every().day.at("00:00", "Europe/Zurich").do(resetter.run)
schedule.every().monday.at("19:15", "Europe/Zurich").do(reminder.run)
schedule.every().tuesday.at("19:15", "Europe/Zurich").do(reminder.run)
schedule.every().wednesday.at("19:15", "Europe/Zurich").do(reminder.run)
schedule.every().thursday.at("19:15", "Europe/Zurich").do(reminder.run)
schedule.every().friday.at("10:33", "Europe/Zurich").do(reminder.run)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute