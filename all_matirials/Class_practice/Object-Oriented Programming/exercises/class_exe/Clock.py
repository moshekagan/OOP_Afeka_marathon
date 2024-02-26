class Clock:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        h = str(self.hours)
        if self.hours < 10:
            h = '0' + h
        m = str(self.minutes)
        if self.minutes < 10:
            m = '0' + m
        return f'{h}:{m}'
        # return (f'{str(self.hours).rjust(2,"0")}:'
        #         f'{str(self.minutes).rjust(2,"0")}')
    def tick(self, m):
        s = self.hours * 60 + self.minutes
        s += m
        self.hours = s // 60 % 24
        self.minutes = s % 60



c1 = Clock(2,55)
print(c1)
c1.tick(168)
print(c1)