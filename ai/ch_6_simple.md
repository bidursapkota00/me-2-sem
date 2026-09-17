# 6. Natural Language Processing (NLP)

**Natural Language Processing (NLP)** is a part of AI that helps computers understand and use human language — like English or Nepali.

Think of it this way: computers only understand numbers and code. NLP is what helps them understand our words, sentences, and conversations.

**Steps in NLP:**

1. **Lexical Analysis:** Breaking a sentence into individual words. Like splitting "I love AI" into ["I", "love", "AI"].
2. **Syntactic Analysis (Parsing):** Checking the grammar. Is the sentence written correctly? Like checking if "Dog the ran" is wrong grammar.
3. **Semantic Analysis:** Understanding the meaning. "Colorless green ideas sleep furiously" has correct grammar but makes no sense — semantic analysis catches that.
4. **Discourse Integration:** Understanding how sentences connect to each other. Example: "Ram went home. He was tired." — here "He" means Ram. The computer needs to figure that out.
5. **Pragmatic Analysis:** Understanding what someone really means. Example: "Can you close the door?" — this is not really a question, it's a polite request.

**Two ways to do NLP:**

- **Rule-Based NLP:** Humans write grammar rules by hand, and the computer follows them. It's easy to understand but very hard to build, and it breaks easily with unusual sentences.
- **Statistical NLP:** The computer learns language patterns from a huge amount of text data. It's like learning a language by reading thousands of books. It handles tricky sentences better but needs lots of data.

---

# 6.1 Language Models

> **What are n-grams in NLP? Discuss their types with examples. (8) (Internal 2025)**

A **language model** is a system that predicts how likely a sequence of words is.

For example, "I am going to school" is very likely. But "School going am I to" is very unlikely. A language model gives higher probability to the first sentence.

**Why is this useful?** It helps in autocomplete (like on your phone keyboard), spell checking, translation, and chatbots.

**The Problem:** To predict the next word perfectly, the computer would need to remember every single word that came before. That's too hard with long sentences.

**Solution → N-Gram Models:** Instead of remembering everything, just look at the last few words.

## N-Gram Models

An **n-gram** is a group of "n" words taken together from a sentence.

**Types of N-grams:**

**1. Unigram (n=1):** Look at each word alone, ignoring what comes before or after.
- Example: In "I love AI" → P("I"), P("love"), P("AI") are all calculated separately.
- It's like guessing a word without reading the rest of the sentence.

**2. Bigram (n=2):** Look at pairs of words. Predict a word based on just the one word before it.
- Example: What word comes after "I"? → P("love" | "I") = How many times "I love" appears ÷ How many times "I" appears.
- Better than unigram because it considers some context.

**3. Trigram (n=3):** Look at groups of 3 words. Predict a word based on the 2 words before it.
- Example: P("AI" | "I love") = How many times "I love AI" appears ÷ How many times "I love" appears.
- Even better context, but needs more data.

**4. Higher n-grams (4-gram, 5-gram):** More context but many word combinations will never appear in the training text, giving zero probability.

**Smoothing (Fixing Zero Counts):**

Sometimes the computer has never seen a word combination in its training data. Smoothing fixes this:

- **Add-1 (Laplace) Smoothing:** Add 1 to every count so nothing has zero probability.
- **Backoff:** If trigram count is zero, try bigram. If bigram is zero, try unigram.
- **Interpolation:** Mix unigram, bigram, and trigram probabilities together using weights.

**Perplexity:** A way to measure how good a language model is. Lower perplexity = better model. Think of it as: how "confused" is the model when it sees new text? Less confusion = better.

---

# 6.2 Part-of-Speech (POS) Tagging

> **Define POS tagging. Explain different approaches to POS tagging with examples. (7) (Spring 2025)**

**POS tagging** means labeling each word in a sentence with its grammar role — like noun, verb, adjective, etc.

**Example:**
- "The/DT cat/NN sat/VBD on/IN the/DT mat/NN"
- DT = Determiner (the, a), NN = Noun, VBD = Verb (past tense), IN = Preposition

