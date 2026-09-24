# 1. Foundation of Deep Neural Networks

# 1.1 Concept of AI, ML, DL and Neural Networks

> **Compare supervised, unsupervised, and self-supervised learning paradigms with suitable examples for each. Discuss how the choice of learning paradigm affects model design. (Fall 2025)**

**Artificial Intelligence (AI)** is the broadest field — it refers to any system designed to simulate human intelligence and perform tasks like reasoning, problem-solving, perception, and language understanding. AI approaches include rule-based systems, search algorithms, expert systems, and learning-based methods.

**Machine Learning (ML)** is a subset of AI where systems learn patterns from data rather than being explicitly programmed. ML uses statistical algorithms to identify structures in data and make predictions. Traditional ML requires manual feature engineering — humans must decide which features (e.g., edges, color histograms) to extract from raw data before feeding them to the model.

**Deep Learning (DL)** is a subset of ML that uses deep neural networks (networks with multiple hidden layers) to automatically learn hierarchical feature representations from raw data. The term "deep" refers to the depth (number of layers) of the network. DL eliminates manual feature engineering — the network learns low-level features (edges, textures) in early layers and high-level features (objects, concepts) in deeper layers.

**Neural Networks** are computational models inspired by the structure of biological neurons. A neural network consists of interconnected nodes (neurons) organized in layers. Each neuron receives inputs, applies weights and a bias, computes a weighted sum, passes it through an activation function, and produces an output. Neural networks are the architectural foundation of deep learning.

The relationship is hierarchical: AI ⊃ ML ⊃ DL, where DL is built upon neural network architectures.

| Aspect      | AI                          | ML                             | DL                                                    |
| :---------- | :-------------------------- | :----------------------------- | :---------------------------------------------------- |
| **Example** | Chess engine, expert system | Spam filter (SVM, Naive Bayes) | Image recognition (CNN), language model (Transformer) |

---

# 1.2 Learning Paradigms

> **Compare supervised, unsupervised, and self-supervised learning paradigms with suitable examples for each. Discuss how the choice of learning paradigm affects model design. (Fall 2025)**

**1. Supervised Learning:** The model is trained on labeled data — each input is paired with the correct output (ground truth). The model learns a mapping function f: X → Y by minimizing the error between predicted and actual outputs. Tasks include **classification** (predicting discrete labels, e.g., cat vs. dog) and **regression** (predicting continuous values, e.g., house price). Model design requires a labeled dataset, a loss function comparing predictions to labels (e.g., cross-entropy for classification, MSE for regression), and an output layer matching the task. Example: image classification using CNNs trained on ImageNet.

**2. Unsupervised Learning:** The model works with unlabeled data and discovers hidden structures, patterns, or groupings without human guidance. Tasks include **clustering** (grouping similar data, e.g., K-means, DBSCAN), **dimensionality reduction** (e.g., PCA, autoencoders), and **density estimation**. Model design uses reconstruction loss or distance-based objectives instead of label-based loss. Example: customer segmentation using K-means clustering on purchase behavior data.

**3. Semi-Supervised Learning:** Combines a small amount of labeled data with a large volume of unlabeled data. The labeled data provides direction while the unlabeled data helps the model learn the overall data distribution. Useful when labeling is expensive or time-consuming. Example: medical image classification where only a few hundred images are labeled by doctors but millions of unlabeled scans are available.

**4. Self-Supervised Learning:** The model generates its own supervisory signals from the input data by creating pretext tasks — predicting missing parts, future elements, or transformations of the data. No manual labels are needed. Example: BERT (masked language model — predicts masked words in a sentence), contrastive learning in vision (SimCLR — learns representations by contrasting augmented views of the same image). Model design requires a pretext task definition and typically a large encoder architecture.

**5. Reinforcement Learning (RL):** An agent learns by interacting with an environment, receiving rewards or penalties for actions, and optimizing cumulative long-term reward. There are no labeled input-output pairs; instead, the agent learns a policy π(s) → a that maps states to actions. The policy is the agent's strategy for choosing an action based on the current state. Model design requires defining the state space, action space, and reward function. Example: AlphaGo learning to play Go by self-play; robotic arm learning to grasp objects.

