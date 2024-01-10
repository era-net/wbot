from .controller import Controller
import datetime

class Resetter:
    # Resets database values every day at 00:00
    controller = Controller(1)

    def run(self):
        if self.is_weekday():
            if self.controller.is_completed():
                self.controller.update_streak()
            else:
                self.controller.reset_streak()

    def is_weekday(self):
        now = datetime.datetime.now()
        weekday = now.weekday()
        if weekday == 5 or weekday == 6:
            return False
        else:
            return True