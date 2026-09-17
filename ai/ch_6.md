# 6. Natural Language Processing

**Natural Language Processing (NLP)** is the subfield of AI concerned with giving computers the ability to understand, interpret, and generate human language.

**\*\*Steps involved in NLP:**

1. **Lexical Analysis:** Tokenizing raw text into words, punctuation, and other meaningful units (tokens). Involves identifying word boundaries and normalizing text.
2. **Syntactic Analysis (Parsing):** Analyzing the grammatical structure of sentences using grammar rules to produce parse trees. Checks whether the sentence is well-formed.
3. **Semantic Analysis:** Extracting the meaning from syntactic structures. Maps syntactic structures to meaningful representations. Checks for meaningfulness (e.g., "colorless green ideas sleep furiously" is syntactically correct but semantically odd).
4. **Discourse Integration:** Understanding meaning in context — how a sentence relates to the sentences before and after it. Resolves references (e.g., "He" in "John went home. He was tired." refers to John).
5. **Pragmatic Analysis:** Understanding the intended effect or purpose of the language in a given context. Goes beyond literal meaning to interpret speaker intent, irony, or implication.

---

# 6.1 Language Models

> **What are n-grams in NLP? Discuss their types with examples. (8) (Internal 2025)**

A **language model** assigns a probability to a sequence of words. Given a sequence of words w₁, w₂, ..., wₙ, a language model computes P(w₁, w₂, ..., wₙ). Language models are fundamental to speech recognition, machine translation, spelling correction, and text generation.

By the chain rule of probability:

P(w₁, w₂, ..., wₙ) = P(w₁) × P(w₂|w₁) × P(w₃|w₁,w₂) × ... × P(wₙ|w₁,...,wₙ₋₁)

For example, "I am going to school" is very likely. But "School going am I to" is very unlikely. A language model gives higher probability to the first sentence.

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

**4. Higher-order n-grams (4-gram, 5-gram, etc.):** More context but many word combinations will never appear in the training text, giving zero probability.

**Smoothing (Fixing Zero Counts):**

Sometimes the computer has never seen a word combination in its training data. Smoothing fixes this:

- **Add-1 (Laplace) Smoothing:** Add 1 to every count so nothing has zero probability.
- **Backoff:** If trigram count is zero, try bigram. If bigram is zero, try unigram.
- **Interpolation:** Mix unigram, bigram, and trigram probabilities together using weights.

---

# 6.2 Part-of-Speech (POS) Tagging

> **Define POS tagging. Explain different approaches to POS tagging with examples. (7) (Spring 2025)**

**POS tagging** is the process of assigning a grammatical category (part-of-speech tag) to each word in a sentence. Common POS tags include NN (noun), VB (verb), JJ (adjective), DT (determiner), RB (adverb), IN (preposition), PRP (pronoun), etc.

Example: "The/DT cat/NN sat/VBD on/IN the/DT mat/NN"

POS tagging is challenging because many words are **ambiguous** — the same word can have different tags depending on context. For example, "book" can be a noun ("read a book") or a verb ("book a flight").

**Approaches to POS Tagging:**

**1. Rule-Based Tagging:** Humans write rules by hand. Rules select the correct tag based on context. Example rules: "If a word follows a determiner and is not known to be a verb, tag it as a noun," or "If a word ends in '-ly', tag it as an adverb (RB)." Advantages: transparent and interpretable. Disadvantages: labor-intensive to create, hard to scale, struggles with unknown words.

**2. Stochastic (Statistical) Tagging:**

- Uses probability and math to guess the best tag.
- **HMM (Hidden Markov Model)** looks at two things:
  - **Emission probability:** How likely is it that this tag produces this word? Example: How often does a verb tag produce the word "run"?
  - **Transition probability:** How likely is it that one tag follows another? Example: How often does a noun come after a determiner?
- It uses an algorithm called **Viterbi Algorithm** to find the most likely sequence of tags for the whole sentence.

**3. Transformation-Based Tagging (Brill Tagger):** A hybrid approach combining rule-based and statistical methods. It starts by assigning each word its most frequent tag from the training corpus, then iteratively learns transformation rules that correct tagging errors. Example rule: "Change tag from VB to NN if the previous word is a DT." The rules are learned automatically from data but are human-readable, combining the interpretability of rule-based methods with the data-driven nature of statistical methods.

