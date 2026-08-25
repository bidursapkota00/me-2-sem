# 3. Planning and Decision Making

# 3.1 STRIPS and PDDL

Classical planning deals with the problem of finding a sequence of actions that transforms an **initial state** into a **goal state**. It assumes the environment is fully observable, deterministic, static, and discrete.

**Planning vs. Problem-Solving Search:** In basic search, states and actions are treated as atomic (black boxes). In planning, states are represented using a **factored representation** — a set of variables (predicates) — which allows the planner to exploit the structure of the problem, making it far more efficient for complex domains.

## STRIPS (Stanford Research Institute Problem Solver)

STRIPS (1971) is both a planning system and a **formal language** for representing planning problems. It became the foundation for most modern planning languages.

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

PDDL is the **standard language** for expressing classical planning problems. It was introduced to provide a common input format for planning competitions and tools.

**PDDL separates the problem into two files:**

1. **Domain File:** Defines the predicates, types, and action schemas that describe the rules of the world. This is reusable across problem instances.
2. **Problem File:** Defines the specific objects, initial state, and goal for a particular instance.

**Relationship to STRIPS:** PDDL includes the STRIPS representation as a subset but extends it with additional features such as typing, conditional effects (when), universal quantification in preconditions, negative preconditions, and derived predicates.

**Planning Algorithms for Classical Planning:**

- **Forward (Progression) State-Space Search:** Start from the initial state, apply applicable actions to generate successors, and search forward until the goal is reached. Uses heuristics derived from the problem structure.
- **Backward (Regression) State-Space Search:** Start from the goal and work backward, finding actions whose effects match the goal, replacing them with their preconditions. Advantage: only considers relevant actions.
- **Planning Graphs (Graphplan):** Build a layered graph of alternating state levels and action levels, then extract a solution by backward search through the graph. Provides useful heuristics and can detect unsolvability.

---

# 3.2 Hierarchical Planning

> **Differentiate between hierarchical planning and probabilistic planning. (7) (Fall 2025)**

**Hierarchical Task Network (HTN) planning** addresses the complexity of planning by decomposing **high-level abstract tasks** into progressively simpler subtasks until only primitive actions remain. This mirrors how humans naturally solve complex problems — breaking them into manageable steps.

**Key Concepts:**

- **Primitive Actions:** Low-level actions that can be directly executed (same as classical planning actions).
- **High-Level Actions (HLAs):** Abstract tasks that need to be refined (decomposed) before execution.
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
- **Discount Factor (γ):** A value between 0 and 1 that determines the importance of future rewards. γ close to 0 makes the agent myopic; γ close to 1 makes it far-sighted.

**Key Difference from Classical Planning:** Instead of finding a fixed **action sequence**, an MDP solution is a **policy** π: S → A — a mapping from every state to the best action to take in that state. A policy handles uncertainty because the agent can react to whichever state it actually ends up in.

**Optimal Policy:** The policy π* that maximizes the **expected cumulative discounted reward:** E[Σ γ^t R(s_t)].

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

**Multi-agent planning** extends single-agent planning to environments containing **multiple autonomous agents**, each with their own sensors, actuators, goals, and possibly different knowledge about the world. The agents must coordinate their actions to achieve individual or shared objectives.

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
- **Adversarial Search:** Minimax and related algorithms (from game playing) are used for zero-sum competitive scenarios.

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

**Axioms of Utility (Von Neumann–Morgenstern):**

1. **Orderability:** For any two states, either A ≻ B, B ≻ A, or A ~ B.
2. **Transitivity:** If A ≻ B and B ≻ C, then A ≻ C.
3. **Continuity:** If A ≻ B ≻ C, there exists some probability p such that B ~ [p, A; (1−p), C].
4. **Substitutability:** If A ~ B, then A can replace B in any lottery without changing the preference.
5. **Monotonicity:** If A ≻ B, then a higher probability of A is preferred: [p, A; (1−p), B] ≻ [q, A; (1−q), B] iff p > q.
6. **Decomposability:** Compound lotteries can be reduced to simple lotteries using probability rules.

If these axioms hold, there exists a utility function such that the agent's preferences are captured by **Maximum Expected Utility (MEU):** choose the action that maximizes E[U] = Σ P(outcome_i | action) × U(outcome_i).

## 3.5.1 Utility Functions

A utility function assigns numerical values to states, reflecting the agent's preferences. It encapsulates the agent's attitude toward risk:

- **Risk-neutral:** Utility is a linear function of monetary value. U(x) = x.
- **Risk-averse:** Utility is a concave function. The agent prefers a certain outcome over a gamble with the same expected value. U(x) = √x.
- **Risk-seeking:** Utility is a convex function. The agent prefers the gamble. U(x) = x².

**Example:** An agent must choose between (A) receiving $100 for certain, or (B) a 50% chance of $200 and 50% chance of $0. Expected monetary value of both is $100. A risk-neutral agent is indifferent. A risk-averse agent prefers (A). A risk-seeking agent prefers (B).

## 3.5.2 Multi-Attribute Utility Functions

Real-world decisions involve outcomes described by **multiple attributes** (e.g., cost, safety, time, quality). Multi-attribute utility theory provides methods for combining preferences across multiple dimensions.

**Dominance:**

- **Strict Dominance:** Option A dominates option B if A is better than B on every attribute. Choose A.
- **Stochastic Dominance:** Option A stochastically dominates B if, for every utility level, the probability of achieving at least that level is higher with A.

