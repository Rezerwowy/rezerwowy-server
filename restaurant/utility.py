from datetime import datetime


class DateTimeRange:
    start: datetime
    end: datetime

    def __init__(self, start: datetime, end: datetime):
        self.start = start
        self.end = end

    def collides(self, other) -> bool:
        return (other.start <= self.start < other.end) or \
                (other.start < self.end <= other.end)


