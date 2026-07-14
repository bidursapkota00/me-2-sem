# 2. Data Modeling and SQL

# 2.1 Concept of Relations

> **Differentiate between a Cartesian Product and a Join in relational databases. [7 marks] (2081)**

A relation is the fundamental data structure of the relational model. It is a two-dimensional table consisting of rows and columns, with a unique name.

**Formal Definitions:**

1. **Relation Schema:** The logical design of a relation, written as R(A1, A2, ..., An), where R is the relation name and A1 through An are its attributes. For example, `Instructor(ID, name, dept_name, salary)` is a relation schema.

2. **Relation Instance:** The actual set of tuples (rows) present in a relation at a particular moment in time. The instance changes whenever data is inserted, updated, or deleted.

3. **Attribute:** A named column of a relation. Each attribute has a domain, which is the set of permitted values. All values in the relational model must be atomic (indivisible). The special value `null` belongs to every domain and signifies that a value is unknown or does not exist.

4. **Tuple:** A single row in a relation. Each tuple represents one record or instance of the entity described by the relation.

5. **Degree (Arity):** The number of attributes in a relation.

6. **Cardinality:** The number of tuples in a relation instance.

**Properties of Relations:**

1. The order of tuples in a relation is immaterial since a relation is defined as a set of tuples.
2. No two tuples in a relation are identical (duplicate rows are not allowed).
3. The order of attributes in a relation schema is immaterial.
4. All attribute values are atomic.

**Keys:**

1. **Superkey:** A set of one or more attributes whose combined values uniquely identify each tuple in a relation. For example, {ID} and {ID, name} are both superkeys of the Instructor relation.
2. **Candidate Key:** A minimal superkey, meaning no proper subset of it is also a superkey. If {ID} uniquely identifies an instructor, then {ID} is a candidate key.
3. **Primary Key:** The candidate key chosen by the database designer as the principal means of identifying tuples. Primary key values must not be null. It is denoted by underlining the attribute(s) in the schema notation.

---

# 2.2 Referential Integrity and Foreign Key

> **Explain how a foreign key can be used to enforce referential integrity constraints, including appropriate SQL syntax. [7 marks] (2081)**

**Foreign Key:**

A foreign key is a set of attributes in one relation whose values are required to match the primary key values of another relation. It creates a logical link between two relations.

For a foreign key constraint from relation R (referencing relation) to relation S (referenced relation), every value appearing in the foreign key columns of R must either match an existing primary key value in S, or be null.

**Referential Integrity:**

Referential integrity is the constraint that ensures that foreign key values always reference valid, existing tuples in the referenced relation. It prevents dangling references where a tuple in one relation points to a non-existent tuple in another.

**Violations and Enforcement:**

The DBMS checks referential integrity whenever a modification could break the constraint:

1. **Insert into referencing relation:** If the new foreign key value does not exist in the referenced relation's primary key, the insert is rejected.
2. **Delete from referenced relation:** If a tuple being deleted is referenced by tuples in the referencing relation, the DBMS can reject the deletion, cascade the delete (also remove referencing tuples), or set the foreign key values to null.
3. **Update:** Similar checks apply when updating primary key or foreign key values.

**SQL Syntax:**

```sql
CREATE TABLE Department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
        ON DELETE CASCADE
        ON UPDATE SET NULL
);
```

In this example, `dept_id` in Employee is a foreign key referencing `Department(dept_id)`. The `ON DELETE CASCADE` clause specifies that if a department is deleted, all employees in that department are also deleted. The `ON UPDATE SET NULL` clause specifies that if a department's `dept_id` changes, the corresponding `dept_id` values in Employee are set to null.

**Other Integrity Constraints:**

1. **NOT NULL:** Ensures that an attribute cannot hold a null value.
2. **UNIQUE:** Ensures that all values in a column or set of columns are distinct.
3. **CHECK:** Ensures that values satisfy a specified predicate (e.g., `CHECK (salary > 0)`).
4. **DEFAULT:** Assigns a default value to an attribute when no value is provided during insertion.

---

# 2.3 Relational Algebra

> **Write relational algebraic expression and SQL for performing operations. [8 marks] (2080)**

