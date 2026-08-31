# 6. Natural Language Processing

**Natural Language Processing (NLP)** is the subfield of AI concerned with giving computers the ability to understand, interpret, and generate human language. NLP bridges the gap between human communication and computer understanding. It involves techniques from linguistics, computer science, and machine learning to process text and speech data.

**Steps involved in NLP:**

1. **Lexical Analysis:** Tokenizing raw text into words, punctuation, and other meaningful units (tokens). Involves identifying word boundaries and normalizing text.
2. **Syntactic Analysis (Parsing):** Analyzing the grammatical structure of sentences using grammar rules to produce parse trees. Checks whether the sentence is well-formed.
3. **Semantic Analysis:** Extracting the meaning from syntactic structures. Maps syntactic structures to meaningful representations. Checks for meaningfulness (e.g., "colorless green ideas sleep furiously" is syntactically correct but semantically odd).
4. **Discourse Integration:** Understanding meaning in context — how a sentence relates to the sentences before and after it. Resolves references (e.g., "He" in "John went home. He was tired." refers to John).
5. **Pragmatic Analysis:** Understanding the intended effect or purpose of the language in a given context. Goes beyond literal meaning to interpret speaker intent, irony, or implication.

**Two main approaches to NLP:**

- **Rule-Based NLP:** Uses hand-crafted linguistic rules and grammars. Rules are written by domain experts. Example: a rule that says "a determiner followed by an adjective followed by a noun forms a noun phrase." Advantage: transparent, interpretable. Disadvantage: brittle, expensive to build, poor generalization.
- **Statistical NLP:** Learns patterns from large corpora of text using probabilistic and machine learning models. Example: a language model that learns P("cat" | "the") from counting co-occurrences in a corpus. Advantage: scalable, handles ambiguity better. Disadvantage: requires large data, less interpretable.

---

# 6.1 Language Models

> **What are n-grams in NLP? Discuss their types with examples. (8) (Internal 2025)**

A **language model** assigns a probability to a sequence of words. Given a sequence of words w₁, w₂, ..., wₙ, a language model computes P(w₁, w₂, ..., wₙ). Language models are fundamental to speech recognition, machine translation, spelling correction, and text generation.

By the chain rule of probability:

P(w₁, w₂, ..., wₙ) = P(w₁) × P(w₂|w₁) × P(w₃|w₁,w₂) × ... × P(wₙ|w₁,...,wₙ₋₁)

Computing the exact conditional probability P(wₙ|w₁,...,wₙ₋₁) requires enormous amounts of data for every possible history. The **n-gram model** approximates this by using only the last (n−1) words as context (the Markov assumption).

## N-Gram Models

An **n-gram** is a contiguous sequence of n items (words) from a given text. The n-gram model approximates the probability of a word given its entire history by conditioning only on the previous (n−1) words:

**P(wₙ | w₁, ..., wₙ₋₁) ≈ P(wₙ | wₙ₋(ₙ₋₁), ..., wₙ₋₁)**

N-gram probabilities are estimated by counting from a corpus using Maximum Likelihood Estimation (MLE):

**P(wₙ | wₙ₋₁) = Count(wₙ₋₁, wₙ) / Count(wₙ₋₁)** (for bigrams)

**Types of N-grams:**

**1. Unigram (n=1):** Each word is independent of all others. P(w₁, w₂, ..., wₙ) = P(w₁) × P(w₂) × ... × P(wₙ). Example: For the sentence "I love AI", P("I") = Count("I")/Total words, P("love") = Count("love")/Total words. Unigrams ignore word order entirely.

**2. Bigram (n=2):** Each word depends only on the immediately preceding word. P(wₙ | wₙ₋₁). Example: P("love" | "I") = Count("I love") / Count("I"). For "I love AI": P = P("I") × P("love"|"I") × P("AI"|"love").

**3. Trigram (n=3):** Each word depends on the two preceding words. P(wₙ | wₙ₋₂, wₙ₋₁). Example: P("AI" | "I", "love") = Count("I love AI") / Count("I love"). Captures more context but requires more data.

**4. Higher-order n-grams (4-gram, 5-gram, etc.):** Provide more context but suffer from data sparsity — many n-grams will never appear in the training corpus, leading to zero probability estimates.

