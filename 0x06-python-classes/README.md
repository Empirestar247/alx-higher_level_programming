Python - Classes and Objects

OOP (Object-Oriented Programming): OOP is a way of organizing and structuring code by treating objects as the main building blocks. It focuses on creating objects that have properties (attributes) and can perform actions (methods).

"First-class everything": In programming, "first-class" means that something is treated as a fundamental element. In OOP, it means that objects are treated as important entities that can be manipulated and used just like any other programming element.

Class: A class is like a blueprint or template for creating objects. It defines the attributes (properties) and behaviors (methods) that objects of that class will have.

Object and Instance: An object is a specific instance created based on a class. It is like a real thing that exists and can have its own unique values for attributes. An instance is another word for an object, emphasizing that it is a specific occurrence of a class.

Difference between Class and Object/Instance: A class is a blueprint or template that describes how objects should be created and what properties and behaviors they should have. An object or instance is an actual occurrence of a class, created based on that blueprint.

Attribute: An attribute is a characteristic or property of an object. It describes something about the object, such as its color, size, or name.

Public, Protected, and Private Attributes: These are ways to control access to attributes. Public attributes can be accessed and modified by anyone. Protected attributes are meant to be accessed only within the class or its subclasses. Private attributes are meant to be accessed only within the class itself.

"self": "self" is a reference to the object itself within a class. It allows the object to access its own attributes and methods.

Method: A method is a function defined within a class that can be called on an object of that class. It represents an action or behavior that the object can perform.

"init" method: The "init" method is a special method in Python that is automatically called when an object is created from a class. It is used to initialize the object's attributes and perform any necessary setup.

Data Abstraction, Data Encapsulation, and Information Hiding: These concepts involve organizing and protecting data within objects. Data abstraction means representing only essential information and hiding unnecessary details. Data encapsulation means bundling data and the methods that operate on that data together in a class. Information hiding means controlling access to data and methods to prevent direct manipulation from outside the class.

Property: A property is a special attribute that allows controlled access and modification. It uses special methods called getters and setters to define how the attribute can be accessed or changed.

Difference between Attribute and Property in Python: An attribute is a characteristic or property of an object, while a property is a special kind of attribute that provides controlled access and modification through getter and setter methods.

Pythonic way to write getters and setters: In Python, properties can be used to define getters and setters for attributes. This allows accessing and modifying attributes in a controlled manner using the dot notation.

Dynamically creating new attributes for existing instances: In Python, you can dynamically create new attributes for existing instances by assigning a value to a new attribute using the instance name followed by a dot and the attribute name.

Binding attributes to objects and classes: Attributes can be bound to objects by assigning values directly to them using the dot notation. Attributes can also be bound to classes by defining them within the class definition, outside of any methods.

"dict" of a class or instance: "dict" is a special attribute in Python that contains a dictionary

of all the attributes (and their values) defined for a class or an instance of a class.

How Python finds attributes: When accessing an attribute of an object or class, Python first looks for it within the object's own namespace (attributes bound to the object itself). If not found, it searches in the class's namespace, and if still not found, it looks in the namespaces of any superclasses.

Using getattr function: The getattr function is used to dynamically retrieve the value of an attribute from an object. It takes the object and the attribute name as arguments and returns the value of that attribute if it exists.

