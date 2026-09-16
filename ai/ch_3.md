# 3. Planning and Decision Making

# 3.1 STRIPS and PDDL

Classical planning deals with the problem of finding a sequence of actions that transforms an **initial state** into a **goal state**. It assumes the environment is fully observable, deterministic, static, and discrete.

**Planning vs. Problem-Solving Search:** In regular search, we treat each situation/states like a closed box — we don't look inside. In planning, we break down each situation into smaller facts (like "Robot is at location A" and "Block B has nothing on top"). This makes it much easier to find solutions.

## STRIPS (Stanford Research Institute Problem Solver)

STRIPS is one of the earliest planning systems (made in 1971). Think of it as a simple and formal language to describe planning problems.

**A STRIPS problem is defined by:**

1. **Initial State:** A conjunction of ground atoms (positive literals) describing the world at the start. Example: At(Robot, A) ∧ Clear(B).
2. **Goal State:** A conjunction of literals that must be true in the final state. Example: At(Robot, B).
3. **Actions (Operators):** Each action is defined by an **action schema** with three components:
   - **Preconditions:** A conjunction of literals that must be true before the action can be executed.
   - **Add List (Positive Effects):** Atoms that become true after the action.
   - **Delete List (Negative Effects):** Atoms that become false after the action.

**Example — Block World:**

```
Action: Move(block, from, to)
  Precondition: On(block, from) ∧ Clear(block) ∧ Clear(to)
  Add List: On(block, to) ∧ Clear(from)
  Delete List: On(block, from) ∧ Clear(to)
```

**Closed-World Assumption:** Any atom not mentioned in a state is assumed false. Effects not mentioned in add/delete lists remain unchanged (frame assumption handled implicitly).

## PDDL (Planning Domain Definition Language)

PDDL is a newer, more powerful standard language for describing planning problems. Think of it as an upgraded version of STRIPS. It was introduced to provide a common input format for planning competitions and tools.

**PDDL separates the problem into two files:**

1. **Domain File:** Defines the predicates, types, and action schemas that describe the rules of the world. This is reusable across problem instances.
2. **Problem File:** Defines the specific objects, initial state, and goal for a particular instance.

**Relationship to STRIPS:** PDDL includes the STRIPS representation as a subset but extends it with additional features such as typing, conditional effects (when), universal quantification in preconditions, negative preconditions, and derived predicates.

**Planning Algorithms for Classical Planning: How do we actually find the plan? (Planning Methods)**

- **Forward (Progression) State-Space Search:** Start from the initial state, apply applicable actions to generate successors, and search forward until the goal is reached. Uses heuristics derived from the problem structure.
- **Backward (Regression) State-Space Search:** Start from the goal and work backward, finding actions whose effects match the goal, replacing them with their preconditions. Advantage: only considers relevant actions.
- **Planning Graphs (Graphplan):** Build a special diagram that shows which actions and facts are possible at each step, then find a solution from the diagram.

---

# 3.2 Hierarchical Planning

> **Differentiate between hierarchical planning and probabilistic planning. (7) (Fall 2025)**

**Hierarchical Task Network (HTN) planning** addresses the complexity of planning by decomposing **high-level abstract tasks** into progressively simpler subtasks until only primitive actions remain. This mirrors how humans naturally solve complex problems — breaking them into manageable steps.

**Key Concepts:**

- **Primitive Actions:** Low-level actions that can be directly executed (like "pick up a glass").
- **High-Level Actions (HLAs):** Abstract tasks that need to be refined (decomposed) before execution (like "make dinner").
- **Methods (Refinements):** Domain-specific recipes that define how a high-level action can be decomposed into a sequence of subtasks (which may be further HLAs or primitives).

**Algorithm:**

1. Start with the initial plan containing high-level actions.
2. Select an HLA in the plan.
3. Choose an applicable method (decomposition) for that HLA.
4. Replace the HLA with the method's subtask sequence.
5. Repeat until the plan contains only primitive actions.
6. Verify that the resulting primitive plan achieves the goal from the initial state.

**Example — Travel Planning:**

