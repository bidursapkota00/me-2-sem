# 5. Video Processing

# 5.1 Video Sequence Processing

A **video** is a temporal sequence of image frames, typically captured at 24–30 frames per second (fps). Unlike a single image, a video contains both **spatial information** (appearance within each frame) and **temporal information** (how objects move and scenes change across frames). Video processing in deep learning must capture this **spatio-temporal** structure.

**Video as a data structure:** A video clip of $T$ frames, each of height $H$, width $W$, and $C$ color channels, forms a 4D tensor of shape $T \times C \times H \times W$. Processing this tensor is far more computationally expensive than processing a single image — a 10-second clip at 30 fps contains 300 frames, each requiring the same computation as an image.

**Challenges in video processing:**

- **High dimensionality:** The data volume grows linearly with the number of frames, making storage, memory, and computation expensive.
- **Temporal redundancy:** Consecutive frames are highly similar. Efficient models must exploit this redundancy rather than processing each frame independently.
- **Temporal dependencies:** Meaningful events (e.g., "a person picking up a cup") span many frames. The model must capture both short-range motion (frame-to-frame pixel displacement) and long-range context (the beginning and end of an action).
- **Variable length:** Videos have different durations, requiring models that handle variable-length sequences.

**Approaches to video understanding:**

| Approach | How It Works | Strength |
| :--- | :--- | :--- |
| **Frame-level (2D CNN)** | Apply a 2D CNN to each frame independently, then aggregate | Simple; leverages pretrained image models |
| **Clip-level (3D CNN)** | Apply 3D convolutions to short clips of stacked frames | Learns spatiotemporal features jointly |
| **Recurrent (CNN + RNN)** | Extract per-frame features with CNN, feed sequence to RNN/LSTM | Captures long-range temporal dependencies |
| **Two-stream** | Separate spatial (RGB) and temporal (optical flow) streams | Explicitly models appearance and motion |
| **Transformer-based** | Apply self-attention over spatial and temporal tokens | Captures global dependencies without recurrence |

**Frame sampling strategies:** Processing every frame is impractical. Common strategies include: **uniform sampling** (select $T$ evenly spaced frames), **random sampling** (random frames during training for augmentation), and **dense sampling** (multiple overlapping clips from a video, predictions averaged).

---

# 5.2 Motion Analysis and Optical Flow

> **Explain how optical flow is used for motion analysis in video sequences. Discuss at least two deep learning approaches that estimate optical flow and their comparative strengths. (Fall 2025)**

## 5.2.1 Optical Flow

**Optical flow** is the pattern of apparent motion of objects, surfaces, and edges in a visual scene caused by relative motion between the camera and the scene. It assigns a 2D displacement vector $(u, v)$ to each pixel, describing how that pixel has moved from one frame to the next.

For a pixel at position $(x, y)$ in frame $t$ with intensity $I(x, y, t)$, the **brightness constancy assumption** states that the pixel's intensity does not change as it moves:

$
I(x, y, t) = I(x + u, y + v, t + 1)
$

Applying a first-order Taylor expansion and dividing by $\delta t$:

$
I_x u + I_y v + I_t = 0
$

where $I_x, I_y$ are spatial gradients and $I_t$ is the temporal gradient. This is one equation with two unknowns $(u, v)$ — the **aperture problem** — requiring additional constraints to solve.

**Classical methods:**

- **Lucas-Kanade (1981):** Assumes flow is constant within a small local window. Solves a system of equations for all pixels in the window using least squares. Produces **sparse** flow (at feature points). Works well for small displacements.
- **Horn-Schunck (1981):** Adds a global smoothness constraint — assumes neighboring pixels have similar flow. Solves a variational optimization to produce **dense** flow (for every pixel). More sensitive to noise.

## 5.2.2 Deep Learning Approaches for Optical Flow

**1. FlowNet (2015) and FlowNet 2.0 (2017):**

FlowNet was the first end-to-end CNN for optical flow estimation. It takes two consecutive frames as input and outputs a dense flow field. Two variants were proposed:

- **FlowNetSimple (FlowNetS):** Stacks two input frames (6-channel input) and passes them through a standard encoder-decoder CNN. The encoder extracts features; the decoder upsamples to produce the flow field.
- **FlowNetCorr (FlowNetC):** Processes each frame through separate encoder branches, then computes a **correlation layer** (cross-correlation of feature maps) to explicitly match features between frames before decoding.