Relational algebra is a procedural query language that consists of a set of operations. Each operation takes one or two relations as input and produces a new relation as output. It provides the formal theoretical foundation for SQL.

**Six Fundamental Operations:**

**1. Select (σ):**

Selects tuples from a relation that satisfy a given predicate. It is a unary operation (operates on one relation).

Notation: σ_p(r), where p is the selection predicate and r is the relation.

Example: Select all instructors from the Physics department.

σ_{dept_name = "Physics"}(Instructor)

```sql
SELECT * FROM Instructor WHERE dept_name = 'Physics';
```

The predicate can use comparison operators (=, ≠, <, >, ≤, ≥) and logical connectives (∧ for AND, ∨ for OR, ¬ for NOT).

**2. Project (∏):**

Returns specified attributes from a relation, removing all other attributes. Duplicate tuples in the result are eliminated. It is a unary operation.

Notation: ∏_{A1, A2, ..., Ak}(r)

Example: List only the names and salaries of all instructors.

∏_{name, salary}(Instructor)

```sql
SELECT DISTINCT name, salary FROM Instructor;
```

**3. Union (∪):**

Combines tuples from two relations, eliminating duplicates. Both relations must be union-compatible (same number of attributes with compatible domains).

Notation: r ∪ s

Example: Find all people who are either instructors or students (assuming both relations have a `name` attribute).

∏_{name}(Instructor) ∪ ∏_{name}(Student)

```sql
SELECT name FROM Instructor
UNION
SELECT name FROM Student;
```

**4. Set Difference (−):**

Returns tuples that exist in the first relation but not in the second. Both relations must be union-compatible.

Notation: r − s

Example: Find names of instructors who are not students.

∏_{name}(Instructor) − ∏_{name}(Student)

```sql
SELECT name FROM Instructor
EXCEPT
SELECT name FROM Student;
```

**5. Cartesian Product (×):**

Combines every tuple of one relation with every tuple of another. If relation r has n1 tuples and s has n2 tuples, the result has n1 × n2 tuples.

Notation: r × s

Example: Combine every instructor with every department.

Instructor × Department

```sql
SELECT * FROM Instructor, Department;
```

The Cartesian product by itself is rarely useful because it produces all possible combinations regardless of any logical relationship. It becomes meaningful only when combined with a selection operation to filter relevant pairs.

**6. Rename (ρ):**

Assigns a new name to a relation or its attributes. This is essential for self-joins and for disambiguating attribute names.

Notation: ρ_x(E) renames the result of expression E to x. ρ_{x(A1, A2, ..., An)}(E) also renames the attributes.

**Additional Operations (derived from the fundamental six):**

**Set Intersection (∩):**

Returns tuples that appear in both relations. It can be expressed as: r ∩ s = r − (r − s).

∏_{name}(Instructor) ∩ ∏_{name}(Student)

```sql
SELECT name FROM Instructor
INTERSECT
SELECT name FROM Student;
```

**Natural Join (⋈):**

Combines two relations by automatically matching on all attributes with the same name, and eliminates duplicate columns. It is equivalent to a Cartesian product followed by a selection on equal common attributes, followed by a projection to remove duplicate columns.

Notation: r ⋈ s

Example: Find instructors along with the courses they teach.

Instructor ⋈ Teaches

```sql
SELECT * FROM Instructor NATURAL JOIN Teaches;
```

**Division (÷):**

Used to answer queries involving "for all" conditions (e.g., find students who have taken all courses offered by the Biology department). It is defined using the fundamental operations.

**Practical Example:**

Given: Employee(eid, emp_name, address, supervisor_id), Department(did, dep_name), Project(pid, prj_name, did), Workson(eid, pid, hours)

(i) List names of all employees in the computer department along with their supervisor name:

∏_{E.emp_name, S.emp_name}(σ_{dep_name="Computer"}(Employee E ⋈_{E.eid = W.eid} Workson W ⋈_{W.pid = P.pid} Project P ⋈_{P.did = D.did} Department D) ⋈_{E.supervisor_id = S.eid} ρ_S(Employee))

