# 6. Acoustic Signal Processing

# 6.1 Music and Audio Classification

> **Explain the pipeline for a music classification system using deep learning. What audio features are typically extracted, and which neural network architectures are best suited for this task? (Fall 2025)**

## 6.1.1 Audio Representation

Sound is a continuous pressure wave. A digital audio signal is obtained by **sampling** the continuous waveform at a fixed rate (e.g., 22,050 Hz or 44,100 Hz) and **quantizing** the amplitude to discrete values (e.g., 16-bit). A 3-second clip at 22,050 Hz contains 66,150 samples — a 1D signal far too long for direct input to a fully connected network.

To make audio suitable for deep learning, the raw waveform is converted into a 2D **time-frequency representation** that can be treated like an image:

**Short-Time Fourier Transform (STFT):** The audio signal is divided into short overlapping segments (windows), and the Fourier Transform is applied to each segment. The result is a **spectrogram** — a 2D matrix where the x-axis is time, the y-axis is frequency, and the value (color/intensity) represents the magnitude (energy) at that frequency and time.

For a signal $x[n]$ with window function $w[n]$ of length $N$ and hop size $H$:

$
X[m, k] = \sum_{n=0}^{N-1} x[n + mH] \cdot w[n] \cdot e^{-j2\pi kn/N}
$

where $m$ is the frame index and $k$ is the frequency bin.

**Mel Spectrogram:** The human ear perceives frequency on a logarithmic scale — a 100 Hz difference is perceptible at low frequencies but not at high frequencies. The **Mel scale** compresses the frequency axis to match human perception. A Mel spectrogram is obtained by applying a bank of triangular filters (Mel filter bank) to the linear-frequency spectrogram, then taking the logarithm of the energies.

$
f_{mel} = 2595 \cdot \log_{10}\left(1 + \frac{f}{700}\right)
$

**MFCC (Mel-Frequency Cepstral Coefficients):** A further compression of the Mel spectrogram. After computing the log-Mel spectrogram, the **Discrete Cosine Transform (DCT)** is applied across the Mel filter bank outputs. Typically the first 13–20 coefficients are kept. MFCCs capture the **spectral envelope** (overall shape of the spectrum), which encodes information about timbre and phonemes. They are compact but discard fine spectral detail.

| Feature | Representation | Information Retained | Typical Use |
| :--- | :--- | :--- | :--- |
| **Raw waveform** | 1D signal | Everything | End-to-end models (WaveNet, 1D CNN) |
| **Spectrogram** | 2D (time × frequency) | Full spectral detail | General analysis |
| **Mel spectrogram** | 2D (time × Mel bins) | Perceptually weighted spectrum | CNN-based classification |
| **MFCC** | 2D (time × coefficients) | Spectral envelope only | Traditional ML, compact models |

Modern deep learning systems generally prefer **log-Mel spectrograms** because they retain rich spectral information while being compact enough for efficient CNN processing.

## 6.1.2 Deep Learning Pipeline for Music Classification

**Step 1 — Data Preprocessing:** Load raw audio files, resample to a uniform sample rate (e.g., 22,050 Hz), convert stereo to mono, and normalize amplitude. Long tracks are segmented into fixed-length clips (e.g., 3–5 seconds) to create uniform-sized inputs and increase the number of training samples.

**Step 2 — Feature Extraction:** Compute the log-Mel spectrogram for each audio segment. Typical parameters: FFT size = 2048, hop length = 512, number of Mel bands = 128. The output is a 2D matrix of shape (128 × T), where T depends on the clip duration. This matrix is treated as a single-channel image.

**Step 3 — Model Architecture:** Feed the spectrogram into a CNN. The convolutional layers learn hierarchical audio patterns — low-level filters detect spectral edges and onsets; deeper layers capture rhythmic patterns, harmonic structures, and timbral characteristics.

**Step 4 — Aggregation:** For song-level prediction from multiple segments, aggregate the segment-level predictions using **majority voting**, **average pooling** of softmax probabilities, or **max pooling.**

**Step 5 — Training:** Use categorical cross-entropy loss for multi-class classification (e.g., genre classification into 10 genres). Apply data augmentation techniques: **time stretching**, **pitch shifting**, **adding background noise**, and **SpecAugment** (randomly masking time and frequency bands in the spectrogram).

## 6.1.3 Neural Network Architectures for Audio

**1. 2D CNN (on spectrograms):** Treats the spectrogram as a grayscale image. Standard architectures like VGG, ResNet, and custom shallow CNNs work effectively. Convolutional filters learn to detect spectro-temporal patterns. This is the most widely used approach for music genre classification, instrument recognition, and mood detection.

**2. 1D CNN (on raw waveform):** Operates directly on the raw audio samples using 1D convolution kernels. The network learns its own time-frequency decomposition instead of relying on hand-designed features like STFT. Requires deeper networks and more data. Examples: SampleCNN, WaveNet-style encoders.

