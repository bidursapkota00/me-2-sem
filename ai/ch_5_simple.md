# 5. Neural Network and Deep Learning

# 5.1 Perceptron, Multi-Layer Perceptron (MLP) and Backpropagation

> **What do you understand by Artificial Neural Network? Design a neural network and explain how it works. (7) (Fall 2025)**
>
> **Explain the concept of a Multi-Layer Perceptron (MLP). Describe its architecture and working mechanism, including the roles of input, hidden, and output layers, as well as the process of forward propagation, activation functions and back-propagation. (7) (Spring 2025)**
>
> **Write a short note on Perceptron. (5) (Fall 2025)**

## Artificial Neural Network (ANN)

An **Artificial Neural Network (ANN)** is a computer system that tries to work like the human brain. Just like our brain has billions of tiny cells called neurons that are connected to each other, an ANN has small computing units (also called neurons) that are connected together in layers. These artificial neurons learn from examples — you show them lots of data, and they figure out the patterns on their own.

**How is it inspired by the brain?** In our brain, a neuron receives signals from other neurons through branches called dendrites, processes the signal in its cell body, and sends the output through a long wire called the axon. Similarly, an artificial neuron takes in some numbers (inputs), does some math on them, and gives out a result (output).

## Perceptron (Single-Layer)

A **perceptron** is the simplest type of neural network. Think of it as a single artificial neuron that can make yes/no decisions. It was invented by Frank Rosenblatt in 1958.

**How does it work?**

1. It takes some inputs (like numbers) — let's say x₁, x₂, x₃.
2. Each input has a **weight** (a number that shows how important that input is) — w₁, w₂, w₃.
3. It multiplies each input by its weight and adds them all up. It also adds a small extra number called **bias (b)**: z = (w₁ × x₁) + (w₂ × x₂) + (w₃ × x₃) + b
4. If the total (z) is 0 or more, the output is **1** (yes). If it's less than 0, the output is **0** (no).

**How does it learn?** If the perceptron gives a wrong answer, it adjusts its weights a little bit using this rule: new weight = old weight + learning rate × (correct answer − wrong answer) × input. It keeps doing this until it gets the answers right.

**Limitation:** A perceptron can only solve simple problems where you can draw a straight line to separate two groups. For example, it cannot solve the **XOR problem** (a problem where the groups are mixed in a criss-cross pattern). This is why we need more complex networks.

## Multi-Layer Perceptron (MLP)

An **MLP** is a neural network with multiple layers of neurons stacked together. Unlike a single perceptron, it can solve complex problems that are not simply divided by a straight line.

**Structure (Architecture):**

- **Input Layer:** This is the first layer. It just receives the raw data (like pixel values of an image). It doesn't do any calculations. The number of neurons here equals the number of features in your data.
- **Hidden Layer(s):** These are the middle layers (between input and output). This is where the real learning happens. Each neuron here takes inputs, multiplies them by weights, adds a bias, and then applies a special function (called activation function). You can have one or more hidden layers. When you have many hidden layers, it's called a "deep" network.
- **Output Layer:** This is the last layer that gives the final answer. For example, if you're classifying images as "cat" or "dog", the output layer will tell you which one it thinks it is.

## Activation Functions

An **activation function** is a math formula applied to the output of each neuron. Without it, the neural network would just be doing simple addition and multiplication, no matter how many layers you add. The activation function adds the ability to learn complex, curved patterns.

Here are the common ones:

- **Sigmoid:** Squishes any number into a range between 0 and 1. Formula: σ(z) = 1 / (1 + e^(−z)). Useful when you want a probability-like output. Problem: for very large or very small inputs, the learning becomes very slow (called "vanishing gradient").
- **Tanh:** Similar to sigmoid but squishes numbers between −1 and +1. It's centered around zero which sometimes helps learning. Still has the slow-learning problem for extreme values.
- **ReLU (Rectified Linear Unit):** Very simple — if the input is positive, keep it; if negative, make it 0. Formula: f(z) = max(0, z). It's the most popular choice for hidden layers because it's fast and works well. Problem: sometimes a neuron can "die" — it always outputs 0 and stops learning.
- **Leaky ReLU:** Similar to ReLU, but instead of making negative values exactly 0, it makes them a very small number. This fixes the "dying neuron" problem.
- **Softmax:** Takes a list of numbers and converts them into probabilities that add up to 1. Used in the output layer when you're classifying into multiple categories (e.g., "cat", "dog", "bird").

