# 1. Foundation of Advanced Artificial Intelligence

# 1.1 Intelligent Agents: Structure, Types and Implementation

An **agent** is anything that perceives its environment through **sensors** and acts upon it through **actuators**. A **rational agent** selects actions that maximize its expected performance measure, given its percept sequence and built-in knowledge.

**Agent Function and Agent Program:**

The **agent function** is the abstract mathematical description that maps every possible percept sequence to an action. The **agent program** is the concrete implementation of the agent function that runs on the physical agent architecture. The relationship is: Agent = Architecture + Program.

**PEAS Framework:**

To design a rational agent, the task environment must be fully specified using the PEAS description:

1. **Performance Measure:** The criterion for evaluating the agent's success (e.g., safe arrival, minimized time, fuel efficiency for a self-driving car).
2. **Environment:** The external world in which the agent operates (e.g., roads, traffic, pedestrians).
3. **Actuators:** The mechanisms through which the agent acts on the environment (e.g., steering, accelerator, brake, signals).
4. **Sensors:** The devices through which the agent perceives the environment (e.g., cameras, GPS, speedometer, LIDAR).

**Environment Types:**

The nature of the environment significantly influences agent design:

1. **Fully observable vs. Partially observable:** In a fully observable environment, the agent's sensors give it access to the complete state of the environment at each time step. In a partially observable environment, some aspects of the state are hidden due to noisy or limited sensors.
2. **Deterministic vs. Stochastic:** A deterministic environment means the next state is completely determined by the current state and the agent's action. A stochastic environment involves randomness or uncertainty in outcomes.
3. **Episodic vs. Sequential:** In an episodic environment, the agent's experience is divided into atomic episodes where each episode's action does not affect future episodes. In a sequential environment, current decisions affect all future decisions.
4. **Static vs. Dynamic:** A static environment does not change while the agent is deliberating. A dynamic environment can change during deliberation, requiring the agent to act quickly or accept a less optimal decision.
5. **Discrete vs. Continuous:** A discrete environment has a finite number of distinct states, percepts, and actions. A continuous environment has a continuous range of values.
6. **Single-agent vs. Multi-agent:** A single-agent environment has only one agent acting. A multi-agent environment has multiple agents that may be cooperative or competitive.
7. **Known vs. Unknown:** In a known environment, the agent knows the outcomes (or outcome probabilities) for all actions. In an unknown environment, the agent must learn how the environment works.

**Types of Intelligent Agents:**

1. **Simple Reflex Agents:** These agents select actions based only on the current percept, ignoring the rest of the percept history. They use condition-action rules of the form "if condition then action." They work only in fully observable environments because they have no memory. For example, a thermostat that turns on heating if the temperature drops below a threshold.

2. **Model-Based Reflex Agents:** These agents maintain an internal state that tracks aspects of the world not currently visible. They use a model of the world that describes how the world evolves independently of the agent and how the agent's actions affect the world. This internal state is updated using the current percept and the previous state. They can handle partially observable environments.

3. **Goal-Based Agents:** In addition to maintaining an internal state, these agents have goal information that describes desirable situations. They consider the future consequences of actions by using search and planning algorithms to find action sequences that achieve their goals. They are more flexible than reflex agents because changing the goal changes the agent's behavior without rewriting condition-action rules.

4. **Utility-Based Agents:** These agents use a utility function that maps a state (or a sequence of states) to a real number representing the degree of happiness or satisfaction. When there are multiple possible goal states or conflicting goals, the utility function allows the agent to choose the action that maximizes expected utility. This is especially useful in stochastic environments where the agent must make trade-offs.

5. **Learning Agents:** These agents can improve their performance over time through experience. A learning agent has four conceptual components: the **learning element** (responsible for making improvements by modifying the performance element based on feedback), the **performance element** (selects external actions based on percepts, equivalent to the agent types described above), the **critic** (provides feedback on how the agent is doing relative to a fixed performance standard), and the **problem generator** (suggests exploratory actions that lead to new and informative experiences).

**Implementation:**

Agent programs can be implemented using various approaches depending on the complexity of the task: lookup tables (impractical for real problems due to enormous table size), condition-action rules, state-based models with internal representations, goal-based search and planning algorithms, or machine learning techniques that adapt over time.

---

# 1.2 Advanced Search Techniques

> **What are the limitations of A\* search? How does the iterative deepening search resolve these problems? Explain in detail. [7 marks] (2025 Spring - PU)**

