# 4. Constraint Satisfaction Problems

# 4.1 What are CSPs?

> **What is Constraint Propagation? Explain how the constraint satisfaction problems are resolved with a suitable example. (8) (Fall 2025)**
>
> **Define the Constraint Satisfaction Problems (CSPs)? What is the need of backtracking search for CSPs? Explain with a suitable example. (8) (Spring 2025)**
>
> **What is the purpose of constraint propagation? Explain the types of local consistency that are used for constraint propagation. (8) (Internal 2025)**
>
> **Write a short note on Constraint Propagation. (5) (Spring 2025)**

In normal search problems, we treat each state like a closed box — we don't know what's inside it. But in a **Constraint Satisfaction Problem (CSP)**, we break the state into **pieces (variables)**, give each piece some **possible values**, and set **rules (constraints)** that say which combinations are allowed. This makes it much easier to solve because we can use smart tricks.

**Simple Definition — A CSP has three parts (X, D, C):**

- **X (Variables):** The things we need to decide. For example: X₁, X₂, X₃, ...
- **D (Domains):** The choices available for each variable. For example: variable X₁ can be Red, Green, or Blue.
- **C (Constraints):** The rules that say what is allowed and what is not. For example: X₁ and X₂ cannot have the same color.

**Some important words:**

- **Assignment:** Giving a value to one or more variables.
- **Consistent assignment:** An assignment that doesn't break any rule.
- **Complete assignment:** Every variable has been given a value.
- **Solution:** A complete assignment where no rule is broken.

**Types of Variables:**

- **Finite choices (most common):** The variable can pick from a small set. Example: colors = {Red, Green, Blue}.
- **Infinite choices:** The variable can pick from an endless set like all integers or all strings. Here, rules are written as formulas (e.g., T₁ + 5 ≤ T₂).
- **Continuous choices:** The variable can be any real number (like 3.7 or 0.001). Used in engineering problems and solved with special math methods.

**Types of Constraints (Rules):**

- **Unary Constraint:** A rule about just ONE variable. Example: "SA cannot be Green." We just remove Green from SA's choices.
- **Binary Constraint:** A rule about TWO variables. Example: "SA and WA must have different colors." This is the most common type. We draw a **constraint graph** — variables are dots, and a line connects two dots if there's a rule between them.
- **Higher-Order (Global) Constraint:** A rule about THREE or more variables. Example: "X₁, X₂, and X₃ must all be different" or "X₁ + X₂ + X₃ = 10."

**Example — Coloring the Map of Australia:**

Imagine you have a map of Australia with 7 regions: WA, NT, SA, Q, NSW, V, T. You have 3 colors: Red, Green, Blue. The rule is: **regions that touch each other must have different colors.**

- **Variables:** WA, NT, SA, Q, NSW, V, T
- **Domains:** {Red, Green, Blue} for each
- **Constraints:** Touching regions can't share a color. For example: WA ≠ NT, WA ≠ SA, NT ≠ SA, etc.

One answer: WA=Red, NT=Green, SA=Blue, Q=Red, NSW=Green, V=Red, T=Red.

**Other Famous CSP Examples:**

- **N-Queens:** Place N queens on an N×N chessboard so no two queens can attack each other.
- **Sudoku:** Fill a 9×9 grid so every row, column, and 3×3 box has digits 1–9 without repeating.
- **Cryptarithmetic:** Replace letters with digits to make a math equation true (e.g., SEND + MORE = MONEY).
- **Job Scheduling:** Decide when to start each task, following order and resource rules.

**Why is CSP useful?**

- Breaking the problem into variables and rules lets us use smart solving methods.
- We can remove bad choices early, so we don't waste time.
- General tricks like MRV and LCV (explained later) work on many different CSPs.

---

# 4.2 Constraint Propagation

**Constraint propagation** means using the rules to **remove bad choices** from variables before or during the search. The idea is simple: if a value can never be part of any valid answer (because it breaks a rule with every possible value of a neighbor), then just throw that value away.

**Why do we use Constraint Propagation?**

- Find out early if there's no solution (before wasting time searching).
- Make the domains smaller, so there are fewer choices to try.
- Sometimes it solves the whole problem without any search!
- When used together with search, it makes things much faster.

## Types of Local Consistency

Think of "consistency" as making sure the choices look okay at a local level — checking small groups of variables.

**1. Node Consistency (checking one variable at a time):**

A variable is **node-consistent** if all its remaining choices satisfy the rules that apply only to it (unary constraints).

This is very easy: just remove any value that breaks a rule about that single variable.

Example: If X₁ can be {Red, Green, Blue} and there's a rule "X₁ ≠ Green", just remove Green. Now X₁ = {Red, Blue}.

**2. Arc Consistency (checking two variables at a time):**

A variable X is **arc-consistent** with another variable Y if for every value in X's domain, there is at least one value in Y's domain that doesn't break their shared rule. That matching value is called a **support**.