**Preference Independence:** Attribute X is **preferentially independent** of attribute Y if preferences over outcomes of X do not depend on the value of Y. If all attributes are mutually preferentially independent, the multi-attribute utility can be decomposed:

**Additive Utility Function:** U(x₁, x₂, ..., x_n) = Σ w_i × U_i(x_i), where w_i are weights reflecting relative importance of each attribute. This is the simplest form and applies when attributes are additively independent.

**Multiplicative Utility Function:** Used when attributes are not fully additively independent but satisfy mutual utility independence. It introduces interaction terms between attributes.

---

# 3.6 Decision Networks

> **What is a decision network? Explain its components with an example. (8) (Spring 2025)**

A **decision network** (also called an **influence diagram**) is a graphical representation that extends Bayesian networks to incorporate decision-making under uncertainty. It combines probability (uncertainty), actions (decisions), and preferences (utilities) into a single framework.

**Components of a Decision Network:**

**1. Chance Nodes (Ovals):** Represent random variables with uncertain values, exactly like nodes in a Bayesian network. Each chance node has a conditional probability table (CPT). Example: Weather (Sunny, Rainy), Oil_Amount (Large, Small, None).

**2. Decision Nodes (Rectangles):** Represent points where the agent must choose an action. The agent has full control over the value of decision nodes. Arrows pointing into a decision node indicate information available to the agent when making that decision. Example: Drill_Decision (Drill, Don't Drill).

**3. Utility Nodes (Diamonds):** Represent the agent's utility (payoff) function. A utility node's parents are all the variables (chance and decision) that directly affect the agent's utility. The utility node contains a table mapping each combination of parent values to a utility value. Example: Profit depends on both Drill_Decision and Oil_Amount.

**Evaluating a Decision Network:**

1. Set the evidence variables (observed values).
2. For each possible value of the decision node, compute the expected utility by summing over all possible outcomes of the chance nodes, weighted by their probabilities.
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

**Formalization using MDP:** A sequential decision problem is formalized as an MDP (defined in Section 3.3). The agent seeks a policy π* that maximizes the expected sum of discounted future rewards.

**Bellman Equation:** Expresses the utility of a state recursively:

U(s) = R(s) + γ × max_a Σ_{s'} P(s' | s, a) × U(s')

This states: the utility of a state equals the immediate reward plus the discounted expected utility of the best action's outcomes.

**Example — Grid World:** An agent navigates a 4×3 grid with a reward of +1 at one terminal state and −1 at another. Each move has a 0.8 probability of going in the intended direction and 0.1 probability of going to each perpendicular direction. The optimal policy tells the agent which direction to move in each cell to maximize expected cumulative reward.

## 3.6.2 Algorithms for MDPs

**1. Value Iteration:**

1. Initialize U(s) = 0 for all states (or arbitrary values).
2. Repeat until convergence (max change < ε):
   - For each state s: U_{i+1}(s) = R(s) + γ × max_a Σ_{s'} P(s' | s, a) × U_i(s')
3. Extract the optimal policy: π*(s) = argmax_a Σ_{s'} P(s' | s, a) × U(s')

Value iteration is guaranteed to converge. The number of iterations depends on γ and the desired precision ε. Time complexity per iteration: O(|S|² × |A|).

**2. Policy Iteration:**

1. Initialize with an arbitrary policy π.
2. **Policy Evaluation:** Compute the utility of each state under the current policy by solving a system of linear equations: U^π(s) = R(s) + γ × Σ_{s'} P(s' | s, π(s)) × U^π(s').
3. **Policy Improvement:** For each state, check if there is an action that yields a higher expected utility than the current policy. If so, update the policy.
4. Repeat steps 2–3 until the policy no longer changes (convergence).

Policy iteration often converges in fewer iterations than value iteration, but each iteration is more expensive (requires solving a linear system).

## 3.6.3 Partially Observable MDP (POMDP)

A **POMDP** extends the MDP framework to environments where the agent **cannot directly observe the current state**. Instead, the agent receives partial observations that provide incomplete information about the true state.

**A POMDP is defined by:**

- **States (S), Actions (A), Transition Model P(s' | s, a), Reward R(s):** Same as MDP.
- **Observations (O):** A finite set of possible observations.
- **Observation Model P(o | s', a):** The probability of observing o after taking action a and arriving in state s'.

**Belief State:** Since the agent cannot observe the true state, it maintains a **belief state** b — a probability distribution over all possible states. b(s) represents the agent's probability estimate that the current state is s.

**Belief Update:** After taking action a and receiving observation o, the belief is updated using Bayes' rule:

b'(s') = α × P(o | s', a) × Σ_s P(s' | s, a) × b(s)

where α is a normalizing constant.

**Solving POMDPs:** A POMDP can be converted into a **belief-state MDP** — an MDP where the states are belief states. The agent's policy maps belief states to actions: π: B → A. However, the belief space is continuous (a probability simplex), making exact solutions intractable for all but very small problems.

**Approximate Methods:** Point-based value iteration, Monte Carlo methods, and online planning algorithms are used for practical POMDP solving.

**Example:** A robot in a building cannot directly see which room it is in (partial observability). It has a belief distribution over rooms. It takes actions (move left, move right) and receives observations (wall sensor readings). After each action and observation, it updates its belief state and selects the next action based on the updated belief.