FlowNet 2.0 stacks multiple FlowNet architectures in a cascade — a large-displacement network followed by a small-displacement refinement network — significantly improving accuracy for both large and small motions.

**2. RAFT — Recurrent All-Pairs Field Transforms (2020):**

RAFT is a state-of-the-art optical flow method that iteratively refines flow estimates using a recurrent architecture.

- **Feature extraction:** A shared CNN encoder extracts features from both frames.
- **Correlation volume:** Computes the dot product between all pairs of feature vectors from the two frames, producing a 4D correlation volume that captures visual similarity at all displacements.
- **Iterative update:** A GRU-based recurrent unit repeatedly looks up the correlation volume at the current flow estimate, and produces a flow update $\Delta f$. After $N$ iterations, the flow converges to an accurate estimate.

| Property | FlowNet / FlowNet 2.0 | RAFT |
| :--- | :--- | :--- |
| **Architecture** | Encoder-decoder (stacked cascade) | Correlation volume + recurrent GRU |
| **Flow estimation** | Single forward pass (or cascade) | Iterative refinement ($N$ iterations) |
| **Accuracy** | Good baseline | State-of-the-art on benchmarks |
| **Large displacements** | FlowNet 2.0 handles via stacking | Handles via all-pairs correlation |
| **Generalization** | Moderate | Strong cross-dataset generalization |

**3. PWC-Net (2018):** Uses a **pyramid, warping, and cost volume** approach. Features are extracted at multiple scales (pyramid). At each scale, the second frame is warped using the upsampled flow from the coarser scale, a cost volume is computed between the first frame and the warped second frame, and the flow is refined. This coarse-to-fine strategy efficiently handles large motions while keeping computational cost low.

**Applications of optical flow:**

- **Action recognition:** Optical flow provides explicit motion features. Two-stream networks use optical flow as input to the temporal stream.
- **Video stabilization:** Flow vectors reveal unwanted camera shake, which can be compensated.
- **Object segmentation:** Moving objects produce different flow patterns than the background, enabling motion-based segmentation.
- **Frame interpolation:** Flow fields allow synthesis of intermediate frames between two existing frames.

---

# 5.3 3D Data and Convolution

> **Describe how 3D convolution differs from standard 2D convolution and explain its role in video-based action recognition. What are the computational trade-offs involved? (Fall 2025)**

## 5.3.1 From 2D to 3D Convolution

A **2D convolution** operates on a 2D spatial grid (height × width). The kernel has shape $k_h \times k_w$ and slides across the spatial dimensions, producing a 2D feature map. When applied to a video, a 2D CNN processes each frame independently — it captures spatial features (edges, textures, objects) but **cannot learn temporal patterns** across frames.

A **3D convolution** extends the kernel to include a temporal dimension. The kernel has shape $k_t \times k_h \times k_w$ (time × height × width) and slides across both spatial and temporal dimensions simultaneously. For an input volume of $T$ frames stacked together:

$
(I * K)[t, i, j] = \sum_{\tau=0}^{k_t-1} \sum_{m=0}^{k_h-1} \sum_{n=0}^{k_w-1} I[t+\tau, i+m, j+n] \cdot K[\tau, m, n]
$

**Output temporal size:**

$
T_{out} = \left\lfloor \frac{T_{in} - k_t + 2p_t}{s_t} \right\rfloor + 1
$

where $p_t$ is temporal padding and $s_t$ is temporal stride.

**Why 3D convolution matters:** A 3D kernel of size $3 \times 3 \times 3$ spans 3 consecutive frames and a $3 \times 3$ spatial region. It can detect motion patterns — for example, an edge that moves rightward across frames produces a specific activation pattern that a 2D kernel cannot capture. This enables the network to learn **spatiotemporal features** end-to-end.

| Property | 2D Convolution | 3D Convolution |
| :--- | :--- | :--- |
| **Kernel shape** | $k_h \times k_w$ | $k_t \times k_h \times k_w$ |
| **Input** | Single frame $H \times W \times C$ | Clip of $T$ frames $T \times H \times W \times C$ |
| **Output** | 2D feature map | 3D feature volume (preserves temporal dim) |
| **Motion capture** | None (spatial only) | Yes (temporal patterns across frames) |
| **Parameters** | $C_{in} \times k_h \times k_w \times C_{out}$ | $C_{in} \times k_t \times k_h \times k_w \times C_{out}$ |
| **Computation** | Lower | $k_t$ times higher |