**Smoothing:** To handle zero-count n-grams (unseen word sequences), smoothing techniques redistribute probability mass:

- **Laplace (Add-1) Smoothing:** Add 1 to all counts. P(wₙ | wₙ₋₁) = (Count(wₙ₋₁, wₙ) + 1) / (Count(wₙ₋₁) + V), where V is vocabulary size.
- **Backoff:** If the trigram count is zero, fall back to the bigram; if bigram is zero, fall back to unigram.
- **Interpolation:** Combine unigram, bigram, and trigram probabilities with weights: P = λ₃P_trigram + λ₂P_bigram + λ₁P_unigram, where λ₁ + λ₂ + λ₃ = 1.

**Perplexity:** A standard evaluation metric for language models. Perplexity = 2^H, where H is the cross-entropy. Lower perplexity indicates a better model — the model is less "surprised" by the test data.

---

# 6.2 Part-of-Speech (POS) Tagging

> **Define POS tagging. Explain different approaches to POS tagging with examples. (7) (Spring 2025)**

**POS tagging** is the process of assigning a grammatical category (part-of-speech tag) to each word in a sentence. Common POS tags include NN (noun), VB (verb), JJ (adjective), DT (determiner), RB (adverb), IN (preposition), PRP (pronoun), etc.

Example: "The/DT cat/NN sat/VBD on/IN the/DT mat/NN"

POS tagging is challenging because many words are **ambiguous** — the same word can have different tags depending on context. For example, "book" can be a noun ("read a book") or a verb ("book a flight").

**Approaches to POS Tagging:**

**1. Rule-Based Tagging:** Uses hand-crafted linguistic rules to assign tags. A lexicon provides all possible tags for each word. Disambiguation rules select the correct tag based on context. Example rules: "If a word follows a determiner and is not known to be a verb, tag it as a noun," or "If a word ends in '-ly', tag it as an adverb (RB)." Advantages: transparent and interpretable. Disadvantages: labor-intensive to create, hard to scale, struggles with unknown words.

**2. Stochastic (Statistical) Tagging:** Uses probabilistic models trained on annotated corpora.

- **HMM-based tagging:** The most common statistical approach. The task is to find the tag sequence T = t₁, t₂, ..., tₙ that maximizes P(T|W) for a word sequence W = w₁, w₂, ..., wₙ. By Bayes' theorem: P(T|W) ∝ P(W|T) × P(T). Two key probabilities:
  - **Emission probability:** P(wᵢ | tᵢ) — probability that tag tᵢ generates word wᵢ.
  - **Transition probability:** P(tᵢ | tᵢ₋₁) — probability of tag tᵢ following tag tᵢ₋₁.
  - The optimal tag sequence is found using the **Viterbi algorithm** (dynamic programming). Example: P(NN→VB) might be 0.3, P("run"|VB) might be 0.02.

**3. Transformation-Based Tagging (Brill Tagger):** A hybrid approach combining rule-based and statistical methods. It starts by assigning each word its most frequent tag from the training corpus, then iteratively learns transformation rules that correct tagging errors. Example rule: "Change tag from VB to NN if the previous word is a DT." The rules are learned automatically from data but are human-readable, combining the interpretability of rule-based methods with the data-driven nature of statistical methods.

**4. Deep Learning-Based Tagging:** Modern approaches use neural networks (Bi-LSTM, Transformers) trained on tagged corpora. These models learn contextual representations and achieve state-of-the-art accuracy without hand-crafted features.

---

# 6.3 Grammar and Parsing

**Grammar** in NLP defines the structural rules governing the composition of sentences. **Parsing** is the process of analyzing a sentence according to a grammar to produce a structured representation (parse tree).

## Context-Free Grammar (CFG)

A **Context-Free Grammar** G is defined as a 4-tuple G = (N, Σ, R, S) where:

- **N:** Set of non-terminal symbols (e.g., S, NP, VP, PP, DT, NN, VB).
- **Σ:** Set of terminal symbols (the actual words).
- **R:** Set of production rules of the form A → α, where A ∈ N and α is a string of terminals and non-terminals.
- **S:** Start symbol (usually S for Sentence).

**Example CFG:**

```
S  → NP VP
NP → DT NN | DT JJ NN | PRP
VP → VB NP | VB NP PP
PP → IN NP
DT → "the" | "a"
NN → "dog" | "cat" | "park"
JJ → "big"
VB → "chased" | "saw"
IN → "in"
PRP → "I"
```

