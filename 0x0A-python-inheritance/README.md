0x0A. Python - Inheritance

In Python, inheritance is a mechanism that allows a class to inherit attributes and methods from another class. The class from which attributes and methods are inherited is called the superclass, base class, or parent class. The class that inherits these attributes and methods is called the subclass or derived class.

Inheritance is defined using the following syntax:

class SubClass(BaseClass):
    # Subclass definition


The SubClass is the name of the subclass, and BaseClass is the name of the superclass that the subclass is inheriting from. The subclass can access and use all the attributes and methods of the superclass, and it can also define its own additional attributes and methods.

Here's an example that demonstrates inheritance:

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof!"


class Cat(Animal):
    def sound(self):
        return "Meow!"


dog = Dog("Buddy")
print(dog.name)     # Output: Buddy
print(dog.sound())  # Output: Woof!

cat = Cat("Whiskers")
print(cat.name)     # Output: Whiskers
print(cat.sound())  # Output: Meow!


In this example, the Animal class is the superclass, and the Dog and Cat classes are subclasses. The subclasses inherit the name attribute and the sound() method from the Animal superclass. Each subclass overrides the sound() method with its own implementation.

The dog object is an instance of the Dog class, and the cat object is an instance of the Cat class. They can access both the inherited attributes and methods as well as the ones specific to their respective classes.

Inheritance allows for code reuse, promotes modularity and extensibility, and facilitates the concept of polymorphism, where different objects can be treated uniformly based on their shared superclass.


A superclass, baseclass, or parentclass is a class that is extended or inherited by another class. It serves as the base for the derived classes and provides common attributes and methods that can be shared among the subclasses.

A subclass is a class that inherits attributes and methods from a superclass or baseclass. It extends or specializes the functionality of the superclass and may add additional attributes and methods or override existing ones.

To list all attributes and methods of a class or instance in Python, you can use the built-in dir() function. For example:

class MyClass:
    attribute = "Hello"

    def method(self):
        print("World")

my_instance = MyClass()

# List attributes and methods of the class
print(dir(MyClass))

# List attributes and methods of the instance
print(dir(my_instance))


Instances can have new attributes at any time. In Python, attributes can be added dynamically to an instance by assigning a value to a new attribute name. For example:

my_instance = MyClass()
my_instance.new_attribute = "New Value"


To inherit a class from another, you can specify the base class in parentheses after the class name in the class definition. For example:

class SubClass(BaseClass):
    # Subclass definition


To define a class with multiple base classes in Python, you can use multiple inheritance. You specify the base classes separated by commas in parentheses after the class name. For example:

class SubClass(BaseClass1, BaseClass2):
    # Subclass definition


The default class that every class inherits from in Python is the object class. If no explicit superclass is specified, the class automatically inherits from object. In Python 3, all classes are new-style classes, which implicitly inherit from object.

To override a method or attribute inherited from the base class, you can redefine the method or attribute in the subclass with the same name. The subclass implementation will be used instead of the base class implementation when the method or attribute is accessed through the subclass.

Subclasses inherit all attributes and methods from their superclass(es). They can access and use these inherited attributes and methods as if they were defined within the subclass itself.

The purpose of inheritance is to enable code reuse and promote modular design. It allows you to define a hierarchy of classes, where subclasses inherit and extend the functionality of their superclasses. Inheritance helps to organize and structure code, promote code reuse, and facilitate polymorphism.

In Python, you can use the following built-in functions:

isinstance(obj, class) checks if an object obj is an instance of a given class or any of its subclasses.
issubclass(cls, class) checks if a class cls is a subclass of a given class.
type(obj) returns the type or class of an object obj.
super() returns a temporary object of the superclass, which allows you to call its methods.

These built-in functions are useful for checking relationships between classes and objects and for obtaining information about class hierarchies.
