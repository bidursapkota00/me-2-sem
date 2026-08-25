# 5. Neural Network and Deep Learning

# 5.1 Perceptron, Multi-Layer Perceptron (MLP) and Backpropagation

> **What do you understand by Artificial Neural Network? Design a neural network and explain how it works. (7) (Fall 2025)**
>
> **Explain the concept of a Multi-Layer Perceptron (MLP). Describe its architecture and working mechanism, including the roles of input, hidden, and output layers, as well as the process of forward propagation, activation functions and back-propagation. (7) (Spring 2025)**
>
> **Write a short note on Perceptron. (5) (Fall 2025)**

## Artificial Neural Network (ANN)

An **Artificial Neural Network** is a computational model inspired by the structure and functioning of biological neural networks in the brain. It consists of interconnected processing units (neurons) organized in layers that learn to map inputs to outputs by adjusting connection weights during training.

**Biological Inspiration:** A biological neuron receives signals through dendrites, processes them in the cell body, and transmits output through the axon. Similarly, an artificial neuron receives weighted inputs, applies an activation function, and produces an output.

## Perceptron (Single-Layer)

The **perceptron** (Frank Rosenblatt, 1958) is the simplest form of a neural network — a single artificial neuron that performs binary classification.

**Working:**

1. Receive inputs x₁, x₂, ..., x_n, each with a corresponding weight w₁, w₂, ..., w_n.
2. Compute the weighted sum: z = Σ(w_i × x_i) + b, where b is the bias.
3. Apply an activation function (step function): output = 1 if z ≥ 0, else output = 0.

**Learning Rule (Perceptron Update Rule):** For each misclassified sample: w_i ← w_i + α × (y − ŷ) × x_i, where α is the learning rate, y is the true label, and ŷ is the predicted output. The perceptron converges if the data is linearly separable.

**Limitation:** A single perceptron can only solve **linearly separable** problems. It cannot solve the XOR problem because XOR is not linearly separable. This limitation motivated the development of multi-layer networks.

## Multi-Layer Perceptron (MLP)

An MLP is a feedforward neural network with one or more **hidden layers** between the input and output layers. Each layer is fully connected to the next. MLPs can learn non-linear decision boundaries.

**Architecture:**

- **Input Layer:** Receives raw feature values. The number of neurons equals the number of input features. No computation is performed here.
- **Hidden Layer(s):** Intermediate layers that perform computations. Each neuron computes a weighted sum of inputs, adds a bias, and applies a non-linear activation function. Multiple hidden layers create a "deep" network.
- **Output Layer:** Produces the final prediction. For binary classification, typically 1 neuron with sigmoid activation. For multi-class classification, n neurons (one per class) with softmax activation. For regression, 1 neuron with linear activation.

## Activation Functions

Activation functions introduce **non-linearity** into the network. Without them, any number of layers would collapse into a single linear transformation.

- **Sigmoid:** σ(z) = 1 / (1 + e^(−z)). Output range: (0, 1). Used in output layers for binary classification. Problem: vanishing gradients for very large or small z.
- **Tanh:** tanh(z) = (e^z − e^(−z)) / (e^z + e^(−z)). Output range: (−1, 1). Zero-centered, which can help optimization. Still suffers from vanishing gradients.
- **ReLU (Rectified Linear Unit):** f(z) = max(0, z). Most popular for hidden layers. Computationally efficient. Mitigates vanishing gradient. Problem: "dying ReLU" — neurons can permanently output 0 if they enter the negative region.
- **Leaky ReLU:** f(z) = z if z > 0, else αz (small α like 0.01). Fixes the dying ReLU problem by allowing a small gradient for negative inputs.
- **Softmax:** Converts a vector of values into a probability distribution: softmax(z_i) = e^(z_i) / Σ e^(z_j). Used in the output layer for multi-class classification.

## Forward Propagation

Forward propagation computes the output of the network layer by layer:

1. For each neuron in layer l: z^(l) = W^(l) · a^(l−1) + b^(l), then a^(l) = f(z^(l)), where W^(l) is the weight matrix, b^(l) is the bias vector, a^(l−1) is the activation from the previous layer, and f is the activation function.
2. The process starts from the input layer (a^(0) = x) and propagates through all hidden layers to produce the output ŷ = a^(L).

