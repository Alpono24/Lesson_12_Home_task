from random import choice

print("Lesson 12. Home task №1.")
"""
1. Класс «Товар» содержит следующие закрытые поля:
● Название товара
● Название магазина, в котором подаётся товар
● Стоимость товара в рублях

Класс «Склад» содержит закрытый массив товаров.

Обеспечить следующие возможности:

● Вывод информации о товаре со склада по индексу
● Вывод информации о товаре со склада по имени товара
● Сортировка товаров по названию, по магазину и по цене
● Перегруженная операция сложения товаров по цене
"""

class Thing:
    def __init__(self, name_of_thing, name_of_shop, price_of_thing):
        self.__name_of_thing = name_of_thing
        self.__name_of_shop = name_of_shop
        self.__price_of_thing = price_of_thing

    @property
    def name_of_thing(self):
        return self.__name_of_thing
    @name_of_thing.setter
    def name_of_thing(self, new_name_of_thing):
        self.__name_of_thing = new_name_of_thing

    @property
    def price_of_thing(self):
        return self.__price_of_thing
    @price_of_thing.setter
    def price_of_thing(self, new_price_of_thing):
        self.__price_of_thing = new_price_of_thing

    @property
    def name_of_shop(self):
        return self.__name_of_shop
    @name_of_shop.setter
    def name_of_shop(self, new_name_of_shop):
        self.__name_of_shop = new_name_of_shop

    def show_thing(self):
        print(f'Название товара: {self.__name_of_thing}')
        print(f'Название магазина: {self.__name_of_shop}')
        print(f'Стоимость товара в рублях: {self.__price_of_thing}')


class Storage:
    def __init__(self):
        self.__storage = []

    #0 Добавляем товар на склад
    def add_item(self, thing):
        self.__storage.append(thing)

    #1 Вывод информации о товаре со склада по индексу
    def find_by_index(self, index):
        return self.__storage[index]

    #2 Вывод информации о товаре со склада по имени товара
    def find_by_name(self, name):
        count = 0
        for i, prod in enumerate(self.__storage):
            if prod.name_of_thing == name:
                count += 1
                print(f'Ваш товар на сладе под номером №{i+1}:', prod.name_of_thing)
        print(f'Всего найдено: {count} наименования(-ий).')

    #3 Сумма всех товаров на складе
    def all_prices(self):
        print(f'Сумма всех товаров на складе: {round(sum(prod.price_of_thing for prod in self.__storage),2)} рублей.')

    #4 Сортировка товаров по названию
    def sorted_by_thing(self):
        self.__storage.sort(key=lambda what: what.name_of_thing)

    #5 Сортировка товаров по магазину
    def sorted_by_shop(self):
        self.__storage.sort(key=lambda what: what.name_of_shop)

    #6 Сортировка товаров по цене
    def sorted_by_price(self):
        self.__storage.sort(key=lambda what: what.price_of_thing)

    #7 Показать все товары
    def display_all(self):
        for i, product in enumerate(self.__storage):
            print('Товар под номером:', i+1)
            product.show_thing()

#Объявляем экземпляр класса Склад - Создаем склад
storage = Storage()

#Объявляем экземпляр класса Товар - Добавляем товары
thing_1 = Thing('Яблоки', 'Евроопт', 2.15)
thing_2 = Thing('Кефир', 'Автолавка', 3.15)
thing_3 = Thing('Батон', 'Ярмарка', 7.15)
thing_4 = Thing('Печенье', 'Евроопт', 6.15)
thing_5 = Thing('Молоко', 'Автолавка', 4.15)
thing_6 = Thing('Арбуз', 'Ярмарка', 8.15)

#Добавляем товар на склад
storage.add_item(thing_1)
storage.add_item(thing_2)
storage.add_item(thing_3)
storage.add_item(thing_4)
storage.add_item(thing_5)
storage.add_item(thing_6)

# 1 Вывод информации о товаре со склада по индексу
print('')
print('# 1 Вывод информации о товаре со склада по индексу')
x = storage.find_by_index(3)
x.show_thing()

#2 Вывод информации о товаре со склада по имени товара
print('')
print('#2 Вывод информации о товаре со склада по имени товара')
y = storage.find_by_name('Молоко')
print('')
y = storage.find_by_name('Печенье')

#3 Сумма всех товаров на складе
print('')
print('#3 Сумма всех товаров на складе')
storage.all_prices()


#4 Сортировка товаров по названию
print('#4 Сортировка товаров по названию')
print('')
storage.sorted_by_thing()

#5 Сортировка товаров по магазину
print('#4 Сортировка товаров по магазину')
print('')
storage.sorted_by_shop()

#6 Сортировка товаров по цене
print('#4 Сортировка товаров по цене')
print('')
storage.sorted_by_price()

#7 Показать все товары
print('')
print('#5 Показать все товары')
storage.display_all()





