# 1. Foundation of Deep Neural Networks

# 1.1 Concept of AI, ML, DL and Neural Networks

> **Compare supervised, unsupervised, and self-supervised learning paradigms with suitable examples for each. Discuss how the choice of learning paradigm affects model design. (Fall 2025)**

**Artificial Intelligence (AI)** is the broadest field — it refers to any system designed to simulate human intelligence and perform tasks like reasoning, problem-solving, perception, and language understanding. AI approaches include rule-based systems, search algorithms, expert systems, and learning-based methods.

**Machine Learning (ML)** is a subset of AI where systems learn patterns from data rather than being explicitly programmed. ML uses statistical algorithms to identify structures in data and make predictions. Traditional ML requires manual feature engineering — humans must decide which features (e.g., edges, color histograms) to extract from raw data before feeding them to the model.

**Deep Learning (DL)** is a subset of ML that uses deep neural networks (networks with multiple hidden layers) to automatically learn hierarchical feature representations from raw data. The term "deep" refers to the depth (number of layers) of the network. DL eliminates manual feature engineering — the network learns low-level features (edges, textures) in early layers and high-level features (objects, concepts) in deeper layers.

**Neural Networks** are computational models inspired by the structure of biological neurons. A neural network consists of interconnected nodes (neurons) organized in layers. Each neuron receives inputs, applies weights and a bias, computes a weighted sum, passes it through an activation function, and produces an output. Neural networks are the architectural foundation of deep learning.

The relationship is hierarchical: AI ⊃ ML ⊃ DL, where DL is built upon neural network architectures.

| Aspect                  | AI                                       | ML                                | DL                                                    |
| :---------------------- | :--------------------------------------- | :-------------------------------- | :---------------------------------------------------- |
| **Scope**               | Broadest — simulating human intelligence | Subset of AI — learning from data | Subset of ML — deep neural networks                   |
| **Feature Engineering** | Rule-based / manual                      | Manual feature extraction         | Automatic feature learning                            |
| **Data Requirement**    | Varies                                   | Moderate                          | Large datasets required                               |
| **Compute**             | Low to moderate                          | Moderate                          | High (GPUs/TPUs)                                      |
| **Example**             | Chess engine, expert system              | Spam filter (SVM, Naive Bayes)    | Image recognition (CNN), language model (Transformer) |

---

# 1.2 Learning Paradigms

> **Compare supervised, unsupervised, and self-supervised learning paradigms with suitable examples for each. Discuss how the choice of learning paradigm affects model design. (Fall 2025)**

**1. Supervised Learning:** The model is trained on labeled data — each input is paired with the correct output (ground truth). The model learns a mapping function f: X → Y by minimizing the error between predicted and actual outputs. Tasks include **classification** (predicting discrete labels, e.g., cat vs. dog) and **regression** (predicting continuous values, e.g., house price). Model design requires a labeled dataset, a loss function comparing predictions to labels (e.g., cross-entropy for classification, MSE for regression), and an output layer matching the task. Example: image classification using CNNs trained on ImageNet.

**2. Unsupervised Learning:** The model works with unlabeled data and discovers hidden structures, patterns, or groupings without human guidance. Tasks include **clustering** (grouping similar data, e.g., K-means, DBSCAN), **dimensionality reduction** (e.g., PCA, autoencoders), and **density estimation**. Model design uses reconstruction loss or distance-based objectives instead of label-based loss. Example: customer segmentation using K-means clustering on purchase behavior data.

**3. Semi-Supervised Learning:** Combines a small amount of labeled data with a large volume of unlabeled data. The labeled data provides direction while the unlabeled data helps the model learn the overall data distribution. Useful when labeling is expensive or time-consuming. Example: medical image classification where only a few hundred images are labeled by doctors but millions of unlabeled scans are available.

**4. Self-Supervised Learning:** The model generates its own supervisory signals from the input data by creating pretext tasks — predicting missing parts, future elements, or transformations of the data. No manual labels are needed. Example: BERT (masked language model — predicts masked words in a sentence), contrastive learning in vision (SimCLR — learns representations by contrasting augmented views of the same image). Model design requires a pretext task definition and typically a large encoder architecture.

**5. Reinforcement Learning (RL):** An agent learns by interacting with an environment, receiving rewards or penalties for actions, and optimizing cumulative long-term reward. There are no labeled input-output pairs; instead, the agent learns a policy π(s) → a that maps states to actions. Model design requires defining the state space, action space, and reward function. Example: AlphaGo learning to play Go by self-play; robotic arm learning to grasp objects.