## Loss Functions

The loss function measures how far the predicted output is from the true output:

- **Mean Squared Error (MSE):** L = (1/n) Σ(y_i − ŷ_i)² — used for regression.
- **Binary Cross-Entropy:** L = −(1/n) Σ[y_i log(ŷ_i) + (1−y_i) log(1−ŷ_i)] — used for binary classification.
- **Categorical Cross-Entropy:** L = −Σ y_i log(ŷ_i) — used for multi-class classification.

## Backpropagation

**Backpropagation** (Rumelhart, Hinton & Williams, 1986) is the algorithm used to compute the gradients of the loss function with respect to each weight in the network. It uses the **chain rule** of calculus to propagate the error backward from the output to the input layer.

**Algorithm:**

1. Perform forward propagation to compute the output and loss L.
2. Compute the gradient of the loss with respect to the output layer: ∂L/∂a^(L).
3. For each layer l from L to 1 (backward):
   - Compute ∂L/∂z^(l) = ∂L/∂a^(l) ⊙ f'(z^(l)), where ⊙ is element-wise multiplication and f' is the derivative of the activation function.
   - Compute ∂L/∂W^(l) = ∂L/∂z^(l) · (a^(l−1))ᵀ.
   - Compute ∂L/∂b^(l) = ∂L/∂z^(l).
   - Propagate: ∂L/∂a^(l−1) = (W^(l))ᵀ · ∂L/∂z^(l).
4. Update weights using gradient descent: W^(l) ← W^(l) − α × ∂L/∂W^(l), b^(l) ← b^(l) − α × ∂L/∂b^(l).

**Optimizers (Variants of Gradient Descent):**

- **SGD (Stochastic Gradient Descent):** Updates weights after each training sample. Noisy but fast.
- **Mini-batch SGD:** Updates after a small batch of samples. Balances speed and stability.
- **Adam (Adaptive Moment Estimation):** Combines momentum and adaptive learning rates. Most widely used in practice.

---

# 5.2 Convolutional Neural Networks (CNN)

> **What is a Neural Network? Explain the working mechanism of a CNN with suitable example. (8) (Internal 2025)**
>
> **Define CNN. (Spring 2025)**

A **Convolutional Neural Network** is a specialized deep learning architecture designed primarily for processing **grid-structured data** such as images. CNNs exploit spatial locality and translational invariance through parameter sharing and local connectivity.

**Key Architectural Components:**

**1. Convolutional Layer:** The core building block. A set of learnable **filters (kernels)** — small matrices (e.g., 3×3, 5×5) — slide (convolve) over the input to produce **feature maps**. Each filter detects a specific feature (edges, textures, patterns). The convolution operation: (feature map)_ij = Σ Σ (input ⊙ kernel) + bias.

- **Stride:** The step size by which the filter moves. Stride=1 moves one pixel at a time; stride=2 skips every other pixel, reducing spatial dimensions.
- **Padding:** Adding zeros around the input border. "Same" padding preserves spatial dimensions; "Valid" padding does not pad.

**2. Pooling Layer:** Reduces the spatial dimensions of feature maps (downsampling), decreasing computation and providing spatial invariance.

- **Max Pooling:** Takes the maximum value from each patch (e.g., 2×2 region). Most commonly used.
- **Average Pooling:** Takes the average value from each patch.

**3. Activation (ReLU):** Applied after each convolution to introduce non-linearity: f(x) = max(0, x).

**4. Fully Connected (Dense) Layer:** After several convolutional and pooling layers, the feature maps are **flattened** into a 1D vector and fed into one or more fully connected layers for final classification or regression.

**Working Mechanism — Image Classification Example:**

Input: 32×32×3 color image (e.g., classifying handwritten digits).

1. **Conv Layer 1:** Apply 32 filters of size 5×5 → 32 feature maps of size 28×28. Apply ReLU.
2. **Pooling Layer 1:** Max pooling with 2×2 → size reduced to 14×14.
3. **Conv Layer 2:** Apply 64 filters of size 5×5 → 64 feature maps of size 10×10. Apply ReLU.
4. **Pooling Layer 2:** Max pooling with 2×2 → size reduced to 5×5.
5. **Flatten:** 64 × 5 × 5 = 1600-dimensional vector.
6. **FC Layer:** 1600 → 128 neurons with ReLU.
7. **Output Layer:** 128 → 10 neurons with softmax (for 10 digit classes).

