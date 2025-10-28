# Тема 8. Основы объектно-ориентированного программирования
Отчет по Теме #8 выполнила:
- Шкабара Злата Александровна
- ПИЭ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ |---------|---------|
| Задание 1 | +       | +       |
| Задание 2 | +       | +       |
| Задание 3 | +       | +       |
| Задание 4 | +       | +       |
| Задание 5 | +       | +       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;



## Лабораторная работа №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car:  # создали класс Car
    def __init__(self, make, model):  # определили конструктор класса
        self.make = make  # установили атрибут make 
        self.model = model  # установили атрибут model 

my_car = Car("Toyota", "Corolla")  # создали объект my_car класса Car
```
### Результат.

![Меню](https://github.com/zlatash05/software-engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/images/lab1.png)

### Выводы
Создали класс “Car” с атрибутами производитель и модель.

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:  # создали класс Car
    def __init__(self, make, model):  # определили конструктор класса
        self.make = make  # установили атрибут make 
        self.model = model  # установили атрибут model 

    def drive(self):  # создали метод drive
        print(f"Driving the {self.make} {self.model}")  # выводим сообщение о вождении

my_car = Car("Toyota", "Corolla")  # создали объект 
my_car.drive()  # вызвали метод drive 
```
### Результат.

![Меню](https://github.com/zlatash05/software-engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/images/lab2.png)

### Выводы
добавили метод drive


## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:  # создали класс Car
    def __init__(self, make, model):  # определили конструктор класса
        self.make = make  # установили атрибут make 
        self.model = model  # установили атрибут model 

    def drive(self):  # создали метод drive
        print(f"Driving the {self.make} {self.model}")  # выводим сообщение о вождении

my_car = Car("Toyota", "Corolla")  # создали объект
my_car.drive()  # вызвали метод drive 

class ElectricCar(Car):  # создали класс ElectricCar, наследующий от Car
    def __init__(self, make, model, battery_capacity):  # определили конструктор
        super().__init__(make, model)  # вызвали конструктор родительского класса
        self.battery_capacity = battery_capacity  # установили атрибут 

    def charge(self):  # создали метод charge
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")  # вывели сообщение о зарядке

my_electric_car = ElectricCar("Tesla", "Model S", 75)  # создали объект ElectricCar
my_electric_car.drive()  # вызвали унаследованный метод drive
my_electric_car.charge()  # вызвали метод charge
```
### Результат.

![Меню](https://github.com/zlatash05/software-engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/images/lab3.png)

### Выводы
Создали новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи


## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании.Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.


```python
class Car:  # создали класс Car
    def __init__(self, make, model):  # определили конструктор класса
        self._make = make  # установили защищенный атрибут 
        self.__model = model  # установили приватный атрибут 

    def drive(self):  # создали метод drive
        print(f"Driving the {self._make} {self.__model}")  # выводим сообщение о вождении

my_car = Car("Toyota", "Corolla")  # создали объект 

print(my_car._make)  # обратились к защищенному атрибуту 
my_car.drive()  # вызвали метод drive 
```
### Результат.

![Меню](https://github.com/zlatash05/software-engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/images/lab4.png)

### Выводы
добавили инкапсуляцию, сделав атрибуты приватными


## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.


```python
class Shape:  # создали базовый класс Shape
    def area(self):  # объявили метод area
        pass  # оставили заглушку

class Rectangle(Shape):  # создали класс Rectangle
    def __init__(self, width, height):  # определили конструктор
        self.width = width  # установили ширину
        self.height = height  # установили высоту

    def area(self):  # переопределили метод area
        return self.width * self.height  # вычислили площадь прямоугольника

class Circle(Shape):  # создали класс Circle, наследующий от Shape
    def __init__(self, radius):  # определили конструктор
        self.radius = radius  # установили радиус

    def area(self):  # переопределили метод area
        return 3.14 * self.radius * self.radius  # вычислили площадь круга

my_rectangle = Rectangle(5, 4)  # создали объект прямоугольника
my_circle = Circle(5)  # создали объект круга

print(my_rectangle.area())  # вывели площадь прямоугольника
print(my_circle.area())  # вывели площадь круга
```
### Результат.

![Меню](https://github.com/zlatash05/software-engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/images/lab5.png)

### Выводы
добавили два класса наследника, переопределили метод area, применив полиморфизм


## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Phone:
    def __init__(self, battery):
        self.battery = battery

    def get_battery(self):
        return self.battery

my_phone = Phone(80)
print(my_phone.get_battery())
```
### Результат.

![Меню](https://github.com/zlatash05/software-engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/images/sam1.png)

### Выводы

1. `class Phone:` создаем класс Phone
2. `def __init__(self, battery):` конструктор класса
3. `my_phone = Phone(80)` создаем объект класса
  
## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Phone:
    def __init__(self, battery, brand):
        self.battery = battery
        self.brand = brand

    def get_battery(self):
        return self.battery

    def get_brand(self):
        return self.brand

my_phone = Phone(80, "Samsung")
print(my_phone.get_battery())
print(my_phone.get_brand())
```
### Результат.

![Меню](https://github.com/zlatash05/software-engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/images/sam2.png)

### Выводы
1. `def __init__(self, pages, cover_color):`  - добавили атрибут бренд телефона
2. `def get_brand(self): ` - добавили метод get_brand
  
## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.


```python
class Phone:
    def __init__(self, battery):
        self.battery = battery
        self.type = "обычный телефон"

    def get_battery(self):
        return self.battery

    def get_type(self):
        return self.type

class Smartphone(Phone):
    def __init__(self, battery):
        super().__init__(battery)
        self.type = "смартфон"

my_phone = Phone(50)
my_smartphone = Smartphone(100)

print(my_phone.get_type())
print(my_smartphone.get_type())
```
### Результат.

![Меню](https://github.com/zlatash05/software-engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/images/sam3.png)

### Выводы

1. `class Smartphone(Phone)` - создали класс Smartphone, наследующий от Phone
2. `super().__init__(battery)` - передаем аргумент в конструктор родительского класса
3. `self.type = "смартфон" ` - переопределяем voice 
4. `my_smartphone = Smartphone(100)` - создаем объект класса Phone
  
## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Phone:
    def __init__(self, battery):
        self.__battery = battery
        self.type = "обычный телефон"

    def get_battery(self):
        return self.__battery

    def set_battery(self, new_battery):
        if 0 <= new_battery <= 100:
            self.__battery = new_battery
        else:
            print("Заряд должен быть от 0 до 100%")

    def get_type(self):
        return self.type

class Smartphone(Phone):
    def __init__(self, battery):
        super().__init__(battery)
        self.type = "смартфон"

my_phone = Phone(50)
my_smartphone = Smartphone(100)

print(my_phone.get_type())
print(my_smartphone.get_type())

print(my_phone.get_battery())
my_phone.set_battery(75)
print(my_phone.get_battery())
my_phone.set_battery(150)
```
### Результат.

![Меню](https://github.com/zlatash05/software-engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/images/sam4.png)

### Выводы

1. `self.__battery = battery` делаем приватным
2. `def get_battery(self):` добавляем геттер
3. `def set_battery(self, new_battery):` добавляем сеттер
  
## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Phone:
    def __init__(self, battery):
        self.__battery = battery

    def get_battery(self):
        return self.__battery

    def set_battery(self, new_battery):
        if 0 <= new_battery <= 100:
            self.__battery = new_battery
        else:
            print("Заряд должен быть от 0 до 100%")

    def make_sound(self):
        return "звонит"


class Smartphone(Phone):
    def __init__(self, battery):
        super().__init__(battery)

    def make_sound(self):
        return "играет мелодия"


class Tablet(Phone):
    def __init__(self, battery):
        super().__init__(battery)

    def make_sound(self):
        return "издает звуковой сигнал"


devices = [Phone(50), Smartphone(100), Tablet(80)]

for device in devices:
    print(device.make_sound())
```

### Результат.

![Меню](https://github.com/zlatash05/software-engineering/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/images/sam5.png)

### Выводы

 Smartphone переопределяет метод make_sound() родительского класса Phone, таким образом получается полиморфизм

## Общие выводы по теме
Базово освоила работу в ооп на python, познакомилась с классами, их конструкторами, полиморфизмом и инкапсуляцией, наследованием