## Forward Propagation

**Forward propagation** is the process of passing data through the network from input to output, layer by layer.

1. Start with your input data.
2. At each layer, every neuron takes the outputs from the previous layer, multiplies by weights, adds bias, and applies the activation function.
3. Pass the result to the next layer.
4. Keep going until you reach the output layer and get your prediction.

Think of it like passing a message through a chain of people — each person modifies the message a little before passing it to the next.

## Loss Functions

A **loss function** (also called error function) measures how wrong the network's prediction is compared to the correct answer. The goal of training is to make this loss as small as possible.

- **Mean Squared Error (MSE):** Takes the difference between predicted and actual values, squares it, and averages. Used when predicting numbers (regression). L = average of (actual − predicted)²
- **Binary Cross-Entropy:** Used when classifying into two groups (yes/no, cat/dog). It measures how well the predicted probabilities match the actual labels.
- **Categorical Cross-Entropy:** Used when classifying into more than two groups (e.g., cat/dog/bird). Works similarly to binary cross-entropy but for multiple classes.

## Backpropagation

**Backpropagation** is how the neural network actually learns. After making a prediction (forward propagation), the network checks how wrong it was (using the loss function) and then goes **backward** through the layers to adjust the weights so that next time, the prediction will be better.

**How it works (step by step):**

1. Do forward propagation and calculate the loss (error).
2. Start from the output layer and calculate how much each weight contributed to the error.
3. Move backward through each layer, calculating the same thing for every weight. This uses a math technique called the **chain rule** — it's like figuring out how a small change in one weight at the beginning affects the final error at the end.
4. Adjust all the weights slightly to reduce the error: new weight = old weight − learning rate × gradient.

The **learning rate** controls how big the adjustment steps are. Too big and you might overshoot; too small and learning will be very slow.

**Optimizers (Ways to adjust weights):**

- **SGD (Stochastic Gradient Descent):** Updates weights after looking at each single example. It's fast but can be jumpy/noisy.
- **Mini-batch SGD:** Updates weights after looking at a small group of examples. A good balance between speed and stability.
- **Adam:** A smart optimizer that adjusts the learning rate automatically for each weight. It's the most popular choice today because it works well in most cases.

---

# 5.2 Convolutional Neural Networks (CNN)

> **What is a Neural Network? Explain the working mechanism of a CNN with suitable example. (8) (Internal 2025)**
>
> **Define CNN. (Spring 2025)**

A **Convolutional Neural Network (CNN)** is a special type of neural network designed mainly for working with **images**. Just like our eyes recognize objects by looking at small parts (edges, shapes, colors) and combining them, a CNN does the same thing — it looks at small pieces of an image and builds up understanding step by step.

**Main Parts of a CNN:**

**1. Convolutional Layer (the most important part):**

Imagine you have a small magnifying glass (called a **filter** or **kernel** — usually 3×3 or 5×5 pixels). You slide this magnifying glass across the entire image. At each position, the filter multiplies its values with the image pixels underneath and adds them up to get one number. This creates a new, smaller image called a **feature map**.

Different filters detect different things — one might detect horizontal edges, another might detect vertical edges, another might detect curves, etc.

- **Stride:** How many pixels the filter moves each time. Stride=1 means it moves 1 pixel at a time. Stride=2 means it skips every other pixel (making the output smaller).
- **Padding:** Adding extra zeros around the edges of the image so the filter can process border pixels properly.

**2. Pooling Layer (shrinking the data):**

After convolution, we shrink the feature maps to reduce the amount of computation. The most common method is **Max Pooling** — you take a small area (e.g., 2×2) and keep only the largest value. This keeps the most important information while making the data smaller.

**3. ReLU Activation:**

After each convolution, we apply the ReLU function (keep positives, turn negatives to 0) to add non-linearity.

**4. Fully Connected Layer (making the final decision):**

After several rounds of convolution and pooling, the remaining data is stretched into a single long list of numbers. This list is fed into a regular neural network (fully connected layers) that makes the final prediction.