Training uses backpropagation with cross-entropy loss.

**Notable CNN Architectures:** LeNet-5 (1998), AlexNet (2012), VGGNet, GoogLeNet/Inception, ResNet (2015, introduced skip connections).

## Zero-Shot and Few-Shot Learning

**Zero-Shot Learning:** The model classifies categories it has **never seen** during training. It relies on auxiliary information (semantic attributes, text descriptions, embeddings) to bridge seen and unseen classes. Example: a model trained on images of cats and dogs can classify a horse if given a semantic description relating horses to the training classes.

**Few-Shot Learning:** The model learns to classify new categories from only a **very small number of examples** (1–5 samples per class). Approaches include:

- **Metric Learning:** Learn a similarity function (e.g., Siamese networks) that compares new examples to the few labeled ones.
- **Meta-Learning ("Learning to Learn"):** Train the model on many small tasks so it can quickly adapt to new tasks with minimal data (e.g., MAML — Model-Agnostic Meta-Learning).

## Graph Convolutional Networks (Graph CNN)

Standard CNNs work on regular grids (images). **Graph CNNs** extend convolution operations to **graph-structured data** (nodes and edges) where the topology is irregular.

**Working:** Each node updates its feature representation by aggregating features from its neighboring nodes. In a GCN layer:

h_v^(l+1) = σ(Σ_{u ∈ N(v)} (1/c_{vu}) W^(l) h_u^(l))

where h_v is the feature of node v, N(v) is its neighbors, c_{vu} is a normalization factor, W is a learnable weight matrix, and σ is an activation function.

**Applications:** Social network analysis, molecular property prediction, recommendation systems, traffic forecasting.

---

# 5.3 Recurrent Neural Networks (RNN)

> **What are the challenges of RNNs? Discuss about the architecture to solve these challenges. (7) (Fall 2025)**
>
> **Explain the working mechanism of RNN with a suitable example. (8) (Spring 2025)**
>
> **Write a short note on RNN. (5) (Internal 2025)**

A **Recurrent Neural Network** is a neural network designed for processing **sequential data** (time series, text, speech) where the order of inputs matters. Unlike feedforward networks, RNNs have **recurrent connections** — the output at each time step is fed back as input to the next step, giving the network a form of memory.

**Architecture:**

At each time step t, the RNN receives input x_t and the previous hidden state h_{t−1}, and computes:

- **Hidden state:** h_t = f(W_xh · x_t + W_hh · h_{t−1} + b_h), where f is typically tanh.
- **Output:** y_t = g(W_hy · h_t + b_y), where g depends on the task (softmax for classification).

The same weight matrices (W_xh, W_hh, W_hy) are **shared across all time steps** (parameter sharing).

**Training:** RNNs are trained using **Backpropagation Through Time (BPTT)** — the network is "unrolled" across time steps, and standard backpropagation is applied to the unrolled graph.

**Example — Next Word Prediction:** Given the sentence "The cat sat on the ___", at each time step, the RNN processes one word, updates its hidden state (accumulating context), and at the final step, predicts the next word from the vocabulary using softmax.

**Challenges of RNNs:**

1. **Vanishing Gradient Problem:** During BPTT, gradients are multiplied by the weight matrix at each time step. If the weights are small (eigenvalues < 1), gradients shrink exponentially, making it impossible to learn **long-range dependencies**. The network "forgets" information from early time steps.
2. **Exploding Gradient Problem:** If weights are large (eigenvalues > 1), gradients grow exponentially, causing numerical instability and divergent training. Mitigated by **gradient clipping** (capping gradient magnitude).
3. **Difficulty with Long Sequences:** Standard RNNs struggle to maintain relevant information over sequences longer than ~10–20 time steps.
4. **Sequential Processing:** RNNs process time steps one by one, preventing parallelization and making training slow on long sequences.

## LSTM (Long Short-Term Memory)

