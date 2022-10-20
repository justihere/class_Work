class Time:
    def __init__(self, time1, time2, time3):
      self.__time1 = time1
      self.__time2 = time2
      self.__time3 = time3


    def setter(self, time1, time2, time3):
        if not isinstance(time1, int):
            raise TypeError('Error!')
        if not isinstance(time2, int):
            raise TypeError('Error!')
        if not isinstance(time3, int):
            raise TypeError('Error!')
        if time1 < 23 | time1 > 0:
            raise TypeError('No more than 1 -24!')
        if time2 < 60 | time1 > 0:
            raise TypeError('Minutes must be No more than 1 -60!')
        if time1 < 50 | time1 > 0:
            raise TypeError('Seconds must be No more than 1 -60!')


    print( sum)

    def puls_hour(self):
        self.__time1 += self.__time1
        print("hours", self.__time1)

    def puls_minute(self):
        self.__time2 += self.__time2
        print("minutes", self.__time2)

    def puls_second(self):
        self.__time3 += self.__time3
        print ("seconds", self.__time3)

t = Time(1, 30, 45)
t.puls_hour()
t.puls_minute()
t.puls_second()

