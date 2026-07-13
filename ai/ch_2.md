# 2. Knowledge Representation and Reasoning

# 2.1 First-Order Logic (FOL) and Reasoning

> **Consider a scenario: Ram was searching a job and attempted two interviews. In attempting the interview, he found the two statements written in the two different companies. In company A, it was written "If you are qualified, you will get the job." and in company B, it was written "If you did not get the job, you were not qualified." Does both statements are saying the same thing? Answer it using a truth-table approach. [7 marks] (2025 Spring - PU)**

**Propositional logic** deals with simple declarative propositions that are either true or false, combined using logical connectives (¬, ∧, ∨, →, ↔). It cannot express relationships between objects, quantify over objects, or represent general statements about categories.

**First-Order Logic (FOL)** extends propositional logic by introducing objects, predicates, functions, and quantifiers, allowing much richer knowledge representation.

**Syntax of FOL:**

1. **Constants:** Refer to specific objects in the domain (e.g., John, 5, BlockA).
2. **Variables:** Stand for arbitrary objects (e.g., x, y, z).
3. **Predicates:** Represent properties of objects or relations between objects (e.g., Brother(x, y), King(John)).
4. **Functions:** Map objects to objects (e.g., Father(John) returns an object).
5. **Connectives:** Same as propositional logic (¬, ∧, ∨, →, ↔).
6. **Quantifiers:**
   - **Universal quantifier (∀):** "For all." ∀x P(x) means P holds for every object x in the domain.
   - **Existential quantifier (∃):** "There exists." ∃x P(x) means P holds for at least one object x.

**Semantics of FOL:**

A sentence in FOL is interpreted with respect to a **model** that specifies the domain of objects, the mapping of constants to objects, the extension of each predicate (the set of tuples for which it is true), and the mapping of each function. A sentence is true in a model if, under the given interpretation, the sentence holds.

**Important equivalences:**

1. ∀x P(x) ≡ ¬∃x ¬P(x) (universal can be expressed using existential and negation).
2. ∃x P(x) ≡ ¬∀x ¬P(x) (existential can be expressed using universal and negation).
3. ∀x ∀y is the same as ∀y ∀x (order of same-type quantifiers can be swapped).
4. ∃x ∃y is the same as ∃y ∃x.
5. ∃x ∀y is NOT the same as ∀y ∃x (order of different quantifiers matters).

**Inference in FOL:**

**Unification:** The process of finding a substitution (a mapping of variables to terms) that makes two logical expressions identical. For example, Knows(John, x) and Knows(John, Jane) unify with substitution {x/Jane}. Unification is the key mechanism that enables inference rules to be applied in FOL.

**Generalized Modus Ponens:** If we know p₁', p₂', ..., pₙ' and a rule (p₁ ∧ p₂ ∧ ... ∧ pₙ) → q, and there exists a substitution θ such that pᵢ'θ = pᵢθ for all i, then we can infer qθ. This "lifts" the propositional Modus Ponens to work with variables.

**Forward Chaining:** Starting from known facts in the knowledge base, the algorithm repeatedly applies inference rules to derive new facts until the query is answered or no new facts can be derived. It is data-driven and useful when the system needs to derive all consequences of new data.

**Backward Chaining:** Starting from the query (the goal), the algorithm works backward to find facts and rules that support the goal. If the goal matches a known fact, it succeeds. If the goal matches the head of a rule, the algorithm recursively tries to prove each premise of the rule. It is goal-driven and avoids deriving irrelevant facts.

**Resolution:** A complete inference procedure for FOL. The knowledge base and the negation of the query are converted to Conjunctive Normal Form (CNF), a conjunction of clauses where each clause is a disjunction of literals. The resolution rule states: from (A ∨ B) and (¬B ∨ C), infer (A ∨ C). If the empty clause is derived, the original query is proved by contradiction (refutation). Conversion to CNF involves eliminating implications, moving negations inward, standardizing variables, Skolemization (eliminating existential quantifiers by replacing them with Skolem functions), dropping universal quantifiers, and distributing disjunctions over conjunctions.

**Truth Table for the Exam Question:**

Let P = "You are qualified" and Q = "You get the job."

Company A says: P → Q (If qualified, then get job).
Company B says: ¬Q → ¬P (If not get job, then not qualified).

| P | Q | P → Q | ¬Q → ¬P |
|---|---|-------|---------|
| T | T |   T   |    T    |
| T | F |   F   |    F    |
| F | T |   T   |    T    |
| F | F |   T   |    T    |

