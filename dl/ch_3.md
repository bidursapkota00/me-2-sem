# 3. Sequence Processing Networks

# 3.1 Fundamentals of Sequence Modeling

> **Describe the Transformer architecture in detail. Explain the role of self-attention and multi-head attention mechanisms, and contrast them with RNN-based sequence modeling. (Fall 2025)**

**Sequential data** is data where the order of elements matters — changing the order changes the meaning. Examples: text (word order defines sentences), audio (temporal order of samples), time series (stock prices over days), video (frame order), DNA sequences (nucleotide order).

**Why standard feedforward networks fail for sequences:** MLPs require fixed-size inputs, process each input independently, and have no mechanism to capture temporal dependencies. A sentence like "the cat sat on the mat" requires the network to understand that "sat" relates to "cat" — information spread across positions. MLPs treat each position independently and cannot model this.

**Sequence modeling tasks (by input-output structure):**

- **One-to-One:** Standard classification/regression (not truly sequential). Example: image classification.
- **One-to-Many:** Single input produces a sequence. Example: image captioning — one image generates a sequence of words.
- **Many-to-One:** A sequence produces a single output. Example: sentiment analysis — a sentence is classified as positive/negative.
- **Many-to-Many (synchronized):** Input and output sequences have the same length. Example: part-of-speech tagging — each word gets a tag.
- **Many-to-Many (encoder-decoder):** Input and output sequences have different lengths. Example: machine translation — an English sentence maps to a French sentence of different length.

**Challenges in sequence modeling:**

- **Variable length:** Sequences can have different lengths (sentences have varying word counts), so the model must handle arbitrary-length inputs.
- **Long-range dependencies:** Meaning often depends on elements far apart in the sequence. In "The cat, which was sitting on the mat, **stood** up," the verb "stood" depends on "cat" many words earlier.
- **Temporal order:** The model must preserve and exploit the ordering of elements.

---

# 3.2 RNN Architecture and Backpropagation

> **Explain the architecture of LSTM and how it solves the vanishing gradient problem present in vanilla RNNs. Use diagrams and equations to support your answer. (Fall 2025)**

## 3.2.1 Vanilla RNN Architecture

A **Recurrent Neural Network (RNN)** processes sequences by maintaining a **hidden state** $h_t$ that is updated at each time step, carrying information from all previous time steps.

**Computation at each time step t:**

$
h_t = \tanh(W_{hh} \cdot h_{t-1} + W_{xh} \cdot x_t + b_h)
$

$
y_t = W_{hy} \cdot h_t + b_y
$

where $x_t$ is the input at time $t$, $h_{t-1}$ is the previous hidden state, $W_{xh}$ is the input-to-hidden weight matrix, $W_{hh}$ is the hidden-to-hidden (recurrent) weight matrix, $W_{hy}$ is the hidden-to-output weight matrix, and $b_h$, $b_y$ are biases.

**Key properties:**

- **Weight sharing:** The same weight matrices ($W_{xh}$, $W_{hh}$, $W_{hy}$) are used at every time step. This allows the network to handle sequences of any length and generalize patterns across positions.
- **Hidden state as memory:** $h_t$ acts as a compressed summary of all inputs seen so far ($x_1, x_2, ..., x_t$).
- **Unrolling:** For training, the RNN is "unrolled" across time steps into a chain of identical modules, creating a computational graph that resembles a very deep feedforward network.

## 3.2.2 Backpropagation Through Time (BPTT)

**BPTT** is the training algorithm for RNNs — it applies standard backpropagation to the unrolled network.

**Forward pass:** Process the entire sequence step by step, computing $h_1, h_2, ..., h_T$ and outputs $y_1, y_2, ..., y_T$. Compute the total loss:

$
L = \sum_{t=1}^{T} L_t(y_t, \hat{y}_t)
$

**Backward pass:** Compute gradients of $L$ with respect to each weight by propagating errors backward through all time steps. The gradient of the loss with respect to the recurrent weight $W_{hh}$ involves the chain rule applied across time:

$
\frac{\partial L}{\partial W_{hh}} = \sum_{t=1}^{T} \sum_{k=1}^{t} \frac{\partial L_t}{\partial y_t} \cdot \frac{\partial y_t}{\partial h_t} \cdot \left( \prod_{j=k+1}^{t} \frac{\partial h_j}{\partial h_{j-1}} \right) \cdot \frac{\partial h_k}{\partial W_{hh}}
$

The term $\prod_{j=k+1}^{t} \frac{\partial h_j}{\partial h_{j-1}}$ is the product of Jacobians across time steps.

## 3.2.3 Vanishing and Exploding Gradients

The product $\prod_{j=k+1}^{t} \frac{\partial h_j}{\partial h_{j-1}}$ involves repeated multiplication of the recurrent weight matrix and the derivative of the activation function.

**Vanishing gradient:** If the spectral radius (largest eigenvalue) of $W_{hh}$ is less than 1, the gradient product shrinks exponentially as $t - k$ grows. Gradients from distant time steps become negligibly small, and the network cannot learn long-range dependencies. The weights effectively stop receiving updates from early time steps.

**Exploding gradient:** If the spectral radius of $W_{hh}$ is greater than 1, the gradient product grows exponentially, causing numerical overflow and unstable training. **Gradient clipping** mitigates this — if the gradient norm exceeds a threshold, it is scaled down:

$
\mathbf{g} \leftarrow \frac{\text{threshold}}{||\mathbf{g}||} \cdot \mathbf{g} \quad \text{if } ||\mathbf{g}|| > \text{threshold}
$

**Truncated BPTT:** Instead of backpropagating through the entire sequence, gradients are propagated for only a fixed number of time steps. This limits computational cost and avoids very long gradient chains, at the expense of not capturing very long-range dependencies.

---

# 3.3 Types of RNNs

> **Compare Vanilla RNN, GRU, LSTM, and Bi-directional RNN in terms of architecture, computational cost, and suitability for different sequential tasks. (Fall 2025)**

## 3.3.1 Vanilla RNN

The basic RNN described in Section 3.2.1. Uses a single hidden state updated by a tanh activation. Simple and computationally cheap, but suffers severely from vanishing gradients — cannot effectively learn dependencies beyond 10–20 time steps.

## 3.3.2 Long Short-Term Memory (LSTM)

> **Explain the architecture of LSTM and how it solves the vanishing gradient problem present in vanilla RNNs. Use diagrams and equations to support your answer. (Fall 2025)**

The **LSTM** (Hochreiter & Schmidhuber, 1997) introduces a **cell state** $C_t$ — a separate memory pathway that runs through the entire sequence with only linear interactions, allowing gradients to flow unchanged over long distances. Three **gates** (sigmoid layers outputting values between 0 and 1) control what information enters, exits, and is retained in the cell state.

**LSTM Equations:**

**1. Forget Gate** — decides what information to discard from the cell state:

$
f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)
$

**2. Input Gate** — decides what new information to store in the cell state:

$
i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)
$

**3. Candidate Cell State** — creates new candidate values:

$
\tilde{C}_t = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C)
$

**4. Cell State Update** — combines old memory (scaled by forget gate) with new information (scaled by input gate):

$
C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t
$

**5. Output Gate** — decides what part of the cell state to output:

$
o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)
$

**6. Hidden State** — filtered version of the cell state:

$
h_t = o_t \odot \tanh(C_t)
$

where $\sigma$ is the sigmoid function, $\odot$ is element-wise multiplication, and $[h_{t-1}, x_t]$ denotes concatenation of the previous hidden state and current input.

**How LSTM solves the vanishing gradient problem:** The cell state update $C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$ is a linear operation (element-wise multiplication and addition). When the forget gate $f_t \approx 1$ and the input gate $i_t \approx 0$, the cell state is copied forward unchanged: $C_t \approx C_{t-1}$. The gradient of $C_t$ with respect to $C_{t-1}$ is simply $f_t$, which can remain close to 1. This creates a "gradient highway" — gradients can flow backward through many time steps without vanishing, allowing the network to learn long-range dependencies.