**LSTM** (Hochreiter & Schmidhuber, 1997) solves the vanishing gradient problem by introducing a **cell state** (a highway for information flow) and three **gating mechanisms** that control what information is stored, forgotten, and output.

**Gates (all use sigmoid activation, outputting values in [0, 1]):**

**1. Forget Gate:** Decides what information to **discard** from the cell state.
f_t = σ(W_f · [h_{t−1}, x_t] + b_f)

**2. Input Gate:** Decides what **new information** to store in the cell state.
i_t = σ(W_i · [h_{t−1}, x_t] + b_i)
C̃_t = tanh(W_C · [h_{t−1}, x_t] + b_C) — candidate cell state

**3. Cell State Update:**
C_t = f_t ⊙ C_{t−1} + i_t ⊙ C̃_t

**4. Output Gate:** Decides what part of the cell state to **output** as the hidden state.
o_t = σ(W_o · [h_{t−1}, x_t] + b_o)
h_t = o_t ⊙ tanh(C_t)

The cell state C_t acts as a conveyor belt — information can flow through it with minimal modification (just element-wise multiplication by the forget gate), allowing gradients to propagate through many time steps without vanishing.

## GRU (Gated Recurrent Unit)

**GRU** (Cho et al., 2014) is a simplified variant of LSTM with **two gates** instead of three, merging the cell state and hidden state into a single state.

**Gates:**

**1. Update Gate:** Controls how much of the previous hidden state to retain (combines forget and input gate functions).
z_t = σ(W_z · [h_{t−1}, x_t])

**2. Reset Gate:** Controls how much of the previous state to "forget" when computing the candidate state.
r_t = σ(W_r · [h_{t−1}, x_t])

**Candidate and final state:**
h̃_t = tanh(W · [r_t ⊙ h_{t−1}, x_t])
h_t = (1 − z_t) ⊙ h_{t−1} + z_t ⊙ h̃_t

GRUs have fewer parameters than LSTMs and train faster, while achieving comparable performance on many tasks.

---

# 5.4 Attention Mechanisms

> **What is the attention mechanism used in transformers? (Spring 2025)**

In standard sequence-to-sequence models (encoder-decoder RNNs), the entire input sequence is compressed into a single fixed-length context vector. This creates a **bottleneck** — for long sequences, the fixed vector cannot capture all relevant information, and performance degrades.

**Attention** (Bahdanau et al., 2015) solves this by allowing the decoder to **look at all encoder hidden states** and focus on the most relevant parts of the input for each output step.

**How Attention Works:**

1. The encoder produces hidden states h₁, h₂, ..., h_T for each input position.
2. At each decoder time step t, compute **attention scores** e_{ti} = score(s_t, h_i), where s_t is the decoder's current state and h_i is each encoder state.
3. Apply softmax to get **attention weights:** α_{ti} = softmax(e_{ti}).
4. Compute the **context vector** as a weighted sum: c_t = Σ α_{ti} · h_i.
5. Use c_t along with the decoder state to generate the output.

**Score Functions:**

- **Dot product:** score(s, h) = sᵀh
- **Scaled dot product:** score(s, h) = sᵀh / √d_k (used in Transformers)
- **Additive (Bahdanau):** score(s, h) = vᵀ tanh(W₁s + W₂h)

## Self-Attention

In self-attention, a sequence attends to **itself** — each position computes attention over all other positions in the same sequence. This captures dependencies between all pairs of tokens regardless of distance.

For each token, three vectors are computed from its embedding:

- **Query (Q):** What this token is looking for.
- **Key (K):** What this token can offer to others.
- **Value (V):** The actual information content.

**Scaled Dot-Product Attention:**

Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V

The division by √d_k prevents dot products from becoming too large, which would push softmax into regions with very small gradients.

## Multi-Head Attention

Instead of computing attention once, **multi-head attention** runs h parallel attention functions (heads) with different learned projections:

MultiHead(Q, K, V) = Concat(head₁, ..., head_h) · W^O
where head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)

Each head can attend to different aspects of the input (e.g., syntactic relationships, semantic similarities), providing a richer representation.

---

# 5.5 Transformers

> **Explain the transformer model architecture. (8) (Fall 2025)**
>
> **Describe transformer with its architectures. (Internal 2025)**

