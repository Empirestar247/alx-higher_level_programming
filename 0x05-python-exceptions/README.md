Python - Exceptions

In Python, exceptions are used to handle errors and exceptional situations that may occur during the execution of a program. When an error occurs, an exception is raised, and if it is not handled properly, it can cause the program to terminate.

Example:
try:
    # Code that might raise an exception
    result = 10 / 0  # Raises a ZeroDivisionError
except ZeroDivisionError:
    # Code to handle the specific exception
    print("Error: Division by zero")

In the example above, the code inside the try block attempts to divide 10 by 0, which raises a ZeroDivisionError. To handle this exception, we use the except block with the specific exception type (ZeroDivisionError) that we want to handle. In this case, we print an error message indicating the division by zero.

Python provides several built-in exception types that can be used to handle different types of errors. Some common built-in exceptions include TypeError, ValueError, FileNotFoundError, and IndexError, among others.

It's also possible to use multiple except blocks to handle different exceptions separately or use a single except block without specifying the exception type to handle any exception that occurs. Additionally, the try-except statement can be followed by an optional else block, which is executed if no exceptions are raised, and a finally block, which is always executed regardless of whether an exception occurs or not.

try:
    # Code that might raise an exception
    result = some_function()
except ValueError:
    # Code to handle a ValueError
    print("ValueError occurred")
except FileNotFoundError:
    # Code to handle a FileNotFoundError
    print("FileNotFoundError occurred")
except:
    # Code to handle any other exception
    print("An exception occurred")
else:
    # Code to execute if no exceptions occurred
    print("No exceptions")
finally:
    # Code that always executes
    print("Finally block")


In the example above, we have multiple except blocks to handle specific exceptions, followed by an else block that executes if no exceptions occur. Finally, we have a finally block that always executes, regardless of whether an exception occurred or not.

Handling exceptions allows you to gracefully recover from errors, provide appropriate error messages to users, and take alternative actions to prevent program termination.

Difference between errors and exceptions:
In Python, the terms "errors" and "exceptions" are often used interchangeably, but they have slightly different meanings.

Errors: Errors are generally referred to as mistakes or issues in a program that prevent it from running or producing the desired output. These errors can occur due to syntax mistakes, logical errors, or issues with system resources.

Exceptions: Exceptions, on the other hand, are events that occur during the execution of a program that disrupt the normal flow of the program. Exceptions are a type of error, but they are specifically related to runtime errors or exceptional conditions that can be handled by the program.

Exceptions are objects that are raised (or thrown) when an exceptional situation occurs. They represent the occurrence of an error or an exceptional condition that needs to be handled.

How to use exceptions:
In Python, exceptions are used to handle runtime errors or exceptional conditions gracefully. They allow you to catch and handle specific types of errors instead of letting the program terminate abruptly. You can use the try-except statement to catch and handle exceptions.


try:
    # Code that might raise a ValueError
    # ...
except ValueError as e:
    # Code to handle the ValueError
    print("ValueError occurred:", e)

In the example above, if a ValueError occurs within the try block, the corresponding except block is executed. The as e part allows you to access the exception object itself, so you can access its properties or display a specific error message.

Purpose of catching exceptions:
The main purpose of catching exceptions is to handle exceptional situations or errors gracefully without causing the program to terminate. By catching exceptions, you can provide alternative paths or actions when errors occur, preventing the program from crashing.

Catching exceptions allows you to:

Provide meaningful error messages to users or log the errors for debugging purposes.
Take appropriate recovery actions, such as retrying an operation or using default values.
Prevent the program from terminating abruptly and allow it to continue executing.
How to raise a built-in exception:
In Python, you can raise a built-in exception explicitly using the raise statement. The raise statement allows you to raise a specific exception of your choice.

def divide(x, y):
    if y == 0:

