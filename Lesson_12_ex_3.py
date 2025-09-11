print("Lesson 12. Home task №3.")
"""
3. Класс «Автобус».
Класс содержит свойства:
● Скорость - speed 
● Максимальное количество посадочных мест - max_seats  
● Максимальная скорость - max_speed 
● Список фамилий пассажиров list_of_passanger
● Флаг наличия свободных мест - availability_flag
● Словарь мест в автобусе dict_seats_bus

Методы:

● Посадка и высадка одного или нескольких пассажиров
● Увеличение и уменьшение скорости на заданное значение
● Операции in, += и -= (посадка и высадка пассажира по
фамилии)
"""
from dataclasses import dataclass

@dataclass
class Bus:
    speed: int
    list_of_passanger: list
    availability_flag: bool
    dict_seats_bus: dict
    __max_speed: int = 129
    _max_seats: int = 6


    def seats_available(self):
        if len(self.list_of_passanger) < self._max_seats:
            self.availability_flag = True
            # print(f'Имеются свободные места в количестве: {self.max_seats - len(self.list_of_passanger)}')
            return True
        elif len(self.list_of_passanger) == 0:
            self.availability_flag = True
            # print(f'В автобусе все места свободны. Всего {self.max_seats}')
            return True
        elif len(self.list_of_passanger) == self._max_seats:
            self.availability_flag = False
            # print(f'Свободных мест нет.')
            return False
        else:
            self.availability_flag = False
            # print(f'Свободных мест нет.')
            return False


    def boarding_passengers(self):
        if self.seats_available():             #self.availability_flag == True:
            new_passenger = input('Введите фамилию имя и инициалы нового пассажира: ')
            self.list_of_passanger.append(new_passenger)
        else:
            print(f'В автобусе нет мест.')

    def disembarkation_of_passengers(self):
        number_of_seat = int(input('Введите номер места пассажира для высадки: '))
        if  number_of_seat >= 1 and number_of_seat <= len(self.list_of_passanger):
            person = self.list_of_passanger[number_of_seat-1]
            print('Этот пассажир должен выйти на остановке: ', person)
            your_choice = int(input('Если подтверждаете нажмите 1, если нет - 0: '))
            if your_choice == 1:
                print(f'Пассажир {person} освобождает своё место №{number_of_seat} и выходит из автобуса.')
                self.list_of_passanger.pop(number_of_seat-1)
            else:
                pass
        else:
            print('Вы ввели некорректные данные.')


    def speed_up(self, add_speed):
        if self.speed + add_speed < self.__max_speed:
            self.speed += add_speed
            return self.speed
        if self.speed + add_speed > self.__max_speed:
            print(f'Скорость не может быть больше максимально ограниченной: {self.__max_speed}')
            return self.speed

    def speed_down(self, down_speed):
        if self.speed - down_speed > 0:
            self.speed -= down_speed
            return self.speed
        if self.speed - down_speed < 0:
            print(f'Скорость не может быть меньше 0')
            return self.speed


list_of_passanger = []
bus = Bus(90,  list_of_passanger , True,  {'place_1': 'Place_1', 'place_2': 'Place_2', 'place_3': 'Place_3', 'place_4':'Place_4', 'place_5': 'Place_5', 'place_6': 'Place_6', 'place_7' : 'Place_7', 'place_8': 'Place_8', 'place_9': 'Place_9'})


def choice_action():
    while True:
        print('              Действия:')
        print('1. Есть ли свободные места в автобусе.')
        print('2. Вывести количество свободных мест в автобусе.')
        print('3. Вывести перечень пассажиров в автобусе.')
        print('4. Посадка пассажира по ФИО')
        print('5. Высадка пассажира номеру места с проверкой ФИО')
        print('6. Увеличение скорости на заданное значение')
        print('7. Уменьшение скорости на заданное значение')
        print('8. Выход из программы')
        print('')
        choice = input('Введите действие от 1 до 8: ')

        if choice == '1':
            if bus.seats_available() == True:
                # pass
                print(f'Свободные места в автобусе есть. Добро пожаловать на посадку!')
            else:
                # pass
                print(f'Свободных мест в автобусе нет')

        if choice == '2':
            print(f'Свободные места в автобусе: {bus._max_seats - len(bus.list_of_passanger)} из {bus._max_seats}.')

        if choice == '3':
            if bus.list_of_passanger != []:
                print('Перечень пассажиров в автобусе:')
                for i, person in enumerate(bus.list_of_passanger):
                    print(i+1, '.', person)
                print(f'Всего: {len(bus.list_of_passanger)} пассажиров.')
            else:
                print(f'Автобус пуст. Пассажиры отсутствуют.')

        if choice == '4':
            bus.boarding_passengers()

        if choice == '5':
            bus.disembarkation_of_passengers()

        if choice == '6':
            add_speed = int(input('Введите значение на которое нужно увеличить скорость: '))
            print('Скорость автобуса повышена до: ', bus.speed_up(add_speed))


        if choice == '7':
            down_speed = int(input('Введите значение на которое нужно уменьшить скорость: '))
            print('Скорость автобуса уменьшена до: ', bus.speed_down(down_speed))

        elif choice == '8':
            print('До новых встреч в нашем комфортабельном автобусе TMS.')
            break

        input('Нажмите Enter для перезапуска программы.')
        print('')

choice_action()