If a value of X has no support in Y, remove it from X.

**AC-3 Algorithm (how to make everything arc-consistent):**

```
function AC-3(csp):
    queue ← all arcs (X_i, X_j) in csp
    while queue is not empty:
        (X_i, X_j) ← remove an arc from queue
        if REVISE(csp, X_i, X_j):
            if D_i is empty: return false  // No solution
            for each X_k (neighbor of X_i, k ≠ j):
                add (X_k, X_i) to queue
    return true

function REVISE(csp, X_i, X_j):
    revised ← false
    for each value v in D_i:
        if no value w in D_j satisfies constraint(X_i, X_j):
            remove v from D_i
            revised ← true
    return revised
```

**How AC-3 works step by step:**

1. Put all pairs of connected variables into a waiting list (queue).
2. Pick a pair (X, Y) from the queue.
3. For each value of X, check: is there at least one value of Y that follows the rule? If not, remove that value from X.
4. If X's domain changed, put all of X's other neighbors back into the queue (because their choices might need updating too).
5. If any variable's domain becomes empty, there's no solution.
6. Repeat until the queue is empty.

**Time Complexity:** O(cd³) — where c = number of constraints, d = biggest domain size. It's not too slow for most problems.

**Example — Map Coloring with AC-3:**

Variables: WA, NT, SA. Domains: {R, G, B}. Rules: WA ≠ NT, WA ≠ SA, NT ≠ SA.

Say we set WA = Red. We remove Red from NT and SA.
- NT = {G, B}, SA = {G, B}.

Check arc (NT, SA): Can NT = G? Yes, SA can be B. Can NT = B? Yes, SA can be G. Everything has support — no changes needed.

But if somehow NT = {G} and SA = {G}, then checking (NT, SA) with rule NT ≠ SA would find no support for NT = G (because SA is also G). So we'd detect failure immediately!

**3. Path Consistency (checking three variables at a time):**

A pair of variables {X, Y} is **path-consistent** with a third variable Z if: for every valid combination of X and Y, there is some value of Z that works with both X and Y.

Path consistency catches problems that arc consistency misses, because it looks at groups of three.

**4. K-Consistency (the general idea):**

A CSP is **k-consistent** if: whenever k−1 variables have a valid assignment, any k-th variable can also find a valid value.

- 1-consistent = node consistent (one variable checked)
- 2-consistent = arc consistent (two variables checked)
- 3-consistent = path consistent (three variables checked)

**Strong k-consistency:** If a CSP is strongly k-consistent (consistent for all levels from 1 to k), and k equals the total number of variables, then we can solve the CSP without any backtracking at all — we just assign values one by one, and a valid value is always available.

**The trade-off:** Checking higher levels of consistency takes more time, but removes more bad choices. In practice, **arc consistency (AC-3)** gives the best balance of effort vs. benefit.

**Special Global Constraints:**

- **AllDifferent:** All variables must have different values. If there are more variables than available values, it's impossible.
- **Atmost (Resource Constraint):** The total of assigned values can't go above a limit. If even the smallest possible total is too big, it's impossible.

---

# 4.3 Inference in CSPs

**Inference** means using constraint propagation **during the search** to catch failures early and shrink the search space.

**1. Forward Checking:**

When we assign a value to variable X, we look at all the **unassigned neighbors** of X and remove any of their values that break a rule with X.

- If any neighbor ends up with zero choices left, we know this path is wrong — go back immediately (backtrack).
- Forward checking catches mistakes **one step ahead**.
- **Limitation:** It only looks at direct neighbors. It doesn't check what happens further down the chain.

**Example — Map Coloring with Forward Checking:**

1. Assign WA = Red → Remove Red from NT's and SA's domains.
2. Assign Q = Green → Remove Green from NT's, SA's, and NSW's domains.
3. Now NT = {Blue}, SA = {Blue} → But the rule says NT ≠ SA! Both can only be Blue, which breaks the rule. Forward checking catches this failure right away.

Without forward checking, the algorithm would blindly assign NT = Blue, then try SA and find nothing works — wasting time.

**2. Maintaining Arc Consistency (MAC):**

MAC is **more powerful** than forward checking. After every assignment, MAC runs the **full AC-3 algorithm** starting from the affected pairs. This spreads the checking across the **entire network**, not just one step ahead.

- MAC catches failures that forward checking would miss.
- It's more work per step, but it removes many more bad branches.
- In practice, MAC is one of the best strategies for solving CSPs.

**Comparison Table:**

| Method | What it does | When it catches failures |
|--------|-------------|------------------------|
| No inference | Only checks rules when assigning | Very late |
| Forward checking | Checks neighbors after assignment | One step ahead |
| MAC (AC-3 during search) | Checks the whole network after assignment | As early as possible |

---

# 4.4 Backtracking Search for CSPs