Since the truth values of P → Q and ¬Q → ¬P are identical in every row, both statements are logically equivalent. The statement ¬Q → ¬P is the **contrapositive** of P → Q, and a conditional statement is always logically equivalent to its contrapositive.

---

# 2.2 Probabilistic Reasoning

Probabilistic reasoning handles uncertainty using probability theory. Instead of asserting that facts are true or false, an agent assigns degrees of belief (probabilities) to propositions and updates these beliefs as new evidence arrives.

**Bayes' Theorem:**

P(H | E) = P(E | H) × P(H) / P(E)

Where P(H | E) is the posterior probability of hypothesis H given evidence E, P(E | H) is the likelihood of observing evidence E given H, P(H) is the prior probability of H, and P(E) is the marginal probability of evidence E.

**Bayesian Networks:**

A Bayesian Network (Belief Network) is a directed acyclic graph (DAG) where each node represents a random variable, directed edges represent direct probabilistic dependencies, and each node has a conditional probability table (CPT) specifying the probability distribution of the node given its parents. A Bayesian Network encodes the full joint probability distribution compactly by exploiting conditional independence: P(X₁, X₂, ..., Xₙ) = Π P(Xᵢ | Parents(Xᵢ)).

## 2.2.1 Hidden Markov Models (HMMs)

An HMM is a temporal probabilistic model used when the system's true state is not directly observable (hidden), but the agent receives observations (evidence) that depend on the hidden state. It is a special case of a Dynamic Bayesian Network with a single discrete hidden state variable.

**Components of an HMM:**

1. **States (S):** A finite set of hidden states {s₁, s₂, ..., sₙ}.
2. **Transition Model P(Xₜ | Xₜ₋₁):** The probability of transitioning from one state to another. Represented as a transition matrix A, where aᵢⱼ = P(Xₜ = sⱼ | Xₜ₋₁ = sᵢ).
3. **Observation Model P(Eₜ | Xₜ):** The probability of observing evidence eₜ given the current hidden state. Represented as an emission/observation matrix B.
4. **Initial Distribution π:** The probability distribution over states at time t = 0.

**Key Assumptions:**

1. **Markov Assumption:** The current state depends only on the immediately previous state, P(Xₜ | X₀:ₜ₋₁) = P(Xₜ | Xₜ₋₁). The future is conditionally independent of the past given the present.
2. **Sensor Markov Assumption:** The current observation depends only on the current state, P(Eₜ | X₀:ₜ, E₀:ₜ₋₁) = P(Eₜ | Xₜ).

**Inference Tasks in HMMs:**

1. **Filtering:** Computing P(Xₜ | e₁:ₜ), the belief state (posterior distribution over the current state given all evidence so far). This is the most common task for real-time monitoring. The **Forward Algorithm** computes this recursively: f₁:ₜ₊₁ = α × O(eₜ₊₁) × T^T × f₁:ₜ, where α is a normalization constant, O is a diagonal observation matrix, and T is the transition matrix.

2. **Prediction:** Computing P(Xₜ₊ₖ | e₁:ₜ) for k > 0, the probability distribution over a future state given evidence up to the present. Prediction is filtering without incorporating new evidence. As k increases, the distribution converges to the stationary distribution of the Markov chain.

3. **Smoothing:** Computing P(Xₖ | e₁:ₜ) for 0 ≤ k < t, the probability distribution over a past state given all evidence including future observations. Smoothing gives a better estimate of past states than filtering because it uses more evidence. The **Forward-Backward Algorithm** computes this by combining the forward message f₁:ₖ and the backward message bₖ₊₁:ₜ.

4. **Most Likely Explanation (Decoding):** Finding the most likely sequence of hidden states argmax_{x₁:ₜ} P(x₁:ₜ | e₁:ₜ). The **Viterbi Algorithm** solves this using dynamic programming. Unlike the forward algorithm which sums over all possible previous states, Viterbi takes the maximum, and maintains backpointers to reconstruct the most probable path.

**Example:** Consider a scenario where the hidden states are {Rainy, Sunny} and the observations are {Umbrella, No Umbrella}. The transition model specifies how weather changes day to day, and the observation model specifies the probability of seeing an umbrella given the weather. Filtering answers "What is the probability it is raining today given the umbrella observations so far?" The Viterbi algorithm answers "What was the most likely weather sequence over the past week given the observations?"