**Why is this hard?** Because the same word can be different parts of speech:
- "book" → noun ("read a **book**") or verb ("**book** a ticket")
- "run" → noun ("a morning **run**") or verb ("**run** fast")

**Approaches to POS Tagging:**

**1. Rule-Based Tagging:**
- Humans write rules by hand.
- Example rules: "If a word comes after 'the' and isn't a known verb, call it a noun." Or "If a word ends in '-ly', call it an adverb."
- **Good:** Easy to understand.
- **Bad:** Takes a lot of effort to write rules, and doesn't handle new or unknown words well.

**2. Stochastic (Statistical) Tagging — Using HMM:**
- Uses probability and math to guess the best tag.
- **HMM (Hidden Markov Model)** looks at two things:
  - **Emission probability:** How likely is it that this tag produces this word? Example: How often does a verb tag produce the word "run"?
  - **Transition probability:** How likely is it that one tag follows another? Example: How often does a noun come after a determiner?
- It uses an algorithm called **Viterbi Algorithm** to find the most likely sequence of tags for the whole sentence.

**3. Transformation-Based Tagging (Brill Tagger):**
- A mix of rule-based and statistical methods.
- Step 1: Give every word its most common tag.
- Step 2: The computer learns correction rules from data. Example: "Change VB to NN if the previous word is DT."
- **Good:** Rules are learned automatically AND humans can read them.

**4. Deep Learning-Based Tagging:**
- Modern approach using neural networks.
- The computer learns on its own from large amounts of tagged text.
- Gives the best results today.

---

# 6.3 Grammar and Parsing

**Grammar** = the rules that tell us how to form correct sentences.
**Parsing** = breaking a sentence into parts according to grammar rules, like making a family tree for a sentence.

## Context-Free Grammar (CFG)

A **Context-Free Grammar** is a set of rules that describe how sentences are built.

It has 4 parts:
- **N (Non-terminals):** Categories like Sentence (S), Noun Phrase (NP), Verb Phrase (VP).
- **Σ (Terminals):** The actual words like "dog", "cat", "chased".
- **R (Rules):** How to break categories into smaller parts. Example: S → NP VP (a sentence = noun phrase + verb phrase).
- **S (Start symbol):** We always start from S (Sentence).

**Example Rules:**
```
S  → NP VP          (A sentence is a noun phrase + verb phrase)
NP → DT NN          (A noun phrase is a determiner + noun)
VP → VB NP          (A verb phrase is a verb + noun phrase)
DT → "the" | "a"
NN → "dog" | "cat"
VB → "chased"
```

**Parsing "The dog chased a cat":**
- S → NP + VP → (the dog) + (chased a cat) ✓

## Types of Parsing

**1. Constituency Parsing:**
- Breaks a sentence into nested groups (phrases within phrases).
- Makes a tree structure. Example: [S [NP The dog] [VP chased [NP a cat]]]
- Shows which words group together as phrases.

**2. Dependency Parsing:**
- Shows which word depends on which other word.
- Example: In "The cat sat on the mat":
  - "sat" is the main word (root)
  - "cat" depends on "sat" (who sat? → the cat)
  - "mat" depends on "on" (on what? → the mat)

**Parsing Methods:**

- **Top-Down:** Start from S and try to reach the words by applying rules downward.
- **Bottom-Up:** Start from the words and try to combine them upward to reach S.
- **CYK Algorithm:** A smart method using a table to efficiently parse sentences. Works like filling in a grid step by step.

---

# 6.4 Complications of Real Natural Language

> **What are the key challenges in NLP? (7) (Internal 2025)**
>
> **Write a short note on Complications of Real Natural Language. (5) (Fall 2025)**

Human language is messy and complicated. Here are the main problems:

**1. Ambiguity (Multiple Meanings):** The biggest problem in NLP!

- **Word ambiguity:** "Bank" = money bank or river bank? "Bat" = animal or cricket bat?
- **Sentence ambiguity:** "I saw the man with a telescope" — Did I use a telescope to see him? Or did I see a man who had a telescope?
- **Meaning ambiguity:** "Every student read a book" — Did they all read the same book or different books?
- **Reference ambiguity:** "John told Bill that he was wrong" — Who is "he"? John or Bill?

