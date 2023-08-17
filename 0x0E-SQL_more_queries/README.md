## SQL - More queries

## ![SQL - More queries](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg)

## A SQL JOIN is a way to combine data from two or more tables based on a common column or condition. There are different types of SQL JOINs, such as:

**Different Types of SQL JOINs**

(INNER) JOIN: Returns records that have matching values in both tables
LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table.

![cheat Sql joins](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230817%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230817T000034Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=694bce05d10c135ae9c85fa1d76419cc5dbb49f699643f0fa620a649cb595006)


 **Creating a New MySQL User:**
   To create a new MySQL user named 'newuser' with the password 'password':
   ```sql
   CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
   ```

**Managing Privileges for a User:**
   To grant all privileges on a specific database to a user:
   ```sql
   GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
   ```

 **PRIMARY KEY:**
   A primary key uniquely identifies each row in a table. For example, creating a primary key on a 'user_id' column:
   ```sql
   CREATE TABLE users (
       user_id INT PRIMARY KEY,
       username VARCHAR(50)
   );
   ```

 **FOREIGN KEY:**
   A foreign key establishes a relationship between tables. For instance, linking an 'order' table to a 'customer' table:
   ```sql
   CREATE TABLE orders (
       order_id INT PRIMARY KEY,
       customer_id INT,
       FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
   );
   ```

**NOT NULL and UNIQUE Constraints:**
   Using both `NOT NULL` and `UNIQUE` constraints on a column:
   ```sql
   CREATE TABLE employees (
       employee_id INT PRIMARY KEY,
       first_name VARCHAR(50) NOT NULL,
       last_name VARCHAR(50) NOT NULL,
       email VARCHAR(100) UNIQUE
   );
   ```

**Retrieving Data from Multiple Tables (JOIN):**
   Combining data from 'orders' and 'customers' tables using an `INNER JOIN`:
   ```sql
   SELECT orders.order_id, customers.customer_name
   FROM orders
   INNER JOIN customers ON orders.customer_id = customers.customer_id;
   ```

**Subqueries:**
   Using a subquery to find customers who made orders over a certain amount:
   ```sql
   SELECT customer_name
   FROM customers
   WHERE customer_id IN (SELECT customer_id FROM orders WHERE order_amount > 100);
   ```

**UNION:**
   Combining results of two SELECT statements to retrieve names from 'employees' and 'customers':
   ```sql
   SELECT first_name FROM employees
   UNION
   SELECT customer_name FROM customers;
   ```