## 2.2.2 Dynamic Bayesian Networks (DBNs)

A Dynamic Bayesian Network is a generalization of the HMM that allows the state at each time step to be represented by multiple state variables rather than a single variable. Each time slice of a DBN is a standard Bayesian Network, and the temporal connections between slices specify the transition model.

**Structure of a DBN:**

1. Each time slice t contains a set of state variables X₁ₜ, X₂ₜ, ..., Xₙₜ and observation variables E₁ₜ, E₂ₜ, ..., Eₘₜ.
2. The transition model specifies dependencies between variables at time t−1 and variables at time t.
3. The sensor model specifies how observation variables depend on state variables within the same time slice.

**Relationship between HMMs and DBNs:**

Every HMM is a DBN with a single hidden state variable. Conversely, every DBN can be "flattened" into an HMM by creating a single composite state variable that is the cross-product of all the individual state variables. However, this flattening results in an exponentially large state space. For example, if a DBN has 20 Boolean state variables, the equivalent HMM would have 2²⁰ (over one million) states, making the transition matrix infeasible to store or compute. DBNs are therefore exponentially more compact than their equivalent HMMs for multi-variable systems.

**Advantages of DBNs over HMMs:**

1. They can represent complex systems with many interacting state variables compactly by exploiting conditional independence among state variables.
2. The transition model in a DBN requires only O(n) parameters (where each variable has a bounded number of parents), compared to O(2ⁿ × 2ⁿ) for the equivalent HMM transition matrix.
3. They support both discrete and continuous variables.

**Inference in DBNs:**

Exact inference can be performed by "unrolling" the DBN into a static Bayesian Network and applying standard algorithms like variable elimination. However, for long time sequences, approximate inference methods such as **particle filtering** (sequential Monte Carlo) are used. Particle filtering represents the belief state by a set of weighted samples (particles) and updates them as new evidence arrives.

---

# 2.3 Ontological Engineering

Ontological engineering is the process of defining a general framework of concepts, categories, and relationships to represent knowledge about the world in a way that enables AI systems to reason about diverse domains.

**Motivation:**

Creating a knowledge base for every specific domain from scratch is inefficient. Ontological engineering aims to build a shared, reusable conceptual framework (an upper ontology) that can be specialized for different applications. This parallels how a library of reusable code components works in software engineering.

**Upper Ontology:**

An upper ontology defines the most general categories that apply across all domains. Russell and Norvig describe a hierarchy with the following general categories:

1. **Things (Entities):** Everything that exists. Divided into abstract objects and physical objects.
2. **Categories:** Sets of objects with common properties (e.g., Dogs, Chairs). Categories can be organized into taxonomies using subcategory relationships.
3. **Measures:** Quantities like length, mass, and currency used to describe properties of objects numerically.
4. **Composite Objects:** Objects that are made up of parts (e.g., a car is composed of an engine, wheels, body). The PartOf relation is transitive.
5. **Time and Events:** Events are occurrences that happen at particular time points or over intervals. Processes are continuous events. Fluents are properties of the world that change over time.
6. **Mental Objects and Beliefs:** Propositions, beliefs, and knowledge that agents hold about the world.

**Key Concepts:**

1. **Reification:** Treating an abstract concept (such as an event or a proposition) as a concrete object so it can be referred to and reasoned about in the knowledge base.
2. **Inheritance:** Subcategories inherit properties of their parent categories. For example, if "All mammals breathe air," then "dogs breathe air" follows automatically because Dog is a subcategory of Mammal.
3. **Intrinsic vs. Extrinsic Properties:** Intrinsic properties are inherent to the object itself (e.g., mass, color). Extrinsic properties depend on the object's relationship to other things (e.g., price, ownership).

**Practical Ontologies:**

1. **CYC:** One of the largest ontological engineering projects, containing millions of assertions about common-sense knowledge.
2. **WordNet:** A lexical database that organizes English words into synsets (synonym sets) linked by semantic relations.
3. **OWL (Web Ontology Language):** A formal language based on description logic, used on the semantic web to define and share ontologies.

---

# 2.4 Semantic Networks

A semantic network is a graph-based knowledge representation formalism where knowledge is encoded as a network of nodes (representing objects, concepts, or categories) connected by labeled links (representing relationships between them).

**Components:**

1. **Nodes:** Represent entities, concepts, events, or categories (e.g., Animal, Bird, Tweety).
2. **Links (Edges):** Represent relationships between nodes. Each link is labeled with the type of relationship.

