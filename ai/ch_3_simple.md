# 3. Planning and Decision Making

# 3.1 STRIPS and PDDL

## What is Planning?

Imagine you want to go from your home to school. You need to think about the steps: wake up, get dressed, eat breakfast, walk to school. **Planning in AI** is exactly this — figuring out a list of steps to go from a **starting situation** to a **goal situation**.

Planning assumes the world is simple:
- You can see everything (nothing is hidden)
- Actions always work as expected (no surprises)
- Nothing changes on its own (the world waits for you)

**How is Planning different from regular searching?**
In regular search, we treat each situation like a closed box — we don't look inside. In planning, we break down each situation into smaller facts (like "Robot is at location A" and "Block B has nothing on top"). This makes it much easier to find solutions.

## STRIPS (Stanford Research Institute Problem Solver)

STRIPS is one of the earliest planning systems (made in 1971). Think of it as a simple language to describe planning problems.

**Every STRIPS problem has 3 parts:**

1. **Starting Situation:** What is true right now?
   - Example: The robot is at place A. Block B has nothing on top of it.

2. **Goal:** What do we want to be true at the end?
   - Example: The robot is at place B.

3. **Actions:** What can we do? Each action has:
   - **What must be true before doing it** (Preconditions) — like needing a key before opening a door
   - **What becomes true after doing it** (Add List) — the door is now open
   - **What becomes false after doing it** (Delete List) — the door is no longer closed

**Example — Moving Blocks:**

Imagine you have blocks stacked on a table and you want to rearrange them.

```
Action: Move(block, from, to)
  Before: block is on "from", nothing is on top of block, nothing is on top of "to"
  Becomes true: block is on "to", "from" is now clear
  Becomes false: block is no longer on "from", "to" is no longer clear
```

**Important Rule:** Anything we don't mention is assumed to be false. If we don't say "the light is on," then the light is off.

## PDDL (Planning Domain Definition Language)

PDDL is a newer, more powerful language for describing planning problems. Think of it as an upgraded version of STRIPS.

**PDDL splits the problem into two files:**

1. **Domain File:** The "rulebook" — describes what actions are possible and what things exist in this type of world. You can reuse this for many different puzzles.
2. **Problem File:** The specific puzzle — describes the exact objects, starting situation, and goal for one particular problem.

**How do we actually find the plan? (Planning Methods):**

- **Forward Search:** Start from the beginning and try actions one by one until you reach the goal. Like walking forward through a maze.
- **Backward Search:** Start from the goal and work backwards — ask "what action could have led to this?" Like solving a maze from the exit.
- **Planning Graphs:** Build a special diagram that shows which actions and facts are possible at each step, then find a solution from the diagram.

---

# 3.2 Hierarchical Planning

> **Exam Question: Differentiate between hierarchical planning and probabilistic planning. (7) (Fall 2025)**

**What is Hierarchical Planning?**

Think about how you plan a vacation:
- First, you think big: "I need to travel, stay somewhere, and do activities"
- Then you break each part down: "To travel, I need to book a flight, pack bags, go to airport"
- Then even smaller: "To pack bags, I need to choose clothes, fold them, put them in suitcase"

This is **Hierarchical Task Network (HTN) planning** — breaking **big tasks into smaller tasks**, and those into even smaller tasks, until you have simple actions you can actually do.

**Key Ideas:**

- **Simple Actions:** Things you can directly do (like "pick up a glass")
- **Big Tasks (HLAs):** Complex tasks that need to be broken down (like "make dinner")
- **Methods:** The "recipes" that tell you how to break a big task into smaller steps

**How does it work?**

1. Start with the big task
2. Pick a big task from your plan
3. Find a recipe to break it into smaller tasks
4. Replace the big task with its smaller steps
5. Keep doing this until every task is a simple action
6. Check if doing all these simple actions actually achieves your goal

**Example — Getting to Office:**

```
Big Task: Travel(Home, Office)
  Recipe 1: Walk to bus stop → Ride bus to office
  Recipe 2: Drive to office

Big Task: Drive(Home, Office)
  Recipe: Get in car → Start engine → Navigate to office → Park
```

**Why is Hierarchical Planning useful?**

- **Faster:** Breaking things down reduces the number of options to search through
- **Handles complex problems:** Can represent complicated plans that are hard to describe otherwise
- **Scales well:** Works well even for very large, real-world problems

**Downside:** Someone (an expert) needs to write all the recipes. If the recipes are bad, the plans will be bad too.

---

