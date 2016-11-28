## Класс
**Класс** – это абстрактный тип данных. С помощью класса описывается некоторая сущность (ее характеристики и возможные действия). Например, класс может описывать студента, автомобиль и т.д. Описав класс, мы можем создать его экземпляр – объект. **Объект** – это уже конкретный представитель класса. **Описание класса одно, а объектов класса может быть много.**

_Пример:_

Допустим, нам в программе необходимо работать со странами. Страна – это абстрактное понятие. У нее есть такие характеристики, как название, население, площадь, флаг и другое. Для **описания** такой страны будет использоваться **класс** с соответствующими полями данных. Такие страны, как **США и Англия** будут уже **объектами – конкретными представителями типа страна**.

### Поля

Это **свойства**, которые есть у **объектов**. 

Например, у каждой страны есть название, столица и ВВП. 

### Методы

Класс может содержать методы, которые связаны логически с классом. 

Например, ВВП страны может измениться. 

### Python
Класс на языке Python выглядит следующим образом:
```python
class Country:
    name = ""
    capital = ""
    gcd = 0
 ```
Создание объекта класса похоже на то, как будто мы делаем вызов функций:
  ``cntr = Country()``
  
Будет создан пустой объект `cntr`. Если мы хотим, чтобы при создании выполнялись какие-то действия (например, инициализация начальных значений), нужно определить конструктор, который будет вызываться автоматически.
Обычный конструктор выглядит вот так:
```python
      def __init__(self):
        name = "Unknown"
        self.capital = "Unknown"
        self.gcd = 0
```
Это похоже на описание метода, но в данном случае название (`__init__`) не может меняться, которое одинаковое для всех классов, и есть обязательный аргумент `self`.  


   
   Конструтор может иметь параметры, что очень полезно. Например, мы можем сразу задать начальные значения:
  ```python
      def __init__(self, name, capital, gcd):
        self.name = name
        self.capital = capital
        self.gcd = gcd
   ```
   
   #### Self
   Первым аргументом каждого метода класса, включая `__init__`, всегда является текущий экземпляр класса. Общепринято всегда называть этот аргумент `self`. В методе `__init__ self` ссылается на только что созданный объект, в других методах — на экземпляр класса, для которого метод вызывается. Хотя и необходимо явно указывать `self` при определении метода, вы его не указываете, когда вызываете метод; Python добавит его автоматически.
 
   
   
   Добавим методы
 ```python
class Country:
    name = ""
    capital = ""
    gcd = 0

    def __init__(self, name, capital, gcd):
        self.name = name
        self.capital = capital
        self.gcd = gcd

    def change_GCD(self, newGcd):
        self.gcd = newGcd

    def print_gcd(self):
        print self.name + ": " + str(self.gcd)
   ```
   
 И поиграемся со странами
 
```python
# Создадим страны
usa = Country('USA', 'Washington', 16)
eng = Country('England', 'London', 2)

# Посмотрим что получилось
usa.print_gcd()  # USA: 16
eng.print_gcd()  # England: 2

# Изменим ВВП и посмотрим на изменения
eng.change_GCD(50)  # self не пишем

usa.print_gcd()  # USA: 16, не поменялось
eng.print_gcd()  # England: 50, изенилось, т.к. именно у этого объекта мы вызывали метод
```