**Why do we need Backtracking Search?**

Constraint propagation alone usually can't solve the entire problem. It removes bad choices and catches some failures, but for most CSPs, we still need to **try different values and search** for a solution. **Backtracking search** is the standard method — it mixes searching with constraint propagation.

The brute-force approach would try every possible combination. If you have n variables and each has d choices, that's d^n combinations — way too many for big problems. Backtracking search is smarter: it assigns one variable at a time and **gives up early** if things look bad.

**Key Idea:** In CSPs, the order we assign variables doesn't matter — only the final result counts. So we assign **one variable at a time** instead of trying all orderings.

**Basic Backtracking Algorithm:**

```
function BACKTRACKING-SEARCH(csp):
    return BACKTRACK({}, csp)

function BACKTRACK(assignment, csp):
    if assignment is complete: return assignment
    var ← SELECT-UNASSIGNED-VARIABLE(csp)
    for each value in ORDER-DOMAIN-VALUES(var, assignment, csp):
        if value is consistent with assignment:
            add {var = value} to assignment
            inferences ← INFERENCE(csp, var, value)
            if inferences ≠ failure:
                add inferences to csp
                result ← BACKTRACK(assignment, csp)
                if result ≠ failure: return result
            remove inferences from csp
        remove {var = value} from assignment
    return failure
```

**How it works in simple words:**

1. Pick a variable that hasn't been assigned yet.
2. Try each of its possible values one by one.
3. If the value doesn't break any rule, assign it and try to solve the rest.
4. If the rest can't be solved, **undo** the assignment (backtrack) and try the next value.
5. If no value works, report failure.

The algorithm's speed depends on three key choices:

## Which Variable to Pick First? (Variable Ordering)

**1. Minimum Remaining Values (MRV) — "Fail First":**

Pick the variable with the **fewest choices left**. Why? If a variable has only 1 choice, assign it now — no point waiting. If it has 0 choices, fail immediately and backtrack. This catches problems early.

Think of it like this: if someone has the least options, deal with them first. If they can't be satisfied, you find out quickly.

**2. Degree Heuristic (Tie-Breaker):**

If two variables have the same number of remaining values (MRV tie), pick the one connected to the **most unassigned neighbors**. This makes future assignments easier by handling the most connected variable first.

## Which Value to Try First? (Value Ordering)

**Least Constraining Value (LCV):**

When you've picked a variable, try the value that **eliminates the fewest choices** from neighbors. This keeps the most options open for future variables, making it more likely to find a solution.

**Remember:** Variable ordering (MRV) tries to **fail fast** — find dead ends quickly. Value ordering (LCV) tries to **succeed fast** — pick values most likely to lead to a solution. They work together!

## Inference During Search

At each step, after assigning a value, we can apply inference to catch problems early:

- **No inference:** Just check if the current assignment is okay. (Slow)
- **Forward Checking:** Remove bad values from neighbors. (Medium)
- **MAC:** Run full arc consistency. (Best but most expensive)

## Intelligent Backtracking

Normal backtracking just goes back to the **previous variable** when something fails. But what if the failure was caused by a variable assigned much earlier? Going back just one step is wasteful.

**Conflict-Directed Backjumping:** Each variable keeps track of a **conflict set** — the list of earlier variables that caused its choices to shrink. When failure happens, instead of going back just one step, we jump back to the **most recent variable in the conflict set**. This skips over variables that weren't part of the problem.

## Local Search for CSPs

Instead of building a solution step by step, **local search** starts with a **complete but possibly wrong** answer and tries to fix it.

**Min-Conflicts Algorithm:**

1. Give every variable a random value (complete assignment).
2. If no rules are broken, we're done!
3. Pick a variable that's **breaking a rule** (a conflicted variable).
4. Change its value to the one that **breaks the fewest rules**.
5. Repeat until solved or we've tried too many times.

Min-conflicts works surprisingly well. It can solve the million-queens problem in about 50 steps! But it can get **stuck** in situations where no single change helps (local minima), so it's not guaranteed to find a solution even if one exists.

## Using the Structure of the Problem

**Tree-Structured CSPs:** If the constraint graph looks like a tree (no loops), we can solve it very fast in **O(nd²)** time:

1. Pick any variable as the root and arrange all variables from root to leaves.
2. Work backwards from leaves to root, enforcing arc consistency.
3. Work forwards from root to leaves, assigning values — a valid value is always available at each step.

**What if the graph has loops?** Two methods to handle this:

- **Cutset Conditioning:** Find a small group of variables (called a **cutset**) whose removal turns the graph into a tree. Try every possible assignment for the cutset variables, and for each one, solve the remaining tree. The smaller the cutset, the faster this is.
- **Tree Decomposition:** Break the problem into overlapping groups (clusters) arranged in a tree. Solve each cluster separately, then combine the answers. Speed depends on the **treewidth** (the size of the biggest cluster minus 1).