# 3.3 Probabilistic Planning

> **Exam Question: Write a short note on Probabilistic Planning. (5) (Internal 2025)**

**What is Probabilistic Planning?**

In the real world, things don't always go as planned. When you try to kick a ball into the goal, sometimes you score, sometimes you miss, sometimes it hits the post. **Probabilistic planning** deals with situations where **actions have uncertain results**.

The main tool for this is called a **Markov Decision Process (MDP)**.

**An MDP has these parts:**

- **States:** All possible situations (like different positions on a board game)
- **Actions:** Things the agent can do (like move left, move right)
- **Transition Probabilities:** The chance of ending up in each new situation after an action
  - Example: "If I try to go North, there's 80% chance I go North, 10% chance I go East, 10% chance I go West"
- **Rewards:** Points you get (or lose) in each situation
  - Example: Reaching the treasure gives +100 points, falling in a pit gives -50 points
- **Discount Factor (γ):** A number between 0 and 1 that decides how much the agent cares about future rewards vs. immediate rewards. Close to 1 = thinks long-term. Close to 0 = only cares about right now.

**Big Difference from Normal Planning:**
- Normal planning gives you a **fixed list of steps:** "Do A, then B, then C"
- Probabilistic planning gives you a **policy** — a rule that says "if you're in THIS situation, do THIS action." It's like a strategy guide, not a recipe.

**Optimal Policy:** The best possible policy — the one that earns the most reward on average over time.

**Hierarchical vs. Probabilistic Planning — Key Differences:**

| Feature | Hierarchical Planning | Probabilistic Planning |
|---|---|---|
| World type | Predictable (actions always work) | Unpredictable (actions might fail) |
| Answer format | Step-by-step plan | Strategy/policy for every situation |
| What it needs | Expert-written recipes | Probabilities and rewards |
| Main goal | Break complex tasks into simple ones | Make the best decisions under uncertainty |
| Method used | Task breakdown | Math formulas (value/policy iteration) |

---

# 3.4 Multi-Agent Planning

> **Exam Questions:**
> - What is multi-agent planning in AI? Discuss the challenges of coordination and communication between agents. (7) (Internal 2025)
> - Why do we require Multi-agent Planning in AI? Give an overview of Multiagent System Architecture and discuss how agents can work in Cooperative & Competitive environments. (8) (Fall 2025)
> - Write a short note on Multi-agent planning in AI. (5) (Spring 2025)

**What is Multi-Agent Planning?**

So far, we've talked about ONE agent making plans. But what if there are MANY agents — like a team of robots in a warehouse, or cars on a road, or players in a video game?

**Multi-agent planning** is about how multiple agents (each with their own eyes, hands, and goals) work together or compete with each other.

**Why do we need Multi-Agent Planning?**

- Some problems naturally involve many agents (like traffic with many cars)
- Some tasks are too big for one agent alone
- Multiple agents can work at the same time (faster!)
- Some situations are competitive (like a game of chess — two players with opposite goals)

**Types of Multi-Agent System Designs:**

- **Reactive:** Agents follow simple "if this, do that" rules. Very fast but not very smart. Think of ants — each ant follows simple rules, but together they do amazing things.
- **Deliberative:** Agents have a mental picture of the world and carefully plan what to do. Smarter but slower.
- **Hybrid:** Mix of both — quick reactions for urgent stuff, careful planning for complex stuff.
- **BDI (Belief-Desire-Intention):** Agents have:
  - **Beliefs** — what they think is true about the world
  - **Desires** — what they want to achieve
  - **Intentions** — what they've decided to do right now

**Cooperative Environments (Teamwork):**

When agents work together toward a shared goal (like a soccer team):
- **Joint Planning:** Agents make plans together
- **Task Sharing:** Divide the work — "You do this part, I'll do that part"
- **Communication:** Agents tell each other what they know and what they're doing
- **Shared Understanding:** Everyone has a similar picture of what's going on

**Competitive Environments (Rivalry):**

When agents have opposite goals (like two players in a board game):
- **Game Theory:** The study of strategic decision-making when competing
- **Nash Equilibrium:** A situation where no player can do better by changing only their own strategy
- **Adversarial Search:** Algorithms like Minimax — "I assume my opponent will play their best move, so I pick the move that's best for me even in that worst case"

**Challenges (What makes Multi-Agent Planning hard?):**