**2. Metaphor:** When we say something but don't mean it literally.
- "Time is money" — Time isn't really money, but it's valuable like money.
- "He has a heart of stone" — His heart isn't actually made of stone, he's just cold-hearted.

**3. Metonymy:** Using a related name to refer to something.
- "The White House announced..." — The building didn't talk; the president did.
- "I read Shakespeare" — You read his books, not the person himself.

**4. Anaphora (Pronouns):** Figuring out who "he", "she", "it", "they" refer to.
- "Sita went to the store. She bought milk." — Computer needs to know "She" = Sita.

**5. Context and Intent:** The same words can mean different things in different situations.
- "Can you pass the salt?" — This isn't a question about your ability. It's a polite request.

**6. Idioms:** Phrases that don't mean what the words say.
- "Kick the bucket" = die (not actually kicking a bucket!)
- "Break a leg" = good luck (not literally!)

**7. Language Variability:** People use slang, abbreviations, misspellings, different dialects, and informal grammar — especially on social media. This makes it hard for computers to understand.

---

# 6.5 Word Embeddings

> **How do prediction-based embeddings overcome the limitations of frequency-based embeddings? Explain how words are converted into vector representations using the Continuous Bag-of-Words model. (7) (Internal 2025)**

Computers can't understand words directly — they need numbers. **Word embeddings** convert words into lists of numbers (vectors) so that similar words have similar numbers.

**Example:** The words "happy" and "joyful" would have very similar number lists because they mean similar things.

## Simple (Frequency-Based) Methods:

**1. Bag of Words (BoW):** Count how many times each word appears.
- "I love AI. I love coding." → I=2, love=2, AI=1, coding=1
- **Problem:** Ignores word order. "Dog bites man" and "Man bites dog" look the same!

**2. TF-IDF:** Similar to BoW, but gives more weight to important words and less weight to common words like "the", "is".
- **Problem:** Still doesn't understand meaning or context.

**3. Co-occurrence Matrix:** Counts how often words appear near each other.
- **Problem:** Very large tables, slow to compute.

**Problems with all these:** They create huge, mostly-empty number lists. They can't understand that "king" and "queen" are related, or that "bank" has multiple meanings.

## Smart (Prediction-Based) Method — Word2Vec:

**Word2Vec** learns word meanings by training a simple neural network to predict words from their neighbors.

**1. CBOW (Continuous Bag of Words):**
- **Task:** Given the surrounding words, predict the middle word.
- **Example:** Sentence: "The cat sat on the mat"
  - Context words: "The", "cat", "on", "the" → Predict: "sat"
- **How it works:**
  1. Take the number lists (vectors) of all context words.
  2. Average them together.
  3. Feed into a neural network.
  4. The network guesses which word should go in the middle.
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

**GloVe:** Another method that combines counting word pairs (like co-occurrence matrix) with prediction (like Word2Vec) to get the best of both worlds.

---

# 6.6 RNN for NLP

> **What are the limitations of RNN in NLP? Explain the approach used to overcome these limitations. (7) (Spring 2025)**

## What is an RNN?

**RNN (Recurrent Neural Network)** is a type of neural network designed for sequential data — data that comes in order, like words in a sentence.

**Normal neural networks** look at input once and give output. They have no memory.

**RNNs have memory!** They remember what they saw before. When reading a sentence word by word, they carry forward information from previous words.

**How it works (simply):**
1. Read word 1 → create a memory (hidden state).
2. Read word 2 + memory from step 1 → update memory.
3. Read word 3 + memory from step 2 → update memory.
4. ...and so on until the sentence ends.

At each step:
- **Input:** Current word + previous memory
- **Output:** Updated memory + prediction

**Uses of RNN in NLP:**
- **Language Modeling:** Predicting the next word (like autocomplete on your phone).
- **Sentiment Analysis:** Reading a review and deciding if it's positive or negative.
- **Named Entity Recognition:** Finding names of people, places, organizations in text.
- **Machine Translation:** Translating from one language to another.

