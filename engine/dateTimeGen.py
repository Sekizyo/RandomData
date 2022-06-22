import time
import random

class dateTimeGenerator():
    def get(self, parr):
        if parr == "unixtime":
            return self.unixTime()
        elif parr == "isotime":
            return self.isoTime()
        elif parr == "isodate":
            return self.isoDate()
        elif parr == "isodatetime":
            return self.isoDateTime()
        else:
            return None

    def unixTime(self):
        time = {
            "time": int(time.time())-random.randint(0, int(time.time()))
        }
        
        return time

    def isoTime(self):
        hour = str(random.randint(0, 23))
        if len(hour) == 1:
            hour = '0' + hour

        minute = str(random.randint(0, 60))
        if len(minute) == 1:
            minute = '0' + minute

        second = str(random.randint(0, 60))
        if len(second) == 1:
            second = '0' + second

        time = {
            "total": f"{hour}:{minute}:{second}",
            "hour": hour,
            "minute": minute,
            "second": second
        }

        return time
        
    def isoDate(self):
        year = random.randint(1900, 2022)

        month = str(random.randint(1, 12))
        if len(month) == 1:
            month = '0' + month

        day = str(random.randint(1, 29))
        if len(day) == 1:
            day = '0' + day

        date = {
            "total": f"{year}-{month}-{day}",
            "year": year,
            "month": month,
            "day": day
        }
        return date

    def isoDateTime(self):
        date = {
            "total": f"{self.isoDate()} {self.isoTime()}",
            "total": self.isoDate(),
            "total": self.isoTime()
        }

        return date

        