**3. CNN + RNN (CRNN):** Convolutional layers extract local spectro-temporal features from the spectrogram. The feature maps are then reshaped and fed into an RNN (typically LSTM or GRU) that models temporal evolution across the entire clip. Particularly effective for tasks where temporal context matters (e.g., distinguishing genres that share similar spectral content but differ in rhythm).

**4. Audio Spectrogram Transformer (AST):** Divides the spectrogram into patches (similar to Vision Transformer), projects each patch into an embedding, adds positional encodings, and processes the sequence of patch embeddings with a Transformer encoder. Captures global context across the entire spectrogram. Achieves state-of-the-art results on large-scale audio classification benchmarks (AudioSet).

| Architecture | Input | Strength | Limitation |
| :--- | :--- | :--- | :--- |
| **2D CNN** | Mel spectrogram | Simple, effective, pretrained models available | Limited temporal context |
| **1D CNN** | Raw waveform | No hand-crafted features needed | Needs more data; longer training |
| **CRNN** | Mel spectrogram | Captures long-range temporal structure | More complex; slower training |
| **AST (Transformer)** | Spectrogram patches | Global attention; state-of-the-art accuracy | High compute; needs large datasets |

**Evaluation metrics:** Accuracy, precision, recall, F1-score (per-class and macro-averaged). Common benchmark datasets: GTZAN (10 genres, 1000 clips), FMA (Free Music Archive), AudioSet (large-scale, multi-label).

---

# 6.2 Music Source Separation

> **Describe the problem of music source separation. Compare at least two deep learning approaches used to solve it and evaluate their effectiveness. (Fall 2025)**

## 6.2.1 Problem Definition

**Music source separation** is the task of decomposing a mixed audio signal (a complete song) into its individual constituent sources — typically **vocals, drums, bass, and other** (accompaniment). Given a mixture signal $x(t)$ that is the sum of $K$ source signals:

$
x(t) = \sum_{k=1}^{K} s_k(t)
$

the goal is to estimate each source $\hat{s}_k(t)$ from $x(t)$ alone. This is an **ill-posed inverse problem** — there are infinitely many possible decompositions of a single mixture. Deep learning provides the prior knowledge (learned from training data) needed to resolve this ambiguity.

**Evaluation metrics:**

- **SDR (Signal-to-Distortion Ratio):** Overall quality of separation. Higher is better. Measures the ratio of the true source energy to the total error (interference + noise + artifacts).
- **SIR (Signal-to-Interference Ratio):** Measures how well other sources are suppressed.
- **SAR (Signal-to-Artifacts Ratio):** Measures the absence of algorithmic artifacts.

## 6.2.2 Approach 1 — Spectrogram Masking (Open-Unmix)

**Principle:** Work in the frequency domain. Compute the STFT of the mixture to obtain a complex spectrogram. Train a neural network to predict a **soft mask** $M(t, f) \in [0, 1]$ for each source. The estimated source spectrogram is obtained by element-wise multiplication:

$
\hat{S}_k(t, f) = M_k(t, f) \cdot |X(t, f)|
$

The phase of the mixture is reused, and the inverse STFT reconstructs the time-domain signal.

**Open-Unmix architecture:**

1. The input magnitude spectrogram passes through a **fully connected layer** that reduces the frequency dimension.
2. Three layers of **bidirectional LSTM** model temporal context — each time frame's mask is influenced by past and future frames.
3. A final fully connected layer with sigmoid activation outputs the mask.
4. A separate model is trained for each source (vocals, drums, bass, other).

**Strengths:** Simple, interpretable, and lightweight. Serves as a strong research baseline. The mask naturally constrains the output to be a filtered version of the input.

**Limitations:** Operates only on the magnitude spectrogram — the phase is borrowed from the mixture, which introduces artifacts, especially for overlapping sources. The mask multiplication limits the output to components already present in the mixture spectrogram.

## 6.2.3 Approach 2 — Waveform-Based Separation (Wave-U-Net)

**Principle:** Work directly in the time domain. The network takes the raw mixture waveform as input and outputs the estimated source waveforms. This avoids the lossy STFT/iSTFT pipeline and learns to reconstruct both magnitude and phase.

**Wave-U-Net architecture:**

1. An **encoder** with 1D convolutions and downsampling progressively reduces the temporal resolution while increasing the number of feature channels — capturing increasingly abstract audio representations.
2. A **decoder** with 1D transposed convolutions and upsampling progressively reconstructs the signal at the original resolution.
3. **Skip connections** between corresponding encoder and decoder layers concatenate high-resolution features from the encoder with upsampled features from the decoder, preserving fine-grained detail (transients, onsets).
4. The final layer outputs $K$ waveforms, one per source.