**Example — Recognizing Handwritten Digits:**

Input: A 32×32 color image of a handwritten digit.

1. **Conv Layer 1:** Apply 32 different filters → get 32 feature maps showing different features. Apply ReLU.
2. **Pooling 1:** Shrink each feature map by half using max pooling.
3. **Conv Layer 2:** Apply 64 filters → get 64 feature maps with more complex features. Apply ReLU.
4. **Pooling 2:** Shrink again by half.
5. **Flatten:** Stretch all the remaining data into one long list (1600 numbers).
6. **Fully Connected:** Connect to 128 neurons.
7. **Output:** 10 neurons (one for each digit 0–9) with softmax to get probabilities.

The network is trained using backpropagation, just like a regular neural network.

**Famous CNN Models:** LeNet-5 (1998), AlexNet (2012), VGGNet, GoogLeNet, ResNet (2015).

## Zero-Shot and Few-Shot Learning

**Zero-Shot Learning:** Imagine you trained a model to recognize cats and dogs, but now you want it to recognize a horse — even though it has **never seen a horse before**. Zero-shot learning can do this! It uses extra information (like text descriptions: "a horse has four legs, a mane, and a tail") to understand and classify things it was never trained on.

**Few-Shot Learning:** What if you only have **1 to 5 pictures** of a new animal? Few-shot learning allows the model to learn from just a handful of examples. It does this by:

- **Metric Learning:** Teaching the model to compare new images with the few examples and find which one is most similar (like matching pictures).
- **Meta-Learning ("Learning to Learn"):** Training the model on many small tasks so it becomes really good at learning quickly from very few examples.

## Graph Convolutional Networks (Graph CNN)

Regular CNNs work on images (which are grids of pixels). But what about data that is shaped like a **network/graph** — like social media connections, molecules, or road maps? **Graph CNNs** extend the idea of convolution to work on such graph-shaped data.

**How it works:** Each node (point) in the graph updates its own information by collecting and combining information from its neighboring nodes. This way, each node learns not just about itself, but also about its surroundings.

**Uses:** Analyzing social networks, predicting properties of molecules, recommendation systems, predicting traffic.

---

# 5.3 Recurrent Neural Networks (RNN)

> **What are the challenges of RNNs? Discuss about the architecture to solve these challenges. (7) (Fall 2025)**
>
> **Explain the working mechanism of RNN with a suitable example. (8) (Spring 2025)**
>
> **Write a short note on RNN. (5) (Internal 2025)**

A **Recurrent Neural Network (RNN)** is a type of neural network made for **sequential data** — data where order matters, like sentences (word by word), music (note by note), or stock prices (day by day).

The special thing about an RNN is that it has **memory**. When processing each step in a sequence, it remembers what it saw in previous steps. It does this by feeding its output back into itself.

**How it works:**

At each time step t:
1. The RNN takes the current input (x_t) — for example, the current word in a sentence.
2. It also takes the **hidden state** from the previous step (h_{t−1}) — this is the "memory" of what it has seen so far.
3. It combines both using weights, adds a bias, and applies the tanh activation function to produce a new hidden state (h_t).
4. This hidden state can be used to make a prediction (output) and is also passed to the next time step.

The same set of weights is used at every time step — this is called **parameter sharing**.

**Training:** RNNs are trained using **Backpropagation Through Time (BPTT)** — the network is "unrolled" across all time steps, and then regular backpropagation is applied.

**Example — Predicting the Next Word:**

Given: "The cat sat on the ___"

- Step 1: RNN reads "The" → updates memory.
- Step 2: RNN reads "cat" → updates memory (now remembers "The cat").
- Step 3: RNN reads "sat" → updates memory.
- Step 4: RNN reads "on" → updates memory.
- Step 5: RNN reads "the" → uses all the accumulated memory to predict the next word, like "mat" or "floor".

**Problems with RNNs:**

1. **Vanishing Gradient Problem:** When the sequence is long, the error signal becomes weaker and weaker as it travels backward through time. It's like playing the telephone game — the message gets lost over many people. The network can't remember things from the beginning of a long sequence.
2. **Exploding Gradient Problem:** Sometimes the error signal grows too large and the numbers blow up, making training unstable. This is fixed by **gradient clipping** (putting a cap on how large the gradients can be).
3. **Hard to remember long sequences:** Standard RNNs can only effectively remember about 10–20 steps back.
4. **Slow to train:** Because it processes one step at a time (sequentially), it can't take advantage of parallel computing.