1. **Too much talking:** If agents communicate too much, it slows everything down. Too little, and they mess things up.
2. **Can't see everything:** Each agent only sees part of the world — they don't know what others see or plan.
3. **Conflicting goals:** Even team members might disagree on how to do things.
4. **Too many agents:** More agents = way more possible combinations of actions = much harder to plan.
5. **Timing problems:** Agents need to act at the right time, or they get in each other's way.
6. **Trust issues:** What if an agent breaks down, sends wrong info, or acts selfishly?
7. **Changing world:** The world keeps changing because of everyone's actions, so plans need constant updating.

---

# 3.5 Utility Theory

**What is Utility Theory?**

When you make decisions, you think about what you like more. You might prefer pizza over salad, or prefer getting Rs.100 for sure over a 50% chance of getting Rs.200 (because you might end up with nothing!).

**Utility theory** is the math behind making smart choices when things are uncertain.

**Basic Ideas:**

- **Preferences:** You can compare things. You either prefer A over B, B over A, or you like them equally.
- **Utility Function U(s):** A way to give a "score" to each outcome. Higher score = you like it more.
  - Example: U(pizza) = 8, U(salad) = 5, U(burger) = 7. So you'd pick pizza first.
- **Lottery (Gamble):** An uncertain situation. Like: "50% chance of winning Rs.200, 50% chance of winning nothing."

**Rules for Rational Preferences (Axioms):**

These are common-sense rules that any rational person would follow:

