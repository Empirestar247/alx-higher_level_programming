0x04. Python - More Data Structures: Set, Dictionary

Python programming is awesome for several reasons:

1. Readability: Python emphasizes code readability with its clean and intuitive syntax, making it easier to write and understand.

2. Versatility: Python can be used for a wide range of applications, including web development, data analysis, artificial intelligence, scientific computing, and more.

3. Large Standard Library: Python comes with a vast standard library that provides numerous modules and functions for various tasks, reducing the need for external dependencies.

4. Third-Party Libraries: Python has a rich ecosystem of third-party libraries, such as NumPy, Pandas, TensorFlow, and Django, which extend its capabilities for specific domains.

5. Easy to Learn: Python's simplicity and readability make it an excellent choice for beginners. It has a gentle learning curve, allowing newcomers to quickly grasp the fundamentals of programming.

Sets in Python:
A set is an unordered collection of unique elements in Python. It is defined by enclosing comma-separated values within curly braces `{}` or by using the `set()` function.

Example:

fruits = {'apple', 'banana', 'orange'}
print(fruits)  # Output: {'banana', 'apple', 'orange'}
```

Common set methods and their usage:
- `add(element)`: Adds an element to the set.
- `remove(element)`: Removes an element from the set. Raises an error if the element doesn't exist.
- `discard(element)`: Removes an element from the set. Does nothing if the element doesn't exist.
- `pop()`: Removes and returns an arbitrary element from the set.
- `clear()`: Removes all elements from the set.
- `union(other_set)`: Returns a new set containing all elements from both sets.
- `intersection(other_set)`: Returns a new set containing common elements of both sets.
- `difference(other_set)`: Returns a new set with elements present in the first set but not in the second set.
- `symmetric_difference(other_set)`: Returns a new set with elements present in either of the sets but not in both.

Sets vs. Lists:
Use sets when you need to store a collection of unique elements without any specific order. If the order or duplicates matter, and you need to access elements by their index, then use a list.

Iterating over a set:
You can iterate over a set using a `for` loop. Each iteration will provide one element from the set.

Example:
fruits = {'apple', 'banana', 'orange'}
for fruit in fruits:
    print(fruit)

Example:
student = {'name': 'John', 'age': 20, 'major': 'Computer Science'}
for key in student:
    print(key, student[key])

# Output:
# name John
# age 20
# major Computer Science


Dictionaries in Python:
A dictionary is an unordered collection of key-value pairs. It is defined using curly braces `{}` and consists of comma-separated `key: value` pairs.

Example:
student = {'name': 'John', 'age': 20, 'major': 'Computer Science'}
print(student)  # Output: {'name': 'John', 'age': 20, 'major': 'Computer Science'}


Dictionaries vs. Lists or Sets:
Use dictionaries when you need to associate values with unique keys and want to access them using those keys. If you only need an ordered collection of elements, use a list. If you need an unordered collection of unique elements, use a set.

Key in a dictionary:
A key in a dictionary is a unique identifier that is used to access the corresponding value associated with it. Keys must be immutable objects, such as strings, numbers, or tuples.

Iterating over a dictionary:
You can iterate over a dictionary using a `for` loop. Each iteration will provide one key from the dictionary, and you can use that key to access the corresponding value.

Example:

student = {'name': 'John', 'age'}

Example:
student = {'name': 'John', 'age': 20, 'major': 'Computer Science'}
print(student['name'])  # Output: 'John'


Lambda function:
A lambda function, also known as an anonymous function, is a small and anonymous function without a name. It is defined using the `lambda` keyword and can take any number of arguments but can only have one expression. Lambda functions are often used when you need a simple function for a short period and don't want to define a separate function.

Example:
```python
addition = lambda a, b: a + b
result = addition(5, 3)
print(result)  # Output: 8
```

Map, Reduce, and Filter functions:
These are built-in functions in Python used for functional programming.

- Map: The `map()` function applies a given function to each element of an iterable and returns an iterator of the results.

Example:

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

- Reduce: The `reduce()` function, which is part of the `functools` module, applies a function of two arguments cumulatively to the items of an iterable, reducing it to a single value.

Example:

from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
```

- Filter: The `filter()` function constructs an iterator from elements of an iterable for which a given function returns true.

Example:

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
```

These functions provide concise and powerful ways to process and manipulate data in Python. They are often used in conjunction with lambda functions to create expressive and functional-style code.