```
HLA: Travel(Home, Office)
  Method 1: [Walk(Home, BusStop), RideBus(BusStop, Office)]
  Method 2: [Drive(Home, Office)]

HLA: Drive(Home, Office)
  Method: [GetInCar, StartEngine, Navigate(Home, Office), Park]
```

**Advantages of HTN Planning:**

- **Efficiency:** Hierarchical decomposition drastically prunes the search space by using domain knowledge encoded in methods.
- **Expressiveness:** Can represent complex procedures and constraints that are difficult to express in flat classical planning.
- **Scalability:** Scales well to large, real-world planning problems because the hierarchy provides natural structure.

**Limitations:** Requires expert-defined methods (domain knowledge). The quality of the solution depends on the quality of the decomposition recipes provided.

---

# 3.3 Probabilistic Planning

> **Write a short note on Probabilistic Planning. (5) (Internal 2025)**

In many real-world environments, actions have **uncertain outcomes** — the result of an action is not fully predictable. **Probabilistic planning** extends classical planning to handle stochastic environments where actions may lead to different successor states with known probabilities.

The standard framework for probabilistic planning is the **Markov Decision Process (MDP)**.

**An MDP is defined by:**

- **States (S):** A finite set of world states.
- **Actions (A):** A finite set of actions available to the agent.
- **Transition Model P(s' | s, a):** The probability of reaching state s' when taking action a in state s. This captures the stochasticity of the environment.
- **Reward Function R(s):** The immediate reward (or cost) the agent receives in state s. Sometimes written as R(s, a) or R(s, a, s').
- **Discount Factor (γ):** A number between 0 and 1 that decides how much the agent cares about future rewards vs. immediate rewards. Close to 1 = thinks long-term. Close to 0 = only cares about right now.

**Difference from Classical Planning:**

- Classical planning gives you a fixed list of steps: "Do A, then B, then C"
- Probabilistic planning gives you a policy — a rule that says "if you're in THIS situation, do THIS action." It's like a strategy guide, not a recipe.

**Optimal Policy:** The best possible policy — the one that earns the most reward on average over time. maximizes the **expected cumulative discounted reward.**

**Differences between Hierarchical and Probabilistic Planning:**

- **Environment:** Hierarchical planning typically assumes deterministic environments; probabilistic planning explicitly handles stochastic outcomes.
- **Solution Form:** Hierarchical planning produces an action sequence (plan); probabilistic planning produces a policy (state-to-action mapping).
- **Knowledge Required:** Hierarchical planning requires expert-defined decomposition methods; probabilistic planning requires transition probabilities and rewards.
- **Goal:** Hierarchical planning decomposes complex tasks for efficiency; probabilistic planning optimizes expected utility under uncertainty.
- **Approach:** Hierarchical planning uses task decomposition; probabilistic planning uses dynamic programming (value/policy iteration).

---

# 3.4 Multi-Agent Planning

> **What is multi-agent planning in AI? Discuss the challenges of coordination and communication between agents. (7) (Internal 2025)**
>
> **Why do we require Multi-agent Planning in AI? Give an overview of Multiagent System Architecture and discuss how agents can work in Cooperative & Competitive environments. (8) (Fall 2025)**
>
> **Write a short note on Multi-agent planning in AI. (5) (Spring 2025)**

**Multi-agent planning** extends single-agent planning to environments containing **multiple autonomous agents**, each with their own sensors, actuators, goals, and possibly different knowledge about the world. The agents must coordinate their actions to achieve individual or shared objectives. Multi-agent planning is about how multiple agents work together or compete with each other.

**Why Multi-Agent Planning is Required:**

- Many real-world problems inherently involve multiple agents (robots in a warehouse, autonomous vehicles, distributed sensor networks).
- Tasks may be too complex or geographically distributed for a single agent.
- Multiple agents can work in parallel, improving efficiency and robustness.
- Some environments are inherently competitive (markets, games), requiring strategic reasoning about other agents.

**Multi-Agent System (MAS) Architecture:**

- **Reactive Architecture:** Agents use simple stimulus-response rules without internal models. Fast but limited reasoning. Example: swarm robotics.
- **Deliberative Architecture:** Agents maintain an internal model of the world and plan their actions using symbolic reasoning. More capable but computationally heavier.
- **Hybrid Architecture:** Combines reactive and deliberative layers — a reactive layer for fast responses and a deliberative layer for complex planning.
- **BDI (Belief-Desire-Intention):** Agents maintain beliefs (knowledge about the world), desires (goals), and intentions (committed plans). They select intentions based on current beliefs and desires.

**Cooperative Environments:**

In cooperative settings, agents share a common goal or benefit from working together. Key mechanisms:

- **Joint Planning:** Agents construct plans together, either through a centralized planner or distributed planning protocols.
- **Task Allocation:** Dividing the overall task among agents based on capabilities and availability (e.g., Contract Net Protocol — agents bid on tasks).
- **Communication:** Agents share information about their states, plans, and observations to maintain coordination.
- **Shared Mental Models:** Agents maintain compatible beliefs about the world and each other's plans to ensure coherent joint action.

**Competitive Environments:**

In competitive settings, agents have conflicting goals — one agent's gain may be another's loss. Key concepts:

- **Game Theory:** Used to analyze strategic interactions. Agents reason about opponents' strategies.
- **Nash Equilibrium:** A set of strategies where no agent can improve its outcome by unilaterally changing its strategy.
- **Adversarial Search:** Algorithms like Minimax — "I assume my opponent will play their best move, so I pick the move that's best for me even in that worst case"

**Challenges of Coordination and Communication:**

1. **Communication Overhead:** Exchanging plans and observations consumes bandwidth and time. Too much communication slows agents; too little leads to miscoordination.
2. **Partial Observability:** Each agent may have incomplete information about the environment and about other agents' states and intentions.
3. **Conflicting Goals:** Even in cooperative settings, agents may have partially conflicting sub-goals requiring negotiation and compromise.
4. **Scalability:** As the number of agents grows, the joint action space grows exponentially, making centralized planning intractable.
5. **Synchronization:** Agents must coordinate the timing of their actions. Without proper synchronization, agents may interfere with each other.
6. **Trust and Reliability:** Agents must handle the possibility that other agents may fail, communicate inaccurate information, or act selfishly.
7. **Dynamic Environment:** The environment may change due to other agents' actions, requiring constant re-planning and adaptation.

---

# 3.5 Utility Theory

**Utility theory** provides the formal mathematical framework for rational decision-making under uncertainty. It defines how a rational agent should quantify preferences and make choices when outcomes are uncertain.

**Key Principles:**

- **Preferences:** A rational agent has preferences over outcomes (states of the world). If an agent prefers outcome A to outcome B, we write A ≻ B. If indifferent, A ~ B.
- **Utility Function U(s):** Maps each state to a real number representing its desirability. Higher utility = more preferred. If A ≻ B, then U(A) > U(B).
- **Lotteries:** An uncertain outcome is modeled as a lottery [p, A; (1−p), B] — outcome A with probability p and outcome B with probability (1−p).

**\*\*Axioms of Utility (Von Neumann–Morgenstern):**

1. **Orderability:** For any two states, either A ≻ B, B ≻ A, or A ~ B.
2. **Transitivity:** If A ≻ B and B ≻ C, then A ≻ C.
3. **Continuity:** If A ≻ B ≻ C, there exists some probability p such that B ~ [p, A; (1−p), C].
4. **Substitutability:** If A ~ B, then A can replace B in any lottery without changing the preference.
5. **Monotonicity:** If A ≻ B, then a higher probability of A is preferred: [p, A; (1−p), B] ≻ [q, A; (1−q), B] iff p > q.
6. **Decomposability:** Compound lotteries can be reduced to simple lotteries using probability rules.

If these axioms hold, there exists a utility function such that the agent's preferences are captured by **Maximum Expected Utility (MEU):** choose the action that maximizes E[U] = Σ P(outcome_i | action) × U(outcome_i).

## 3.5.1 Utility Functions

A utility function assigns numerical values to states, reflecting the agent's preferences. It encapsulates the agent's attitude toward risk:

- **Risk-neutral:** You only care about the average. Rs.100 for sure = 50% chance of Rs.200 (same average). U(x) = x.
- **Risk-averse:** You prefer safety. You'd take Rs.100 for sure rather than a 50/50 shot at Rs.200 or nothing. U(x) = √x. (Most people are like this!)
- **Risk-seeking:** You love gambling. You'd take the 50/50 chance over the safe Rs.100. U(x) = x².

**Example:** An agent must choose between (A) receiving $100 for certain, or (B) a 50% chance of $200 and 50% chance of $0. Expected monetary value of both is $100. A risk-neutral agent is indifferent. A risk-averse agent prefers (A). A risk-seeking agent prefers (B).

## 3.5.2 Multi-Attribute Utility Functions

Real-world decisions involve outcomes described by **multiple attributes** (e.g., cost, safety, time, quality). Multi-attribute utility theory provides methods for combining preferences across multiple dimensions.

**Dominance:**

- **Strict Dominance:** Option A dominates option B if A is better than B on every attribute. Choose A.
- **Stochastic Dominance:** Option A gives you a better chance of a good outcome at every level, pick A.

**Preference Independence:** Attribute X is **preferentially independent** of attribute Y if preferences over outcomes of X do not depend on the value of Y. If all attributes are mutually preferentially independent, the multi-attribute utility can be decomposed:

**Combining Factors:**

**Preference Independence:** If your preference for one factor doesn't depend on the others (e.g., you always prefer cheaper regardless of location), then you can use a simple formula:

**Additive Utility Function:** Total Score = (Weight₁ × Score on Factor 1) + (Weight₂ × Score on Factor 2) + ...

Example for choosing a college:

- Total = 0.3 × (cost score) + 0.25 × (reputation score) + 0.2 × (location score) + 0.25 × (campus life score)

The weights (0.3, 0.25, etc.) show how important each factor is to you.

If factors affect each other (e.g., you only care about campus life if the cost is affordable), you need a **multiplicative utility function** which is more complex.

---

# 3.6 Decision Networks

> **What is a decision network? Explain its components with an example. (8) (Spring 2025)**

A decision network (also called an influence diagram) is a diagram that helps an agent make decisions when things are uncertain. It combines probability (uncertainty), actions (decisions, choices), and preferences (utilities) into a single framework.

**Components of a Decision Network:**

**1. Chance Nodes (Ovals):** Represent random variables with uncertain values, exactly like nodes in a Bayesian network. Each chance node has a conditional probability table (CPT). Example: Weather (60% Sunny, 40% Rainy), Oil Underground (20% Large, 30% Small, 50% None).

**2. Decision Nodes (Rectangles):** Represent points where the agent must choose an action. The agent has full control over the value of decision nodes. Arrows pointing into a decision node indicate information available to the agent when making that decision. Example: Drill_Decision (Drill, Don't Drill) Take umbrella or not.

**3. Utility Nodes (Diamonds):** Represent the agent's utility (payoff) function. The "payoff" — how good or bad each outcome is for you. It depends on both the uncertain events and your decisions. Example: Profit depends on both Drill_Decision and Oil_Amount.

**Evaluating a Decision Network:**

1. Set the evidence variables (observed values).
2. For each possible value of the decision node (choice), compute the expected utility by summing over all possible outcomes of the chance nodes, weighted by their probabilities.
3. Choose the decision that maximizes expected utility.

**Example — Oil Drilling Decision:**

- Chance node: Oil_Amount = {Large, Small, None} with prior probabilities P(Large)=0.2, P(Small)=0.3, P(None)=0.5.
- Decision node: Action = {Drill, Don't Drill}.
- Utility node: If Drill and Large → profit $500K; Drill and Small → profit $100K; Drill and None → loss −$200K; Don't Drill → $0.

EU(Drill) = 0.2(500) + 0.3(100) + 0.5(−200) = 100 + 30 − 100 = $30K.
EU(Don't Drill) = $0.

Since EU(Drill) > EU(Don't Drill), the rational decision is to **Drill**.

The network can be extended with additional chance nodes (e.g., a Seismic Test result that provides partial information about Oil_Amount), allowing the agent to compute the **value of information** — how much the test result would change the decision.

## 3.6.1 Sequential Decision Problems

When an agent must make a **series of decisions over time**, each decision potentially affecting future states and future decisions, we have a **sequential decision problem**. The outcome depends on the entire sequence of decisions and the stochastic transitions between states.

**Formalization using MDP:** A sequential decision problem is formalized as an MDP (defined in Section 3.3). The agent seeks a policy π\* that maximizes the expected sum of discounted future rewards.

**Bellman Equation:** Expresses the utility of a state recursively:

$$
U(s)=R(s)+\gamma \times \max_a \sum_{s'}P(s'|s,a)U(s')
$$

This states: the utility of a state equals the immediate reward plus the discounted expected utility of the best action's outcomes.

**Example:**

Current state: s = At(Home)

Actions:
a₁ = GoToCollege
a₂ = GoToPark
a₃ = StayHome

```text
s = At(Home)
a = GoToCollege
```

Because the environment is uncertain:

```text
P(College | Home, GoToCollege) = 0.8
P(Traffic | Home, GoToCollege)  = 0.2
```

So there is an **80% chance** of reaching College and a **20% chance** of ending up in Traffic.

### 3. `U(s')` — utility of the next state

`s'` means the **next state**.

`U(s')` means:

> How valuable/good is that next state?

Suppose:

```text
U(College) = 100
U(Traffic) = 20
```

Then:

$$
P(College|Home,GoToCollege)U(College)
$$

$$
=0.8\times100=80
$$

and

$$
P(Traffic|Home,GoToCollege)U(Traffic)
$$

$$
=0.2\times20=4
$$

Add them:

$$
80+4=84
$$

So **84 is the expected future utility** of choosing `GoToCollege`.

## 3.6.2 Algorithms for MDPs

**How do we actually find the best policy?**

**Method 1: Value Iteration**

Think of it as a "guessing game" where you keep improving your guesses:

1. Start by guessing that every state has a value of 0
2. Update each state's value using the Bellman formula
3. Keep repeating until the values barely change anymore
4. Once you have the final values, the best action in each state is the one that leads to states with the highest value

It's guaranteed to find the right answer eventually!

**Method 2: Policy Iteration**

Instead of guessing values, you guess a whole strategy and keep improving it:

1. Start with any strategy (even a random one)
2. **Evaluate:** Calculate how good each state is if you follow this strategy
3. **Improve:** For each state, check if a different action would be better. If yes, update the strategy.
4. Repeat steps 2-3 until the strategy stops changing

This usually needs fewer rounds than Value Iteration, but each round takes more work.

## 3.6.3 Partially Observable MDP (POMDP)

A **POMDP** extends the MDP framework to environments where the agent **cannot directly observe the current state**. Instead, the agent receives partial observations that provide incomplete information about the true state.

A robot might not know exactly which room it's in — it can only see walls nearby and guess.

**A POMDP is defined by:**

- **States (S), Actions (A), Transition Model P(s' | s, a), Reward R(s):** Same as MDP.
- **Observations (O):** A finite set of possible observations.
- **Observation Model P(o | s', a):** The probability of observing o after taking action a and arriving in state s'.

Example: "If I'm in the kitchen, there's a 90% chance I see a stove, 10% chance I don't"

**Belief State:** Since the agent cannot observe the true state, it maintains a **belief state** b — a probability distribution over all possible states. b(s) represents the agent's probability estimate that the current state is s.

Example: "I think there's a 60% chance I'm in the kitchen and 40% chance I'm in the living room."

**How does it update its beliefs?**

After taking an action and seeing an observation:

1. "Given my previous belief, what action I took, and what I observed, where am I most likely now?"
2. Use Bayes' rule (a probability formula) to update the belief

**The Challenge:** Solving POMDPs is VERY hard because the "belief state" is continuous (there are infinite possible beliefs). For big problems, we use approximate methods that find "good enough" answers. Point-based value iteration, Monte Carlo methods.

**Example:**
A robot is in a building but doesn't know which room it's in. It has a rough idea (belief). It moves left and its wall sensors detect "wall on the right." Using this observation, it updates its belief — "Oh, there's a wall on my right, so I'm probably in the hallway, not the open hall." Then it chooses its next action based on this updated belief.
