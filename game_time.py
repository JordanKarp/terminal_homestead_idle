from dataclasses import dataclass
from datetime import datetime, timedelta, time

@dataclass
class GameTime:
    current: datetime

    def set_time(self, datetime):
        self.current = datetime

    def start_of_next_day(self):
        next_day = self.current + timedelta(days=1)
        self.current = datetime.combine(next_day.date(), time(8, 0))
        return self.current


    def add_hours(self, num_hours):
        self.current += timedelta(hours=num_hours)