## 5.3.2 C3D — Convolutional 3D Network

**C3D (2015)** was one of the first deep 3D CNNs for video feature learning. It demonstrated that simple 3D convolutions can learn effective spatiotemporal features directly from raw video.

**Architecture:** C3D uses a homogeneous design with all convolution kernels of size $3 \times 3 \times 3$ and all pooling kernels of size $2 \times 2 \times 2$ (except the first pooling layer which is $1 \times 2 \times 2$ to preserve temporal resolution early on). The network has 8 convolution layers, 5 pooling layers, and 2 fully connected layers. It takes a clip of **16 frames** resized to $112 \times 112$ as input.

**Key finding:** The $3 \times 3 \times 3$ kernel was empirically found to be the best temporal kernel size — similar to how $3 \times 3$ spatial kernels dominated in 2D CNNs (VGGNet). Features from C3D's fc6 layer serve as powerful **generic video descriptors** that transfer well across tasks (action recognition, scene classification, event detection).

## 5.3.3 I3D — Inflated 3D ConvNet

**I3D (2017)** by Carreira and Zisserman introduced the concept of **inflating** a pretrained 2D CNN into a 3D CNN.

**Inflation strategy:** Take a 2D filter of shape $k \times k$ from a pretrained ImageNet model (e.g., Inception-V1). Repeat it $k_t$ times along the temporal dimension to create a $k_t \times k \times k$ 3D filter. Divide each weight by $k_t$ to preserve the output scale. This **bootstrapping** from 2D pretrained weights gives I3D a massive advantage over training a 3D CNN from scratch — it inherits the rich visual representations learned on ImageNet.

**Two-stream I3D:** I3D is often used as a two-stream architecture — one stream processes RGB frames and the other processes precomputed optical flow. The predictions from both streams are averaged for the final classification. This consistently outperforms single-stream models.

**Computational trade-offs of 3D CNNs:**

- **Parameters:** A $3 \times 3 \times 3$ filter has 27 weights vs. 9 for a $3 \times 3$ filter — 3× more parameters per filter.
- **FLOPs:** The number of multiply-add operations scales with the temporal extent of both the input and the kernel, often making 3D CNNs 10–100× more expensive than their 2D counterparts.
- **Memory:** Intermediate 3D feature maps are large — a feature volume of $T' \times H' \times W' \times C'$ requires $T'$ times more memory than a 2D feature map.
- **Mitigation strategies:** (2+1)D convolutions (R(2+1)D) factorize a 3D kernel into a spatial $1 \times k \times k$ kernel followed by a temporal $k_t \times 1 \times 1$ kernel, reducing parameters and computation while often improving accuracy due to the added nonlinearity between the two decomposed operations.

---

# 5.4 Recurrent Neural Networks for Video Sequence

## 5.4.1 CNN + RNN Framework

While 3D CNNs jointly learn spatiotemporal features from short clips, they are limited in their temporal extent (typically 16–64 frames). For longer video understanding, a natural approach is to combine **CNNs for spatial feature extraction** with **RNNs for temporal modeling.**

**Long-term Recurrent Convolutional Network (LRCN):**

1. **Feature extraction:** Pass each frame $x_t$ through a pretrained CNN (e.g., VGG, ResNet) to obtain a feature vector $\mathbf{v}_t \in \mathbb{R}^d$.
2. **Sequence modeling:** Feed the sequence of feature vectors $\mathbf{v}_1, \mathbf{v}_2, ..., \mathbf{v}_T$ into an LSTM.
3. **Classification:** The final hidden state $\mathbf{h}_T$ (or the pooled hidden states) is passed through a fully connected layer with softmax for classification.

The LSTM maintains a cell state $\mathbf{c}_t$ and hidden state $\mathbf{h}_t$, updated at each time step:

$
\mathbf{f}_t = \sigma(\mathbf{W}_f [\mathbf{h}_{t-1}, \mathbf{v}_t] + \mathbf{b}_f) \quad \text{(forget gate)}
$

$
\mathbf{i}_t = \sigma(\mathbf{W}_i [\mathbf{h}_{t-1}, \mathbf{v}_t] + \mathbf{b}_i) \quad \text{(input gate)}
$