The **Transformer** (Vaswani et al., 2017, "Attention Is All You Need") is an architecture based **entirely on attention mechanisms**, dispensing with recurrence and convolutions. It processes all positions in parallel, enabling much faster training and superior performance on sequence tasks.

**Architecture — Encoder-Decoder:**

## Encoder

The encoder consists of a stack of N identical layers (N=6 in the original paper). Each layer has two sub-layers:

1. **Multi-Head Self-Attention:** Each position attends to all positions in the input. Captures contextual relationships.
2. **Position-wise Feed-Forward Network:** Two linear transformations with a ReLU activation: FFN(x) = max(0, xW₁ + b₁)W₂ + b₂. Applied independently to each position.

Each sub-layer has a **residual connection** (x + sublayer(x)) followed by **layer normalization**. Residual connections help gradients flow and enable training of deep networks.

## Decoder

The decoder also consists of N identical layers, each with three sub-layers:

1. **Masked Multi-Head Self-Attention:** Same as encoder self-attention but with masking — each position can only attend to previous positions (and itself), preventing information from future tokens from leaking during generation.
2. **Encoder-Decoder Attention:** Queries come from the decoder, while keys and values come from the encoder output. This allows the decoder to attend to all positions of the input sequence.
3. **Position-wise Feed-Forward Network:** Same as in the encoder.

## Positional Encoding

Since the Transformer has no recurrence, it has no inherent notion of token order. **Positional encodings** are added to the input embeddings to inject information about token positions:

PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

where pos is the position and i is the dimension index. The sinusoidal functions allow the model to extrapolate to sequence lengths not seen during training.

**Advantages of Transformers over RNNs:**

- **Parallelization:** All positions are processed simultaneously, unlike RNNs which process sequentially.
- **Long-range dependencies:** Self-attention connects every pair of positions directly (O(1) path length), unlike RNNs (O(n) path length).
- **Scalability:** Scales better to large datasets and long sequences.

**Transformer Variants:**

- **Encoder-only:** BERT — used for understanding tasks (classification, QA, NER).
- **Decoder-only:** GPT — used for generation tasks (text generation, chatbots).
- **Encoder-Decoder:** Original Transformer, T5, BART — used for sequence-to-sequence tasks (translation, summarization).

## BERT (Bidirectional Encoder Representations from Transformers)

BERT (Devlin et al., 2019) uses the **encoder** portion of the Transformer. It reads the entire input sequence **bidirectionally** — every token attends to every other token in both directions simultaneously.

**Pre-training objectives:**

- **Masked Language Model (MLM):** Randomly mask 15% of tokens and train the model to predict them from context.
- **Next Sentence Prediction (NSP):** Given two sentences, predict whether the second sentence follows the first in the original text.

After pre-training on large corpora, BERT is **fine-tuned** on specific downstream tasks (sentiment analysis, question answering, NER) by adding a task-specific output layer.

## GPT (Generative Pre-trained Transformer)

GPT uses the **decoder** portion of the Transformer. It reads the input **left-to-right** (unidirectional/autoregressive) — each token can only attend to tokens before it.

**Pre-training objective:** Next-token prediction — predict the next token given all previous tokens. This autoregressive approach is ideal for text generation.

GPT models (GPT-2, GPT-3, GPT-4) scale by increasing model size, data, and compute, demonstrating emergent abilities with scale.

---

# 5.6 Graph Attention Networks (GAT)

**Graph Attention Networks** (Veličković et al., 2018) apply the attention mechanism to graph-structured data. Unlike Graph CNNs (GCNs) which assign fixed weights to neighbors based on graph structure (node degrees), GATs **learn dynamic attention weights** for each neighbor, allowing the model to focus on the most important connections.

**Architecture of a GAT Layer:**