**Common Link Types:**

1. **IS-A (subclass):** Represents that one category is a subcategory of another (e.g., Bird IS-A Animal).
2. **Instance-of:** Represents that an individual object is a member of a category (e.g., Tweety Instance-of Bird).
3. **Has-Part:** Represents composition (e.g., Bird Has-Part Wing).
4. **Has-Property:** Represents an attribute (e.g., Bird Has-Property CanFly).
5. **Other domain-specific relations:** e.g., Lives-In, Eats, Caused-By.

**Inheritance in Semantic Networks:**

A fundamental feature is property inheritance through the IS-A hierarchy. A subclass inherits all properties of its superclass. For example, if Bird Has-Property CanFly and Sparrow IS-A Bird, then Sparrow inherits the property CanFly. This reduces redundancy because shared properties need only be stated once at the most general applicable level.

**Exceptions and Overriding:**

Inheritance can be overridden for specific subcategories. For example, Penguin IS-A Bird, but Penguin Has-Property CannotFly overrides the inherited CanFly property from Bird. This is handled using a **shortest-path heuristic**: the property defined at the most specific (closest) node takes precedence.

**Multiple Inheritance:**

A concept can have multiple parent categories (e.g., a Platypus IS-A Mammal and IS-A EggLayingAnimal). Multiple inheritance can lead to ambiguity when conflicting properties are inherited from different parents, creating the "diamond problem."

**Advantages:**

1. Intuitive and visual representation of knowledge that is easy for humans to understand.
2. Efficient inheritance-based reasoning for simple queries.
3. Natural representation of taxonomic hierarchies.

**Limitations:**

1. Lack of formal semantics. Unlike FOL, the meaning of nodes and links is not precisely defined, leading to potential ambiguity.
2. Difficulty representing complex logical expressions (negation, disjunction, quantification).
3. Limited to binary relations (each link connects exactly two nodes). Representing n-ary relations requires workarounds like reification.
4. No standard for handling conflicting inherited properties in multiple inheritance.

---

# 2.5 Description Logic

> **Define descriptive logic. Explain the components of descriptive logic in detail. [8 marks] (2025 Spring - PU)**

Description Logic (DL) is a family of formal knowledge representation languages that provide a logical foundation for representing structured knowledge. It addresses the limitations of semantic networks and frames by providing precise, formal semantics grounded in logic while remaining computationally decidable. Description Logic is the formal basis of the Web Ontology Language (OWL).

**Key Idea:** DL balances expressive power (the ability to describe complex domains) with computational tractability (the guarantee that reasoning algorithms will terminate with a correct answer in finite time).

**Components of Description Logic:**

1. **Concepts (Classes):** Represent sets of individuals. Atomic concepts are basic named sets (e.g., Person, Student, Course). Complex concepts are built from atomic concepts using constructors.

2. **Roles (Properties):** Represent binary relations between individuals (e.g., hasChild, enrolledIn, teaches).

3. **Individuals (Instances):** Represent specific named objects in the domain (e.g., John, CS101, Kathmandu).

**Knowledge Base Structure:**

A DL knowledge base consists of two components:

1. **TBox (Terminological Box):** Contains axioms that define concepts and their relationships. It describes the schema or vocabulary of the domain.
   - **Concept Inclusion:** Mother ⊑ Female (every mother is female).
   - **Concept Equivalence:** Bachelor ≡ Male ⊓ ¬Married (a bachelor is exactly a male who is not married).

2. **ABox (Assertional Box):** Contains assertions about specific individuals using the vocabulary defined in the TBox.
   - **Concept Assertion:** John : Student (John is a student).
   - **Role Assertion:** (John, CS101) : enrolledIn (John is enrolled in CS101).

**Concept Constructors in ALC (Attributive Language with Complement):**

ALC is the foundational description logic. It builds complex concepts from atomic ones using these constructors:

1. **Negation (¬C):** The set of all individuals that are NOT in concept C. Example: ¬Student represents all non-students.
2. **Conjunction (C ⊓ D):** The set of individuals that belong to both C and D. Example: Student ⊓ Female represents female students.
3. **Disjunction (C ⊔ D):** The set of individuals that belong to C or D or both. Example: Student ⊔ Employee represents anyone who is a student or an employee.
4. **Existential Restriction (∃R.C):** The set of individuals that have at least one R-relationship to some individual in C. Example: ∃hasChild.Doctor represents individuals who have at least one child who is a doctor.
5. **Universal Restriction (∀R.C):** The set of individuals whose R-relationships all lead to individuals in C. Example: ∀hasChild.Female represents individuals all of whose children are female.
6. **Top (⊤):** The set of all individuals in the domain.
7. **Bottom (⊥):** The empty set (no individuals).

