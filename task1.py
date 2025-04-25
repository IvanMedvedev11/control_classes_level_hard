class Animal:
    def make_sound(self):
        print("Животное издает звук")
class Dog(Animal):
    def make_sound(self):
        print("Собака лает")
class Cat(Animal):
    def make_sound(self):
        print("Кошка мяукает")
animal = Animal()
dog = Dog()
cat = Cat()
for elem in [animal, dog, cat]:
    elem.make_sound()
