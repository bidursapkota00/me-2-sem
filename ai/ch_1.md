# 1. Foundation of Advanced Artificial Intelligence

# 1.1 Intelligent Agents — Structure, Types and Implementation

> **Define an intelligent agent. Discuss different types of agents with example. (7) (Fall 2025)**
>
> **Write a short note on Learning Agent. (5) (Internal 2025)**

An **intelligent agent** is anything that perceives its environment through **sensors** and acts upon it through **actuators**. A human agent has eyes, ears (sensors) and hands, legs, vocal tract (actuators). A robotic agent has cameras, infrared sensors and motors, grippers. A software agent receives keystrokes, file contents and displays output, writes files.

<!-- The agent function maps a percept sequence to an action: **f: P* → A**. The agent program is the concrete implementation running on a physical architecture. Agent = Architecture + Program. -->

**Rationality:** A rational agent selects the action that maximizes its expected performance measure, given the percept sequence and built-in knowledge. Rationality **≠ omniscience (knowing everything) and ≠ perfection (always correct outcomes).** A rational agent should be **autonomous — it learns from experience rather than relying solely on prior knowledge.**

**PEAS Framework:** To design an agent, we specify its task environment using PEAS:

- **P — Performance Measure:** Criteria for success (e.g., safe, fast, legal driving for a taxi agent).
- **E — Environment:** The world the agent operates in (e.g., roads, traffic, pedestrians).
- **A — Actuators:** Mechanisms to take actions (e.g., steering, accelerator, brake, signal).
- **S — Sensors:** Devices to perceive the environment (e.g., cameras, GPS, speedometer).

**Environment Properties:**

1. **Fully observable vs. Partially observable:** Whether sensors detect all relevant aspects of the environment state.
2. **Deterministic vs. Stochastic:** Whether the next state is completely determined by the current state and action.
3. **Episodic vs. Sequential:** Whether the agent's experience is divided into independent episodes or current decisions affect future ones.
4. **Static vs. Dynamic:** Whether the environment changes while the agent deliberates.
5. **Discrete vs. Continuous:** Whether there are a finite number of distinct states, percepts, and actions.
6. **Single agent vs. Multi-agent:** Whether the environment contains other agents (cooperative or competitive).
7. **Known vs. Unknown:** Whether the agent knows the rules/laws governing the environment.

**Types of Agents:**

**1. Simple Reflex Agents:** Act based only on the current percept using condition-action rules (if-then rules), ignoring percept history. They work only in fully observable environments. Example: a thermostat that turns on heating when temperature drops below a threshold.

**2. Model-Based Reflex Agents:** Maintain an internal state (model of the world) to handle partial observability. The internal state is updated using knowledge of how the world evolves and how the agent's actions affect the world. Example: a self-driving car that tracks the positions of other vehicles even when they are temporarily occluded.

**3. Goal-Based Agents:** Beyond knowing the current state, these agents have goal information that describes desirable states. They use search and planning to find action sequences leading to the goal. More flexible than reflex agents because the goal can be changed without rewriting rules. Example: a navigation agent planning a route from source to destination.

**4. Utility-Based Agents:** Use a utility function that maps a state to a real number indicating the degree of "happiness." When multiple action sequences achieve the goal, the agent chooses the one that maximizes expected utility. Handles trade-offs (e.g., faster but riskier vs. slower but safer routes). Example: a taxi agent that balances speed, safety, fuel cost, and passenger comfort.

**5. Learning Agents:** Have four conceptual components:

- **Learning element:** Makes improvements based on feedback from the critic.
- **Performance element:** Selects external actions (this is the previously described agent).
- **Critic:** Provides feedback on how the agent is doing relative to a fixed performance standard.
- **Problem generator:** Suggests exploratory actions that may lead to new and informative experiences.

Example: a chess-playing agent that starts with basic rules, plays games, learns from wins and losses, and improves its strategy over time.

---

# 1.2 Advanced Search Techniques

> **Why is the bidirectional A\* search more efficient than the standard A\* search? Illustrate with a suitable example. (7) (Spring 2025)**
>
> **What are the limitations of A\* search? How does the iterative deepening search resolve these problems? (7) (Internal 2025)**

**A\* Search (Recap):** A\* is a best-first search that uses the evaluation function **f(n) = g(n) + h(n)**, where g(n) is the path cost from start to node n, and h(n) is the heuristic estimate from n to the goal.

