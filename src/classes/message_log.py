from datetime import datetime, timedelta
from typing import List


class Message:
    def __init__(self, text: str, start_time: datetime, duration):
        self.text = text
        self.start_time = start_time
        self.duration = duration

    @property
    def end_time(self):
        delta = timedelta(minutes=self.duration)
        return self.start_time + delta
    
    @property
    def format(self):
        return f"Day {self.start_time.day}: {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')} - {self.text} "

    def __str__(self):
        return f"Day {self.start_time.day}: {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')} - {self.text} "
    
    def __repr__(self):
        return f"Day {self.start_time.day}: {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')} - {self.text} "



class MessageLog:
    def __init__(self) -> None:
        self.messages: List[Message] = []

    @property
    def show_most_recent(self):
        if not self.messages:
            return ""
        return self.messages[-1].format
    
    def show_log(self):
        """Return the full message log as a string (one message per line)."""
        return "\n".join([m.format for m in self.messages])
    
    def add_message(self, text, start_time, duration):
        if self.messages and text == self.messages[-1].text:
            self.messages[-1].duration += duration
        else:
            self.messages.append(Message(text, start_time, duration))
