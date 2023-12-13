# class Sample():
#     pass  #to not do anything
#
# x = Sample()
# print(type(x))

class Dog:
    # Class object Attribute
    species = "mammal"

    # A special method -needed when creating objects.
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


my_dog = Dog(breed="Husky", name="Bandit")


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    # Method  - Allow us to preform actions based off the attributes of an object
    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, radius):
        self.radius = radius


myc = Circle(3)
# Change attributes of an object
# myc.name = 100
myc.set_radius(4)


# print(myc.area())


# Inheritance
class Animal():
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):  # inheriting a class inside this class
    def __init__(self):
        # Animal.__init__(self)
        print("Dog created")

    # You can override previous methods
    def eat(self):
        print("Dog eating")


mydog = Dog()
mydog.whoAmI()
mydog.eat()


# Special Methods __special method__
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Special Methods
    def __str__(self):
        return "Title: {} Author: {} Pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("Book deleted")


b = Book("Bob", "Betty", 200)
# print(b)
# print(len(b))   # Goes into the object and checks what you've defined

# To delete an object that's been created.
del b