**6. Online Learning:** The model is updated incrementally as new data arrives, one sample (or mini-batch) at a time, rather than retraining on the entire dataset. Suitable for streaming data or when the dataset is too large to fit in memory. Example: recommendation systems updating user preferences in real-time.

**7. Active Learning:** The model proactively selects the most informative unlabeled data points and queries a human oracle to label them. This minimizes the total labeling effort while maximizing model improvement. Example: a text classifier that identifies the most ambiguous documents and asks a human to label only those.

**Impact on Model Design:** The choice of paradigm determines the loss function (label-based vs. reconstruction-based vs. reward-based), the output architecture (classification head vs. decoder vs. policy network), the data pipeline (labeled vs. unlabeled vs. environment interaction), and the training loop (single-pass vs. iterative interaction).

---

# 1.3 Ethical Concerns and Responsible AI

> **Discuss the ethical concerns surrounding AI systems. How can principles of responsible AI be incorporated during the design and deployment of deep learning models? (Fall 2025)**

**1. Bias and Fairness:** AI models learn from historical data that often contains societal biases. If training data underrepresents certain demographics or reflects historical discrimination, the model inherits and amplifies these biases. Example: a hiring model trained on past recruitment data may systematically disadvantage women if historical hiring was biased. Mitigation: use diverse, representative training datasets; apply fairness-aware algorithms; conduct regular bias audits across protected groups (gender, race, age).

**2. Transparency and the "Black Box" Problem:** Deep neural networks are complex nonlinear systems whose internal decision-making is difficult for humans to interpret. This lack of transparency makes it hard to explain, audit, or justify AI-driven decisions — especially critical in healthcare, criminal justice, and finance. Mitigation: use Explainable AI (XAI) techniques such as SHAP (SHapley Additive exPlanations), LIME (Local Interpretable Model-agnostic Explanations), Grad-CAM (for visual explanations in CNNs), and attention visualization in Transformers.

**3. Privacy and Data Security:** DL requires vast amounts of data, raising concerns about informed consent, data ownership, unauthorized surveillance, and data breaches. Models can memorize sensitive training data and leak it during inference. Mitigation: use differential privacy (adding calibrated noise during training), federated learning (training on decentralized data without collecting it centrally), and data anonymization techniques.

**4. Accountability and Liability:** As AI systems become more autonomous, assigning responsibility for errors becomes difficult. When an autonomous vehicle causes an accident or a medical AI misdiagnoses a patient, it is unclear whether the developer, deployer, or user is liable. Mitigation: establish clear governance frameworks defining roles and responsibilities; maintain audit trails of model decisions; implement human-in-the-loop systems for high-stakes decisions.

**5. Environmental Impact:** Training large deep learning models consumes significant energy and produces substantial carbon emissions. Training GPT-3 consumed an estimated 1,287 MWh of electricity. Mitigation: use more efficient architectures, model compression (pruning, quantization, distillation), and renewable energy-powered data centers.

**6. Misuse and Dual Use:** DL can be used to create deepfakes, autonomous weapons, mass surveillance, and social manipulation tools. Mitigation: establish ethical review boards, implement usage policies, develop detection tools for synthetic media.

**Principles of Responsible AI:** Fairness (equitable treatment across groups), Transparency (explainable decisions), Privacy (data protection), Accountability (clear responsibility), Safety (robust and reliable systems), Human oversight (meaningful human control over AI decisions), and Societal benefit (AI should serve the common good). These principles should be embedded throughout the AI lifecycle — from data collection and model design to deployment and monitoring.

---

# 1.4 Perceptron and Multi-Layer Perceptron

> **Explain the role of activation functions in a neural network. Compare ReLU, Sigmoid, and Tanh in terms of their mathematical properties, advantages, and limitations. (Fall 2025)**

## 1.4.1 Perceptron (Single-Layer)

The **perceptron** is the simplest neural network model — a single neuron that performs binary classification. It was proposed by Frank Rosenblatt (1958).

**Architecture:** Input layer connects directly to a single output node. There are no hidden layers.

**Computation:** Given inputs $x_1, x_2, ..., x_n$ with weights $w_1, w_2, ..., w_n$ and bias $b$:

$
z = \sum_{i=1}^{n} w_i x_i + b
$