**6. Online Learning:** The model is updated incrementally as new data arrives, one sample (or mini-batch) at a time, rather than retraining on the entire dataset. Suitable for streaming data or when the dataset is too large to fit in memory. Example: recommendation systems updating user preferences in real-time.

**7. Active Learning:** The model proactively selects the most informative unlabeled data points and queries a human oracle to label them. This minimizes the total labeling effort while maximizing model improvement. Example: a text classifier that identifies the most ambiguous documents and asks a human to label only those.

**Impact on Model Design:** The choice of paradigm determines the loss function (label-based vs. reconstruction-based vs. reward-based), the output architecture (classification head vs. decoder vs. policy network), the data pipeline (labeled vs. unlabeled vs. environment interaction), and the training loop (single-pass vs. iterative interaction). _Example:_ A supervised classification model requires a discrete output head and cross-entropy loss over labeled data, whereas an RL agent requires a policy network outputting action probabilities and is trained via trial-and-error in a simulated environment using a reward signal.

---

# 1.3 Ethical Concerns and Responsible AI

> **Discuss the ethical concerns surrounding AI systems. How can principles of responsible AI be incorporated during the design and deployment of deep learning models? (Fall 2025)**

**1. Bias and Fairness:** AI models learn from historical data that often contains societal biases. If training data underrepresents certain demographics or reflects historical discrimination, the model inherits and amplifies these biases. Example: a hiring model trained on past recruitment data may systematically disadvantage women if historical hiring was biased. Mitigation: use diverse, representative training datasets; apply fairness-aware algorithms; conduct regular bias audits across protected groups (gender, race, age).

**2. Transparency and the "Black Box" Problem:** Deep neural networks are complex nonlinear systems whose internal decision-making is difficult for humans to interpret. This lack of transparency makes it hard to explain, audit, or justify AI-driven decisions — especially critical in healthcare, criminal justice, and finance. Mitigation: **use Explainable AI (XAI) techniques** such as SHAP (SHapley Additive exPlanations), LIME (Local Interpretable Model-agnostic Explanations), Grad-CAM (for visual explanations in CNNs), and **attention visualization** in Transformers.

**3. Privacy and Data Security:** DL requires vast amounts of data, raising concerns about informed consent, data ownership, unauthorized surveillance, and data breaches. Models can memorize sensitive training data and leak it during inference. Mitigation: use differential privacy (adding calibrated noise during training), federated learning (training on decentralized data without collecting it centrally), and data anonymization techniques.

**4. Accountability and Liability:** As AI systems become more autonomous, assigning responsibility for errors becomes difficult. When an autonomous vehicle causes an accident or a medical AI misdiagnoses a patient, it is unclear whether the developer, deployer, or user is liable. Mitigation: establish clear governance frameworks defining roles and responsibilities; maintain audit trails of model decisions; implement human-in-the-loop systems for high-stakes decisions.

**5. Environmental Impact:** Training large deep learning models consumes significant energy and produces substantial carbon emissions. Training GPT-3 consumed an estimated 1,287 MWh of electricity. Mitigation: use more efficient architectures, model compression (pruning, quantization, distillation), and renewable energy-powered data centers.

**6. Misuse and Dual Use:** DL can be used to create deepfakes, autonomous weapons, mass surveillance, and social manipulation tools. Mitigation: establish ethical review boards, implement usage policies, develop detection tools for synthetic media.

**Principles of Responsible AI:** Fairness (equitable treatment across groups), Transparency (explainable decisions), Privacy (data protection), Accountability (clear responsibility), Safety (robust and reliable systems), Human oversight (meaningful human control over AI decisions), and Societal benefit (AI should serve the common good). These principles should be embedded throughout the AI lifecycle — from data collection and model design to deployment and monitoring.

---

# 1.4 Perceptron and Multi-Layer Perceptron

> **Explain the role of activation functions in a neural network. Compare ReLU, Sigmoid, and Tanh in terms of their mathematical properties, advantages, and limitations. (Fall 2025)**

An Artificial Neural Network is a computational model inspired by the structure and functioning of biological neural networks in the brain. It consists of interconnected processing units (neurons) organized in layers that learn to map inputs to outputs by adjusting connection weights during training.

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
$
b \leftarrow b + \eta (t - y)
$

where $\eta$ is the learning rate. The weights are updated only when the prediction is incorrect ($t \neq y$).

