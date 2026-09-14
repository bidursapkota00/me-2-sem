**Question**

Consider the following relations:

- **Student**(SID, Name, DeptID)
- **Department**(DeptID, DeptName)
- **Course**(CID, Title, DeptID)
- **Enrollment**(SID, CID, Marks)

Write both SQL queries and Relational Algebra for the following:

---

**i. Display names of students who scored more than 80 marks.**

- **SQL:**

```sql
SELECT DISTINCT S.Name
FROM Student S
JOIN Enrollment E ON S.SID = E.SID
WHERE E.Marks > 80;

```

- **Relational Algebra:**
  $\pi_{Name}(\sigma_{Marks > 80}(Student \bowtie Enrollment))$

---

**ii. List student names along with course titles they are enrolled in.**

- **SQL:**

```sql
SELECT S.Name, C.Title
FROM Student S
JOIN Enrollment E ON S.SID = E.SID
JOIN Course C ON E.CID = C.CID;

```

- **Relational Algebra:**
  $\pi_{Name, Title}(Student \bowtie Enrollment \bowtie Course)$

---

**iii. Find the average marks of each course.**

- **SQL:**

```sql
SELECT CID, AVG(Marks) AS Average_Marks
FROM Enrollment
GROUP BY CID;

```

- **Relational Algebra:**
  $_{CID}\gamma_{AVG(Marks)}(Enrollment)$

---

**iv. Display department names with the number of students in each department.**

- **SQL:**

```sql
SELECT D.DeptName, COUNT(S.SID) AS Number_Of_Students
FROM Department D
JOIN Student S ON D.DeptID = S.DeptID
GROUP BY D.DeptID, D.DeptName;

```

- **Relational Algebra:**
  $_{DeptName}\gamma_{COUNT(SID)}(Department \bowtie Student)$