```sql
SELECT E.emp_name, S.emp_name AS supervisor_name
FROM Employee E
JOIN Workson W ON E.eid = W.eid
JOIN Project P ON W.pid = P.pid
JOIN Department D ON P.did = D.did
JOIN Employee S ON E.supervisor_id = S.eid
WHERE D.dep_name = 'Computer';
```

(ii) Find total number of projects from each department along with department name:

_{did} G _{COUNT(pid)}(Project) ⋈ Department

```sql
SELECT D.dep_name, COUNT(P.pid) AS total_projects
FROM Project P
JOIN Department D ON P.did = D.did
GROUP BY D.dep_name;
```

(iii) Find names of employees who do not work on any project:

∏_{emp_name}(Employee) − ∏_{emp_name}(Employee ⋈_{Employee.eid = Workson.eid} Workson)

```sql
SELECT emp_name FROM Employee
WHERE eid NOT IN (SELECT eid FROM Workson);
```

(iv) Find name of each project with more than 3 employees:

∏_{prj_name}(σ_{count ≥ 3}(_{pid} G _{COUNT(eid) AS count}(Workson)) ⋈ Project)

```sql
SELECT P.prj_name
FROM Project P
JOIN Workson W ON P.pid = W.pid
GROUP BY P.prj_name
HAVING COUNT(W.eid) > 3;
```

---

# 2.4 Various Types of Joins

Joins combine tuples from two or more relations based on a related column. They are among the most important and frequently used operations in relational databases.

**1. Inner Join:**

Returns only those tuples from both relations that satisfy the join condition. Tuples without a matching partner in the other relation are excluded from the result.

```sql
SELECT E.emp_name, D.dept_name
FROM Employee E
INNER JOIN Department D ON E.dept_id = D.dept_id;
```

**2. Natural Join:**

A special case of inner join that automatically matches on all attributes with the same name in both relations. It retains only one copy of each common column and eliminates duplicates.

```sql
SELECT *
FROM Student NATURAL JOIN Takes;
```

**3. Left Outer Join:**

Returns all tuples from the left relation. If a left tuple has no matching tuple in the right relation, the right-side attributes are filled with null values. This ensures no information from the left relation is lost.

```sql
SELECT E.emp_name, D.dept_name
FROM Employee E
LEFT OUTER JOIN Department D ON E.dept_id = D.dept_id;
```

**4. Right Outer Join:**

Returns all tuples from the right relation. If a right tuple has no matching tuple in the left relation, the left-side attributes are filled with null values.

```sql
SELECT E.emp_name, D.dept_name
FROM Employee E
RIGHT OUTER JOIN Department D ON E.dept_id = D.dept_id;
```

**5. Full Outer Join:**

Returns all tuples from both relations. If a tuple in either relation has no match in the other, the missing side is filled with null values. It is the union of left and right outer joins.

```sql
SELECT E.emp_name, D.dept_name
FROM Employee E
FULL OUTER JOIN Department D ON E.dept_id = D.dept_id;
```

**6. Cross Join (Cartesian Product):**

Produces every possible combination of tuples from two relations. If relation A has m rows and relation B has n rows, the result has m × n rows. No join condition is specified.

```sql
SELECT *
FROM Employee CROSS JOIN Department;
```

**7. Self Join:**

A join where a table is joined with itself. This requires using table aliases to distinguish the two copies of the same table. It is useful for queries involving hierarchical or recursive relationships within a single table.

```sql
SELECT E.emp_name AS employee, S.emp_name AS supervisor
FROM Employee E
JOIN Employee S ON E.supervisor_id = S.eid;
```

**Join Clauses in SQL:**

1. **ON:** Specifies an arbitrary join predicate. Example: `ON A.id = B.id`.
2. **USING:** Specifies join on columns with the same name in both tables. Example: `USING (dept_id)`.
3. **NATURAL:** Implicitly joins on all common column names. No explicit condition is needed.

**Cartesian Product vs. Join:**

A Cartesian product combines every tuple of one relation with every tuple of another without any condition, producing a very large result set (m × n rows). A join is a Cartesian product followed by a selection that filters only the meaningful combinations based on a join condition. The join is therefore a more selective and useful operation.

---

# 2.5 SQL Fundamentals: DDL, DML

> **Design ER model for conference management system. Also write SQL DDL to convert this ER model to equivalent relational schemas. [8 marks] (2080)**