**Strengths:** End-to-end learning without hand-designed time-frequency transforms. Naturally handles phase reconstruction. Better preservation of transients and sharp onsets.

**Limitations:** Requires learning the time-frequency decomposition from scratch, needing more training data. Early versions produced lower SDR than spectrogram-based methods on standard benchmarks.

## 6.2.4 Approach 3 — Hybrid (Demucs)

**Demucs** combines both approaches. The Hybrid Demucs architecture has two parallel branches:

- A **temporal branch** (1D U-Net operating on the waveform).
- A **spectral branch** (2D U-Net operating on the complex spectrogram).

The two branches are connected via cross-attention layers that allow them to share information. Later versions incorporate **Transformer layers** within the U-Net to capture long-range dependencies. Demucs achieves state-of-the-art SDR on the MUSDB18 benchmark.

| Method | Domain | Architecture | Phase Handling | SDR (vocals) |
| :--- | :--- | :--- | :--- | :--- |
| **Open-Unmix** | Frequency (STFT) | FC + Bi-LSTM | Reuses mixture phase | ~6.3 dB |
| **Wave-U-Net** | Time (waveform) | 1D U-Net | Learned implicitly | ~5.7 dB |
| **Hybrid Demucs** | Both | Dual U-Net + Transformer | Learned (both domains) | ~8.1 dB |

---

# 6.3 Sound Event Detection

> **Explain sound event detection as a deep learning task. How is it different from audio classification, and what network architectures and training strategies are commonly used? (Fall 2025)**

## 6.3.1 Task Definition and Difference from Audio Classification

**Audio classification (audio tagging)** assigns one or more labels to an **entire audio clip** — the output is a set of clip-level labels. It answers: **what** sounds are present? Example: given a 10-second recording, output "dog bark, car horn."

**Sound event detection (SED)** identifies **what** sounds are present **and when** they occur — the output includes the onset (start time) and offset (end time) of each event. It answers: **what** sounds and **when**? Example: "dog bark from 2.1s to 3.4s, car horn from 5.0s to 5.8s."

**Polyphonic SED** further requires detecting **multiple overlapping events** at the same time — e.g., a dog barking while a car horn is blowing simultaneously.

| Property | Audio Classification | Sound Event Detection |
| :--- | :--- | :--- |
| **Output granularity** | Clip-level labels | Frame-level labels with timestamps |
| **Temporal localization** | No | Yes (onset + offset) |
| **Overlapping events** | Multi-label (present/absent) | Multi-label per time frame |
| **Annotation** | Weak labels (clip-level) | Strong labels (frame-level timestamps) |
| **Evaluation metric** | Accuracy, mAP | Event-based F1, segment-based F1, ER (error rate) |

## 6.3.2 SED as a Sequence Labeling Problem

SED is formulated as a **frame-level multi-label classification** problem:

1. The audio is converted into a sequence of feature frames (e.g., log-Mel spectrogram with shape $T \times F$, where $T$ is the number of time frames and $F$ is the number of Mel bins).
2. For each time frame $t$, the model outputs a binary vector $\mathbf{y}_t \in \{0, 1\}^C$ indicating which of the $C$ event classes are active at that frame.
3. The output is a matrix of shape $T \times C$ — a binary activity map across time and event classes.

Post-processing: A **median filter** is applied to smooth the frame-level predictions, removing spurious activations and filling short gaps. Onset and offset timestamps are extracted from contiguous active regions.

## 6.3.3 Network Architectures for SED

**1. CRNN (Convolutional Recurrent Neural Network):**

The CRNN is the dominant architecture for SED. It combines the local feature extraction of CNNs with the temporal modeling of RNNs:

- **CNN block:** Multiple convolutional layers (with batch normalization, ReLU, and pooling) process the log-Mel spectrogram to extract local spectro-temporal features. Pooling is applied primarily along the frequency axis to reduce the frequency dimension while preserving the temporal resolution.
- **RNN block:** The CNN output (reduced in frequency, full in time) is reshaped and fed into bidirectional GRU or LSTM layers. The recurrent layers model temporal context — they learn that a "door slam" is a short event while "rain" is sustained.
- **Output layer:** A time-distributed fully connected layer with **sigmoid activation** (not softmax, because multiple events can be active simultaneously) outputs the probability of each event class at each time frame.

**2. CNN with Attention:**

Replace the RNN with a **self-attention mechanism** applied along the time axis. Attention allows each frame to attend to all other frames, capturing long-range dependencies without the sequential processing bottleneck of RNNs. More parallelizable and often faster to train.

**3. CNN-Transformer:**

Use a CNN encoder to extract features, then apply a Transformer encoder over the temporal sequence. The Transformer's multi-head self-attention captures complex temporal patterns. This approach achieves strong results on the DCASE (Detection and Classification of Acoustic Scenes and Events) challenge benchmarks.

