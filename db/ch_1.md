# 1. Introduction

# 1.1 Introduction to Database Systems

> **What are the key differences between structured, semi-structured, and unstructured data? [8 marks] (2081)**

A database is an organized collection of interrelated data that models some aspect of the real world. A database system provides an environment that is both convenient and efficient for storing, retrieving, and managing data.

**File System vs. Database System:**

In early computing, data was stored and managed using file systems. Applications directly interacted with OS files, leading to several critical problems that motivated the development of database systems.

**Problems with file-based approach:**

1. **Data Redundancy and Inconsistency:** Information is duplicated across multiple files, possibly in different formats, leading to inconsistent copies of the same data.
2. **Difficulty in Accessing Data:** Every new data retrieval task requires writing a new program. There is no general-purpose query facility.
3. **Data Isolation:** Data is scattered across multiple files in different formats, making it difficult to write new programs to retrieve appropriate data.
4. **Integrity Problems:** Consistency constraints (e.g., account balance must not fall below zero) are buried deep in program code, making them hard to add or modify.
5. **Atomicity Problems:** File systems cannot guarantee that a group of related updates either all succeed or all fail. A partial failure (e.g., during a fund transfer) can leave data in an inconsistent state.
6. **Concurrent Access Anomalies:** Uncontrolled simultaneous access by multiple users can lead to data inconsistencies.
7. **Security Problems:** It is difficult to enforce fine-grained access control on subsets of data when the unit of access is an entire file.

**Structured, Semi-Structured, and Unstructured Data:**

1. **Structured Data:**

Structured data conforms to a rigid, predefined schema and is stored in a tabular format (rows and columns) where every field has a specific data type. It is highly optimized for querying using SQL. Examples include relational database tables, financial transaction records, and inventory logs.

2. **Semi-Structured Data:**

Semi-structured data does not conform to a strict tabular schema but contains tags, markers, or metadata that provide some organizational structure. It has a flexible or self-describing schema. Examples include JSON, XML, YAML documents, and email headers.

3. **Unstructured Data:**

Unstructured data has no predefined format or schema. It is rich in information but difficult to store in a relational database or query with SQL. It requires advanced techniques like NLP or machine learning for analysis. Examples include images, videos, audio files, free-form text documents, and social media posts.

---

# 1.2 Database Management System

A Database Management System (DBMS) is a collection of interrelated data (the database) and a set of programs to access and manage that data. The primary goal of a DBMS is to provide a way to store and retrieve database information that is both convenient and efficient.

**Purpose of a DBMS:**

A DBMS acts as an intermediary between the user/application and the database. It provides mechanisms for data definition, data manipulation, data security, data integrity, concurrency control, and recovery from failures.

**Components of a DBMS:**

1. **Storage Manager:**

The storage manager is the component that provides the interface between the low-level data stored on disk and the application programs and queries submitted to the system. It is responsible for efficient storage, retrieval, and updating of data. It includes:
- **Authorization and Integrity Manager:** Checks that security and integrity constraints are satisfied.
- **Transaction Manager:** Ensures the database remains in a consistent state despite system failures and manages concurrent transactions so that they do not interfere with one another.
- **File Manager:** Manages the allocation of disk space and the data structures used to represent stored information.
- **Buffer Manager:** Fetches data from disk storage into main memory and decides which data to cache in memory for optimal performance.

2. **Query Processor:**

The query processor interprets and executes database queries. It includes:
- **Parser and Translator:** Checks query syntax and translates SQL into an internal representation (relational algebra expression).
- **Optimizer:** Evaluates multiple equivalent execution plans and selects the most efficient one based on statistical information about the data.
- **Evaluation Engine:** Executes the selected query execution plan and returns the results.

**Database Users:**

1. **Naive Users:** Interact with the system by invoking pre-written application programs (e.g., a bank teller using a deposit form, a web user browsing a catalogue).
2. **Application Programmers:** Write application programs that interact with the database through DML calls embedded in a host language.
3. **Sophisticated Users:** Interact directly with the system using a database query language (e.g., SQL) without writing full application programs.
4. **Database Administrator (DBA):** Has central control over the database system. Responsibilities include schema definition, storage structure and access method definition, schema and physical organization modification, granting user access authorization, specifying integrity constraints, and monitoring performance.

**Database Languages:**

