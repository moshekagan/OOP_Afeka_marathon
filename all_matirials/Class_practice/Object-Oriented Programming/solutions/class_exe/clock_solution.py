class Clock:

    def __init__(self, hour, minutes, seconds=0):
        self.hour = hour % 24
        self.minutes = minutes % 60
        self.seconds = seconds % 60

    def __str__(self):
        time = f'{self.hour}'
        if self.hour < 10:
            time = '0' + f'{self.hour}:'
        if self.minutes < 10:
            time += f'0{self.minutes}'
        else:
            time += f'{self.minutes}'
        if self.seconds < 10:
            time += f':0{self.seconds}'
        else:
            time += f':{self.seconds}'
        return time

    def tick(self, seconds):
        self.seconds += seconds
        if self.seconds > 59:
            self.minutes += self.seconds // 60
            self.seconds %= 60
        if self.minutes > 59:
            self.hour += self.minutes // 60
            self.minutes %= 60
            self.hour %= 24


def main():
    # Q2_a
    print('Q2a')
    c1 = Clock(28, 89)
    print(c1)
    c1.tick(20 * 60)
    print(c1)

    # Q1_b
    print('Q2_b')
    c1 = Clock(28, 89, 56)
    print(c1)
    c1.tick(80)
    print(c1)


if __name__ == '__main__':
    main()