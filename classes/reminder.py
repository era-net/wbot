from .controller import Controller
from .telegram import Telegram
import random

class Reminder:
    # Reminds every weekday evening to complete excercises if not done already
    controller = Controller(1)

    # motivational messages
    mmt = [
        "Hi 🖐\nToday is a great day to start excercising and getting your daily streak going\. Complete your exercises today and [mark them as done](https://era-kast.ch)\!",
        "Good evening 🙋‍♀️\nYou could make your day just a little bit more beautiful by completing some exercises\. [Mark them as done](https://era-kast.ch) once you finish\!",
        "Exercise? 🏋️‍♀️ [Mark it as done](https://era-kast.ch) once you finish\!",
        "Let's GO\! 🏋️‍♀️ [Mark it as done](https://era-kast.ch) once you finish\!",
        "Hi\nYou'd feel better after an exercise 💪 [Mark it as done](https://era-kast.ch) once you finish\!"
    ]

    def run(self):
        tgm = Telegram()
        if not self.controller.is_completed():
            strk = self.controller.get_streak()
            if strk == 0:
                rand_int = random.randint(0, len(self.mmt)-1)
                tgm.send_md2(self.mmt[rand_int])
            elif strk == 1:
                tgm.send_md2(f"You're about to loose your {strk}st daily streak 😥 Complete your todays exercises till 00:00 and [mark them as done](https://era-kast.ch) to continue your streak\!")
            elif strk == 2:
                tgm.send_md2(f"You're about to loose your {strk}nd daily streak 😥 Complete your todays exercises till 00:00 and [mark them as done](https://era-kast.ch) to continue your streak\!")
            elif strk == 3:
                tgm.send_md2(f"You're about to loose your {strk}rd daily streak 😥 Complete your todays exercises till 00:00 and [mark them as done](https://era-kast.ch) to continue your streak\!")
            else:
                tgm.send_md2(f"You're about to loose your {strk}th daily streak 😥 Complete your todays exercises till 00:00 and [mark them as done](https://era-kast.ch) to continue your streak\!")