Parsing "The dog chased a cat":
- S → NP VP → (DT NN)(VB NP) → ("the" "dog")("chased" DT NN) → "the dog chased a cat"

## Types of Parsing

**1. Constituency (Phrase-Structure) Parsing:** Breaks a sentence into nested sub-phrases (constituents) based on CFG rules. The result is a hierarchical tree where internal nodes are non-terminals (NP, VP) and leaves are words. Useful for understanding the phrase structure of a sentence.

**2. Dependency Parsing:** Focuses on binary relations between words. Each word is connected to its syntactic "head" by a labeled directed edge (e.g., nsubj, dobj, det). There is no nesting of phrases — the structure is a tree of word-to-word dependencies. Example: In "The cat sat on the mat", "sat" is the root; "cat" depends on "sat" (nsubj); "mat" depends on "on" (pobj); "on" depends on "sat" (prep).

**Parsing Algorithms:**

- **Top-Down Parsing:** Starts from the start symbol S and tries to derive the sentence by expanding rules. May explore many dead-end paths.
- **Bottom-Up Parsing:** Starts from the words and applies rules in reverse to reduce them to the start symbol S.
- **CYK Algorithm (Cocke-Younger-Kasami):** A dynamic programming algorithm for parsing with CFGs. Requires the grammar to be in **Chomsky Normal Form** (CNF), where every rule is either A → BC or A → a. Fills a triangular table where each cell [i, j] contains the set of non-terminals that can derive the substring from position i to j. Time complexity: O(n³ · |G|).

---

# 6.4 Complications of Real Natural Language

> **What are the key challenges in NLP? (7) (Internal 2025)**
>
> **Write a short note on Complications of Real Natural Language. (5) (Fall 2025)**

Real natural language is far more complex than formal languages. The major complications include:

**1. Ambiguity:** The single greatest challenge in NLP. A word, phrase, or sentence can have multiple valid interpretations.

- **Lexical ambiguity:** A word has multiple meanings. "Bank" can mean a financial institution or a river bank. "Bat" can mean a flying mammal or a cricket bat.
- **Syntactic ambiguity:** A sentence has multiple valid parse trees. "I saw the man with a telescope" — did I use a telescope to see him, or did I see a man who had a telescope?
- **Semantic ambiguity:** "Every student read a book" — did all students read the same book, or each a different one?
- **Referential ambiguity:** "John told Bill that he was wrong" — does "he" refer to John or Bill?

**2. Metaphor:** Non-literal use of language where one concept is described in terms of another. "Time is money," "He has a heart of stone," "She drowned in paperwork." The literal meaning of the words does not convey the intended meaning.

