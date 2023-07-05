An object is a fundamental concept in programming that represents a particular instance of a class. It is a data structure that contains both data (attributes) and code (methods) to manipulate that data.

A class is a blueprint or template for creating objects. It defines the characteristics and behaviors that objects of that class will have. An object, also known as an instance, is a specific realization of a class.

The main difference between a class and an object is that a class is a definition or a blueprint, while an object is an instance or a specific occurrence of that class.

An immutable object is one whose state (data) cannot be modified after it is created. Immutable objects are fixed and cannot be changed. Examples of immutable objects in Python include numbers (integers, floats), strings, and tuples.

On the other hand, a mutable object can be modified or changed after it is created. Mutable objects have the ability to be updated, added to, or removed from. Examples of mutable objects in Python include lists, dictionaries, and sets.

A reference in programming refers to a value that points to the memory location of an object. It allows us to access and work with objects indirectly by referring to their memory addresses.

An assignment is the process of giving a value to a variable. It associates a name (variable) with a value, allowing us to store and manipulate data in our program.

An alias refers to two or more variables that are assigned to the same memory location. Modifying one variable will affect the other since they point to the same object.

To check if two variables are identical, you can use the is operator in Python. If two variables are identical, it means they refer to the exact same object in memory.

To determine if two variables are linked to the same object, you can use the == operator in Python. It compares the values of the variables and returns True if they are equal.

In Python, you can display the memory address (variable identifier) of an object using the id() function. It returns a unique identifier for an object based on its memory address.

Mutable objects can be changed or modified after they are created, while immutable objects cannot be changed once they are created.

Some built-in mutable types in Python include lists, dictionaries, and sets. These types can be modified by adding, removing, or updating elements.

Some built-in immutable types in Python include numbers (integers, floats), strings, and tuples. Once these objects are created, their values cannot be changed.

Python passes variables to functions by using a combination of pass-by-value and pass-by-reference. Immutable objects are passed by value, meaning a copy of the object's value is passed to the function. Mutable objects are passed by reference, meaning the function receives a reference to the original object, allowing modifications to be made directly.

In summary, an object represents a specific instance of a class. A class is a blueprint for creating objects. Immutable objects cannot be changed after creation, while mutable objects can be modified. References are values that point to memory locations of objects. Assignment associates a value with a variable. Aliases refer to multiple variables that share the same memory location. The is operator checks if variables are identical, while the == operator compares their values. The id() function displays the memory address of an object. Python has both mutable and immutable built-in types. Variables are passed to functions either by value (immutable objects) or by reference (mutable objects).


Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a newline character
The first line of all your script files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc

.txt Answer Files
Only one line
No Shebang
All your files should end with a new line