## LSTM (Long Short-Term Memory)

**LSTM** was invented in 1997 by Hochreiter and Schmidhuber to solve the vanishing gradient problem. Think of it as an RNN with a better, more reliable memory system.

The key idea is that LSTM has a **cell state** — think of it as a conveyor belt that carries important information along the entire sequence. The LSTM uses three **gates** (like doors) to control what information to keep, what to throw away, and what to output.

**The Three Gates:**

**1. Forget Gate — "What should I forget?"**
It looks at the previous output and the current input, and decides what old information to throw away from the cell state. It outputs a number between 0 (forget everything) and 1 (keep everything) for each piece of information.

**2. Input Gate — "What new information should I add?"**
It decides what new information from the current input is worth storing in the cell state.

**3. Output Gate — "What should I output?"**
It decides what part of the cell state to use as the output for this step.

**Why is LSTM better?** The cell state acts like a highway — information can flow through it easily across many time steps. This means the network can remember important information from the beginning of a very long sequence.

## GRU (Gated Recurrent Unit)

**GRU** (2014) is a simpler version of LSTM. Instead of three gates, it uses only **two gates:**

**1. Update Gate — "How much old info to keep vs. how much new info to add?"**
It combines the job of LSTM's forget gate and input gate into one gate.

**2. Reset Gate — "How much of the old info to ignore when computing new info?"**
It controls how much of the previous memory to use when calculating the new candidate state.

GRU is faster to train than LSTM (because it has fewer parts) and often works just as well.

---

# 5.4 Attention Mechanisms

> **What is the attention mechanism used in transformers? (Spring 2025)**

In older sequence-to-sequence models (like RNN-based translators), the entire input sentence was squeezed into a single fixed-size vector before generating the output. This is like trying to memorize an entire book and then summarizing it from memory — you'll miss a lot of details, especially for long texts. This creates a **bottleneck**.

**Attention** (introduced in 2015) solves this problem. Instead of relying on just one compressed memory, the model can **look back at any part of the input** while generating each word of the output. It "pays attention" to the most relevant parts.

**How Attention Works (step by step):**

1. The encoder (input processor) creates a summary for each input word — these are called hidden states (h₁, h₂, ...).
2. When generating each output word, the decoder asks: "Which input words are most important right now?"
3. It calculates an **attention score** for each input word — higher score means more relevant.
4. These scores are converted to **attention weights** (numbers between 0 and 1 that add up to 1) using softmax.
5. A **context vector** is created by taking a weighted average of all input summaries (words with higher weights contribute more).
6. This context vector is used along with the decoder's own state to generate the next output word.

**Example:** When translating "The cat is black" to Nepali, while generating the word for "cat", the attention mechanism would focus most on the word "cat" in the input.

## Self-Attention

**Self-attention** is when a sequence pays attention to **itself**. Each word in a sentence looks at every other word in the **same** sentence to understand context. This helps capture relationships between words regardless of how far apart they are.

For each word, three vectors are created:

- **Query (Q):** "What am I looking for?" — what this word wants to know.
- **Key (K):** "What do I contain?" — what this word can offer to others.
- **Value (V):** "What is my actual information?" — the content to pass along.

The attention is calculated as: Attention = softmax(Q × Kᵀ / √d_k) × V. The division by √d_k keeps the numbers from getting too large.

**Example:** In "The animal didn't cross the street because **it** was too tired" — self-attention helps the model understand that "it" refers to "animal" (not "street") by assigning a high attention weight between "it" and "animal".

## Multi-Head Attention

Instead of doing attention just once, **multi-head attention** does it multiple times in parallel with different learned perspectives. Each "head" can focus on different types of relationships — one might focus on grammar, another on meaning, another on position.

The results from all heads are combined together, giving a much richer understanding than a single attention computation.

---

# 5.5 Transformers

> **Explain the transformer model architecture. (8) (Fall 2025)**
>
> **Describe transformer with its architectures. (Internal 2025)**

