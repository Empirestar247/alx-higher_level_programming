## # Project Title: Python Object-Relational Mapping (ORM) with MySQL

## Introduction
This project explores the world of Python programming, focusing on the power of Object-Relational Mapping (ORM) with MySQL. It provides an alternative approach to working with databases, allowing you to interact with data using Python objects instead of writing raw SQL queries. In this README, we'll cover the key concepts and requirements for this project.

## Why Python Programming is Awesome
Python is awesome for its simplicity, readability, and extensive libraries. With Python, you can achieve complex tasks with fewer lines of code, making it a great choice for various programming challenges, including database interactions.

## How to Connect to a MySQL Database from a Python Script
You can establish a connection to a MySQL database from your Python script using the `MySQLdb` library. This connection allows you to interact with the database and perform various operations like querying and inserting data.

## How to SELECT Rows in a MySQL Table from a Python Script
In the traditional approach, you can use the `MySQLdb` library to execute SQL queries and retrieve rows from a MySQL table. This involves writing SQL statements to fetch the data you need.

## How to INSERT Rows in a MySQL Table from a Python Script
Similarly, you can use `MySQLdb` to insert rows into a MySQL table. This involves creating SQL `INSERT` statements and executing them to add data to the database.

## What ORM Means
ORM stands for Object-Relational Mapping. It's a technique that allows you to map Python classes to database tables, eliminating the need to write raw SQL queries. With an ORM like SQLAlchemy, you work with Python objects, and the ORM handles the underlying database operations.

## How to Map a Python Class to a MySQL Table
With an ORM like SQLAlchemy, you can map a Python class to a MySQL table. This mapping defines how the class properties relate to the table columns. You can then use Python objects to interact with the database, without writing SQL queries explicitly.

## How to Create a Python Virtual Environment
Python virtual environments are isolated environments for your Python projects. They allow you to manage project-specific dependencies, ensuring that your project remains independent of system-wide Python packages. You can create a virtual environment using the `venv` module and activate it with the `source` command.

## Requirements
Before you begin this project, make sure you have the following:

- Python 3.8.5 or later
- MySQL server version 8.0
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- Pycodestyle for code formatting
- A README.md file at the root of your project folder

## Installation
Here are the steps to set up your environment:

1. **Install Python Virtual Environment:**
   ```
   $ sudo apt-get install python3.8-venv
   ```

2. **Create a Python Virtual Environment:**
   ```
   $ python3 -m venv venv
   ```

3. **Activate the Virtual Environment:**
   ```
   $ source venv/bin/activate
   ```

4. **Install MySQLdb Module (version 2.0.x):**
   ```
   $ sudo apt-get install python3-dev
   $ sudo apt-get install libmysqlclient-dev
   $ sudo apt-get install zlib1g-dev
   $ sudo pip3 install mysqlclient
   ```

5. **Install SQLAlchemy Module (version 1.4.x):**
   ```
   $ sudo pip3 install SQLAlchemy
   ```

## Notes
- The project is developed and tested on Ubuntu 20.04 LTS using Python 3.8.5. Ensure you have a compatible environment.

- You may encounter a warning message when using SQLAlchemy, which can be safely ignored.

## Conclusion
This project introduces you to the world of Python programming with databases and the power of ORM. By mastering these concepts, you can build more robust and maintainable database-driven applications, freeing yourself from the complexities of raw SQL queries. Happy coding!