SQL (Structured Query Language) is the most widely used language for interacting with relational database systems. It combines features of both relational algebra and relational calculus. SQL has several parts:

**Data Definition Language (DDL):**

DDL is used to define, modify, and remove the structure (schema) of database objects such as tables, indexes, and views. DDL statements produce metadata that is stored in the data dictionary (system catalog).

**CREATE TABLE:**

Defines a new relation with its attributes, data types, and constraints.

```sql
CREATE TABLE Course (
    course_id VARCHAR(10) PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    credits INT CHECK (credits > 0),
    dept_name VARCHAR(50),
    FOREIGN KEY (dept_name) REFERENCES Department(dept_name)
);
```

**Common SQL Data Types:**

1. **CHAR(n):** Fixed-length character string of length n.
2. **VARCHAR(n):** Variable-length character string with maximum length n.
3. **INT / INTEGER:** Integer value.
4. **NUMERIC(p, d):** Fixed-point number with p digits total and d digits after the decimal point.
5. **FLOAT(n) / REAL / DOUBLE PRECISION:** Floating-point number.
6. **DATE:** Calendar date (year, month, day).
7. **TIME:** Time of day (hours, minutes, seconds).
8. **TIMESTAMP:** Combination of date and time.
9. **BOOLEAN:** True or false value.

**ALTER TABLE:**

Modifies the structure of an existing table.

```sql
-- Add a new column
ALTER TABLE Student ADD email VARCHAR(100);

-- Drop an existing column
ALTER TABLE Student DROP COLUMN email;

-- Modify column data type
ALTER TABLE Student ALTER COLUMN name TYPE VARCHAR(200);
```

**DROP TABLE:**

Removes a table and all its data from the database.

```sql
DROP TABLE Student;
```

**TRUNCATE TABLE:**

Removes all rows from a table without deleting the table structure itself.

```sql
TRUNCATE TABLE Enrolls;
```

**Data Manipulation Language (DML):**

DML is used to retrieve, insert, modify, and delete data within relations.

**SELECT (Query):**

The fundamental operation for data retrieval.

```sql
SELECT column1, column2
FROM table_name
WHERE condition
ORDER BY column1 ASC;
```

The general form of a SQL query is:

```sql
SELECT A1, A2, ..., An
FROM r1, r2, ..., rm
WHERE P;
```

This is equivalent to the relational algebra expression: ∏_{A1, A2, ..., An}(σ_P(r1 × r2 × ... × rm)).

**Important SELECT Clauses:**

1. **DISTINCT:** Eliminates duplicate rows from the result. Example: `SELECT DISTINCT dept_name FROM Instructor;`
2. **ALL:** Retains duplicates (this is the default behavior).
3. **AS (Alias):** Renames columns or tables in the result. Example: `SELECT name AS instructor_name FROM Instructor;`
4. **ORDER BY:** Sorts the result by one or more columns. Default is ascending (ASC). Example: `ORDER BY salary DESC;`
5. **LIMIT / FETCH FIRST:** Restricts the number of rows returned. Example: `LIMIT 10;`

**WHERE Clause Operators:**

1. **Comparison:** =, <>, <, >, <=, >=
2. **Logical:** AND, OR, NOT
3. **Range:** BETWEEN ... AND ...
4. **Pattern matching:** LIKE (with wildcards % for any string, _ for any single character)
5. **Null check:** IS NULL, IS NOT NULL

**INSERT:**

Adds new tuples to a relation.

```sql
-- Insert a single tuple
INSERT INTO Student VALUES ('S001', 'Alice', 'CS');

-- Insert with specified columns
INSERT INTO Student (student_id, name)
VALUES ('S002', 'Bob');

-- Insert from a query result
INSERT INTO Archive_Student
SELECT * FROM Student WHERE graduation_year < 2020;
```

**UPDATE:**

Modifies existing tuples in a relation.

```sql
UPDATE Instructor
SET salary = salary * 1.05
WHERE dept_name = 'Computer Science';
```

**DELETE:**

Removes tuples from a relation.

```sql
-- Delete specific tuples
DELETE FROM Student WHERE student_id = 'S001';

-- Delete all tuples
DELETE FROM Student;
```