**Types of RNN:**
- **One-to-Many:** One input → many outputs (Example: give an image → get a sentence describing it)
- **Many-to-One:** Many inputs → one output (Example: read a full review → decide positive/negative)
- **Many-to-Many:** Many inputs → many outputs (Example: translate a sentence)

**Bidirectional RNN:** Reads the sentence both forward AND backward. This helps because sometimes you need to see future words to understand the current word.
- Example: "He went to the bank to fish" — you need to read "fish" to know "bank" means river bank, not money bank.

## Problems with RNN:

**1. Vanishing Gradient Problem (The Biggest Problem):**
- When sentences are long, the RNN "forgets" what it read at the beginning.
- During training, the learning signal gets weaker and weaker as it goes back through many steps — like a whisper getting lost in a long chain of people.
- Result: RNN can't learn long-distance connections.

**2. Exploding Gradient Problem:**
- Opposite problem — the learning signal grows too large and causes errors.
- Fix: **Gradient clipping** — put a cap on how large the signal can be.

**3. Slow Training:**
- RNN reads one word at a time, so it can't process words in parallel. This makes it slow.

**4. Short Memory:**
- Because of vanishing gradients, standard RNNs can only remember recent words well. They struggle with long sentences.

**Solution → LSTM and GRU** (explained in the next section).

---

# 6.7 LSTMs for NLP

> **What is a LSTM? Explain in detail how the LSTMs are used in NLP. (Spring 2025)**
>
> **What are the limitations of RNN in NLP? Explain the approach used to overcome these limitations. (7) (Spring 2025)**
>
> **What are the challenges of RNNs? Discuss about the architecture to solve these challenges. (7) (Fall 2025)**

## What is LSTM?

**LSTM (Long Short-Term Memory)** is a special type of RNN that can remember things for a long time. It was invented to solve the vanishing gradient problem of regular RNNs.

**Simple Analogy:** Think of LSTM like a notebook:
- Regular RNN = trying to remember everything in your head (you forget quickly).
- LSTM = writing important things in a notebook (you can remember for a long time).

## How LSTM Works:

LSTM has a special **cell state** — like a conveyor belt that carries important information through the entire sequence. It also has three **gates** that control what information to add, keep, or remove:

**1. Forget Gate — "What should I forget?"**
- Looks at the current word and previous memory.
- Decides what old information to throw away.
- Outputs a number between 0 (forget everything) and 1 (remember everything) for each piece of information.
- Example: When starting a new topic in a paragraph, forget the old topic.

**2. Input Gate — "What new information should I store?"**
- Decides what new information to add to the cell state.
- Two parts:
  - Which values to update (input gate)
  - What new candidate values to create (tanh layer)
- Example: Store the gender of a new subject so we use the right pronoun later.

**3. Cell State Update:**
- Combine: (Old cell state × forget gate values) + (New candidate values × input gate values)
- This is how the notebook gets updated — erase some old notes, write some new ones.

**4. Output Gate — "What should I output?"**
- Decides what part of the cell state to use as output.
- The output becomes the new hidden state (short-term memory).

**Why LSTM solves the vanishing gradient problem:**
- The cell state acts like a highway for information — data can flow through many steps without being changed much.
- The forget gate can learn to keep its value close to 1, allowing information (and gradients during training) to pass through unchanged over long distances.

## GRU (Gated Recurrent Unit):

- A simpler version of LSTM.
- Has only 2 gates instead of 3 (reset gate and update gate).
- No separate cell state.
- Faster to train, and often works just as well as LSTM.
- Think of it as a lighter, faster version of LSTM.

## Uses of LSTM in NLP:

- **Language Modeling:** Better at understanding long sentences than regular RNN. Example: matching a subject with its verb even when they're far apart.
- **Machine Translation:** Reads a sentence in one language and generates the translation.
- **Text Generation:** Writes text one word at a time, keeping the story consistent over long passages.
- **Sentiment Analysis:** Bi-directional LSTM reads text both ways for better understanding.
- **Named Entity Recognition:** Bi-LSTM + CRF models are very good at finding names, places, etc. in text.

---

# 6.8 Sequence-to-Sequence Models