## 3.3.3 Gated Recurrent Unit (GRU)

The **GRU** (Cho et al., 2014) is a simplified variant of the LSTM that merges the cell state and hidden state into a single hidden state $h_t$ and uses two gates instead of three.

**GRU Equations:**

**1. Reset Gate** — controls how much of the previous hidden state to forget:

$
r_t = \sigma(W_r \cdot [h_{t-1}, x_t] + b_r)
$

**2. Update Gate** — controls the balance between old state and new candidate (acts as both forget and input gate):

$
z_t = \sigma(W_z \cdot [h_{t-1}, x_t] + b_z)
$

**3. Candidate Hidden State:**

$
\tilde{h}_t = \tanh(W_h \cdot [r_t \odot h_{t-1}, x_t] + b_h)
$

**4. Hidden State Update:**

$
h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t
$

When $z_t \approx 0$, $h_t \approx h_{t-1}$ (the state is carried forward unchanged — similar to LSTM's forget gate being ~1). When $z_t \approx 1$, $h_t \approx \tilde{h}_t$ (the state is replaced with new information).

**GRU vs. LSTM:** GRU has fewer parameters (~25% fewer), trains faster, and performs comparably to LSTM on many tasks. LSTM may perform better on tasks requiring very fine-grained memory control due to the separate cell state and output gate.

## 3.3.4 Bidirectional RNN

A **Bidirectional RNN (Bi-RNN)** processes the input sequence in both directions — forward (left-to-right) and backward (right-to-left) — using two separate hidden layers.

**Architecture:**

- **Forward RNN** computes hidden states $\overrightarrow{h}_1, \overrightarrow{h}_2, ..., \overrightarrow{h}_T$ by processing $x_1 \rightarrow x_T$.
- **Backward RNN** computes hidden states $\overleftarrow{h}_T, \overleftarrow{h}_{T-1}, ..., \overleftarrow{h}_1$ by processing $x_T \rightarrow x_1$.
- At each time step, the output combines both: $h_t = [\overrightarrow{h}_t ; \overleftarrow{h}_t]$ (concatenation).

**Advantage:** Each position has access to context from both the past and the future. This is critical for tasks where the meaning of a word depends on what comes after it.

**Limitation:** Requires the entire input sequence to be available upfront — cannot be used for real-time or autoregressive tasks (e.g., language generation where future tokens are not available).

**Applications:** Named entity recognition, part-of-speech tagging, speech recognition, machine translation encoding.

The bidirectional approach can use Vanilla RNN, LSTM, or GRU as the base unit. **Bi-LSTM** is the most common variant.

## 3.3.5 Recursive Neural Network

A **Recursive Neural Network (RvNN)** is designed for hierarchically structured (tree-structured) data rather than linear sequences. It applies the same weight matrix recursively over a tree structure, combining child node representations to compute parent node representations.

**Architecture:** Given a binary tree, each leaf node is an input vector. For each internal node with children $c_1$ and $c_2$:

$
h_{\text{parent}} = \tanh(W \cdot [h_{c_1}; h_{c_2}] + b)
$

The same $W$ is applied at every internal node. The root node's representation captures the meaning of the entire tree.

**Applications:** Sentence-level sentiment analysis using parse trees (where the tree structure reflects the syntactic structure of the sentence), program analysis, molecular structure processing.

**Comparison Table:**

| Feature            | Vanilla RNN      | LSTM                  | GRU                   | Bi-RNN                    |
| :----------------- | :--------------- | :-------------------- | :-------------------- | :------------------------- |
| **Gates**          | None             | 3 (forget, input, output) | 2 (reset, update)   | Depends on base unit       |
| **Memory**         | Hidden state only | Cell state + hidden   | Hidden state only     | Forward + backward states  |
| **Parameters**     | Fewest           | Most (~4× vanilla)    | Moderate (~3× vanilla)| 2× base unit               |
| **Long-range**     | Poor             | Excellent             | Good                  | Excellent (with LSTM/GRU)  |
| **Training speed** | Fastest          | Slowest               | Moderate              | ~2× base unit              |
| **Best for**       | Short sequences  | Complex long sequences | General sequences     | Tasks needing full context |

---

# 3.4 Transformer and Attention Mechanism

> **Describe the Transformer architecture in detail. Explain the role of self-attention and multi-head attention mechanisms, and contrast them with RNN-based sequence modeling. (Fall 2025)**

## 3.4.1 Attention Mechanism

**Motivation:** In RNN-based encoder-decoder models for tasks like machine translation, the entire input sequence is compressed into a single fixed-length context vector (the encoder's final hidden state). This creates an information bottleneck — long sequences lose information, and the decoder struggles with distant input tokens.

**Attention** allows the decoder to "look back" at all encoder hidden states and selectively focus on the most relevant ones for each output token.

**Mechanism:** Given decoder hidden state $s_t$ and encoder hidden states $h_1, h_2, ..., h_n$:

**1. Compute alignment scores** — how relevant each encoder state is to the current decoder state:

$
e_{t,i} = \text{score}(s_t, h_i)
$

Common scoring functions: dot product ($s_t^T h_i$), additive ($v^T \tanh(W_1 s_t + W_2 h_i)$).

**2. Compute attention weights** via softmax:

$
\alpha_{t,i} = \frac{\exp(e_{t,i})}{\sum_{j=1}^{n} \exp(e_{t,j})}
$

**3. Compute context vector** — weighted sum of encoder hidden states:

$
c_t = \sum_{i=1}^{n} \alpha_{t,i} \cdot h_i
$

The context vector $c_t$ is concatenated with the decoder state to produce the output.

## 3.4.2 Self-Attention

In **self-attention**, each element in a sequence attends to every other element in the same sequence to compute a context-aware representation. Unlike RNN-based attention (which is cross-attention between encoder and decoder), self-attention operates within a single sequence.

For each input token, three vectors are computed using learned weight matrices:

- **Query (Q):** "What am I looking for?"
- **Key (K):** "What do I contain?"
- **Value (V):** "What information do I provide?"

**Scaled Dot-Product Attention:**

$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V
$

where $d_k$ is the dimension of the key vectors. The scaling factor $\sqrt{d_k}$ prevents dot products from becoming too large, which would push softmax into regions with very small gradients.

**Step-by-step:** For each token, compute dot products of its query with all keys → scale → apply softmax to get attention weights → multiply by corresponding values → sum to get the output representation.

## 3.4.3 Multi-Head Attention

Instead of performing a single attention computation, **multi-head attention** runs $h$ attention operations in parallel, each with different learned projection matrices. This allows the model to attend to information from different representation subspaces at different positions simultaneously.

$
\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, ..., \text{head}_h) \cdot W^O
$

$
\text{head}_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)
$