1. **Data Definition Language (DDL):** Used to define the database schema, including table structures, data types, integrity constraints, and access privileges. DDL statements produce output that is stored in the data dictionary (a special set of tables containing metadata).
2. **Data Manipulation Language (DML):** Used to access and manipulate data. It provides the ability to retrieve (query), insert, delete, and modify data in the database. SQL is the most widely used DML.

**Three-Schema Architecture (ANSI/SPARC):**

This architecture separates user applications from the physical database into three levels:

1. **Internal Level (Physical Level):** Describes how data is actually stored on physical storage devices. It deals with file organizations, indexing techniques, and access paths.
2. **Conceptual Level (Logical Level):** Describes what data is stored in the database and the relationships among those data. It defines the overall logical structure using entities, data types, relationships, and constraints, hiding physical storage details.
3. **External Level (View Level):** Consists of multiple external schemas or user views. Each view describes only the part of the database that a particular user group is interested in, hiding the rest.

**Data Independence:**

Data independence is the capacity to change the schema at one level without requiring changes at the next higher level.

1. **Physical Data Independence:** The ability to modify the physical schema (e.g., changing storage structures, adding indexes) without altering the logical schema or application programs.
2. **Logical Data Independence:** The ability to modify the logical schema (e.g., adding or removing a table, adding an attribute) without changing the external schemas or application programs. This is harder to achieve than physical data independence.

**Instances and Schemas:**

1. **Schema:** The overall logical design or structure of the database. It is specified during database design and changes infrequently. It is analogous to a type definition in a programming language.
2. **Instance:** The actual collection of data stored in the database at a particular point in time. It changes frequently as data is inserted, updated, or deleted. It is analogous to a variable's value.

---

# 1.3 Data Models

> **What are the key differences between structured, semi-structured, and unstructured data? Explain in detail why graph databases are better suited for social network applications over relational databases? [8 marks] (2081)**

A data model is a collection of conceptual tools for describing data, data relationships, data semantics, and consistency constraints. Data models provide a way to describe the design of a database at the physical, logical, and view levels.

**Types of Data Models:**

1. **Relational Model:**

The relational model uses a collection of tables (relations) to represent both data and the relationships among data. Each table has multiple columns (attributes) and rows (tuples). It is the most widely used model in commercial database systems. Its mathematical foundation (relational algebra) provides a rigorous basis for data manipulation.

2. **Entity-Relationship (E-R) Model:**

The E-R model is a high-level conceptual data model used primarily for database design. It uses entities (real-world objects), attributes (properties of entities), and relationships (associations among entities) to describe the structure of data. E-R diagrams provide a graphical notation for representing database designs before they are implemented in a specific data model.

3. **Object-Based Data Models:**

These models extend the E-R model with concepts from object-oriented programming, such as encapsulation, methods, and object identity. The object-relational data model combines features of the relational and object-oriented models, supporting complex data types and inheritance within a tabular structure.

4. **Semi-Structured Data Model:**

This model allows individual data items of the same type to have different sets of attributes, unlike the relational model where every item of a given type must have the same attributes. XML and JSON are widely used representations for semi-structured data.

5. **Network Model:**

An older model that represents data as a collection of records connected by links (pointers). The schema is organized as an arbitrary graph, allowing many-to-many relationships to be represented directly. It provides more flexibility than the hierarchical model but is more complex to navigate.

6. **Hierarchical Model:**

One of the earliest data models, it organizes records in a tree structure (parent-child relationships). Each child record has exactly one parent, restricting relationships to one-to-many. While simple and efficient for hierarchical data, it cannot directly represent many-to-many relationships.

**Why Graph Databases Suit Social Networks Better Than Relational Databases:**

In a social network, the core data involves users (nodes) and their connections such as friendships, follows, and likes (edges). Relational databases struggle with this for several reasons:

1. **Join-Intensive Queries:** Traversing relationships in a relational database requires costly JOIN operations. A query like "find friends of friends" requires multiple self-joins on a relationship table, which becomes increasingly expensive as the depth of traversal grows.
2. **Index-Free Adjacency:** Graph databases store relationships as direct physical links (pointers) between nodes. Traversals follow these pointers directly, making multi-hop queries (friends of friends of friends) execute in near-constant time per hop rather than requiring full table scans or index lookups.
3. **Flexible Schema:** Social network data is highly dynamic. Graph databases naturally accommodate new relationship types and node properties without expensive schema migrations.
4. **Natural Representation:** The graph data model directly mirrors the structure of a social network. Queries are expressed as graph traversals (e.g., using Cypher in Neo4j), making them more intuitive and readable than equivalent multi-join SQL queries.