**4. Deep Learning-Based Tagging:**

- Modern approach using neural networks.
- The computer learns on its own from large amounts of tagged text.
- Gives the best results today.

---

# 6.3 Grammar and Parsing

**Grammar** = the rules that tell us how to form correct sentences.

Example Rules:

```text
S  → NP VP          (A sentence is a noun phrase + verb phrase)
NP → DT NN          (A noun phrase is a determiner + noun)
VP → VB NP          (A verb phrase is a verb + noun phrase)
DT → "the" | "a"
NN → "dog" | "cat"
VB → "chased"
```

**Parsing** = breaking a sentence into parts according to grammar rules, to produce a structured representation (parse tree) for a sentence.

Example:

**Parsing "The dog chased a cat":**

- S → NP + VP → (the dog) + (chased a cat) ✓

---

# 6.4 Complications of Real Natural Language

> **What are the key challenges in NLP? (7) (Internal 2025)**
>
> **Write a short note on Complications of Real Natural Language. (5) (Fall 2025)**

Real natural language is far more complex than formal languages. The major complications include:

**iLAMP: Idioms, Language Variability, Ambiguity, Anaphora, Metaphor, Metonymy and Pragmatics**

**1. Ambiguity:** The single greatest challenge in NLP. A word, phrase, or sentence can have multiple valid interpretations.

- **Lexical ambiguity:** A word has multiple meanings. "Bank" can mean a financial institution or a river bank. "Bat" can mean a flying mammal or a cricket bat.
- **Syntactic ambiguity:** A sentence has multiple valid parse trees. "I saw the man with a telescope" — did I use a telescope to see him, or did I see a man who had a telescope?
- **Semantic ambiguity:** "Every student read a book" — did all students read the same book, or each a different one?
- **Referential ambiguity:** "John told Bill that he was wrong" — does "he" refer to John or Bill?

**2. Metaphor:** When we say something but don't mean it literally.

- "Time is money" — Time isn't really money, but it's valuable like money.
- "He has a heart of stone" — His heart isn't actually made of stone, he's just cold-hearted.

**3. Metonymy:** something is referred to by the name of something closely associated with it.

- "The White House announced..." — The building didn't talk; the president did.
- "I read Shakespeare" — You read his books, not the person himself.

**4. Anaphora (Pronouns):** Figuring out who "he", "she", "it", "they" refer to.

- "Sita went to the store. She bought milk." — Computer needs to know "She" = Sita.

**5. Pragmatics and Context-Dependence:** The same words can mean different things in different situations.

- "Can you pass the salt?" — This isn't a question about your ability. It's a polite request.

**6. Idioms:** Phrases that don't mean what the words say.

- "Kick the bucket" = die (not actually kicking a bucket!)
- "Break a leg" = good luck

**7. Language Variability:** People use slang, abbreviations, misspellings, different dialects, and informal grammar — especially on social media. This makes it hard for computers to understand.

---

# 6.5 Word Embeddings

> **How do prediction-based embeddings overcome the limitations of frequency-based embeddings? Explain how words are converted into vector representations using the Continuous Bag-of-Words model. (7) (Internal 2025)**

Computers can't understand words directly — they need numbers. **Word embeddings** convert words into lists of numbers (vectors) so that similar words have similar numbers.

**Example:** The words "happy" and "joyful" would have very similar number lists because they mean similar things.

**Frequency-Based Embeddings:**

**1. Bag of Words (BoW):** Count how many times each word appears.

- "I love AI. I love coding." → I=2, love=2, AI=1, coding=1
- **Problem:** Ignores word order. "Dog bites man" and "Man bites dog" look the same!

**2. TF-IDF:** Similar to BoW, but gives more weight to important words and less weight to common words like "the", "is".

- **Problem:** Still doesn't understand meaning or context.

**3. Co-occurrence Matrix:** Counts how often words appear near each other.

- **Problem:** Very large tables, slow to compute.

**Problems with all these:** They create huge, mostly-empty number lists. They can't understand that "king" and "queen" are related, or that "bank" has multiple meanings.

**Prediction-Based Embeddings (Word2Vec):**

**Word2Vec** learns word meanings by training a simple neural network to predict words from their neighbors.

