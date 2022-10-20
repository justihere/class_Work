class Client:
    def __init__(self, name, surname, fathers_name, number_porposition, sum, date):
      self.name = name
      self.surname = surname
      self.fathers_name = fathers_name
      self.number_porposition = number_porposition
      self.sum = sum
      self.date = date

    @property
    def get_fathers_name(self):
        return self.__fathers_name

    @property
    def get_number_porposition(self):
        return self.__number_porposition

    @property
    def get_date(self):
        return self.__date

    @property
    def get_name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    def setter(self, name, surname, fathers_name, number_porposition, sum, date):
        if not isinstance(name, str):
            raise TypeError('Name should be string data type!')
        if not isinstance(surname, str):
            raise TypeError('Surname should be string data type!')
        if not isinstance(fathers_name, str):
            raise TypeError('Name should be string data type!')
        if not all(isinstance(x, int) for x in number_porposition.values()):
            raise TypeError('Grades values should be int type!')
        if not all(isinstance(x, int) for x in sum.keys()):
            raise TypeError('Grades keys should be string type!')
        if not all(isinstance(x, int) for x in sum.keys()):
            raise TypeError('Grades keys should be string type!')
        if not isinstance(date, str):
            raise TypeError('Surname should be string data type!')



    def year(self):
        sum *= 0.15

        print( sum)


client = Client("Jack", "Smith", "Tom", 15, 4700, 1102022)
client.year()