---

# 1.4 Relational Model and Entity-Relationship Diagrams

> **Design an appropriate ER model for Pokhara University Examination Section. Then, convert the ER model into a relational schema with necessary DDL, SQL Queries and Keys. [8 marks] (2082)**
>
> **Differentiate between a Cartesian Product and a Join in relational databases. Additionally, explain how a foreign key can be used to enforce referential integrity constraints. [7 marks] (2081)**

## 1.4.1 The Relational Model

The relational model organizes data into relations (tables). Each relation has a name and consists of a set of attributes (columns) and a set of tuples (rows).

**Key Terminology:**

1. **Relation (Table):** A two-dimensional table with a unique name. Each relation stores data about a particular entity type.
2. **Attribute (Column):** A named column of a relation. Each attribute has a domain, which is the set of permitted atomic (indivisible) values for that attribute.
3. **Tuple (Row):** A single row in a relation representing one instance of the entity or relationship.
4. **Domain:** The set of allowable values for an attribute. The special value null is a member of every domain to indicate that a value is unknown or does not exist.
5. **Relation Schema:** The logical design of a relation, expressed as `R(A1, A2, ..., An)` where R is the relation name and A1 through An are its attributes.
6. **Relation Instance:** The set of tuples in a relation at a particular point in time.

**Keys:**

1. **Superkey:** A set of one or more attributes that, taken collectively, uniquely identifies a tuple within a relation. For example, {ID} and {ID, name} are both superkeys of a student relation if ID is unique.
2. **Candidate Key:** A minimal superkey, meaning no proper subset of it is also a superkey. If {ID} uniquely identifies a student, then {ID} is a candidate key, but {ID, name} is not because {ID} alone suffices.
3. **Primary Key:** A candidate key chosen by the database designer as the principal means of identifying tuples. It is underlined in the relation schema. Primary key values must not be null.
4. **Foreign Key:** A set of attributes in one relation whose values must match the primary key values of another relation. It establishes and enforces referential integrity between two relations.

**Referential Integrity:**

Referential integrity is a constraint that ensures a foreign key value in one relation must either match an existing primary key value in the referenced relation or be null. It prevents dangling references.

```sql
CREATE TABLE Department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);
```

In this example, the `dept_id` column in the Employee table is a foreign key referencing the Department table. Any value inserted into `Employee.dept_id` must already exist in `Department.dept_id`, or the DBMS will reject the operation.

**Cartesian Product vs. Join:**

1. **Cartesian Product (×):** Combines every tuple of one relation with every tuple of another relation. If relation R has m tuples and relation S has n tuples, the result has m × n tuples with all attributes from both relations. It does not use any matching condition and typically produces a very large, mostly meaningless result set.

2. **Join:** A join combines tuples from two relations based on a matching condition (usually equality of shared attributes). It is essentially a Cartesian product followed by a selection. A natural join automatically matches on all common attribute names and eliminates duplicate columns. Joins produce only the meaningful combinations of tuples.

```sql
-- Cartesian Product
SELECT * FROM Employee, Department;

-- Join (only matching departments)
SELECT * FROM Employee
JOIN Department ON Employee.dept_id = Department.dept_id;
```

## 1.4.2 Entity-Relationship (E-R) Model

The E-R model is a high-level conceptual model used for database design. It describes data in terms of entities, attributes, and relationships, and is typically represented using E-R diagrams.

**Core Components:**

1. **Entity:** A distinguishable real-world object or concept (e.g., a student, a course, an instructor).
2. **Entity Set:** A collection of entities of the same type that share the same properties (e.g., the set of all students).
3. **Relationship:** An association among two or more entities (e.g., a student enrolls in a course).
4. **Relationship Set:** A set of relationships of the same type (e.g., all enrollment relationships).

**Attribute Types:**

1. **Simple (Atomic):** Cannot be divided further (e.g., age, ID).
2. **Composite:** Can be divided into smaller sub-parts (e.g., name divided into first_name and last_name, address divided into street, city, and zip).
3. **Single-Valued:** Holds exactly one value per entity (e.g., date of birth).
4. **Multivalued:** Can hold multiple values for a single entity (e.g., phone numbers, email addresses). Denoted by double ellipses in E-R diagrams.
5. **Derived:** Value is computed from other attributes (e.g., age derived from date of birth). Denoted by dashed ellipses.