## 6.3.4 Training Strategies

**Weakly supervised learning:** Frame-level annotations (strong labels) are expensive to create. Often, only clip-level labels (weak labels) are available — we know a "dog bark" is somewhere in the clip but not when. **Multiple Instance Learning (MIL)** training uses pooling functions to aggregate frame-level predictions into clip-level predictions for loss computation:

- **Max pooling (MIL):** The clip-level prediction is the maximum frame-level prediction. Assumes the event is present in at least one frame.
- **Average pooling:** The clip-level prediction is the mean of all frame-level predictions. Works better for sustained events.
- **Attention pooling:** A learned attention mechanism weights the contribution of each frame. Frames containing the event receive higher weight.

**Semi-supervised and self-supervised learning:** Use large amounts of unlabeled audio with a small set of labeled data. Techniques include **mean teacher** (an exponential moving average of the student model provides pseudo-labels) and **contrastive pretraining** (learn general audio representations before fine-tuning for SED).

**Data augmentation:** SpecAugment (mask time/frequency bands), **mixup** (blend two training examples and their labels), time shifting, and adding environmental noise.

---

# 6.4 Structural Analysis of Music

## 6.4.1 Problem Definition

**Music Structure Analysis (MSA)** is the task of automatically segmenting a piece of music into its structural sections (intro, verse, chorus, bridge, outro, etc.) and labeling the function of each section. It consists of two sub-tasks:

- **Boundary detection:** Identifying the precise time points where one section ends and another begins.
- **Section labeling:** Assigning functional labels (e.g., "A" for verse, "B" for chorus) to the segments between boundaries.

A song might have the structure: Intro → Verse (A) → Chorus (B) → Verse (A) → Chorus (B) → Bridge (C) → Chorus (B) → Outro. MSA aims to recover this structure automatically from audio.

## 6.4.2 Feature Representations for MSA

**Self-Similarity Matrix (SSM):** A fundamental tool for MSA. Given a sequence of feature vectors $\mathbf{v}_1, \mathbf{v}_2, ..., \mathbf{v}_T$ (e.g., chroma features or Mel spectrogram frames), the SSM is a $T \times T$ matrix where entry $(i, j)$ measures the similarity between frames $i$ and $j$:

$
S[i, j] = \text{sim}(\mathbf{v}_i, \mathbf{v}_j)
$

using cosine similarity or dot product. In the SSM, **repeating sections** appear as off-diagonal stripes (the chorus at time $t_1$ is similar to the chorus at time $t_2$), and **homogeneous sections** appear as bright blocks along the diagonal. The SSM converts the 1D temporal structure into a 2D image-like representation that CNNs can process.

**Chroma features:** Represent the distribution of energy across the 12 pitch classes (C, C#, D, ..., B), invariant to octave. They capture harmonic content and are robust to timbral changes, making them ideal for detecting harmonic repetition (verse-chorus patterns).

**MFCCs and Mel spectrograms:** Capture timbral characteristics. Useful for detecting transitions where instrumentation changes (e.g., verse with guitar vs. chorus with full band).

## 6.4.3 Deep Learning Approaches for MSA

**1. CNN on SSM:** Compute the SSM from chroma or Mel features and treat it as an image. A CNN is trained to detect boundary locations — it learns to recognize the characteristic patterns in the SSM that correspond to section transitions (changes in block structure). The CNN outputs a boundary activation function — peaks indicate boundary locations.

**2. CNN on Mel spectrogram (direct):** Instead of computing an explicit SSM, feed the Mel spectrogram directly into a CNN. The network learns to detect structural boundaries from spectral changes. Architectures like VGG or ResNet, pretrained on audio classification tasks, can be fine-tuned for boundary detection.

**3. CNN + RNN / Transformer:** For section labeling, the boundary detection output is combined with temporal modeling. An RNN or Transformer processes the sequence of segment-level features and assigns functional labels. Self-attention is particularly useful because labeling requires comparing distant segments (e.g., recognizing that the segment at time 1:30 is the same "chorus" as the segment at 0:45).

## 6.4.4 Evaluation

Boundary detection is evaluated using **hit rate** with a tolerance window (typically ±0.5s or ±3s). A detected boundary is a "hit" if it falls within the tolerance of a ground-truth boundary. **Precision, recall, and F1-score** are computed over the set of detected and ground-truth boundaries.

Section labeling is evaluated using **pairwise F-measure** — checking whether pairs of frames that belong to the same section in the ground truth are also labeled as the same section by the algorithm, and vice versa.

Common benchmarks: **SALAMI** (Structural Analysis of Large Amounts of Music Information) dataset, **MIREX** (Music Information Retrieval Evaluation eXchange) structural segmentation task, and the **Beatles** annotated dataset.

---