where $W_i^Q$, $W_i^K$, $W_i^V$ are learned projection matrices for head $i$, and $W^O$ is the output projection matrix.

Example: with $d_{\text{model}} = 512$ and $h = 8$ heads, each head operates on $d_k = d_v = 512/8 = 64$ dimensions.

## 3.4.4 Transformer Architecture (Vaswani et al., 2017)

The Transformer is built entirely on attention mechanisms — it uses no recurrence or convolution. This allows full parallelization during training.

**Encoder (stack of N=6 identical layers):** Each layer has two sub-layers:

1. **Multi-head self-attention** — each position attends to all positions in the input.
2. **Position-wise feedforward network** — two linear transformations with a ReLU in between: $\text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2$.

Each sub-layer is followed by a **residual connection** and **layer normalization**: $\text{output} = \text{LayerNorm}(x + \text{SubLayer}(x))$.

**Decoder (stack of N=6 identical layers):** Each layer has three sub-layers:

1. **Masked multi-head self-attention** — positions can only attend to earlier positions (masking prevents the decoder from "seeing" future tokens during training).
2. **Multi-head cross-attention** — queries come from the decoder, keys and values come from the encoder output.
3. **Position-wise feedforward network** — same as encoder.

**Positional Encoding:** Since the Transformer processes all tokens in parallel (no recurrence), it has no inherent notion of token order. Positional encodings are added to the input embeddings to inject position information:

