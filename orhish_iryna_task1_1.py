
class Client:
    def __init__(self, new_name, new_surname, new_fathers_name, New_number_porposition, new_sum_val, new_date):
        self.name = new_name
        self.surname = new_surname
        self.fathers_name = new_fathers_name
        self.number_porposition = New_number_porposition
        self.sum_val = new_sum_val
        self.date = new_date

    def __str__(self):
        return f'name     : {self.__name}\
               \nsurname    : {self.__surname}\
               \nfathers_name   : {self.__sfathers_name}\
               \nnumber_porposition    : {self.__number_porposition}\
               \nsum: {self.__sum_val}\
               \ndate     : {self.__date}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Only type str allowed for name.')
        self.__name = new_name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        if not isinstance(new_surname, str):
            raise TypeError('Only type str allowed for surname.')
        self.__surname = new_surname

    @property
    def fathers_name(self):
        return self.__fathers_name

    @fathers_name.setter
    def fathers_name(self, new_fathers_name):
        if not isinstance(new_fathers_name, str):
            raise TypeError('Only type str allowed for fathers_name.')
        self.__fathers_name = new_fathers_name

    @property
    def number_porposition(self):
        return self.__number_porposition

    @number_porposition.setter
    def number_porposition(self, New_number_porposition):
        if not isinstance(New_number_porposition, int):
            raise TypeError('Only type str allowed for number_porposition.')
        self.__number_porposition = New_number_porposition

    @property
    def sum_val(self):
        return self.__sum_val

    @sum_val.setter
    def sum_val(self, new_sum):
        if not isinstance(new_sum, int | float):
            raise TypeError('Only types int and float allowed for sum.')
        self.__sum_val = new_sum

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, new_date):
        if not isinstance(new_date, str):
            raise TypeError('Only type str allowed for date.')
        self.__date = new_date


    def year(self):
       s = (self.sum_val * 15 * (273)/365)/100
       print(s)


cli1 = Client('Jack', 'Smith', 'Tom', 15, 4700.55, '1.10.2022')

cli1.year()
