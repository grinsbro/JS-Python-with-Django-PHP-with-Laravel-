class Animal():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print("Я животное: ", self.name)


class Dog(Animal): # Чтобы присвоить наследование, в скобках пишется класс, от которого наследуется
    
    def __init__(self, name, age, silaLay):
        super().__init__(name, age) # Таким образом наследуется конструктор
        self.silaLay = silaLay

    def printInfo(self):
        print('Я собака', self.silaLay, 'это моя сила лая')


# dog1 = Dog('Пэс', 20, 89)

# dog1.printInfo()
# print(isinstance(dog1, Dog)) # Так проверяется принадлежность объекта к классу

class Work():

    def work(self):
        print('Класс Work - Работа')

class Study():

    def study(self):
        print('Класс Study - Учеба')

class Student(Work,Study): # это множественное наследование
    pass

student1 = Student()
student1.work()
student1.study()