---

# 2.6 Advanced SQL (Joins, Subqueries, Aggregation)

> **Explain advanced SQL subqueries and aggregations. Provide an SQL snippet that uses a Window Function (like RANK() or OVER()) to solve a real-world data analytical problem. [7 marks] (2082)**

## 2.6.1 Aggregate Functions

Aggregate functions take a collection (set or multiset) of values as input and return a single value.

**Built-in Aggregate Functions:**

1. **AVG(column):** Returns the average of values.
2. **MIN(column):** Returns the minimum value.
3. **MAX(column):** Returns the maximum value.
4. **SUM(column):** Returns the sum of values.
5. **COUNT(column):** Returns the number of values. `COUNT(*)` counts the number of tuples.

**GROUP BY Clause:**

Groups tuples that have the same values in specified attributes, and then applies the aggregate function to each group separately. Any attribute in the SELECT clause that is not inside an aggregate function must appear in the GROUP BY clause.

```sql
SELECT dept_name, AVG(salary) AS avg_salary
FROM Instructor
GROUP BY dept_name;
```

**HAVING Clause:**

Filters groups produced by GROUP BY based on a condition. It is applied after grouping, unlike WHERE which filters individual tuples before grouping.

```sql
SELECT dept_name, AVG(salary) AS avg_salary
FROM Instructor
GROUP BY dept_name
HAVING AVG(salary) > 50000;
```

**Order of Execution in SQL:**

1. FROM (identify tables)
2. WHERE (filter rows)
3. GROUP BY (group rows)
4. HAVING (filter groups)
5. SELECT (select columns and compute aggregates)
6. ORDER BY (sort results)
7. LIMIT (restrict output)

## 2.6.2 Subqueries

A subquery (nested query) is a SELECT statement embedded inside another SQL statement. Subqueries can appear in the WHERE, FROM, or SELECT clauses.

**Subquery in WHERE Clause:**

```sql
-- Find instructors whose salary is above the average
SELECT name, salary
FROM Instructor
WHERE salary > (SELECT AVG(salary) FROM Instructor);
```

**Set Membership (IN, NOT IN):**

Tests whether a value belongs to a set returned by a subquery.

```sql
-- Find courses offered in both Fall 2017 and Spring 2018
SELECT DISTINCT course_id
FROM Section
WHERE semester = 'Fall' AND year = 2017
  AND course_id IN (
      SELECT course_id FROM Section
      WHERE semester = 'Spring' AND year = 2018
  );
```

**Set Comparison (SOME/ANY, ALL):**

Compares a value against a set of values returned by a subquery.

```sql
-- Find instructors earning more than at least one instructor in Biology
SELECT name
FROM Instructor
WHERE salary > SOME (
    SELECT salary FROM Instructor WHERE dept_name = 'Biology'
);

-- Find instructors earning more than every instructor in Biology
SELECT name
FROM Instructor
WHERE salary > ALL (
    SELECT salary FROM Instructor WHERE dept_name = 'Biology'
);
```

**Existence Testing (EXISTS, NOT EXISTS):**

Tests whether a subquery returns any rows.

```sql
-- Find all courses that were offered at least once
SELECT course_id, title
FROM Course C
WHERE EXISTS (
    SELECT 1 FROM Section S WHERE S.course_id = C.course_id
);
```

**Correlated Subqueries:**

A correlated subquery references attributes from the outer query and is re-evaluated for each tuple of the outer query. The EXISTS example above is a correlated subquery because the inner query references `C.course_id` from the outer query.

```sql
-- Find employees earning more than the average salary of their department
SELECT emp_name, salary, dept_id
FROM Employee E
WHERE salary > (
    SELECT AVG(salary)
    FROM Employee
    WHERE dept_id = E.dept_id
);
```

**Subquery in FROM Clause (Derived Tables):**

A subquery can act as a temporary relation in the FROM clause.

```sql
SELECT dept_name, avg_salary
FROM (
    SELECT dept_name, AVG(salary) AS avg_salary
    FROM Instructor
    GROUP BY dept_name
) AS dept_avg
WHERE avg_salary > 50000;
```

**Scalar Subqueries:**