<!-- A\* is complete and optimal when the heuristic is admissible (never overestimates) and consistent (h(n) ≤ c(n,a,n') + h(n')). -->

**Limitations of A\*:** A\* stores all generated nodes in memory (both OPEN and CLOSED lists). Its space complexity is O(b^d), which makes it impractical for large state spaces — it often runs out of memory before running out of time.

## 1.2.1 Bidirectional A\* Search

Bidirectional A\* runs two simultaneous searches: one **forward** from the initial state and one **backward** from the goal state, until the two search frontiers meet. Each direction uses the A\* evaluation function.

**Why more efficient:** If the branching factor is b and the solution depth is d, standard A\* explores O(b^d) nodes. Bidirectional search explores roughly O(2 × b^(d/2)) = O(b^(d/2)) nodes, which is exponentially smaller.

**Working:**

1. Maintain two open lists: OPEN_F (forward) and OPEN_B (backward).
2. Alternate expanding the node with the smallest f-value from each frontier.
3. When a node appears in both the forward and backward CLOSED lists, a solution path is found.
4. The algorithm must verify this is the optimal path by checking if the sum g_F(n) + g_B(n) for the meeting node is ≤ the minimum f-value in either open list.

**Example:** Finding shortest path from city A to city Z in a road network. Forward search explores from A; backward search explores from Z. They meet at some intermediate city M, producing path A→...→M→...→Z. Instead of exploring the entire space from A to Z, each direction only explores roughly half the depth.

**Challenges:** Requires a well-defined way to search backward (predecessor generation), and selecting which frontier to expand next is non-trivial.

## 1.2.2 Iterative Deepening A\* (IDA\*)

IDA\* combines the optimality of A\* with the space efficiency of depth-first search. It performs a series of depth-first searches, each with an increasing f-cost limit (threshold), instead of a depth limit.

**Algorithm:**

1. Set the initial threshold = h(start).
2. Perform a depth-first search, pruning any node where f(n) > threshold.
3. If the goal is found, return the solution.
4. Otherwise, set the new threshold = minimum f-value among all nodes that exceeded the previous threshold.
5. Repeat until a solution is found.

**Properties:**

- **Space complexity:** O(bd) — linear, like depth-first search, since it does not store the frontier.
- **Optimality:** Guaranteed when the heuristic is admissible.
- **Time complexity:** May revisit nodes in successive iterations, but the overhead is usually small because most nodes are at the deepest level.

IDA\* resolves A\*'s memory problem by trading space for time — it uses only linear memory while still finding optimal solutions.

## 1.2.3 Online Search

In **offline search**, the agent computes a complete solution before taking any action. In **online search**, the agent interleaves computation and action — it must act before knowing the full search space. Online search is necessary in **unknown or partially observable environments** where the agent discovers the state space by exploring.