**1. CBOW (Continuous Bag of Words):**

- **Task:** Given the surrounding words, predict the middle word.
- **Example:** Sentence: "The cat sat on the mat"
  - Context words: "The", "cat", "on", "the" → Predict: "sat"
- **How it works:**
  1. Take the number lists (vectors) of all context words.
  2. Average them together.
  3. Feed into a neural network.
  4. The network guesses which word should go in the middle. uses softmax to produce a probability distribution over the entire vocabulary.
  5. After lots of training, the word vectors become meaningful.
- CBOW is fast and works well for common words.

**2. Skip-Gram:**

- Does the opposite of CBOW.
- **Task:** Given the middle word, predict the surrounding words.
- **Example:** Given "sat" → predict "The", "cat", "on", "the"
- Works better for rare words.

**Cool Property of Word Embeddings:**
After training, you can do math with words!

- vector("king") − vector("man") + vector("woman") ≈ vector("queen")
- This shows the model truly understands relationships between words.

---

# 6.6 RNN for NLP

> **What are the limitations of RNN in NLP? Explain the approach used to overcome these limitations. (7) (Spring 2025)**

see ch 5:

**RNN/LSTM Applications in NLP:**

- **Language Modeling:** Predict the next word given previous words. The hidden state encodes the history of the sequence.
- **Sentiment Analysis:** Process the entire text sequence and use the final hidden state (or pooled states) to classify the text (e.g., positive/negative sentiment).
- **Named Entity Recognition (NER):** Tag each word in a sequence with an entity label (person, location, organization, etc.).
- **Machine Translation:** Encode a source sentence and decode it into a target language (with the encoder-decoder framework).

**RNN Variants:**

- **One-to-One:** Standard neural network (no recurrence).
- **One-to-Many:** Single input, sequence output (e.g., image captioning).
- **Many-to-One:** Sequence input, single output (e.g., sentiment analysis).
- **Many-to-Many:** Sequence input, sequence output (e.g., machine translation, POS tagging).

---

# 6.7 LSTMs for NLP

> **What is a LSTM? Explain in detail how the LSTMs are used in NLP. (Spring 2025)**
>
> **What are the limitations of RNN in NLP? Explain the approach used to overcome these limitations. (7) (Spring 2025)**
>
> **What are the challenges of RNNs? Discuss about the architecture to solve these challenges. (7) (Fall 2025)**

**Why LSTM Solves the Vanishing Gradient Problem:** The cell state provides a direct path for gradients to flow through many time steps with minimal transformation. The forget gate can learn to keep its value close to 1, allowing gradients to pass through unchanged. This enables LSTMs to learn dependencies over hundreds of time steps.

---

# 6.8 Sequence-to-Sequence Models

**Sequence-to-Sequence (Seq2Seq)** models map an input sequence of variable length to an output sequence of variable length. They are the foundation for machine translation, text summarization, dialogue systems, and question answering.

**Encoder-Decoder Architecture:**

**Encoder:** An RNN (typically LSTM or GRU) that reads the input sequence x₁, x₂, ..., xₘ one token at a time and produces a sequence of hidden states. The final hidden state (and cell state for LSTM) is called the **context vector** — a fixed-length summary of the entire input.

**Decoder:** Another RNN that takes the context vector as its initial hidden state and generates the output sequence y₁, y₂, ..., yₙ one token at a time. At each step, the decoder takes the previous output word and its current hidden state to predict the next word.

**Training:** The model is trained end-to-end to maximize the probability of the correct output sequence given the input. Loss is computed using cross-entropy between the predicted and actual output tokens.

**The Bottleneck Problem:** The entire input sequence is compressed into a single fixed-length context vector. For long input sequences, this vector cannot capture all the necessary information, leading to information loss and degraded performance on long sentences.

**Solution → Attention Mechanism:**

---

# 6.9 The Transformer Architecture — BERT, GPT, Attention

> **Describe transformer with its architecture. (8) (Internal 2025)**
>
> **Explain the transformer model architecture. (8) (Fall 2025)**
>
> **What is the attention mechanism used in transformers? Describe the architecture of BERT. (8) (Spring 2025)**
>
> **LLMs have revolutionized AI. What is the foundational innovation and architecture beneath these breakthroughs? Explain. (8) (Fall 2025)**

see ch5