$
\tilde{\mathbf{c}}_t = \tanh(\mathbf{W}_c [\mathbf{h}_{t-1}, \mathbf{v}_t] + \mathbf{b}_c) \quad \text{(candidate)}
$

$
\mathbf{c}_t = \mathbf{f}_t \odot \mathbf{c}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{c}}_t \quad \text{(cell update)}
$

$
\mathbf{o}_t = \sigma(\mathbf{W}_o [\mathbf{h}_{t-1}, \mathbf{v}_t] + \mathbf{b}_o) \quad \text{(output gate)}
$

$
\mathbf{h}_t = \mathbf{o}_t \odot \tanh(\mathbf{c}_t) \quad \text{(hidden state)}
$

This allows the LSTM to selectively remember or forget information over long sequences, capturing the temporal evolution of visual features.

## 5.4.2 ConvLSTM

Standard LSTMs use fully connected operations internally, discarding spatial structure. **ConvLSTM** replaces the matrix multiplications inside the LSTM gates with convolution operations, so both the inputs and hidden states are 3D tensors (channels × height × width) rather than 1D vectors.

$
\mathbf{f}_t = \sigma(\mathbf{W}_f * [\mathbf{H}_{t-1}, \mathbf{X}_t] + \mathbf{b}_f)
$

where $*$ denotes convolution and $\mathbf{X}_t, \mathbf{H}_t$ are 3D tensors. ConvLSTM preserves spatial information while modeling temporal dynamics, making it effective for spatiotemporal prediction tasks (e.g., video prediction, precipitation nowcasting).

## 5.4.3 Comparison of Video Architectures

| Architecture | Temporal Range | Spatial Awareness | Pretraining | Computation |
| :--- | :--- | :--- | :--- | :--- |
| **2D CNN (per-frame)** | None | Full | ImageNet | Low |
| **3D CNN (C3D/I3D)** | Short (16–64 frames) | Full | Kinetics / Inflated | High |
| **CNN + LSTM** | Long (entire video) | Via CNN features | CNN: ImageNet | Moderate |
| **ConvLSTM** | Long | Preserved in gates | Limited | Moderate |
| **Two-stream** | Short–Medium | Full (two paths) | ImageNet + flow | High |

---

# 5.5 Action Recognition and Object Tracking

> **Explain how optical flow is used for motion analysis in video sequences. Discuss at least two deep learning approaches that estimate optical flow and their comparative strengths. (Fall 2025)**
>
> **Describe how 3D convolution differs from standard 2D convolution and explain its role in video-based action recognition. What are the computational trade-offs involved? (Fall 2025)**

## 5.5.1 Action Recognition

**Action recognition** is the task of classifying the activity occurring in a video clip (e.g., "running," "cooking," "handshaking"). It is one of the most fundamental video understanding tasks.

**Two-Stream Networks (Simonyan & Zisserman, 2014):**

The two-stream architecture processes appearance and motion information through separate convolutional pathways:

- **Spatial stream:** Takes a single RGB frame as input, processes it through a 2D CNN (e.g., VGGNet). Captures the scene and object appearance — **what** is in the video.
- **Temporal stream:** Takes a stack of $L$ consecutive optical flow fields (2L channels for horizontal and vertical flow) as input, processes it through a separate 2D CNN. Captures the motion pattern — **how** things move.
- **Fusion:** The softmax outputs of both streams are combined (by averaging or using a learned fusion layer) for final classification.

The temporal stream operating on precomputed optical flow provides explicit motion features, which significantly improves performance over spatial-only models.

**SlowFast Networks (Feichtenhofer et al., 2019):**

SlowFast is a more modern architecture that replaces optical flow with a dual-pathway design:

- **Slow pathway:** Operates at a low frame rate (e.g., 4 fps). Uses a large channel capacity (many filters). Captures fine spatial semantics and slow-changing appearance.
- **Fast pathway:** Operates at a high frame rate (e.g., 32 fps). Uses a small channel capacity (fewer filters, ~1/8 of Slow). Captures rapidly changing motion and temporal dynamics.
- **Lateral connections:** Information flows from the Fast pathway to the Slow pathway via lateral connections at multiple stages, allowing the Slow pathway to incorporate temporal information.