$
PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
$

$
PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
$

where $pos$ is the token position and $i$ is the dimension index. Sinusoidal functions allow the model to generalize to sequence lengths not seen during training.

## 3.4.5 Transformer vs. RNN

| Feature               | RNN/LSTM/GRU                 | Transformer                      |
| :-------------------- | :--------------------------- | :------------------------------- |
| **Processing**        | Sequential (step by step)    | Parallel (all tokens at once)    |
| **Training speed**    | Slow (cannot parallelize)    | Fast (fully parallelizable)      |
| **Long-range deps**   | Struggles (vanishing gradient)| Excellent (direct attention)    |
| **Memory mechanism**  | Hidden state (bottleneck)    | Attention over all positions     |
| **Position info**     | Implicit (from sequential processing) | Explicit (positional encoding) |
| **Complexity per layer** | $O(T \cdot d^2)$         | $O(T^2 \cdot d)$                |
| **Inductive bias**    | Strong (sequential)          | Weak (needs more data)           |

For short sequences, RNNs are competitive. For long sequences and large datasets, Transformers significantly outperform RNNs. Transformers dominate modern NLP (BERT, GPT), but RNNs/LSTMs remain relevant for streaming/online applications where the full sequence is not available.

---

# 3.5 Applications of Sequential Networks

**1. Natural Language Processing (NLP):**

- **Machine Translation:** Encoder-decoder models (Seq2Seq with attention, Transformer) translate text between languages. The encoder processes the source sentence; the decoder generates the target sentence token by token. Example: Google Translate uses Transformer-based models.
- **Sentiment Analysis:** A many-to-one task — an LSTM/Bi-LSTM reads a review and outputs a sentiment label (positive/negative/neutral).
- **Language Modeling:** Predicting the next word in a sequence. Autoregressive models like GPT use masked self-attention (decoder-only Transformer) to generate text token by token.
- **Named Entity Recognition (NER):** A many-to-many task — Bi-LSTM-CRF models tag each word in a sentence with entity types (PERSON, LOCATION, ORGANIZATION).
- **Text Summarization:** Encoder-decoder models compress long documents into concise summaries (abstractive summarization).

**2. Speech and Audio Processing:**

- **Speech Recognition (ASR):** Converts audio waveforms into text. Deep Speech models use Bi-directional RNNs; modern systems use Transformer-based architectures (Whisper). The input is a sequence of audio features (mel-spectrograms); the output is a sequence of characters or words.
- **Text-to-Speech (TTS):** Generates natural-sounding audio from text (Tacotron uses an attention-based encoder-decoder; WaveNet uses causal convolutions).

**3. Time Series Forecasting:**

- Predicting future values from historical observations — stock prices, weather, energy demand, disease spread. LSTMs and GRUs capture temporal patterns (trends, seasonality). The model takes a window of past values and predicts the next value or a horizon of future values.

**4. Video Processing:**

- Video captioning, action recognition, and video summarization use RNNs/LSTMs applied to sequences of frame-level features (often extracted by a CNN). Temporal ordering of frames is critical.

**5. Music Generation:**

- RNNs/LSTMs generate sequences of musical notes by learning patterns from training music. Each time step predicts the next note/chord conditioned on the previous sequence.

**6. Biological Sequence Analysis:**

- Protein structure prediction, gene expression analysis, and DNA sequence classification use sequential models to capture patterns in nucleotide or amino acid sequences.

---