The output is determined by a step (threshold) activation function:

$
y = \begin{cases} 1 & \text{if } z \geq 0 \\ 0 & \text{if } z < 0 \end{cases}
$

**Learning Rule (Perceptron Update Rule):** For a training sample with target $t$ and prediction $y$:

$
w_i \leftarrow w_i + \eta (t - y) x_i
$

where $\eta$ is the learning rate. The weights are updated only when the prediction is incorrect ($t \neq y$).

**Limitation:** A single perceptron can only learn **linearly separable** functions. It can learn AND and OR gates but **cannot learn XOR** because XOR is not linearly separable — no single straight line can separate the two classes.

## 1.4.2 Multi-Layer Perceptron (MLP)

The **MLP** overcomes the limitation of the single-layer perceptron by introducing one or more hidden layers between the input and output layers.

**Architecture:** An MLP is a **feedforward** neural network with three types of layers:

- **Input layer:** Receives raw input features. No computation occurs here.
- **Hidden layer(s):** One or more layers where actual computation happens. Each neuron is connected to every neuron in the adjacent layers (fully connected / dense).
- **Output layer:** Produces the final prediction. Its size and activation depend on the task.

**Computation in each neuron:**

$
z = \sum_{i=1}^{n} w_i x_i + b \quad \text{(weighted sum)}
$

$
a = \sigma(z) \quad \text{(activation)}
$

where $\sigma$ is a non-linear activation function (ReLU, Sigmoid, Tanh, etc.).

**Why non-linearity is essential:** Without non-linear activation functions, stacking multiple layers is equivalent to a single linear transformation (because the composition of linear functions is linear). Non-linear activations enable the network to learn complex, non-linear decision boundaries.

**Training:** MLPs are trained using **backpropagation** combined with **gradient descent** optimization. The network performs a forward pass (compute predictions), calculates the loss, then propagates gradients backward to update all weights.

**Universal Approximation Theorem:** An MLP with a single hidden layer containing a sufficient number of neurons can approximate any continuous function to arbitrary accuracy. However, deeper networks (more layers) can represent the same functions with exponentially fewer neurons, making depth practically important.

| Feature               | Perceptron                        | MLP                                   |
| :-------------------- | :-------------------------------- | :------------------------------------ |
| **Layers**            | Input → Output (no hidden)        | Input → Hidden(s) → Output            |
| **Decision Boundary** | Linear (straight line/hyperplane) | Non-linear (curved, complex)          |
| **Activation**        | Step function                     | Non-linear (ReLU, Sigmoid, Tanh)      |
| **Training**          | Perceptron update rule            | Backpropagation + gradient descent    |
| **Capability**        | Linearly separable problems only  | Can solve XOR and any complex pattern |

---

# 1.5 Components of Neural Networks

## 1.5.1 Activation Functions

> **Explain the role of activation functions in a neural network. Compare ReLU, Sigmoid, and Tanh in terms of their mathematical properties, advantages, and limitations. (Fall 2025)**

Activation functions introduce **non-linearity** into the network, enabling it to learn complex mappings from inputs to outputs.

**1. Sigmoid:**

$
\sigma(z) = \frac{1}{1 + e^{-z}}
$

- **Range:** (0, 1)
- **Derivative:** $\sigma'(z) = \sigma(z)(1 - \sigma(z))$, maximum value = 0.25 at z = 0
- **Advantages:** Smooth, differentiable; output interpretable as probability; suitable for binary classification output layer.
- **Limitations:** Suffers from **vanishing gradient** — derivative is very small for large |z|, causing gradients to shrink to near zero in deep networks. Outputs are **not zero-centered**, which can cause zig-zag gradient updates. Computationally expensive due to exponential operation.

**2. Tanh (Hyperbolic Tangent):**

$
\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}
$

- **Range:** (−1, 1)
- **Derivative:** $\tanh'(z) = 1 - \tanh^2(z)$, maximum value = 1.0 at z = 0
- **Advantages:** **Zero-centered** output — makes optimization easier as gradients are not biased in one direction. Stronger gradients than sigmoid (derivative up to 1.0 vs. 0.25).
- **Limitations:** Still suffers from **vanishing gradient** for large |z|. Computationally expensive.

**3. ReLU (Rectified Linear Unit):**

$
f(z) = \max(0, z)
$

