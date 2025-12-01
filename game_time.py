# from dataclasses import dataclass
from datetime import datetime, timedelta, time

START_YEAR = 2000
START_MONTH = 1


class GameTime:
    """
    In-game time built on Python's datetime.
    Time only advances through player actions.
    """

    def __init__(self, start_day=1, start_hour=7, start_minute=0):
        # Anchor the game at an arbitrary fixed date; year/month don't matter.
        self.time = datetime(
            START_YEAR, START_MONTH, start_day, start_hour, start_minute
        )

    def advance(self, minutes=0, hours=0, days=0):
        """Advance in-game time using timedelta."""
        delta = timedelta(days=days, hours=hours, minutes=minutes)
        self.time += delta

    @property
    def day(self):
        return self.time.day

    @property
    def hour(self):
        return self.time.hour

    @property
    def minute(self):
        return self.time.minute

    def advance_to_start_of_next_day(self):
        next_day = self.time + timedelta(days=1)
        self.time = datetime.combine(next_day.date(), time(8, 0))
        return self.time

    def as_tuple(self):
        return (self.day, self.hour, self.minute)

    def __str__(self):
        return f"Day {self.day} {self.hour:02d}:{self.minute:02d}"