## What is Seq2Seq?

**Sequence-to-Sequence (Seq2Seq)** models take a sequence of words as input and produce a different sequence of words as output. The input and output can have different lengths.

**Examples:**
- **Translation:** "I love you" (English, 3 words) → "म तिमीलाई माया गर्छु" (Nepali, 4 words)
- **Summarization:** A long paragraph → A short summary
- **Chatbot:** A question → An answer

## How it Works — Encoder-Decoder:

**Think of it like this:** One person (Encoder) reads a book and writes a summary note. Another person (Decoder) reads only that note and writes the book in a different language.

**Encoder:**
- An RNN/LSTM that reads the input sentence word by word.
- After reading everything, it creates a summary called the **context vector** — a single list of numbers that represents the entire input sentence.

**Decoder:**
- Another RNN/LSTM that takes the context vector and generates the output sentence word by word.
- At each step, it predicts the next word based on the context vector and the words it has already generated.

**Teacher Forcing:** During training, instead of using the decoder's own (possibly wrong) predictions, we feed it the correct answer at each step. This makes training faster and more stable.

## The Bottleneck Problem:

**The problem:** The entire input sentence is squeezed into one single context vector. For long sentences, this vector can't hold all the information. It's like trying to summarize a whole book in one sentence — you lose important details.

## Solution → Attention Mechanism:

**Attention** lets the decoder look back at ALL the encoder's outputs at each step, instead of relying on just one summary vector.

**How Attention Works (Simply):**

1. The encoder creates a hidden state for each input word (like taking notes on each word separately).
2. When the decoder is generating each output word, it asks: "Which input words are most important right now?"
3. It calculates a **score** for each input word — how relevant is this input word for the current output word?
4. These scores become **attention weights** (they add up to 1, like percentages).
5. It creates a **weighted combination** of all encoder states — paying more attention to relevant words.
6. This focused context helps the decoder make a better prediction.

**Example:** When translating "The cat sat on the mat" to Nepali, when generating the word for "cat", the decoder pays most attention to "cat" in the input, not to "on" or "mat".

**Types of Attention:**
- **Bahdanau (Additive):** Uses a small neural network to calculate scores. More flexible.
- **Luong (Dot-Product):** Uses simple multiplication to calculate scores. Faster and simpler.

**Why Attention is Great:**
- Works much better on long sentences.
- You can visualize the attention weights to see which input words the model is focusing on — this makes the model more interpretable.

---

# 6.9 The Transformer — BERT, GPT, Attention

> **Describe transformer with its architecture. (8) (Internal 2025)**
>
> **Explain the transformer model architecture. (8) (Fall 2025)**
>
> **What is the attention mechanism used in transformers? Describe the architecture of BERT. (8) (Spring 2025)**
>
> **LLMs have revolutionized AI. What is the foundational innovation and architecture beneath these breakthroughs? Explain. (8) (Fall 2025)**

## What is a Transformer?

The **Transformer** is a revolutionary neural network model (introduced in 2017) that powers almost all modern AI language tools — including ChatGPT, Google Translate, and BERT.

**Why was it needed?**
- RNNs and LSTMs read words one by one (sequentially) — this is slow.
- Even LSTMs struggle with very long sentences.
- Transformers read ALL words at the same time (in parallel) — much faster!
- Transformers can directly connect any word to any other word, no matter how far apart they are.

## Self-Attention — The Key Idea

Self-attention answers the question: **"How much should each word pay attention to every other word in the sentence?"**

For each word, the model creates three vectors:
- **Query (Q):** "What am I looking for?"
- **Key (K):** "What do I have to offer?"
- **Value (V):** "What is my actual content?"

**How it works:**
1. Each word's Query is compared with every other word's Key (using dot product — like multiplying).
2. This gives a score showing how relevant each word is to every other word.
3. The scores are converted to percentages (using softmax).
4. Each word's output is a weighted combination of all Value vectors, based on these percentages.

**Example:** In "The cat sat on the mat because it was tired":
- When processing "it", the model gives high attention to "cat" (because "it" refers to "cat").
- This is how the model understands references!