SlowFast does not require precomputed optical flow, simplifying the pipeline while achieving state-of-the-art results on benchmarks like Kinetics and AVA.

**Other notable architectures for action recognition:**

- **TSN (Temporal Segment Networks):** Divides a video into segments, samples one frame per segment, processes each with a shared 2D CNN, and aggregates (average consensus) for classification. Efficient and effective for long videos.
- **R(2+1)D:** Decomposes 3D convolutions into separate spatial ($1 \times k \times k$) and temporal ($k_t \times 1 \times 1$) convolutions. This factorization adds an extra nonlinearity (ReLU between the two), doubles the number of nonlinearities compared to 3D convolutions, and often improves accuracy while reducing computation.

| Method | Input | Motion Modeling | Requires Optical Flow | Strength |
| :--- | :--- | :--- | :--- | :--- |
| **Two-Stream** | RGB + Flow | Explicit (optical flow stream) | Yes | Strong motion features |
| **C3D / I3D** | RGB clips | Implicit (3D convolutions) | No (optional) | End-to-end spatiotemporal |
| **CNN + LSTM** | Frame features | Sequential (recurrence) | No | Long-range dependencies |
| **SlowFast** | RGB (dual rate) | Implicit (fast pathway) | No | No flow needed; state-of-the-art |
| **R(2+1)D** | RGB clips | Factorized 3D convolution | No | Efficient; more nonlinearities |

## 5.5.2 Object Tracking

**Object tracking** is the task of locating a target object across consecutive video frames, maintaining its identity over time. Unlike detection (which independently identifies objects per frame), tracking establishes **temporal correspondence** — the same object in frame $t$ and frame $t+1$ must receive the same identity.

**Tracking paradigms:**

- **Single Object Tracking (SOT):** Given the bounding box of a target in the first frame, track it throughout the video. The object class is unknown — the tracker must generalize to any object.
- **Multi-Object Tracking (MOT):** Track multiple objects simultaneously, handling new objects entering the scene, objects leaving, and maintaining unique IDs. Typically uses a **tracking-by-detection** paradigm.

**Deep Learning Methods for Object Tracking:**

**1. SORT (Simple Online and Realtime Tracking):**

SORT uses a **tracking-by-detection** approach:

- An object detector (e.g., YOLO, Faster R-CNN) detects objects in each frame.
- A **Kalman filter** predicts the next position of each tracked object based on its previous motion (constant velocity model).
- The **Hungarian algorithm** associates predicted positions with new detections based on **IoU (Intersection over Union)** overlap.
- Unmatched detections start new tracks; unmatched tracks are terminated after a threshold.

SORT is extremely fast but struggles with occlusions — if an object is hidden for several frames, the track is lost and a new ID is assigned when it reappears.

**2. DeepSORT (Deep SORT):**

DeepSORT extends SORT by adding a **CNN-based appearance model:**

- For each detected bounding box, a small CNN extracts a 128-dimensional **appearance embedding** (feature vector describing the object's visual appearance — color, texture, shape).
- During data association, both **motion distance** (Mahalanobis distance from Kalman filter) and **appearance distance** (cosine distance between embeddings) are used.
- A track is associated with a detection only if both distances are below their respective thresholds.
- This allows DeepSORT to re-identify objects after occlusion by matching their appearance, significantly reducing **ID switches.**

**3. Siamese Network Trackers (SiamFC, SiamRPN):**

Siamese trackers are used for **single object tracking:**

- **SiamFC (2016):** Two identical CNN branches (sharing weights) process: (a) a **template** — the target patch from the first frame, and (b) a **search region** — a larger region in the current frame. A cross-correlation operation between the two feature maps produces a response map. The peak of the response map indicates the target's location.
- **SiamRPN:** Extends SiamFC by adding a Region Proposal Network (RPN) head, enabling bounding box regression in addition to localization, improving scale and aspect ratio handling.

Siamese trackers run at real-time speeds and do not require online fine-tuning during tracking.

| Method | Type | Core Mechanism | Handles Occlusion | Speed |
| :--- | :--- | :--- | :--- | :--- |
| **SORT** | MOT | Kalman filter + Hungarian (IoU) | Poor | Very fast |
| **DeepSORT** | MOT | SORT + CNN appearance embeddings | Good | Fast |
| **SiamFC** | SOT | Siamese cross-correlation | Moderate | Real-time |

---