A subquery that returns exactly one row with one column. It can be used wherever a single value is expected.

```sql
SELECT name,
       (SELECT COUNT(*) FROM Teaches T WHERE T.ID = I.ID) AS num_courses
FROM Instructor I;
```

## 2.6.3 Window Functions

Window functions perform calculations across a set of rows that are related to the current row, called the window. Unlike GROUP BY, window functions do not collapse rows into a single output row. Each row retains its identity and gains an additional computed value.

**Syntax:**

```sql
function_name(args) OVER (
    [PARTITION BY column_list]
    [ORDER BY column_list]
    [ROWS/RANGE frame_specification]
)
```

1. **PARTITION BY:** Divides the result set into partitions (groups). The window function is applied independently to each partition.
2. **ORDER BY:** Defines the order of rows within each partition.
3. **Frame (ROWS/RANGE):** Defines the subset of rows within the partition relative to the current row (e.g., preceding or following rows).

**Common Window Functions:**

1. **RANK():** Assigns a rank to each row within a partition. Rows with equal values receive the same rank, and the next rank is skipped (e.g., 1, 2, 2, 4).
2. **DENSE_RANK():** Similar to RANK() but does not skip ranks after ties (e.g., 1, 2, 2, 3).
3. **ROW_NUMBER():** Assigns a unique sequential number to each row within a partition, regardless of ties.
4. **NTILE(n):** Distributes rows of a partition into n approximately equal groups and assigns a group number.
5. **LAG(column, offset):** Accesses data from a preceding row within the partition.
6. **LEAD(column, offset):** Accesses data from a following row within the partition.
7. **SUM(), AVG(), COUNT(), MIN(), MAX():** Standard aggregate functions can also be used as window functions when combined with OVER().

**Example: Rank Instructors by Salary Within Each Department:**

```sql
SELECT name, dept_name, salary,
       RANK() OVER (PARTITION BY dept_name ORDER BY salary DESC)
           AS dept_rank
FROM Instructor;
```

This query assigns a rank to each instructor within their department based on descending salary. An instructor with the highest salary in their department gets rank 1. Two instructors with the same salary receive the same rank, and the subsequent rank is skipped.

**Example: Running Total of Sales:**

```sql
SELECT order_date, amount,
       SUM(amount) OVER (ORDER BY order_date
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
           AS running_total
FROM Orders;
```

This query computes a cumulative sum of the `amount` column ordered by date. For each row, the running total includes all preceding rows and the current row.

**Example: Compare Each Employee's Salary with the Department Average:**

```sql
SELECT emp_name, dept_id, salary,
       AVG(salary) OVER (PARTITION BY dept_id) AS dept_avg,
       salary - AVG(salary) OVER (PARTITION BY dept_id) AS diff_from_avg
FROM Employee;
```

**Set Operations in SQL:**

SQL provides set operations that correspond directly to relational algebra set operations. These operations require union-compatible relations (same number of columns with compatible data types).

1. **UNION:** Returns all distinct rows from both queries. `UNION ALL` retains duplicates.
2. **INTERSECT:** Returns rows common to both queries. `INTERSECT ALL` retains duplicates.
3. **EXCEPT:** Returns rows in the first query that are not in the second. `EXCEPT ALL` retains duplicates. Some systems use MINUS instead of EXCEPT.

```sql
-- All people who are either instructors or students
SELECT name FROM Instructor
UNION
SELECT name FROM Student;

-- People who are both instructors and students
SELECT name FROM Instructor
INTERSECT
SELECT name FROM Student;

-- Instructors who are not students
SELECT name FROM Instructor
EXCEPT
SELECT name FROM Student;
```

## 2.6.4 WITH Clause (Common Table Expressions)

The WITH clause defines a temporary named relation (CTE) that is available only within the scope of the query in which it is defined. It improves readability for complex queries.

```sql
WITH dept_total AS (
    SELECT dept_name, SUM(salary) AS total_salary
    FROM Instructor
    GROUP BY dept_name
)
SELECT dept_name, total_salary
FROM dept_total
WHERE total_salary > (SELECT AVG(total_salary) FROM dept_total);
```

This query first computes the total salary per department, then selects only those departments whose total salary exceeds the average total salary across all departments.
