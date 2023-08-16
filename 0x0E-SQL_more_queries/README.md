SQL - More queries


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
