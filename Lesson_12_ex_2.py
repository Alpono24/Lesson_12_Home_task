print("Lesson 12. Home task №2.")
"""
2. ПчёлоСлон
Экземпляр класса инициализируется двумя целыми числами,
первое относится к пчеле, второе – к слону. Класс реализует
следующие методы:

● Fly() – возвращает True, если часть пчелы не меньше части
слона, иначе – False

● Trumpet() – если часть слона не меньше части пчелы,
возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”

● Eat(meal, value) – может принимать в meal только ”nectar” или
“grass”. Если съедает нектар, то value вычитается из части
слона, пчеле добавляется. Иначе – наоборот. Не может
увеличиваться больше 100 и уменьшаться меньше 0.
"""


class BeeElephant:
    def __init__(self, Bee, Elephant):
        self.Bee = Bee
        self.Elephant = Elephant

    def Fly(self):
        if self.Bee >= self.Elephant:
            print("Это TRUE - Часть пчелы не меньше части слона!")
            return True
        else:
            print("Это FALSE - Часть пчелы МЕНЬШЕ части слона!")
            return False

    def Trumpet(self):
        if self.Bee <= self.Elephant:
            print("tu-tu-doo-doo")
            return True
        else:
            print("wzzzz")
            return False

    def Eat(self, meal, value):
        if meal == 'nectar':
            self.Elephant = max(min(self.Elephant - value, 100), 0)
            self.Bee = max(min(self.Bee + value, 100), 0)
        elif meal == 'grass':
            self.Elephant = max(min(self.Elephant +  value, 100),0)
            self.Bee = max(min(self.Bee - value, 100),0)
        else:
            print("Приняла что-то не то")




animal = BeeElephant(20, 30)
print('Это изначальное состояние пчелы:', animal.Bee)
print('Это изначальное состояние слона:' , animal.Elephant)

print('')
print('<<<<<Это метод Fly>>>>>>')
animal.Fly()

print('')
print('<<<<<Это метод Trumpet>>>>>>')
animal.Trumpet()

print('')
print('<<<<<Это метод Eat +- 20>>>>>>')
animal.Eat('nectar', 20)

print('Это пчела после еды:',animal.Bee)
print('Это слон после еды:',animal.Elephant)

print('<<<<<Это метод Eat +- 60 >>>>>>')
animal.Eat('grass', 90)
print('Это пчела после еды:',animal.Bee)
print('Это слон после еды:',animal.Elephant)