The **Transformer** was introduced in 2017 in the famous paper "Attention Is All You Need." It's a revolutionary architecture that **relies entirely on attention** — no RNNs, no CNNs. It processes all words at the same time (in parallel), making it much faster than RNNs.

**Overall Structure — Two Main Parts:**

## Encoder (Understanding the Input)

The encoder reads the entire input and creates a deep understanding of it. It's made of a stack of 6 identical layers. Each layer has two parts:

1. **Multi-Head Self-Attention:** Every word looks at every other word in the input to understand context and relationships.
2. **Feed-Forward Network:** A simple neural network applied to each word independently. It's like giving each word its own mini brain to process the information further.

Each of these parts also has:
- **Residual Connection:** A shortcut that adds the input of a layer directly to its output (like a skip road). This helps the network train better by letting information flow easily.
- **Layer Normalization:** A technique that keeps the numbers in a stable range, preventing training problems.

## Decoder (Generating the Output)

The decoder generates the output one word at a time. It's also a stack of 6 identical layers, but each layer has three parts:

1. **Masked Multi-Head Self-Attention:** Similar to the encoder's self-attention, but with a **mask** — each word can only look at words that came **before** it (not future words). This is important because when generating text, you shouldn't peek at words that haven't been generated yet.
2. **Encoder-Decoder Attention:** The decoder looks at the encoder's output to understand the input. Queries come from the decoder, but keys and values come from the encoder.
3. **Feed-Forward Network:** Same as in the encoder.

## Positional Encoding

Since the Transformer processes all words at the same time (not one by one like RNNs), it doesn't naturally know the **order** of words. "The cat sat on the mat" and "mat the on sat cat the" would look the same! To fix this, **positional encodings** — special numbers representing each word's position — are added to the word representations before feeding them into the model.

**Why Transformers are better than RNNs:**

- **Parallel processing:** All words are processed at the same time, making training much faster.
- **Better at long-range connections:** Any two words can directly attend to each other, no matter how far apart. In RNNs, distant words had to pass through many steps.
- **Scalable:** Can handle bigger datasets and longer sequences.

**Types of Transformer Models:**

- **Encoder-only (e.g., BERT):** Good at understanding text (classification, question answering).
- **Decoder-only (e.g., GPT):** Good at generating text (writing stories, chatbots).
- **Encoder-Decoder (e.g., T5, original Transformer):** Good at converting one sequence to another (translation, summarization).

## BERT (Bidirectional Encoder Representations from Transformers)

**BERT** (2019) uses only the **encoder** part of the Transformer. The special thing about BERT is that it reads text in **both directions** at the same time — it looks at words to the left AND right of each word to understand context.

**How is BERT trained?**

- **Masked Language Model:** Randomly hide (mask) 15% of the words in a sentence and ask the model to guess the hidden words. This forces it to understand context from both directions.
- **Next Sentence Prediction:** Give the model two sentences and ask: "Does the second sentence come after the first?" This helps it understand relationships between sentences.

After this pre-training on huge amounts of text, BERT can be **fine-tuned** (slightly adjusted) for specific tasks like sentiment analysis, question answering, etc.

## GPT (Generative Pre-trained Transformer)

**GPT** uses only the **decoder** part of the Transformer. Unlike BERT, it reads text in **one direction only** (left to right). At each step, it can only see the words that came before.

**How is GPT trained?** It's trained to predict the **next word** given all the previous words. For example: "The cat sat on the" → predict "mat". This makes GPT excellent at generating text.

GPT models (GPT-2, GPT-3, GPT-4) have gotten bigger and bigger, with more data and more computing power, and they've become remarkably good at writing, reasoning, and answering questions.

---

# 5.6 Graph Attention Networks (GAT)

**Graph Attention Networks (GATs)** (2018) apply the attention mechanism to **graph-shaped data** (data with nodes and connections, like social networks or molecular structures).

**The problem with regular Graph CNNs:** In Graph CNNs, every neighbor of a node is treated equally or weighted based on the graph structure (how many connections each node has). But in reality, some neighbors are more important than others!

**How GATs solve this:** GATs **learn** how important each neighbor is. They use attention to give different weights to different neighbors — important neighbors get more attention, less important ones get less.

