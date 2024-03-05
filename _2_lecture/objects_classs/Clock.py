class Clock:
    MINUTE_IN_HOUR = 60
    def __init__(self, hours=0, minutes=0):
        self.__hours = hours
        self.__minutes = minutes

    def tick(self, minutes):
        min = self.__minutes + minutes
        self.__minutes = min % self.MINUTE_IN_HOUR
        self.__hours += min // self.MINUTE_IN_HOUR

    def __str__(self):
        return f'{self.__hours}:{self.__minutes}'