- **Range:** [0, ∞)
- **Derivative:** $f'(z) = \begin{cases} 1 & \text{if } z > 0 \\ 0 & \text{if } z \leq 0 \end{cases}$
- **Advantages:** Computationally very efficient (simple thresholding). Does **not suffer from vanishing gradient** for positive inputs (gradient is constant 1). Leads to sparse activations (many neurons output 0), which improves efficiency. Faster convergence in practice.
- **Limitations:** **Dying ReLU problem** — neurons can get stuck outputting 0 for all inputs if weights update such that the input to ReLU is always negative. These neurons effectively "die" and stop learning. Not zero-centered.

**4. Leaky ReLU:**

$
f(z) = \begin{cases} z & \text{if } z > 0 \\ \alpha z & \text{if } z \leq 0 \end{cases}
$

where $\alpha$ is a small constant (typically 0.01). Solves the dying ReLU problem by allowing a small gradient when z < 0.

**5. Softmax (used in output layer for multi-class classification):**

$
\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}
$

Converts a vector of raw scores (logits) into a probability distribution where all outputs sum to 1.

| Activation     | Range   | Zero-Centered | Vanishing Gradient | Computation | Typical Use                  |
| :------------- | :------ | :------------ | :----------------- | :---------- | :--------------------------- |
| **Sigmoid**    | (0, 1)  | No            | Yes                | Expensive   | Binary classification output |
| **Tanh**       | (−1, 1) | Yes           | Yes                | Expensive   | Hidden layers (RNNs)         |
| **ReLU**       | [0, ∞)  | No            | No (for z > 0)     | Very fast   | Default for hidden layers    |
| **Leaky ReLU** | (−∞, ∞) | No            | No                 | Fast        | Alternative to ReLU          |
| **Softmax**    | (0, 1)  | N/A           | N/A                | Moderate    | Multi-class output           |

## 1.5.2 Weight Initialization

Proper weight initialization is critical to ensure stable training and avoid vanishing or exploding gradients.

**Problem with zero initialization:** If all weights are initialized to zero, all neurons in a layer compute the same output and receive the same gradient — they learn identical features forever (**symmetry problem**). The network effectively has one neuron per layer.

**Problem with random large initialization:** If weights are too large, activations and gradients explode exponentially through layers (**exploding gradient**), causing numerical overflow and unstable training.

**Problem with random small initialization:** If weights are too small, activations and gradients shrink exponentially through layers (**vanishing gradient**), causing early layers to learn extremely slowly.

**Xavier (Glorot) Initialization:** Designed for **Sigmoid and Tanh** activations. Weights are drawn from a distribution with variance:

$
\text{Var}(w) = \frac{2}{n_{in} + n_{out}}
$

where $n_{in}$ is the number of input neurons and $n_{out}$ is the number of output neurons in the layer. This keeps the variance of activations and gradients approximately constant across layers.

**He (Kaiming) Initialization:** Designed for **ReLU** activations. Since ReLU sets half the outputs to zero, the variance must be larger to compensate:

$
\text{Var}(w) = \frac{2}{n_{in}}
$

He initialization is the standard for modern deep networks using ReLU.

| Method              | Formula                                   | Best For                     |
| :------------------ | :---------------------------------------- | :--------------------------- |
| **Zero**            | $w = 0$                                   | Never use (symmetry problem) |
| **Random Small**    | $w \sim \mathcal{N}(0, 0.01)$             | Shallow networks only        |
| **Xavier (Glorot)** | $\text{Var} = \frac{2}{n_{in} + n_{out}}$ | Sigmoid, Tanh                |
| **He (Kaiming)**    | $\text{Var} = \frac{2}{n_{in}}$           | ReLU and variants            |

## 1.5.3 Optimization Algorithms

**Gradient Descent (GD):** The fundamental optimization algorithm. It updates weights in the direction that reduces the loss function:

$
w \leftarrow w - \eta \frac{\partial L}{\partial w}
$

where $\eta$ is the learning rate and $\frac{\partial L}{\partial w}$ is the gradient of the loss with respect to weight $w$.

**Variants by batch size:**

- **Batch GD:** Computes gradient using the entire training dataset per update. Stable but very slow for large datasets.
- **Stochastic GD (SGD):** Computes gradient using a single training sample per update. Noisy but fast; the noise can help escape local minima.
- **Mini-Batch GD:** Computes gradient using a small batch (e.g., 32, 64, 128 samples). Balances stability and speed. Most commonly used in practice.