1. **Linear Transformation:** Apply a shared weight matrix W to transform node features: h'_i = W · h_i.
2. **Attention Coefficients:** For each edge (i, j), compute a raw attention score using a learnable attention mechanism a: e_{ij} = LeakyReLU(aᵀ · [h'_i ∥ h'_j]), where ∥ denotes concatenation.
3. **Normalization:** Apply softmax across all neighbors of node i: α_{ij} = softmax_j(e_{ij}) = exp(e_{ij}) / Σ_{k ∈ N(i)} exp(e_{ik}).
4. **Aggregation:** Compute the updated node representation: h_i^(new) = σ(Σ_{j ∈ N(i)} α_{ij} · h'_j).
5. **Multi-Head Attention:** Use K independent attention heads and concatenate (or average) their outputs for stability.

**Advantages over GCNs:**

- **Adaptive weighting:** Different neighbors get different importance weights rather than uniform or degree-based weights.
- **Inductive capability:** Can generalize to unseen graph structures because attention weights depend on features, not fixed graph topology.
- **Interpretability:** Attention weights reveal which neighbors are most influential for each node's prediction.

**Applications:** Node classification in citation networks, social network analysis, protein-protein interaction prediction, knowledge graph completion.

---

# 5.7 Transfer Learning

> **What is the purpose of Transfer Learning? Differentiate between a Tokenizer and an Embedding. Justify which one is more suitable for machine learning procedures. (7) (Internal 2025)**
>
> **Write a short note on Transfer Learning. (5) (Fall 2025, Spring 2025)**

**Transfer Learning** is a technique where a model trained on one (usually large) task or dataset is **reused as the starting point** for a different but related task. Instead of training from scratch, the knowledge (learned features, weights, representations) from the source task is transferred to accelerate learning on the target task.

**Purpose:**

- **Reduces data requirements:** Enables training with limited labeled data for the target task.
- **Reduces training time:** Pre-trained weights provide a strong initialization, converging faster.
- **Improves performance:** Pre-trained models have learned general features (edges, textures in images; syntax, semantics in text) that transfer well to many tasks.

**Two Main Strategies:**

**1. Feature Extraction:** Use the pre-trained model as a fixed feature extractor. Freeze all pre-trained layers (no weight updates) and train only a new classifier/output layer on top. Best when: the target dataset is small and similar to the source dataset.

**2. Fine-Tuning:** Unfreeze some or all pre-trained layers and retrain them with a **low learning rate** on the target dataset. The early layers (which learn general features) are often kept frozen, while later layers (which learn task-specific features) are fine-tuned. Best when: the target dataset is moderately large or differs significantly from the source.

**Examples:**

- **Computer Vision:** Use ImageNet-pretrained ResNet/VGG as a feature extractor, then fine-tune on medical image classification.
- **NLP:** Use BERT/GPT pre-trained on large text corpora, then fine-tune on sentiment analysis, question answering, or named entity recognition.

## Tokenizer vs. Embedding

**Tokenizer:** A **preprocessing tool** that converts raw text into discrete tokens (units). It breaks text into words, subwords, or characters and maps each to an integer ID from a vocabulary. The tokenizer is a rule-based or trained algorithm — it does **not** capture semantic meaning.

- Types: Word-level (split by spaces), Subword-level (BPE, WordPiece, SentencePiece), Character-level.
- Output: A sequence of integer IDs. Example: "I love AI" → [101, 1045, 2293, 9932, 102].

**Embedding:** A **learned dense vector representation** of each token. It maps each token ID to a continuous vector in a high-dimensional space where semantically similar tokens are closer together. Embeddings capture meaning, relationships, and context.

- Output: A matrix of real-valued vectors. Example: token ID 1045 → [0.12, −0.34, 0.56, ...] (d-dimensional).

**Tokenizer vs. Embedding — Key Differences:**

- **Function:** Tokenizer = text → integer IDs (preprocessing). Embedding = integer IDs → dense vectors (representation learning).
- **Semantic Understanding:** Tokenizer has no semantic knowledge. Embedding captures semantic meaning.
- **Learnability:** Tokenizer is typically fixed (rule-based or pre-trained). Embedding weights are learned during model training.
- **Order in Pipeline:** Tokenization happens first; embedding happens second.

**Which is more suitable for ML?** **Embeddings** are more suitable for machine learning because they provide continuous, differentiable representations that neural networks can process and learn from. Tokenizers are a necessary preprocessing step but do not themselves contribute to learning — they merely convert text into a format that can be embedded. The power of modern NLP models lies in their embedding layers, which encode rich semantic information that enables tasks like classification, generation, and reasoning.