**How a GAT layer works:**

1. **Transform:** Each node's features are transformed using a weight matrix.
2. **Score:** For each pair of connected nodes, calculate an attention score (how relevant is this neighbor?).
3. **Normalize:** Use softmax to convert scores into weights that add up to 1.
4. **Aggregate:** Each node creates its new representation by taking a weighted combination of its neighbors' features.
5. **Multi-Head:** This is done multiple times with different attention heads for stability and richer learning.

**Why GATs are better than Graph CNNs:**

- **Adaptive:** Different neighbors can have different importance (not treated equally).
- **Flexible:** Can work on new, unseen graph structures because weights depend on features, not the fixed graph shape.
- **Explainable:** You can look at the attention weights to see which neighbors were most important for a decision.

**Uses:** Classifying nodes in networks, analyzing social media, predicting drug interactions, completing knowledge graphs.

---

# 5.7 Transfer Learning

> **What is the purpose of Transfer Learning? Differentiate between a Tokenizer and an Embedding. Justify which one is more suitable for machine learning procedures. (7) (Internal 2025)**
>
> **Write a short note on Transfer Learning. (5) (Fall 2025, Spring 2025)**

**Transfer Learning** is like a student who learned math in one school and then transfers to a new school — they don't have to re-learn math from scratch! Similarly, in transfer learning, a model trained on one task is **reused** for a different but related task.

**Why is Transfer Learning useful?**

- **Need less data:** You don't need millions of examples for the new task because the model already knows a lot.
- **Saves time:** Training from scratch takes a long time. With transfer learning, you start with a model that already knows general patterns.
- **Better results:** A pre-trained model has already learned useful features (like recognizing edges, shapes, and textures in images, or grammar and word meanings in text).

**Two Main Approaches:**

**1. Feature Extraction:** Take a pre-trained model, freeze it (don't change its weights), and use it as a feature extractor. Just add a new small layer at the end for your specific task and train only that new layer. Best when: you have very little data for your new task.

**2. Fine-Tuning:** Take a pre-trained model and continue training it on your new task with a very small learning rate. You might freeze the early layers (which learn basic features) and only fine-tune the later layers (which learn task-specific features). Best when: you have a decent amount of data for your new task.

**Examples:**

- **Images:** Take a model trained on millions of general images (like ImageNet), then fine-tune it to recognize medical X-rays — even if you only have a few thousand X-ray images.
- **Text:** Take BERT or GPT (pre-trained on massive amounts of text), then fine-tune it for sentiment analysis or question answering with a small dataset.

## Tokenizer vs. Embedding

**Tokenizer:** A tokenizer is a **text splitter**. It takes a sentence and breaks it into smaller pieces (tokens) — these could be words, parts of words, or even individual characters. Then it assigns each piece a number (ID).

- Example: "I love AI" → ["I", "love", "AI"] → [45, 312, 89]
- It's just a preprocessing step — it doesn't understand meaning. It's like cutting a pizza into slices — you're just dividing it up.
- Types: Word-level (split by spaces), Subword-level (split common words and break rare words into parts), Character-level (each letter is a token).

**Embedding:** An embedding takes those token IDs and converts each one into a **list of numbers (a vector)** that captures the **meaning** of that word. Words with similar meanings will have similar vectors — so "king" and "queen" would be closer together than "king" and "banana".

- Example: Token ID 312 ("love") → [0.12, −0.34, 0.56, 0.78, ...] (a vector with many dimensions)
- Embeddings are **learned** by the model during training — the model figures out the best vectors on its own.

**Key Differences:**

| Feature | Tokenizer | Embedding |
|---|---|---|
| What it does | Splits text into pieces and assigns IDs | Converts IDs into meaningful number vectors |
| Understands meaning? | No | Yes |
| Can be learned? | Usually fixed (rule-based) | Learned during training |
| Order in pipeline | First (step 1) | Second (step 2) |

**Which is more suitable for ML?** **Embeddings** are more suitable for machine learning because they give words a meaningful numerical representation that the model can actually learn from. A tokenizer is just a necessary first step (like chopping vegetables before cooking) — it doesn't contribute to learning itself. The real power of modern language models comes from their embeddings, which capture rich information about word meanings and relationships.