**Mapping Cardinalities:**

Mapping cardinalities express the number of entities in one entity set that can be associated with entities in another entity set through a relationship. For binary relationships:

1. **One-to-One (1:1):** An entity in A is associated with at most one entity in B, and vice versa. Example: Each department has exactly one head, and each head manages exactly one department.
2. **One-to-Many (1:N):** An entity in A can be associated with many entities in B, but an entity in B is associated with at most one entity in A. Example: A department has many employees, but each employee belongs to one department.
3. **Many-to-One (N:1):** Many entities in A can be associated with one entity in B. This is the reverse perspective of One-to-Many.
4. **Many-to-Many (M:N):** An entity in A can be associated with many entities in B, and vice versa. Example: A student can enroll in many courses, and a course can have many students.

**Participation Constraints:**

1. **Total Participation:** Every entity in the entity set must participate in at least one relationship in the relationship set. Represented by a double line connecting the entity set to the relationship set.
2. **Partial Participation:** Some entities may not participate in any relationship. Represented by a single line.

**Weak Entity Set:**

A weak entity set does not have sufficient attributes to form a primary key on its own. It depends on a related strong (owner) entity set for identification. It is identified by its discriminator (partial key) combined with the primary key of the owner entity. In E-R diagrams, weak entity sets are denoted by double rectangles, and their identifying relationship by a double diamond.

Example: A "Dependent" entity (of an employee) is weak because dependents are identified by their name combined with the employee's ID.

**Specialization and Generalization:**

1. **Specialization (Top-Down):** The process of defining subclasses of an entity set based on distinguishing characteristics. For example, a Person entity set may be specialized into Student and Employee subsets, each with additional attributes.
2. **Generalization (Bottom-Up):** The reverse process where multiple entity sets with common features are combined into a higher-level, more general entity set.

**E-R Diagram Notation:**

1. **Rectangles** represent entity sets.
2. **Double Rectangles** represent weak entity sets.
3. **Diamonds** represent relationship sets.
4. **Double Diamonds** represent identifying relationships for weak entities.
5. **Ellipses** represent attributes.
6. **Double Ellipses** represent multivalued attributes.
7. **Dashed Ellipses** represent derived attributes.
8. **Underlined attributes** indicate the primary key.
9. **Lines** connect entity sets to relationship sets and attributes to entity sets.
10. **Arrows** and cardinality labels (1, M, N) indicate mapping cardinalities.
11. **Double Lines** indicate total participation.

**Converting an E-R Diagram to a Relational Schema:**

The process follows these rules:

1. **Strong Entity Set:** Each strong entity set becomes a table. All simple attributes become columns. The primary key of the entity set becomes the primary key of the table. Composite attributes are flattened (only leaf sub-attributes become columns). Multivalued attributes are represented in a separate table with a foreign key referencing the entity.

2. **Weak Entity Set:** Becomes a table that includes its own discriminator attributes plus the primary key of the owner entity set as a foreign key. The primary key of the resulting table is the combination of the discriminator and the owner's primary key.

3. **Relationship Set:** A many-to-many relationship set becomes a separate table containing the primary keys of all participating entity sets as foreign keys, plus any descriptive attributes of the relationship. The primary key is typically the combination of all participating entity primary keys. For one-to-many or one-to-one relationships, the relationship can often be represented by adding a foreign key to the table on the "many" side (or either side for 1:1).

**Example: University Examination System**

Consider entities: Student, Course, Exam, and Result.

```
Entity Sets:
  Student(student_id, name, program)
  Course(course_id, course_name, credits)
  Exam(exam_id, exam_date, exam_type)

Relationships:
  Enrolls(student_id, course_id)         -- M:N
  Has_Exam(course_id, exam_id)           -- 1:N (a course has many exams)
  Result(student_id, exam_id, marks)     -- M:N with descriptive attribute
```

**DDL for the relational schema:**

```sql
CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    program VARCHAR(50)
);

CREATE TABLE Course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits INT
);

CREATE TABLE Exam (
    exam_id INT PRIMARY KEY,
    course_id INT NOT NULL,
    exam_date DATE,
    exam_type VARCHAR(20),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE Enrolls (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE Result (
    student_id INT,
    exam_id INT,
    marks DECIMAL(5,2),
    PRIMARY KEY (student_id, exam_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (exam_id) REFERENCES Exam(exam_id)
);
```
