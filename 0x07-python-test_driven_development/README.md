 Python - Test-driven development

An interactive test is a type of test that allows the user to interact with the program or system being tested. It typically involves providing input and observing the corresponding output or behavior. Interactive tests are useful for verifying the functionality and usability of software, as they simulate real-world user interactions.

Tests are important because they help ensure the correctness, reliability, and quality of software. They provide a systematic way to verify that a program behaves as intended and help catch bugs and errors early in the development process. By running tests regularly, developers can detect and fix issues before they impact users.

To write Docstrings for creating tests:

Begin with a concise summary of the test's purpose and functionality.
Describe the input parameters and their expected types.
Explain the expected behavior or outcome of the test.
Include any relevant examples or sample inputs and outputs.
Mention any preconditions or assumptions required for the test.

Documentation for each module and function is essential for understanding how to use them correctly. Here are some tips for writing module and function documentation:

Provide an overview of the module or function's purpose and functionality.
Explain the input parameters, their types, and any constraints or requirements.
Describe the return value or side effects of the function.
Include examples or code snippets to illustrate usage.
Document any exceptions that can be raised and their meanings.
Mention any dependencies or external requirements.
Consider including usage notes, best practices, or additional resources.

Basic option flags for creating tests may vary depending on the testing framework or tool you're using. However, some common options include:

-v or --verbose: Displays detailed information about each test case, including pass/fail status and any diagnostic messages.
-q or --quiet: Suppresses or reduces the amount of output produced by the test runner.
-k EXPRESSION or --keyword EXPRESSION: Allows you to run specific tests that match a given keyword or expression.
-x or --stop: Stops the test execution after the first failure.
-s or --capture=no: Disables output capturing, allowing print statements and other output to be displayed in real-time.
--failfast: Stops the test execution immediately after the first failure without running any remaining tests.

To find edge cases, you need to consider inputs or scenarios that are at the extremes or boundaries of the expected range. These are situations where the behavior of the program may differ or be more prone to errors. Some strategies to find edge cases include:

Identifying the minimum and maximum valid values for input parameters.
Testing with empty or null values if applicable.
Trying inputs that are just below or above limits.
Considering special cases, such as zero, negative numbers, or extreme values.
Evaluating edge cases based on the context and requirements of the software being tested.
Exploring combinations of multiple inputs or parameters that could lead to unusual or unexpected behavior.

By testing with edge cases, you can increase the coverage of your tests and uncover potential issues that might not be apparent with typical or common inputs.

Testing Python: Understanding Doctest and Unittest:

Testing is crucial in the software development phase. It helps ensure easy debugging, agile code, and enhanced reusability. Performing tests that cover all use cases helps prevent a codebase from breaking — minimizing exposure to vulnerabilities. Python has two main testing frameworks that developers can use, doctest and unittest.

What is Doctest?
Doctest is an inbuilt test framework that comes bundled with Python by default. The doctest module searches for code fragments that resemble interactive Python sessions and runs those sessions to confirm they operate.

The doctest module looks for sequences of prompts in a docstring, re-executes the extracted command, and compares the output with the command’s input given in the docstrings test example.

The default action when running doctests is not to show the output when a test passes. However, we can change this in the doctest runner options. In addition, doctest’s integration with the Python unittest module enables us to run doctests as standard unittest test cases.

What is Unittest?
Unittest test case runners allow more options when running tests, like reporting test statistics such as tests that passed and failed.

Unittest uses methods created in classes to manage tests. It has support for automation, setup, and shutdown code when testing. Unittest has several rich, in-built features that are unavailable in doctest, including generators and group fixture managers like setUp and tearDown.

Since unittest follows the object-oriented method, it’s more suitable for testing class-based methods in a non-production environment. Continuous delivery tools such as Jenkins or Travis CI work better for production environments.
We’ll create a real-world example in the following sections, some code with customer information and discounts, and test it using doctest and unittest.