**Online DFS Agent:** Maintains a map of states it has visited and the results of actions taken. It uses depth-first exploration, backtracking when it reaches dead ends. It maintains an untried list for each state (actions not yet attempted) and an unbacktracked list (states from which it hasn't backtracked).

**Key characteristics:**

- The agent cannot plan ahead because the transition model is unknown.
- Competitive ratio measures online algorithm quality: the ratio of the online path cost to the actual optimal path cost.
- Learning real-time A\* (LRTA\*) is an online version that updates heuristic estimates based on experience, eventually finding optimal paths.

---

# 1.3 Local Search

> **Why are the local searches more space-efficient? Why may the hill-climbing search get stuck in local maximum? How can this be resolved? (8) (Spring 2025)**
>
> **How does the simulated annealing resolve the problems of local hill-climbing search? Apply the simulated annealing to optimize a function: f(x) = −x² + 4x. (8) (Internal 2025)**
>
> **What is the idea behind the local beam search? Illustrate with a suitable example. (Internal 2025)**

Local search algorithms operate on a **single current state** (or a small set of states) and move to neighboring states. They do not maintain a search tree or track paths. They are useful for **optimization problems** where the goal is to find the best state according to an objective function, and the path to the solution is irrelevant.

**Advantages:** Use very little memory (constant space) and can find reasonable solutions in large or infinite state spaces where systematic search is impractical.

**State-space landscape:** Visualized as a surface where each point is a state, the height is the objective function value, and the agent moves across the landscape trying to find the highest peak (maximum) or lowest valley (minimum).

## 1.3.1 Hill-Climbing Search

Also called **greedy local search**, it continuously moves to the neighboring state with the highest value (for maximization). It terminates when no neighbor has a higher value than the current state.

**Algorithm:**

1. Start with an initial state (current).
2. Generate all neighbors of current.
3. If the best neighbor is better than current, move to it. Otherwise, stop.

**Problems (why it gets stuck):**

1. **Local maxima:** A peak that is higher than all its neighbors but not the global maximum. The algorithm stops here, thinking it has found the best.
2. **Ridges:** A sequence of local maxima that makes it difficult for greedy moves to navigate.
3. **Plateaus (flat regions):** Areas where neighboring states have the same value. The algorithm cannot determine which direction to move. A plateau may be a shoulder (eventually leads upward) or a flat local maximum.

**Variants to mitigate these issues:**

- **Stochastic hill climbing:** Chooses randomly among uphill moves, with probability proportional to steepness. Slower convergence but may escape some local maxima.
- **First-choice hill climbing:** Generates successors randomly until one is better than current. Useful when a state has many successors.
- **Random-restart hill climbing:** Conducts a series of hill-climbing searches from randomly generated initial states. Complete with probability approaching 1. If each search has probability p of finding the global maximum, the expected number of restarts is 1/p.

## 1.3.2 Simulated Annealing

Simulated annealing resolves the local maxima problem of hill climbing by allowing **"downhill" moves** (moves to worse states) with a probability that decreases over time. It is inspired by the metallurgical process of annealing — heating metal and slowly cooling it to reach a low-energy crystalline state.

**Algorithm:**

1. Start with initial state and a high temperature T.
2. At each step, pick a random neighbor.
3. If the neighbor is better (ΔE > 0), always move to it.
4. If the neighbor is worse (ΔE < 0), move to it with probability **p = e^(ΔE/T)**.
5. Decrease T according to a cooling schedule.
6. Repeat until T ≈ 0 or a termination condition is met.

At high T, the probability of accepting bad moves is high (exploration). As T decreases, the probability drops and the search behaves more like hill climbing (exploitation). If the schedule lowers T slowly enough, the algorithm is guaranteed to find the global optimum.

**Example — Optimize f(x) = −x² + 4x:**

The maximum is at x = 2 (by calculus: f'(x) = −2x + 4 = 0 → x = 2, f(2) = 4).

1. Initialize: x_current = 0, T = 10, cooling rate α = 0.9.
2. Iteration 1: Random neighbor x_new = 1. ΔE = f(1) − f(0) = 3 − 0 = 3 > 0 → Accept. Current = 1.
3. Iteration 2: T = 9. Random neighbor x_new = 3. ΔE = f(3) − f(1) = 3 − 3 = 0 → Accept (no change).
4. Iteration 3: T = 8.1. Random neighbor x_new = 2. ΔE = f(2) − f(3) = 4 − 3 = 1 > 0 → Accept. Current = 2.
5. As T → 0, the algorithm settles at x = 2, f(x) = 4, which is the global maximum.

## 1.3.3 Local Beam Search

Local beam search keeps track of **k states** simultaneously rather than just one.

**Algorithm:**

1. Start with k randomly generated states.
2. At each step, generate all successors of all k states.
3. If any successor is a goal, stop.
4. Otherwise, select the k best successors from the entire pool and repeat.

**Key difference from k parallel hill climbs:** In random-restart hill climbing with k parallel searches, each search is independent. In local beam search, information is **shared** — if one state generates several good successors, the other states can be abandoned, concentrating resources on the more promising region.

**Problem:** Can suffer from lack of diversity — all k states may converge to the same local region. **Stochastic beam search** addresses this by selecting successors with probability proportional to their value, similar to natural selection, maintaining diversity.

**Example:** Finding the minimum of a function over integers 1–10 with k=3. Start with states {2, 7, 5}. Generate neighbors for each, evaluate, pick the 3 best from all neighbors combined, and repeat.

## 1.3.4 Searching in Partially Observable Environments

When the environment is partially observable, the agent cannot determine the exact current state. Instead, it works with **belief states** — sets of possible physical states the agent might be in.

**Sensorless (Conformant) problems:** The agent has no observations at all. It searches in belief-state space, where each belief state is a set of physical states. An action transforms a belief state by applying the transition model to every state in the set. A solution is a sequence of actions that maps the initial belief state to a belief state where every physical state is a goal.

**Partially observable problems:** The agent receives partial observations after each action. The belief state is updated using both the action's predicted effect and the observation received (state estimation). This combines prediction (through the transition model) and filtering (through the observation model).

**Contingency problems:** When observations are possible, the agent can create contingency plans — plans that branch based on what is observed. The plan takes the form: [action, if observation₁ then plan₁, if observation₂ then plan₂, ...].

---

# 1.4 Games — Adversarial Search

> **No direct question appeared yet on this topic in available papers, but the syllabus explicitly includes it.**

Game playing is a classic AI problem because games are well-defined, have clear success criteria, and involve adversarial agents. A **game** can be formally defined by: initial state, player function (whose turn), actions, transition model, terminal test, and utility function.

## 1.4.1 Adversarial Search (Minimax)

In a two-player zero-sum game, one player's gain is the other's loss. The **minimax algorithm** determines the optimal strategy by assuming the opponent also plays optimally.

**Minimax Value:**

- If the node is terminal: UTILITY(n).
- If it is MAX's turn: minimax(n) = max over successors s of minimax(s).
- If it is MIN's turn: minimax(n) = min over successors s of minimax(s).

**Algorithm:** Performs a complete depth-first exploration of the game tree. Time complexity: O(b^m), Space complexity: O(bm), where b is the branching factor and m is the maximum depth.

**Alpha-Beta Pruning:** An optimization of minimax that eliminates branches that cannot influence the final decision. It maintains two values: α (best value MAX can guarantee) and β (best value MIN can guarantee). If α ≥ β at any node, prune the remaining children. With perfect move ordering, it reduces the effective branching factor from b to √b, allowing search to twice the depth in the same time.

**Imperfect real-time decisions:** In practice, the game tree is too large to search completely. The agent uses:

- **Cutoff test:** Replace the terminal test with a depth limit.
- **Evaluation function:** Replace the utility function with a heuristic estimate of the position's value (e.g., weighted material count in chess).

## 1.4.2 Monte Carlo Tree Search (MCTS)

MCTS evaluates moves through **random simulations** (playouts) rather than heuristic evaluation functions. It is especially effective for games with enormous branching factors (e.g., Go, with b ≈ 250).

**Four steps per iteration:**

1. **Selection:** Starting from the root, use a tree policy (e.g., UCB1 — Upper Confidence Bound) to traverse the tree, balancing exploration and exploitation.
2. **Expansion:** When a leaf node is reached, add one or more child nodes to the tree.
3. **Simulation (Rollout):** From the new node, play out the game randomly (or with a lightweight policy) until a terminal state.
4. **Backpropagation:** Update the statistics (win/visit counts) of all nodes along the path from the new node back to the root.

The UCB1 formula for node selection: **UCB1(n) = w_i/n_i + c × √(ln(N)/n_i)**, where w_i = wins, n_i = visits of child, N = visits of parent, c = exploration constant.

**Advantages:** Does not require a domain-specific evaluation function. It is anytime — more iterations improve the decision. It naturally handles large branching factors by focusing on promising moves.

## 1.4.3 Stochastic Games

Stochastic games introduce **chance elements** (e.g., dice rolls, card deals). The game tree includes **chance nodes** in addition to MAX and MIN nodes. At chance nodes, the outcome is determined by probability.

**Expectiminimax Algorithm:** Extends minimax to handle chance:

- Terminal node: UTILITY(n).
- MAX node: max over successors.
- MIN node: min over successors.
- CHANCE node: **weighted average** (expected value) over all outcomes: Σ P(outcome) × expectiminimax(successor).

**Example:** In backgammon, after MAX decides a move, dice are rolled (chance node), then MIN plays. The algorithm computes the expected utility across all possible dice outcomes.

**Implication:** Alpha-beta pruning is less effective in stochastic games because chance nodes prevent tight bounding. The evaluation function must be a positive linear transformation of the true utility (not just order-preserving) for correct expectiminimax behavior.

**Partially observable games:** Games where players have hidden information (e.g., card games like poker). The agent must reason about information sets — sets of states that are indistinguishable given the player's observations. Strategies may involve randomized actions to prevent exploitation.