**Reasoning Tasks in Description Logic:**

1. **Satisfiability:** Determining whether a concept can possibly have any instances (is not inherently contradictory). Example: Male ⊓ ¬Male is unsatisfiable.
2. **Subsumption:** Determining whether one concept is more general than another (C ⊑ D). Example: checking whether Mother ⊑ Parent.
3. **Consistency:** Determining whether the knowledge base (TBox + ABox) is free of contradictions.
4. **Instance Checking:** Determining whether a specific individual belongs to a given concept.

**Relationship to FOL:**

Description Logic is a decidable fragment of First-Order Logic. Every DL statement can be translated into FOL, but DL restricts the expressiveness to ensure that all reasoning tasks are decidable. For example, ∃hasChild.Doctor translates to ∃y (hasChild(x, y) ∧ Doctor(y)) in FOL.

---

# 2.6 Fuzzy Logic

> **Illustrate the Mamdani Fuzzy Inference System with a suitable example. [8 marks] (2025 Spring - PU)**

Classical logic and probability deal with propositions that are either true or false, or with events that either occur or do not. **Fuzzy logic** extends classical logic to handle degrees of truth, allowing a proposition to be partially true (e.g., "The water is warm" might be 0.7 true and "The water is hot" might be 0.3 true simultaneously).

**Fuzzy Sets:**

A classical (crisp) set has a sharp boundary: an element either belongs to the set or does not. A fuzzy set has a gradual boundary defined by a **membership function** μ(x) that maps each element to a value in [0, 1], indicating the degree to which it belongs to the set. Common membership function shapes include triangular, trapezoidal, Gaussian, and bell-shaped functions.

**Fuzzy Operations:**

1. **Union (OR):** μ(A ∪ B) = max(μ_A(x), μ_B(x))
2. **Intersection (AND):** μ(A ∩ B) = min(μ_A(x), μ_B(x))
3. **Complement (NOT):** μ(¬A) = 1 − μ_A(x)

**Linguistic Variables and Hedges:**

A linguistic variable takes linguistic values rather than numerical ones (e.g., Temperature = {Cold, Warm, Hot}). Each linguistic value is defined by a fuzzy set. Hedges are modifiers that alter the meaning of a linguistic value (e.g., "Very Hot" is obtained by squaring the membership function of "Hot"; "Somewhat Hot" is obtained by taking the square root).

## 2.6.1 Fuzzy Inference Systems (FIS)

A Fuzzy Inference System maps crisp inputs to crisp outputs through a set of fuzzy If-Then rules. The general steps are:

1. **Fuzzification:** Convert crisp input values into degrees of membership in fuzzy sets using input membership functions.
2. **Rule Evaluation:** Apply the fuzzy If-Then rules. For each rule, compute the firing strength by applying fuzzy AND (min) or OR (max) operations to the antecedent membership values.
3. **Implication:** Apply the firing strength to the consequent of each rule to produce a fuzzy output.
4. **Aggregation:** Combine the fuzzy outputs from all rules into a single fuzzy set.
5. **Defuzzification:** Convert the aggregated fuzzy output into a single crisp value.

### Mamdani Fuzzy Inference System

The Mamdani FIS is the most widely used type. Both the antecedent and the consequent of each rule are fuzzy sets. The output is a fuzzy set that must be defuzzified.

**Steps:**

1. **Fuzzification:** Determine the degree of membership of each crisp input in each relevant fuzzy set.
2. **Rule Evaluation:** For each rule, apply the AND operator (typically min) across antecedent conditions to get the firing strength.
3. **Implication:** Clip (or scale) the consequent fuzzy set of each rule by its firing strength. The min implication clips the output fuzzy set at the firing strength level.
4. **Aggregation:** Combine all clipped output fuzzy sets using the max operator (union) to produce a single aggregated output fuzzy set.
5. **Defuzzification:** Convert the aggregated fuzzy set to a crisp value using a defuzzification method (typically centroid).

**Example: Tipping Problem**

Inputs: Food Quality (0–10), Service Quality (0–10). Output: Tip Percentage (5–25%).