1. **You can always compare:** Given any two options, you can say which you prefer (or that you're indifferent).
2. **No circular preferences:** If you prefer A over B, and B over C, then you must prefer A over C.
3. **Continuity:** If you prefer A over B, and B over C, then there's some gamble between A and C that you'd value equally to B.
4. **Substitutability:** If you value A and B equally, you can swap them in any gamble without caring.
5. **More is better:** If you prefer A over B, then a gamble with a higher chance of A is better.
6. **Compound gambles simplify:** A "gamble within a gamble" can be simplified using basic probability.

**The Golden Rule — Maximum Expected Utility (MEU):**
A rational agent should always pick the option with the **highest expected (average) utility**.

Expected Utility = (Chance of outcome 1 × Score of outcome 1) + (Chance of outcome 2 × Score of outcome 2) + ...

## 3.5.1 Utility Functions

A utility function turns outcomes into numbers. How the numbers relate to actual value shows your **attitude toward risk**:

- **Risk-neutral:** You only care about the average. Rs.100 for sure = 50% chance of Rs.200 (same average). U(x) = x.
- **Risk-averse:** You prefer safety. You'd take Rs.100 for sure rather than a 50/50 shot at Rs.200 or nothing. U(x) = √x. (Most people are like this!)
- **Risk-seeking:** You love gambling. You'd take the 50/50 chance over the safe Rs.100. U(x) = x².

**Example:**
Option A: Get Rs.100 for sure.
Option B: 50% chance of Rs.200, 50% chance of Rs.0.

Both have the same average money (Rs.100). But:
- Risk-neutral person: "Both are the same to me"
- Risk-averse person: "I'll take the safe Rs.100, thanks!"
- Risk-seeking person: "Give me the gamble!"

## 3.5.2 Multi-Attribute Utility Functions

In real life, decisions involve **many factors at once**. Choosing a college involves: cost, reputation, location, available courses, campus life, etc.

**How do we handle multiple factors?**

**Dominance:**
- **Strict Dominance:** If Option A is better than Option B in EVERY factor, just pick A. Easy!
- **Stochastic Dominance:** If Option A gives you a better chance of a good outcome at every level, pick A.

**Combining Factors:**

If your preference for one factor doesn't depend on the others (e.g., you always prefer cheaper regardless of location), then you can use a simple formula:

**Additive Utility:** Total Score = (Weight₁ × Score on Factor 1) + (Weight₂ × Score on Factor 2) + ...

Example for choosing a college:
- Total = 0.3 × (cost score) + 0.25 × (reputation score) + 0.2 × (location score) + 0.25 × (campus life score)

The weights (0.3, 0.25, etc.) show how important each factor is to you.

If factors affect each other (e.g., you only care about campus life if the cost is affordable), you need a **multiplicative utility function** which is more complex.

---

# 3.6 Decision Networks

> **Exam Question: What is a decision network? Explain its components with an example. (8) (Spring 2025)**

**What is a Decision Network?**

A **decision network** (also called an **influence diagram**) is a diagram that helps an agent make decisions when things are uncertain. Think of it as a map that shows:
- What you're unsure about
- What choices you have
- What outcomes you care about

**The 3 Parts of a Decision Network:**

**1. Chance Nodes (drawn as ovals/circles):**
Things you can't control — uncertain events. Each has probabilities.
- Example: Weather (60% Sunny, 40% Rainy)
- Example: Oil Underground (20% Large, 30% Small, 50% None)

**2. Decision Nodes (drawn as rectangles/boxes):**
Your choices — things you CAN control.
- Example: Should I Drill for oil, or Not Drill?
- Example: Should I take an umbrella or not?
- Arrows pointing INTO a decision node show what information you have when making the decision.

**3. Utility Nodes (drawn as diamonds):**
The "payoff" — how good or bad each outcome is for you. It depends on both the uncertain events and your decisions.
- Example: Profit depends on whether you drilled AND how much oil was there.

**How to Use a Decision Network:**

1. Look at what you know (evidence)
2. For each choice, calculate the average (expected) payoff by considering all possible uncertain outcomes
3. Pick the choice with the highest expected payoff

**Example — Should I Drill for Oil?**

- **Uncertain event (Chance Node):** How much oil is underground?
  - 20% chance: Large amount
  - 30% chance: Small amount
  - 50% chance: No oil at all

- **My choice (Decision Node):** Drill or Don't Drill?

- **Payoff (Utility Node):**
  - Drill + Large oil = Earn Rs.500K
  - Drill + Small oil = Earn Rs.100K
  - Drill + No oil = Lose Rs.200K
  - Don't Drill = Earn Rs.0

**Calculating Expected Utility:**

EU(Drill) = 0.2 × 500 + 0.3 × 100 + 0.5 × (−200)
         = 100 + 30 − 100
         = **Rs.30K**

EU(Don't Drill) = **Rs.0**

Since Rs.30K > Rs.0, the smart choice is to **Drill!**

You can also add a "test" to the network (like doing a soil survey before drilling). This lets you calculate the **value of information** — is it worth paying for the test?

## 3.6.1 Sequential Decision Problems

**What if you have to make many decisions, one after another?**

Sometimes you don't just make ONE decision — you make a whole SERIES of decisions over time. Each decision affects what happens next.

**Example:** A robot navigating a maze. At every step, it decides: go up, down, left, or right. Each choice leads to a new position, and it gets points or penalties along the way.

This is called a **Sequential Decision Problem**, and we use the MDP framework (from Section 3.3) to solve it.

**The Bellman Equation:**

This is the key formula. It says:

> The value of being in a state = Immediate reward + (discount × value of the best next state)

In math: U(s) = R(s) + γ × max_a Σ P(s' | s, a) × U(s')

In simple words: "How good a state is = what you get right now + how good the best future will be (considering uncertainty)"

**Example — Grid World:**
Imagine a 4×3 grid. One cell has a treasure (+1 point), another has a trap (−1 point). When the robot tries to go in a direction, it goes the right way 80% of the time, but accidentally slips sideways 10% each way. The solution (optimal policy) tells the robot which direction to move in EACH cell to collect the most points on average.

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

**What if the agent can't see the full picture?**

In a regular MDP, the agent always knows exactly where it is. But in real life, that's often not true! A robot might not know exactly which room it's in — it can only see walls nearby and guess.

A **POMDP** is an MDP where the agent **can't directly see the current state**. Instead, it gets **clues (observations)** that help it guess.

**What's different from a regular MDP?**

- **Observations:** Things the agent can see (like sensor readings)
- **Observation Probabilities:** How likely each observation is in each state
  - Example: "If I'm in the kitchen, there's a 90% chance I see a stove, 10% chance I don't"

**Belief State:**

Since the agent doesn't know for sure where it is, it keeps a **belief** — a set of guesses with probabilities.

Example: "I think there's a 60% chance I'm in the kitchen and 40% chance I'm in the living room."

**How does it update its beliefs?**

After taking an action and seeing an observation:
1. "Given my previous belief, what action I took, and what I observed, where am I most likely now?"
2. Use Bayes' rule (a probability formula) to update the belief

**The Challenge:** Solving POMDPs is VERY hard because the "belief state" is continuous (there are infinite possible beliefs). For big problems, we use approximate methods that find "good enough" answers.

**Example:**
A robot is in a building but doesn't know which room it's in. It has a rough idea (belief). It moves left and its wall sensors detect "wall on the right." Using this observation, it updates its belief — "Oh, there's a wall on my right, so I'm probably in the hallway, not the open hall." Then it chooses its next action based on this updated belief.