The formula divides scores by √dₖ (square root of key dimension) to keep numbers in a good range.

## Multi-Head Attention

Instead of doing attention once, the Transformer does it **multiple times in parallel** (multiple "heads").

- Each head can focus on different things — one might focus on grammar, another on meaning, another on position.
- Their results are combined at the end.
- It's like having multiple pairs of eyes, each looking for different patterns.

## Positional Encoding

Since the Transformer reads all words at the same time, it doesn't know the order of words. "Dog bites man" and "Man bites dog" would look the same!

**Solution:** Add special position numbers to each word's vector before processing. These numbers tell the model which word comes first, second, third, etc. The original paper uses sine and cosine functions to create these position codes.

## Transformer Architecture

The Transformer has two main parts:

**Encoder (for understanding):**
Each layer has:
1. **Multi-Head Self-Attention:** Each word looks at all other words.
2. **Add & Normalize:** Adds the original input back (residual connection) and normalizes.
3. **Feed-Forward Network:** A small neural network that processes each word individually.
4. **Add & Normalize:** Again.

Multiple such layers are stacked (usually 6).

**Decoder (for generating):**
Each layer has:
1. **Masked Self-Attention:** Each word can only look at words before it (can't peek at future words!).
2. **Add & Normalize.**
3. **Cross-Attention:** The decoder looks at the encoder's output to understand the input.
4. **Add & Normalize.**
5. **Feed-Forward Network.**
6. **Add & Normalize.**

**Final Step:** The decoder's output goes through a layer that produces probabilities for each word in the vocabulary. The most likely word is selected as the output.

## BERT (Bidirectional Encoder Representations from Transformers)

BERT uses only the **Encoder** part of the Transformer. It's designed for **understanding** language.

**What makes BERT special — Bidirectional Reading:**
- GPT reads left-to-right only.
- BERT reads in **both directions** — it sees words on the left AND right of each word simultaneously.
- This gives it a deeper understanding of each word's meaning.

**How BERT is trained:**

1. **Masked Language Model (MLM):**
   - Randomly hide (mask) 15% of words in a sentence.
   - Train the model to guess the hidden words.
   - Example: "The [MASK] sat on the mat" → predict "cat"
   - This forces BERT to understand context from both sides.

2. **Next Sentence Prediction (NSP):**
   - Give BERT two sentences.
   - Ask: "Does sentence B come after sentence A in the original text?"
   - This helps BERT understand how sentences relate to each other.

**How BERT is used:**
- First, it's **pre-trained** on massive amounts of text (like all of Wikipedia).
- Then, it's **fine-tuned** on your specific task (like sentiment analysis or question answering) with a small amount of labeled data.
- Fine-tuning is fast because BERT already knows a lot about language.

**BERT Sizes:**
- BERT-Base: 12 layers, 110 million parameters
- BERT-Large: 24 layers, 340 million parameters

## GPT (Generative Pre-trained Transformer)

GPT uses only the **Decoder** part of the Transformer. It's designed for **generating** text.

**How GPT works:**
- It reads text left-to-right and predicts the next word.
- "I love" → predicts "you" or "coding" or "AI"
- It generates text one word at a time, always looking only at what came before.

**GPT vs BERT — Simple Comparison:**

| Feature | BERT | GPT |
|---------|------|-----|
| Uses | Encoder only | Decoder only |
| Direction | Both directions (bidirectional) | Left-to-right only |
| Best for | Understanding (classification, Q&A) | Generating (writing, chatting) |
| Training task | Guess masked words | Predict next word |

**GPT has grown huge over time:**
- GPT-2: 1.5 billion parameters
- GPT-3: 175 billion parameters
- GPT-4: Even larger!

The bigger the model, the more it can do — including answering questions, writing essays, coding, and reasoning.

## Why Transformers Changed Everything:

1. **Parallel processing:** All words processed at the same time → very fast training.
2. **Long-range connections:** Any word can directly attend to any other word, regardless of distance.
3. **Scalability:** Transformers work better and better as you make them bigger and give them more data.
4. **Foundation for all modern AI:** ChatGPT, Google Bard, BERT, T5 — all built on Transformers!