**SGD with Momentum:** Adds a fraction of the previous update to the current update, accelerating convergence in consistent gradient directions and dampening oscillations:

$
v_t = \beta v_{t-1} + \eta \nabla L(w)
$

$
w \leftarrow w - v_t
$

where $\beta$ (typically 0.9) is the momentum coefficient. Analogous to a ball rolling downhill — it accumulates velocity.

**RMSprop (Root Mean Square Propagation):** Adapts the learning rate for each parameter by dividing by a running average of recent gradient magnitudes:

$
s_t = \beta s_{t-1} + (1-\beta)(\nabla L)^2
$

$
w \leftarrow w - \frac{\eta}{\sqrt{s_t + \epsilon}} \nabla L
$

This prevents the learning rate from being too large for parameters with large gradients and too small for parameters with small gradients.

**Adam (Adaptive Moment Estimation):** Combines Momentum (first moment — mean of gradients) and RMSprop (second moment — variance of gradients) with bias correction:

$
m_t = \beta_1 m_{t-1} + (1-\beta_1) \nabla L \quad \text{(first moment)}
$

$
v_t = \beta_2 v_{t-1} + (1-\beta_2) (\nabla L)^2 \quad \text{(second moment)}
$

$
\hat{m}_t = \frac{m_t}{1-\beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1-\beta_2^t} \quad \text{(bias correction)}
$

$
w \leftarrow w - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t
$

Default hyperparameters: $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\epsilon = 10^{-8}$. Adam is the most widely used optimizer in modern deep learning due to its robust performance across architectures and minimal tuning requirements.

| Optimizer    | Mechanism                                 | Strength                                 |
| :----------- | :---------------------------------------- | :--------------------------------------- |
| **SGD**      | Fixed learning rate, simple gradient step | Good generalization                      |
| **Momentum** | Accumulates velocity from past gradients  | Faster convergence, smooths oscillations |
| **RMSprop**  | Per-parameter adaptive learning rate      | Handles sparse gradients well            |
| **Adam**     | Momentum + RMSprop + bias correction      | Fast, robust, default choice             |

## 1.5.4 Backpropagation

> **Describe the backpropagation algorithm in detail. Derive the weight update rule using chain rule and explain how vanishing gradient problems arise. (Fall 2025)**

Backpropagation (backprop) is the algorithm used to compute gradients of the loss function with respect to every weight in the network. It applies the **chain rule** of calculus to efficiently propagate error signals backward from the output layer to the input layer.

**Forward Pass:** Input flows through the network layer by layer. At each neuron:

$
z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]} \quad \text{(weighted sum)}
$

$
a^{[l]} = \sigma(z^{[l]}) \quad \text{(activation)}
$

The final output $a^{[L]}$ is compared to the true label using the loss function $L$.

**Backward Pass (Chain Rule Application):** To update weight $W^{[l]}$ connecting layer $l-1$ to layer $l$, we need $\frac{\partial L}{\partial W^{[l]}}$. By the chain rule:

$
\frac{\partial L}{\partial W^{[l]}} = \frac{\partial L}{\partial a^{[l]}} \cdot \frac{\partial a^{[l]}}{\partial z^{[l]}} \cdot \frac{\partial z^{[l]}}{\partial W^{[l]}}
$

Breaking this down:

- $\frac{\partial L}{\partial a^{[l]}}$: how the loss changes with the neuron's output (computed from the layer above)
- $\frac{\partial a^{[l]}}{\partial z^{[l]}} = \sigma'(z^{[l]})$: the derivative of the activation function
- $\frac{\partial z^{[l]}}{\partial W^{[l]}} = a^{[l-1]}$: the input to this layer (activation from the previous layer)

Define the **error signal** (delta) at layer $l$:

$
\delta^{[l]} = \frac{\partial L}{\partial z^{[l]}} = \frac{\partial L}{\partial a^{[l]}} \cdot \sigma'(z^{[l]})
$

Then the gradient and weight update become:

$
\frac{\partial L}{\partial W^{[l]}} = \delta^{[l]} \cdot (a^{[l-1]})^T
$

$
W^{[l]} \leftarrow W^{[l]} - \eta \cdot \delta^{[l]} \cdot (a^{[l-1]})^T
$

The error propagates backward: $\delta^{[l-1]} = (W^{[l]})^T \delta^{[l]} \cdot \sigma'(z^{[l-1]})$