**Limitations of A\* Search:**

A\* is an optimal and complete best-first search algorithm that uses the evaluation function f(n) = g(n) + h(n), where g(n) is the path cost from the start to node n, and h(n) is an admissible heuristic estimate of the cost from n to the goal. Despite its optimality, A\* has significant limitations:

1. **Exponential memory usage:** A\* stores all generated nodes in memory (both the open list and closed list). For large state spaces, this causes the algorithm to exhaust available memory long before it exhausts time.
2. **Exponential time complexity:** In the worst case, the number of nodes expanded is exponential in the solution depth, specifically O(b^d) where b is the branching factor and d is the solution depth.
3. **Impractical for large-scale problems:** Problems like the 15-puzzle or route planning on large maps can generate millions of nodes, making standard A\* infeasible.

## 1.2.1 Bidirectional A\* Search

Bidirectional A\* runs two simultaneous A\* searches: a forward search from the initial state toward the goal and a backward search from the goal state toward the initial state. The algorithm terminates when the two search frontiers meet.

**Advantage:** The theoretical time complexity is reduced from O(b^d) to O(b^(d/2)), because each search only needs to explore half the depth of the solution.

**Challenges:**

1. The backward search requires the ability to generate predecessor states, which is not always straightforward.
2. Determining the optimal termination condition is complex. Simply stopping when the frontiers first meet does not guarantee an optimal path. The algorithm must ensure that no unexplored path could produce a shorter total cost.
3. The two searches need different heuristic functions: the forward search uses h(n) estimating cost to the goal, while the backward search uses h(n) estimating cost to the start.
4. The algorithmic complexity of correctly implementing and synchronizing the two searches often outweighs the practical performance gains over standard unidirectional A\*.

## 1.2.2 Iterative Deepening A\* (IDA\*)

IDA\* combines the optimality guarantee of A\* with the linear memory usage of depth-first search. It resolves the primary limitation of A\*, which is its exponential memory requirement.

**Algorithm:**

1. Set the initial cost threshold (cutoff) to f(start) = h(start), since g(start) = 0.
2. Perform a depth-first search, expanding nodes only if f(n) = g(n) + h(n) does not exceed the current threshold. If f(n) exceeds the threshold, the node is not expanded and its f-value is recorded.
3. If the goal is found, return the solution. If the goal is not found within the current threshold, set the new threshold to the minimum f-value among all nodes that exceeded the previous threshold.
4. Repeat the depth-first search with the new threshold.
5. Continue until the goal is found.

**Properties:**