**Limitation:** A single perceptron can only learn **linearly separable** functions. It can learn AND and OR gates but **cannot learn XOR** because XOR is not linearly separable — no single straight line can separate the two classes.

## 1.4.2 Multi-Layer Perceptron (MLP)

An MLP is a feedforward neural network with one or more hidden layers between the input and output layers. Each layer is fully connected to the next. MLPs can learn non-linear decision boundaries.

**Architecture:** An MLP is a **feedforward** neural network with three types of layers:

- **Input layer:** Receives raw input features. No computation occurs here. The number of neurons equals the number of input features.
- **Hidden layer(s):** One or more layers where actual computation happens. Each neuron is connected to every neuron in the adjacent layers (fully connected / dense). Each neuron computes a weighted sum of inputs, adds a bias, and applies a non-linear activation function.
- **Output layer:** Produces the final prediction. Its size and activation depend on the task. For binary classification, typically 1 neuron with sigmoid activation. For multi-class classification, n neurons (one per class) with softmax activation. For regression, 1 neuron with linear activation.

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

Activation functions introduce **non-linearity** into the network. Without them, any number of layers would collapse into a single linear transformation.

- **Sigmoid:** σ(z) = 1 / (1 + e^(−z)). Output range: (0, 1). Used in output layers for binary classification. Problem: vanishing gradients for very large or small z.
- **Tanh:** tanh(z) = (e^z − e^(−z)) / (e^z + e^(−z)). Output range: (−1, 1). Zero-centered, which can help optimization. Still suffers from vanishing gradients.
- **ReLU (Rectified Linear Unit):** f(z) = max(0, z). Most popular for hidden layers. Computationally efficient. Mitigates vanishing gradient. Problem: "dying ReLU" — neurons can permanently output 0 if they enter the negative region.
- **Leaky ReLU:** f(z) = z if z > 0, else αz (small α like 0.01). Fixes the dying ReLU problem by allowing a small gradient for negative inputs.
- **Softmax:** Converts a vector of values into a probability distribution: softmax(z_i) = e^(z_i) / Σ e^(z_j). Used in the output layer for multi-class classification.

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

## 1.5.3 Optimization Algorithms

**Gradient Descent (GD):** The fundamental optimization algorithm. It updates weights in the direction that reduces the loss function:

$
w \leftarrow w - \eta \frac{\partial L}{\partial w}
$

where $\eta$ is the learning rate and $\frac{\partial L}{\partial w}$ is the gradient of the loss with respect to weight $w$.

**Variants by batch size / (Ways to adjust weights):**

- **Batch GD:** Computes gradient using the entire training dataset per update. Stable but very slow for large datasets.
- **Stochastic GD (SGD):** Computes gradient using a single training sample per update. Noisy but fast; the noise can help escape local minima.
- **Mini-Batch GD:** Computes gradient using a small batch (e.g., 32, 64, 128 samples). Balances stability and speed. Most commonly used in practice.
- **Adam:** A smart optimizer that adjusts the learning rate automatically for each weight. It's the most popular choice today because it works well in most cases.

## 1.5.4 Backpropagation

> **Describe the backpropagation algorithm in detail. Derive the weight update rule using chain rule and explain how vanishing gradient problems arise. (Fall 2025)**

**Backpropagation** is how the neural network actually learns. After making a prediction (forward propagation), the network checks how wrong it was (using the loss function) and then goes **backward** through the layers to adjust the weights so that next time, the prediction will be better.

**How it works (step by step):**

1. Do forward propagation and calculate the loss (error).
2. Start from the output layer and calculate how much each weight contributed to the error.
3. Move backward through each layer, calculating the same thing for every weight. This uses a math technique called the **chain rule** — it's like figuring out how a small change in one weight at the beginning affects the final error at the end.
4. Adjust all the weights slightly to reduce the error: new weight = old weight − learning rate × gradient.

The **learning rate** controls how big the adjustment steps are. Too big and you might overshoot; too small and learning will be very slow.

**Forward Pass:** Input flows through the network layer by layer. At each neuron:

$
z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]} \quad \text{(weighted sum)}
$

$
a^{[l]} = \sigma(z^{[l]}) \quad \text{(activation)}
$

The final output $\hat{y}$ = $a^{[L]}$ is compared to the true label using the loss function $L$.

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