**3. Metonymy:** A figure of speech where something is referred to by the name of something closely associated with it. "The White House announced" (the president/administration announced), "I read Shakespeare" (I read Shakespeare's works), "The pen is mightier than the sword" (writing/diplomacy vs. military force).

**4. Anaphora and Coreference:** Pronouns and definite descriptions refer back to previously mentioned entities. "Alice went to the store. She bought milk." — resolving that "She" = Alice requires discourse understanding.

**5. Pragmatics and Context-Dependence:** The meaning of an utterance depends on context, speaker intent, and shared world knowledge. "Can you pass the salt?" is literally a question about ability but pragmatically a request.

**6. Idioms and Non-Compositionality:** Phrases whose meaning cannot be derived from individual word meanings. "Kick the bucket" means to die, not literally kicking a bucket.

**7. Language Variability:** Dialects, slang, misspellings, code-switching, abbreviations, and informal grammar in real-world text (social media, chat) make processing difficult.

---

# 6.5 Word Embeddings

> **How do prediction-based embeddings overcome the limitations of frequency-based embeddings? Explain how words are converted into vector representations using the Continuous Bag-of-Words model. (7) (Internal 2025)**

**Word embeddings** are dense, low-dimensional vector representations of words that capture semantic and syntactic relationships. Unlike one-hot encoding (sparse, high-dimensional, no semantic information), embeddings place semantically similar words close together in vector space.

**Frequency-Based Embeddings:**

- **Bag of Words (BoW):** Represents a document as a vector of word counts. Ignores word order and context. High-dimensional and sparse.
- **TF-IDF (Term Frequency–Inverse Document Frequency):** Weights word counts by how important they are to a document relative to the corpus. Still sparse and high-dimensional.
- **Co-occurrence Matrix:** Counts how often words co-occur within a context window across the corpus. Can be reduced using SVD (Singular Value Decomposition) to get dense vectors. Limitation: large matrices, computationally expensive, cannot capture complex patterns.

**Limitations of Frequency-Based Methods:** High dimensionality, sparsity, inability to capture nuanced semantic relationships, no handling of polysemy (multiple meanings), and poor scalability.

**Prediction-Based Embeddings (Word2Vec):**

**Word2Vec** (Mikolov et al., 2013) learns word embeddings by training a shallow neural network on a prediction task. It overcomes frequency-based limitations by learning dense, low-dimensional vectors that capture context-dependent semantic relationships. Two architectures:

**1. Continuous Bag of Words (CBOW):**

CBOW predicts the **target word** from its surrounding **context words**.

- **Input:** Context words within a window of size m around the target. For window size 2 and sentence "The cat sat on the mat", to predict "sat": context = {"The", "cat", "on", "the"}.
- **Architecture:** Input layer maps each context word to its embedding vector. These vectors are **averaged** (or summed) to produce a single context vector. A hidden layer processes this context vector. The output layer uses softmax to produce a probability distribution over the entire vocabulary. The word with the highest probability is the predicted target.
- **Training:** The network is trained to minimize the prediction error (cross-entropy loss). The learned weight matrices give the word embeddings.
- CBOW is faster to train and works well for frequent words.

**2. Skip-Gram:**

Skip-gram does the reverse — predicts the **context words** from the **target word**.

- **Input:** A single target word.
- **Output:** Predicts each context word within the window independently.
- Makes multiple predictions per target word, so it works better for rare words and larger datasets.
- Training uses techniques like **Negative Sampling** (instead of full softmax over the vocabulary, sample a few "negative" words and train the model to distinguish true context words from random ones) for efficiency.

**Properties of Word Embeddings:** After training, word vectors exhibit meaningful algebraic properties. For example: vec("king") − vec("man") + vec("woman") ≈ vec("queen"). Similar words (e.g., "happy" and "joyful") have high cosine similarity between their vectors.

**GloVe (Global Vectors):** Combines the advantages of co-occurrence statistics (global) with prediction-based learning. It factorizes the log of the word co-occurrence matrix to produce embeddings that capture both local context and global corpus statistics.

---

# 6.6 RNN for NLP

> **What are the limitations of RNN in NLP? Explain the approach used to overcome these limitations. (7) (Spring 2025)**

**Recurrent Neural Networks (RNNs)** are neural networks designed for sequential data. Unlike feedforward networks, RNNs have connections that loop back, allowing them to maintain a **hidden state** that acts as a memory of previous inputs. This makes them naturally suited for NLP tasks where word order matters.

**RNN Architecture:**

At each time step t, the RNN takes an input xₜ (e.g., a word embedding) and the previous hidden state hₜ₋₁, and computes:

- **hₜ = f(W_xh · xₜ + W_hh · hₜ₋₁ + b_h)** — new hidden state
- **yₜ = g(W_hy · hₜ + b_y)** — output

where f is typically tanh or ReLU, g is softmax for classification, W_xh, W_hh, W_hy are weight matrices shared across all time steps, and b_h, b_y are biases.

**RNN Applications in NLP:**

- **Language Modeling:** Predict the next word given previous words. The hidden state encodes the history of the sequence.
- **Text Classification / Sentiment Analysis:** Process the entire text sequence and use the final hidden state (or pooled states) to classify the text (e.g., positive/negative sentiment).
- **Named Entity Recognition (NER):** Tag each word in a sequence with an entity label (person, location, organization, etc.).
- **Machine Translation:** Encode a source sentence and decode it into a target language (with the encoder-decoder framework).

**RNN Variants:**

- **One-to-One:** Standard neural network (no recurrence).
- **One-to-Many:** Single input, sequence output (e.g., image captioning).
- **Many-to-One:** Sequence input, single output (e.g., sentiment analysis).
- **Many-to-Many:** Sequence input, sequence output (e.g., machine translation, POS tagging).

**Bidirectional RNN:** Processes the sequence in both forward and backward directions, capturing context from both past and future. Two hidden states (forward and backward) are concatenated at each time step. Useful for tasks where the meaning of a word depends on words that come after it (e.g., "He went to the bank to fish" — "fish" disambiguates "bank").

**Limitations of RNNs:**

1. **Vanishing Gradient Problem:** During backpropagation through time (BPTT), gradients are multiplied repeatedly through many time steps. If the gradients are < 1, they shrink exponentially, making it nearly impossible for the network to learn long-range dependencies. The network effectively "forgets" early inputs.
2. **Exploding Gradient Problem:** If gradients are > 1, they grow exponentially, causing numerical instability. Mitigated by **gradient clipping** (capping gradient values at a threshold).
3. **Sequential Processing:** RNNs process tokens one at a time, preventing parallelization. This makes training slow on long sequences.
4. **Short-Term Memory:** Due to vanishing gradients, standard RNNs struggle to retain information from many time steps ago.

**Solution → LSTM and GRU** (discussed in detail in Section 6.7).

---

# 6.7 LSTMs for NLP

> **What is a LSTM? Explain in detail how the LSTMs are used in NLP. (Spring 2025)**
>
> **What are the limitations of RNN in NLP? Explain the approach used to overcome these limitations. (7) (Spring 2025)**
>
> **What are the challenges of RNNs? Discuss about the architecture to solve these challenges. (7) (Fall 2025)**

**Long Short-Term Memory (LSTM)** networks are a specialized variant of RNNs designed to overcome the vanishing gradient problem by introducing a **gating mechanism** that controls the flow of information. Proposed by Hochreiter and Schmidhuber (1997).

**LSTM Architecture:**

Each LSTM unit has a **cell state** (Cₜ) — a long-term memory that runs through the entire chain — and three **gates** that regulate information flow:

**1. Forget Gate (fₜ):** Decides what information to **discard** from the cell state. It looks at the previous hidden state hₜ₋₁ and current input xₜ, and outputs a value between 0 (forget completely) and 1 (keep completely) for each element of the cell state.

**fₜ = σ(W_f · [hₜ₋₁, xₜ] + b_f)**

**2. Input Gate (iₜ):** Decides what new information to **store** in the cell state. Two parts:
- The input gate layer decides which values to update: **iₜ = σ(W_i · [hₜ₋₁, xₜ] + b_i)**
- A tanh layer creates a vector of candidate values: **C̃ₜ = tanh(W_C · [hₜ₋₁, xₜ] + b_C)**

**3. Cell State Update:** The old cell state Cₜ₋₁ is updated by forgetting some old information and adding some new: **Cₜ = fₜ ⊙ Cₜ₋₁ + iₜ ⊙ C̃ₜ** (where ⊙ denotes element-wise multiplication).

**4. Output Gate (oₜ):** Decides what part of the cell state to **output** as the hidden state.
- **oₜ = σ(W_o · [hₜ₋₁, xₜ] + b_o)**
- **hₜ = oₜ ⊙ tanh(Cₜ)**

**Why LSTM Solves the Vanishing Gradient Problem:** The cell state provides a direct path for gradients to flow through many time steps with minimal transformation. The forget gate can learn to keep its value close to 1, allowing gradients to pass through unchanged. This enables LSTMs to learn dependencies over hundreds of time steps.

**GRU (Gated Recurrent Unit):** A simplified variant of LSTM with only two gates (reset gate and update gate) and no separate cell state. Combines the forget and input gates into a single "update gate." Fewer parameters than LSTM, so faster to train, with comparable performance on many tasks.

**LSTM Applications in NLP:**

- **Language Modeling:** LSTMs can model long-range dependencies in text that standard RNNs cannot (e.g., subject-verb agreement across a long clause).
- **Machine Translation:** LSTM-based encoder-decoder models encode a source sentence and generate a translation.
- **Text Generation:** Generate text one word at a time, with the cell state maintaining coherence over long passages.
- **Sentiment Analysis:** Bi-directional LSTMs capture context from both directions for accurate classification.
- **Named Entity Recognition:** Bi-LSTM + CRF (Conditional Random Field) models are highly effective for sequence labeling tasks.

---

# 6.8 Sequence-to-Sequence Models

**Sequence-to-Sequence (Seq2Seq)** models map an input sequence of variable length to an output sequence of variable length. Introduced by Sutskever et al. (2014), they are the foundation for machine translation, text summarization, dialogue systems, and question answering.

**Encoder-Decoder Architecture:**

**Encoder:** An RNN (typically LSTM or GRU) that reads the input sequence x₁, x₂, ..., xₘ one token at a time and produces a sequence of hidden states. The final hidden state (and cell state for LSTM) is called the **context vector** — a fixed-length summary of the entire input.

**Decoder:** Another RNN that takes the context vector as its initial hidden state and generates the output sequence y₁, y₂, ..., yₙ one token at a time. At each step, the decoder takes the previous output word (or the ground-truth word during training — called **teacher forcing**) and its current hidden state to predict the next word.

**Training:** The model is trained end-to-end to maximize the probability of the correct output sequence given the input. Loss is computed using cross-entropy between the predicted and actual output tokens.

**The Bottleneck Problem:** The entire input sequence is compressed into a single fixed-length context vector. For long input sequences, this vector cannot capture all the necessary information, leading to information loss and degraded performance on long sentences.

**Solution → Attention Mechanism:**

The **attention mechanism** (Bahdanau et al., 2015) allows the decoder to "look back" at all encoder hidden states at every decoding step, rather than relying on a single context vector.

**How Attention Works:**

1. The encoder produces hidden states h₁, h₂, ..., hₘ for each input token.
2. At each decoder time step t, the decoder hidden state sₜ is compared with every encoder hidden state hⱼ to compute an **alignment score** eₜⱼ.
3. The scores are normalized using softmax to get **attention weights** αₜⱼ = softmax(eₜⱼ).
4. A **dynamic context vector** cₜ is computed as the weighted sum: cₜ = Σⱼ αₜⱼ · hⱼ.
5. The context vector cₜ is concatenated with the decoder state sₜ and used to predict the output word.

**Types of Attention:**

- **Bahdanau (Additive) Attention:** Computes alignment scores using a feedforward network: eₜⱼ = vᵀ · tanh(W₁ · sₜ + W₂ · hⱼ).
- **Luong (Dot-Product) Attention:** Computes scores using a simple dot product: eₜⱼ = sₜᵀ · hⱼ. Simpler and faster.

**Effect:** Attention dramatically improves translation quality, especially on long sentences, by letting the decoder focus on relevant parts of the input at each step. The attention weights also provide an interpretable alignment between input and output tokens.

---

# 6.9 The Transformer Architecture — BERT, GPT, Attention

> **Describe transformer with its architecture. (8) (Internal 2025)**
>
> **Explain the transformer model architecture. (8) (Fall 2025)**
>
> **What is the attention mechanism used in transformers? Describe the architecture of BERT. (8) (Spring 2025)**
>
> **LLMs have revolutionized AI. What is the foundational innovation and architecture beneath these breakthroughs? Explain. (8) (Fall 2025)**

The **Transformer** (Vaswani et al., 2017, "Attention Is All You Need") is a neural network architecture that relies entirely on **self-attention** mechanisms, dispensing with recurrence and convolutions altogether. It is the foundation of all modern large language models (LLMs) including BERT, GPT, T5, and others.

**Why Transformers over RNNs/LSTMs:**

- RNNs process tokens sequentially — token t must wait for token t−1. This prevents parallelization and is slow for long sequences.
- RNNs still struggle with very long-range dependencies despite LSTMs.
- Transformers process all tokens **in parallel** using self-attention, making them much faster to train on modern hardware (GPUs/TPUs).
- Self-attention directly connects every token to every other token, regardless of distance.

## Self-Attention (Scaled Dot-Product Attention)

For each input token, the model creates three vectors by multiplying the input embedding with learned weight matrices:

- **Query (Q):** What this token is looking for.
- **Key (K):** What this token offers to others.
- **Value (V):** The actual content of this token.

The attention output is computed as:

**Attention(Q, K, V) = softmax(QKᵀ / √dₖ) · V**

where dₖ is the dimension of the key vectors (scaling prevents dot products from growing too large and pushing softmax into regions of tiny gradients).

**Intuition:** Each token computes a similarity score (via dot product) with every other token. High scores mean high relevance. The output is a weighted sum of all value vectors, where the weights reflect how much attention each token pays to the others.

## Multi-Head Attention

Instead of performing a single attention function, the model runs **h parallel attention heads**, each with different learned projections of Q, K, V:

**MultiHead(Q, K, V) = Concat(head₁, head₂, ..., headₕ) · W_O**

where headᵢ = Attention(QWᵢQ, KWᵢK, VWᵢV).

Each head can learn to attend to different types of relationships (e.g., one head focuses on syntactic relations, another on semantic similarity). The outputs are concatenated and linearly projected.

## Positional Encoding

Since the Transformer has no recurrence or convolution, it has no inherent notion of token order. **Positional encodings** are added to the input embeddings to inject information about the position of each token. The original paper uses sine and cosine functions of different frequencies:

- PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
- PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

This allows the model to learn to attend to relative positions.

## Transformer Architecture

The full Transformer consists of an **Encoder** and a **Decoder**, each composed of stacked identical layers (typically 6):

**Encoder Layer:**
1. **Multi-Head Self-Attention:** Each token attends to all tokens in the input.
2. **Add & Norm:** Residual connection + Layer Normalization.
3. **Feed-Forward Network (FFN):** Two linear transformations with a ReLU activation: FFN(x) = max(0, xW₁ + b₁)W₂ + b₂. Applied independently to each position.
4. **Add & Norm:** Another residual connection + Layer Normalization.

**Decoder Layer:**
1. **Masked Multi-Head Self-Attention:** Each token attends only to previous tokens (masking future positions to prevent "cheating" during generation).
2. **Add & Norm.**
3. **Multi-Head Cross-Attention:** The decoder attends to the encoder's output (queries from decoder, keys and values from encoder).
4. **Add & Norm.**
5. **Feed-Forward Network.**
6. **Add & Norm.**

**Final Output:** The decoder's output goes through a linear layer and softmax to produce probabilities over the vocabulary for the next token.

## BERT (Bidirectional Encoder Representations from Transformers)

BERT (Devlin et al., 2018) uses only the **Encoder** part of the Transformer. It is designed for **understanding** tasks (classification, question answering, NER).

**Key Innovation — Bidirectional Context:** Unlike GPT which reads text left-to-right, BERT reads text in **both directions simultaneously**. Every token can attend to all other tokens (both left and right context).

**Pre-training Objectives:**

1. **Masked Language Model (MLM):** Randomly mask 15% of the input tokens and train the model to predict the masked words from context. This forces the model to learn deep bidirectional representations. Example: "The [MASK] sat on the mat" → predict "cat."
2. **Next Sentence Prediction (NSP):** Given two sentences, predict whether the second sentence follows the first in the original text. This helps the model understand sentence-level relationships.

**Fine-tuning:** After pre-training on a large corpus, BERT is fine-tuned on specific downstream tasks (sentiment analysis, question answering, NER) by adding a task-specific output layer and training on labeled data. Fine-tuning is fast because BERT already has rich language representations.

**BERT Architecture:** BERT-Base: 12 encoder layers, 768 hidden units, 12 attention heads, 110M parameters. BERT-Large: 24 layers, 1024 hidden units, 16 heads, 340M parameters.

## GPT (Generative Pre-trained Transformer)

GPT (Radford et al., 2018) uses only the **Decoder** part of the Transformer. It is designed for **generative** tasks (text generation, completion, dialogue).

**Key Design — Unidirectional (Autoregressive):** GPT predicts the next token conditioned only on the preceding tokens (left-to-right). This is natural for text generation — the model generates one token at a time.

**Pre-training:** Trained on causal language modeling — predict the next word given all previous words. P(wₜ | w₁, w₂, ..., wₜ₋₁).

**GPT vs. BERT:**

- BERT: Encoder-only, bidirectional, MLM training → excels at understanding/classification.
- GPT: Decoder-only, unidirectional, causal LM training → excels at generation.
- GPT scales to very large models (GPT-3: 175B parameters, GPT-4: rumored >1T) and exhibits emergent abilities (few-shot learning, reasoning) at scale.

**Why Transformers are the Foundation of LLMs:** The self-attention mechanism allows Transformers to capture long-range dependencies efficiently, process sequences in parallel for fast training, and scale to billions of parameters. These properties make them the backbone of all current large language models that power chatbots, translation systems, code generators, and more.