1. **Space complexity:** O(bd), which is linear, since it only stores the nodes along the current path (like DFS). This is the key advantage over A\*.
2. **Optimality:** IDA\* is optimal if the heuristic h(n) is admissible (never overestimates the true cost).
3. **Completeness:** IDA\* is complete for finite state spaces with non-negative step costs.
4. **Re-expansion overhead:** Because IDA\* does not maintain a closed list, it may re-expand the same nodes across different iterations. However, this overhead is typically acceptable because the majority of nodes are generated in the final iteration.
5. **Best suited for:** Memory-constrained environments where standard A\* runs out of memory, such as large combinatorial puzzles (e.g., 15-puzzle, Rubik's Cube).

**Limitation of IDA\*:** In domains where f-values are real-valued (continuous), the threshold may only increase by a tiny amount at each iteration, causing an impractically large number of iterations. In such cases, IDA\* with an epsilon-increase strategy or other memory-bounded algorithms like RBFS or SMA\* are preferred.

## 1.2.3 Online Search

In standard (offline) search, the agent computes a complete solution before taking any action. In contrast, **online search** interleaves computation with action. The agent does not have a complete model of the environment and must explore it by physically taking actions, observing outcomes, and updating its knowledge.

**Why online search is needed:**

1. The environment is unknown, so the agent cannot build a complete search tree in advance.
2. The environment may be dynamic, requiring the agent to react to changes.
3. The environment may be too large for offline computation.

**Online DFS Agent:**

The simplest online search algorithm is Online DFS, which explores the state space using depth-first traversal. It maintains a map of visited states and the results of actions taken. When the agent reaches a dead end (no unvisited successors), it backtracks to the most recent state that has unexplored successors. This requires that actions be reversible.

**LRTA\* (Learning Real-Time A\*):**

LRTA\* is an online heuristic search algorithm that allows the agent to learn better heuristic values through experience. At each step, the agent updates the heuristic value of the current state to reflect the best f-value among its neighbors, then moves to the neighbor with the lowest estimated cost. Over time, the heuristic values converge to the true shortest-path distances, ensuring that the agent eventually finds the optimal path if the environment is safely explorable.

**Challenges in online search:**

1. **Irreversible actions:** If the agent takes an action that cannot be undone (e.g., falling off a cliff), it may reach a dead end from which the goal is unreachable.
2. **Competitive ratio:** The performance of an online algorithm is measured by comparing the actual path cost (including exploration) to the optimal offline path cost. The competitive ratio can be unbounded in the worst case for environments with dead ends.
3. **Safely explorable environments:** An environment is safely explorable if there exists a path from every reachable state to every other reachable state. In such environments, the agent is guaranteed to eventually find the goal.

---

# 1.3 Local Search

Local search algorithms operate on a single current state (rather than maintaining a search tree) and move to neighboring states. They are useful for optimization problems where the path to the solution does not matter, only the final state. They use very little memory and can find reasonable solutions in large or infinite state spaces.

**Hill-Climbing Search (Steepest-Ascent):**

Hill climbing continuously moves to the neighbor with the highest value (or lowest cost). It terminates when no neighbor has a better value than the current state. Hill climbing is fast and memory-efficient but suffers from several problems:

1. **Local maxima:** A peak higher than all its neighbors but lower than the global maximum. The algorithm gets stuck because all moves appear to go downhill.
2. **Ridges:** A sequence of local maxima that are not directly connected by uphill moves. The surface slopes upward in a direction that is not aligned with the available moves.
3. **Plateaux:** A flat area of the state space where all neighbors have the same value. The algorithm cannot determine which direction to move.

## 1.3.1 Simulated Annealing

> **How does the simulated annealing resolve the problems of local hill-climbing search? Apply the simulated annealing to optimize a function: f(x) = −x² + 4x. [8 marks] (2025 Spring - PU)**
>
> **OR**
>
> **What is the idea behind the local beam search? Illustrate with a suitable example. (2025 Spring - PU)**

Simulated annealing resolves the problems of hill climbing by allowing the algorithm to occasionally accept worse moves, thereby escaping local maxima. It is inspired by the metallurgical process of annealing, where a material is heated and then slowly cooled to reach a low-energy crystalline state.

**Algorithm:**

1. Start with an initial state and a high temperature T.
2. At each step, randomly select a neighbor of the current state.
3. If the neighbor is better (higher value for maximization), always accept the move.
4. If the neighbor is worse by an amount ΔE (where ΔE = value(neighbor) − value(current) < 0), accept the move with probability p = e^(ΔE/T). At high temperatures, this probability is close to 1, so worse moves are accepted frequently. At low temperatures, the probability approaches 0, making the algorithm behave like standard hill climbing.
5. Gradually decrease the temperature according to a cooling schedule (e.g., T = T × α, where 0 < α < 1).
6. Terminate when the temperature reaches zero or a sufficiently small value.

**Properties:**

1. If the temperature is decreased slowly enough, simulated annealing is guaranteed to find the global optimum with probability approaching 1.
2. The cooling schedule is critical. Too fast results in getting stuck; too slow wastes computation.
3. It is widely used in VLSI layout, scheduling, and combinatorial optimization problems.

**Example: Optimizing f(x) = −x² + 4x**

The maximum of f(x) = −x² + 4x occurs at x = 2 (by setting f'(x) = −2x + 4 = 0), giving f(2) = 4.

Step-by-step application:

1. Start with x₀ = 0, T = 10, cooling rate α = 0.8.
2. f(0) = 0. Generate random neighbor x₁ = 1. f(1) = −1 + 4 = 3. ΔE = 3 − 0 = 3 > 0, so accept. Current state: x = 1.
3. T = 10 × 0.8 = 8. Generate neighbor x₂ = 3. f(3) = −9 + 12 = 3. ΔE = 3 − 3 = 0, accept.
4. T = 8 × 0.8 = 6.4. Generate neighbor x₃ = 2. f(2) = −4 + 8 = 4. ΔE = 4 − 3 = 1 > 0, accept. Current state: x = 2.
5. T = 6.4 × 0.8 = 5.12. Generate neighbor x₄ = 4. f(4) = −16 + 16 = 0. ΔE = 0 − 4 = −4. Probability = e^(−4/5.12) ≈ e^(−0.78) ≈ 0.458. Generate random number r. If r < 0.458, accept; otherwise reject.
6. Continue decreasing T and repeating until convergence. The algorithm converges to x = 2 with f(2) = 4.

## 1.3.2 Local Beam Search

Local beam search maintains k states in parallel rather than just one. At each step, it generates all successors of all k states, then selects the k best successors from the entire pool.

**Algorithm:**

1. Start with k randomly generated states.
2. At each step, generate all successors of all k current states.
3. If any successor is a goal state, stop and return it.
4. Otherwise, select the k best successors from the complete list and repeat.

**Distinction from running k random hill climbs in parallel:** In k parallel hill climbs, each search is independent and does not share information. In local beam search, the k searches share information through the selection step. If one state generates several good successors and another state generates poor successors, the algorithm abandons the poor line of search and concentrates resources on the more promising region.

**Problem:** Local beam search can suffer from a lack of diversity. All k states may quickly converge to a small region of the state space, effectively reducing the search to a single hill climb.

**Stochastic beam search** addresses this by selecting successors probabilistically, with probability proportional to the successor's value, rather than always selecting the k best. This maintains diversity and is analogous to natural selection in evolutionary biology.

**Example:** Consider finding the maximum of f(x) = −(x−3)² + 9 with k = 3.

1. Start with k = 3 random states: x₁ = 0, x₂ = 5, x₃ = 1.
2. f(0) = 0, f(5) = 5, f(1) = 5. Generate neighbors: for x₁: {−1, 1}, for x₂: {4, 6}, for x₃: {0, 2}.
3. Evaluate all successors: f(−1) = −7, f(1) = 5, f(4) = 8, f(6) = 0, f(0) = 0, f(2) = 8.
4. Select k = 3 best: x = 4 (f=8), x = 2 (f=8), x = 1 (f=5). The search concentrates around the optimal region (x = 3).

## 1.3.3 Searching in Partially Observable Environments

When the agent cannot fully observe the environment's state, it must reason about sets of possible states rather than a single known state.

**Belief State:**

A belief state is the set of all physical states the agent considers possible given its percept history. The agent searches through belief-state space rather than physical state space.

**Sensorless (Conformant) Problems:**

When the agent has no sensors at all, it must find a plan that works regardless of which state it starts in. The initial belief state is the set of all possible states. Each action transforms the belief state by applying the action to every state in the set. A solution is a sequence of actions that maps the initial belief state to a belief state where every state satisfies the goal.

**Contingency Problems:**

When the agent receives partial observations, it can use percepts to narrow its belief state during execution. This leads to contingency plans (conditional plans) that branch depending on what the agent perceives. The solution takes the form of an AND-OR tree, where OR nodes represent agent choices and AND nodes represent possible outcomes of actions or observations.

**AND-OR Search:**

AND-OR search is used to find contingent solutions. An OR node succeeds if any one of its children succeeds (the agent can choose the best action). An AND node succeeds only if all of its children succeed (the solution must handle every possible outcome). The solution is a subtree (not just a path) that reaches goal states at every leaf.

---

# 1.4 Games

Games are a natural domain for studying adversarial search because they have well-defined rules, clear criteria for success, and an opponent whose behavior must be anticipated. In AI, a game is formally defined by: the initial state, a function that defines legal moves (actions) from a state, a transition model defining the result of each move, a terminal test determining when the game ends, and a utility function that assigns a numeric value to terminal states.

## 1.4.1 Adversarial Search

Adversarial search algorithms are used in competitive multi-agent environments where one agent's gain is another agent's loss (zero-sum games).

**Minimax Algorithm:**

Minimax is the foundational algorithm for two-player, zero-sum, perfect-information games. It constructs a complete game tree where MAX (the agent) tries to maximize the utility and MIN (the opponent) tries to minimize it.

**Algorithm:**

1. Generate the complete game tree from the current state down to terminal states.
2. Apply the utility function to each terminal state.
3. Propagate values upward: at MAX nodes, choose the maximum of the children's values; at MIN nodes, choose the minimum.
4. The optimal move for MAX at the root is the action leading to the child with the highest minimax value.

**Properties:** Minimax is complete (if the game tree is finite), optimal (against an optimal opponent), has time complexity O(b^m) and space complexity O(bm), where b is the branching factor and m is the maximum depth.

**Alpha-Beta Pruning:**

Alpha-beta pruning is an optimization of minimax that prunes branches that cannot influence the final decision, without changing the result.

1. **Alpha (α):** The best value that MAX can guarantee along the current path (initialized to −∞).
2. **Beta (β):** The best value that MIN can guarantee along the current path (initialized to +∞).
3. **Pruning rule:** At a MIN node, if the value becomes ≤ α, prune the remaining children (MAX will never choose this path). At a MAX node, if the value becomes ≥ β, prune the remaining children (MIN will never choose this path).

**Efficiency:** With perfect move ordering, alpha-beta pruning reduces the effective branching factor from b to approximately √b, effectively doubling the searchable depth compared to plain minimax within the same time budget.

**Evaluation Functions and Cutoff:**

For complex games like chess, it is infeasible to search to terminal states. The agent uses a depth-limited search with a heuristic evaluation function that estimates the utility of non-terminal states. The evaluation function should be fast to compute, agree with the utility function on terminal states, and correlate strongly with actual winning chances.

## 1.4.2 Monte Carlo Tree Search (MCTS)

MCTS is a heuristic search algorithm that does not require a domain-specific evaluation function. Instead, it uses random simulations (playouts) to estimate the value of moves.

**Four phases (repeated iteratively):**

1. **Selection:** Starting from the root, repeatedly select child nodes using a tree policy until a leaf node or an unexpanded node is reached. The most common tree policy is the Upper Confidence Bound for Trees (UCT), which balances exploitation (choosing moves with high average reward) and exploration (choosing less-visited moves). UCT selects the child that maximizes: UCT(n) = Q(n)/N(n) + c × √(ln N(parent) / N(n)), where Q(n) is the total reward, N(n) is the visit count of node n, N(parent) is the visit count of the parent, and c is an exploration constant.

2. **Expansion:** Add one or more child nodes to the tree corresponding to untried actions from the selected leaf node.

3. **Simulation (Playout/Rollout):** From the newly expanded node, perform a random simulation by playing random moves until a terminal state is reached. The result (win, loss, or draw) is recorded.

4. **Backpropagation:** Propagate the simulation result back up the tree, updating the visit count N and total reward Q of each ancestor node.

**Properties:**

1. MCTS is an anytime algorithm. It can be stopped at any time and will return the best move found so far (typically the move with the highest visit count from the root).
2. With enough simulations, MCTS converges to the optimal solution (minimax).
3. MCTS does not require a heuristic evaluation function, making it applicable to games where designing such a function is difficult.
4. MCTS was the key algorithm behind AlphaGo's success in the game of Go, combined with deep neural networks for position evaluation and move selection.

## 1.4.3 Stochastic Games

Stochastic games introduce an element of chance (randomness) into the game, such as dice rolls or card draws. The game tree now includes **chance nodes** in addition to MAX and MIN nodes.

**Expectiminimax Algorithm:**

Expectiminimax extends minimax to handle chance nodes. It computes the expected utility at chance nodes by taking the weighted average of all possible outcomes.

1. At MAX nodes: choose the action with the maximum expected value.
2. At MIN nodes: choose the action with the minimum expected value.
3. At CHANCE nodes: compute the expected value as the sum of (probability × value) over all possible outcomes. That is, ExpectiMinimax(Chance) = Σᵢ P(dᵢ) × ExpectiMinimax(childᵢ).

**Example: Backgammon.**

In backgammon, after each player decides a move, dice are rolled to determine the actual outcome. The game tree alternates: MAX → CHANCE → MIN → CHANCE → MAX → .... At each chance node, the algorithm weighs every possible dice roll by its probability.

**Complexity:** The time complexity is O(b^m × n^m), where n is the number of distinct chance outcomes. This makes stochastic games significantly more expensive to solve than deterministic games.

**Effect on evaluation functions:** In deterministic games, an evaluation function only needs to preserve the ordering of states (ordinal utility). In stochastic games, the evaluation function must preserve the relative magnitude of differences between state values because these are multiplied by probabilities. A nonlinear transformation of the utility values would change the expected values and lead to different (incorrect) decisions.

**Pruning in stochastic games:** Standard alpha-beta pruning cannot be directly applied to chance nodes because the expected value depends on all children. However, if bounds on the utility values are known, a variant called star-alpha-beta (*-alpha-beta) pruning can be used to prune some branches.