**Backpropagation Algorithm (Step-by-Step):**

1. **Initialize** all weights (Xavier/He initialization).
2. **Forward pass:** Compute $z^{[l]}$ and $a^{[l]}$ for all layers $l = 1, 2, ..., L$.
3. **Compute output error:** $\delta^{[L]} = \frac{\partial L}{\partial a^{[L]}} \cdot \sigma'(z^{[L]})$.
4. **Backpropagate:** For $l = L-1, L-2, ..., 1$: compute $\delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]} \cdot \sigma'(z^{[l]})$.
5. **Update weights:** For all layers: $W^{[l]} \leftarrow W^{[l]} - \eta \cdot \delta^{[l]} \cdot (a^{[l-1]})^T$.
6. **Update biases:** $b^{[l]} \leftarrow b^{[l]} - \eta \cdot \delta^{[l]}$.
7. **Repeat** steps 2–6 for each batch until convergence.

**Vanishing Gradient Problem:** In a deep network with $L$ layers, the gradient at layer $l$ involves a product of $L - l$ activation derivatives:

$
\frac{\partial L}{\partial W^{[l]}} \propto \prod_{k=l}^{L} \sigma'(z^{[k]})
$

For **sigmoid** activation, $\sigma'(z) \leq 0.25$. In a 10-layer network, the gradient at the first layer is scaled by approximately $(0.25)^{10} \approx 10^{-6}$ — effectively zero. This means early layers receive negligible gradients and learn extremely slowly or not at all. Similarly for **tanh**, the derivative is at most 1.0 but is much smaller for large |z|.

**Solutions to Vanishing Gradient:**

- **ReLU activation:** Derivative is 1 for positive inputs — gradients pass through without shrinking.
- **He initialization:** Maintains proper signal variance across layers when using ReLU.
- **Batch Normalization:** Normalizes layer inputs to maintain activations in the effective range of the activation function.
- **Residual connections (Skip connections):** Add the input of a layer directly to its output ($a^{[l]} = \sigma(z^{[l]}) + a^{[l-1]}$), providing a direct gradient pathway that bypasses the multiplicative chain.
- **Gradient clipping:** Caps gradient magnitude to prevent exploding gradients (the complementary problem).

**Exploding Gradient Problem:** When activation derivatives or weight magnitudes are > 1, repeated multiplication causes gradients to grow exponentially. This leads to numerically unstable updates (NaN values). Solutions include gradient clipping, proper weight initialization, and batch normalization.

## 1.5.5 Loss Functions

The loss function (cost function/objective function) quantifies how far the model's predictions are from the true values. Training minimizes this function.

**1. Mean Squared Error (MSE) — for Regression:**

$
L_{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$

Heavily penalizes large errors (due to squaring). Sensitive to outliers. Differentiable everywhere — gradient is straightforward.

**2. Mean Absolute Error (MAE) — for Regression:**

$
L_{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
$

More robust to outliers than MSE. Gradient is constant magnitude (not smooth at zero).

**3. Binary Cross-Entropy — for Binary Classification:**

$
L_{BCE} = -\frac{1}{n} \sum_{i=1}^{n} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)]
$

Used with sigmoid output. Penalizes confident wrong predictions very heavily (log of near-zero value is very large negative).

**4. Categorical Cross-Entropy — for Multi-Class Classification:**

$
L_{CCE} = -\sum_{i=1}^{K} y_i \log(\hat{y}_i)
$

where $K$ is the number of classes, $y_i$ is 1 for the correct class and 0 otherwise (one-hot encoding), and $\hat{y}_i$ is the predicted probability from softmax.

**5. Hinge Loss — for SVM-style classification:**

$
L_{hinge} = \sum_{i=1}^{n} \max(0, 1 - y_i \cdot \hat{y}_i)
$

Encourages a margin of separation. Zero loss when prediction is correct and confident.

| Loss Function      | Task                       | Output Activation | Sensitivity                 |
| :----------------- | :------------------------- | :---------------- | :-------------------------- |
| **MSE**            | Regression                 | Linear            | Sensitive to outliers       |
| **MAE**            | Regression                 | Linear            | Robust to outliers          |
| **Binary CE**      | Binary classification      | Sigmoid           | Penalizes wrong confidence  |
| **Categorical CE** | Multi-class classification | Softmax           | Standard for classification |
| **Hinge**          | Binary classification      | Linear / tanh     | Margin-based                |