Fuzzy sets for Food Quality: Poor, Average, Good. Fuzzy sets for Service Quality: Poor, Average, Good. Fuzzy sets for Tip: Low, Medium, High.

Rules:
- Rule 1: IF Food is Poor OR Service is Poor THEN Tip is Low.
- Rule 2: IF Service is Average THEN Tip is Medium.
- Rule 3: IF Food is Good OR Service is Good THEN Tip is High.

Suppose Food = 7.5 and Service = 4.0.

Step 1 (Fuzzification): Food = 7.5 → μ_Average(7.5) = 0.3, μ_Good(7.5) = 0.7. Service = 4.0 → μ_Poor(4.0) = 0.2, μ_Average(4.0) = 0.6.

Step 2 (Rule Evaluation): Rule 1: max(μ_PoorFood, μ_PoorService) = max(0, 0.2) = 0.2. Rule 2: μ_AverageService = 0.6. Rule 3: max(μ_GoodFood, μ_GoodService) = max(0.7, 0) = 0.7.

Step 3 (Implication): Clip the Low tip fuzzy set at 0.2, the Medium tip set at 0.6, and the High tip set at 0.7.

Step 4 (Aggregation): Take the max (union) of all three clipped output sets to form one combined fuzzy set.

Step 5 (Defuzzification): Apply the centroid method to find the center of gravity of the combined set. The result is the crisp tip percentage (e.g., approximately 19.6%).

### Sugeno Fuzzy Inference System

In the Sugeno (Takagi-Sugeno-Kang) FIS, the antecedent is a fuzzy set (same as Mamdani), but the consequent is a crisp mathematical function of the inputs rather than a fuzzy set.

**Rule format:** IF x is A AND y is B THEN z = f(x, y), where f is typically a constant (zero-order Sugeno) or a linear function (first-order Sugeno: z = ax + by + c).

**Steps:**

1. Fuzzification and rule evaluation are the same as Mamdani.
2. Each rule produces a crisp output value zᵢ = f(x, y) along with its firing strength wᵢ.
3. The final output is computed as a **weighted average**: z = Σ(wᵢ × zᵢ) / Σ(wᵢ).

**Advantages over Mamdani:** Computationally efficient because no complex defuzzification is needed. Well-suited for mathematical analysis, optimization, and control systems. Works well with linear techniques and adaptive methods (e.g., ANFIS).

**Disadvantage:** Less intuitive than Mamdani because the output rules are mathematical functions rather than linguistic terms.

### Tsukamoto Fuzzy Inference System

In the Tsukamoto FIS, each rule has a fuzzy set as the consequent, but the membership functions must be **monotonic** (either monotonically increasing or monotonically decreasing). Because of monotonicity, each rule's firing strength maps directly to a unique crisp output value.

**Steps:**

1. Fuzzification and rule evaluation are the same as Mamdani.
2. For each rule, the firing strength wᵢ is used to find a crisp value zᵢ by inverting the monotonic output membership function (i.e., finding the z where μ(z) = wᵢ).
3. The final output is a **weighted average**: z = Σ(wᵢ × zᵢ) / Σ(wᵢ).

**Advantage:** Produces a crisp output directly without aggregation or defuzzification of fuzzy sets.

**Limitation:** Restricted to monotonic output membership functions, which limits its expressiveness.

## 2.6.2 Defuzzification Techniques

Defuzzification converts the aggregated fuzzy output set into a single crisp numerical value. The main methods are:

1. **Centroid (Center of Gravity):** Calculates the center of mass of the aggregated fuzzy set. z* = ∫ z × μ(z) dz / ∫ μ(z) dz. It is the most commonly used method because it considers the entire shape of the output distribution. It produces smooth output changes.

2. **Bisector:** Finds the vertical line that divides the area of the aggregated fuzzy set into two equal halves. It is similar to the centroid but focuses on equal-area partitioning.

3. **Mean of Maxima (MOM):** Finds the average of all z values that have the maximum membership degree in the aggregated set. It is computationally simpler but ignores the shape of the output distribution.

4. **Smallest of Maxima (SOM):** Returns the smallest z value that has the maximum membership degree.

5. **Largest of Maxima (LOM):** Returns the largest z value that has the maximum membership degree.

6. **Weighted Average:** Used specifically in Sugeno and Tsukamoto systems. z* = Σ(wᵢ × zᵢ) / Σ(wᵢ), where wᵢ is the firing strength and zᵢ is the crisp output of the i-th rule. It is computationally the most efficient method.
