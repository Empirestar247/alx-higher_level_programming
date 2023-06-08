 Python - import & modules
 In Python, modules are separate files that contain Python code and can be imported into other Python programs. They allow you to organize and reuse code effectively. To import a module, you can use the `import` statement followed by the name of the module.

Here's an example of importing a module called `math` and using one of its functions:

```python
import math

# Using a function from the math module
print(math.sqrt(25))  # Output: 5.0
```

In this example, the `math` module is imported using the `import` statement. The `math.sqrt()` function is then used to calculate the square root of 25, which is printed to the console.

You can also import specific items from a module using the `from` keyword. Here's an example:

```python
from math import sqrt

# Using the sqrt function directly
print(sqrt(25))  # Output: 5.0
```

In this case, only the `sqrt` function is imported from the `math` module. As a result, you can use the function directly without referencing the module name.

Additionally, you can import a module and assign it an alias using the `as` keyword. Here's an example:

```python
import math as m

# Using the math module with an alias
print(m.sqrt(25))  # Output: 5.0
```

In this example, the `math` module is imported and assigned the alias `m`. This allows you to use the `sqrt` function as `m.sqrt()`.

Python provides a rich set of built-in modules for various purposes, such as `random` for random number generation, `datetime` for working with dates and times, and `os` for interacting with the operating system. Additionally, you can create your own modules by defining Python code in separate files and importing them into your programs.


Python programming is awesome for several reasons:

1. Readability: Python emphasizes clean and readable code, making it easier to understand and maintain.

2. Simplicity: Python has a simple and intuitive syntax, making it easy to learn and use, especially for beginners.

3. Large standard library: Python comes with a vast standard library that provides ready-to-use modules for various tasks, reducing the need for additional external dependencies.

4. Community and ecosystem: Python has a large and active community of developers who contribute to open-source projects, provide support, and create libraries and frameworks for various domains.

5. Cross-platform compatibility: Python programs can run on different platforms without significant modifications, allowing for easy portability.

To import functions from another file in Python, you can use the `import` statement followed by the module or file name. Here's an example:

```python
# Assuming the file "my_module.py" contains a function called "my_function"
import my_module

# Using the imported function
my_module.my_function()
```

In this example, the `my_module` file is imported, and you can access its functions using the dot notation (`my_module.my_function()`).

If you only want to import specific functions from a module, you can use the `from` keyword. Here's an example:

```python
from my_module import my_function

# Using the imported function directly
my_function()
```

In this case, only the `my_function` is imported, and you can use it directly without referencing the module name.

To create a module in Python, you can simply create a new Python file with the desired code. The file's name will serve as the module name. For example, if you create a file called `my_module.py`, you can define functions, variables, and classes inside it. Then, you can import and use these definitions in other Python scripts.

The `dir()` function in Python returns a list of names in the current namespace or the attributes of an object if provided. It can be used to explore the available functions, classes, and variables within a module or an object. Here's an example:

```python
import math

# Get the list of attributes in the math module
print(dir(math))
```

The `dir(math)` statement will print a list of attributes available in the `math` module, including functions like `sqrt`, `sin`, and constants like `pi`.

To prevent code in your script from being executed when imported, you can use the `__name__` variable. The `__name__` variable is a built-in variable in Python that holds the name of the current module.

By checking the value of `__name__`, you can determine if the script is being run as the main program or if it is being imported as a module. Here's an example:

```python
# Code that should only run when the script is the main program
if __name__ == "__main__":
    # Your main program code here
    print("This code will only execute when the script is run directly")
```

When the script is run directly (as the main program), the `__name__` variable will be set to `"__main__"`. If the script is imported as a module, the `__name__` variable will have the name of the module instead.

To use command-line arguments with your Python programs, you can use the `sys.argv` list provided by the `sys` module. The `sys.argv` list contains the command-line arguments passed to the script.

Here's a simple example:

```python
import sys

# Get command-line arguments
arguments = sys.argv

# Print each argument
for arg in arguments:
    print(arg)
```

When you run the script from the command line, the `sys.argv` list will contain the command-line arguments. By convention, the first element in the list (`sys.argv[0]`) is the script's filename itself.

For example, if you run the following command:

```
python my_script.py arg1 arg2 arg3
```

The `sys.argv` list will be `['my_script.py', 'arg1', 'arg2', 'arg3']`. You can access the command-line arguments by indexing into the list.

Here's an example that demonstrates using command-line arguments to perform a simple calculation:

```python
import sys

# Get command-line arguments
arguments = sys.argv

# Check if the correct number of arguments is provided
if len(arguments) != 3:
    print("Usage: python my_script.py number1 number2")
    sys.exit(1)  # Exit the script with a non-zero status code

# Get the numbers from the arguments
number1 = int(arguments[1])
number2 = int(arguments[2])

# Perform a calculation
result = number1 + number2

# Print the result
print("Result:", result)
```

In this example, the script expects two command-line arguments, which are interpreted as numbers. It performs a calculation by adding the two numbers and then prints the result.

If the script is run with incorrect usage (e.g., missing or extra arguments), it will display a usage message and exit with a non-zero status code using `sys.exit(1)`.

To run this script, you would execute the following command:

```
python my_script.py 10 20
```

The output will be:

```
Result: 30
```

Note that command-line arguments are always passed as strings, so you might need to convert them to the appropriate data types (e.g., integers).


You can also use the `argparse` module, which provides a more flexible and powerful way to handle command-line arguments. It allows you to define the expected arguments, their types, default values, and provides built-in help messages.

Here's an example of using `argparse` to handle command-line arguments:

```python
import argparse

# Create the argument parser
parser = argparse.ArgumentParser(description="A simple program to perform a calculation.")

# Add the command-line arguments
parser.add_argument("number1", type=int, help="The first number")
parser.add_argument("number2", type=int, help="The second number")

# Parse the arguments
args = parser.parse_args()

# Perform the calculation
result = args.number1 + args.number2

# Print the result
print("Result:", result)
```

In this example, the `argparse` module is used to create an argument parser. The `add_argument` method is used to define the expected arguments. The `type` parameter is used to specify the data type of the argument, and the `help` parameter provides a description of the argument for the built-in help message.

The `parse_args` method is then called to parse the command-line arguments and store them in the `args` object. You can access the argument values using dot notation (`args.number1`, `args.number2`).

If you run the script with incorrect usage or use the `-h` or `--help` flag, it will display an automatically generated help message with the argument descriptions.

For example, you can run the script with the following command:

```
python my_script.py 10 20
```

The output will be:

```
Result: 30
```

Using `argparse` provides more robust argument handling and allows you to easily extend your program with more complex argument requirements.
