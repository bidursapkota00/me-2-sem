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

### Vanishing Gradient Problem

The **vanishing gradient** problem happens during backpropagation when the gradients become **smaller and smaller as they are propagated toward the earlier layers** of a deep neural network.

Think of a deep network:

**Input → Layer 1 → Layer 2 → Layer 3 → ... → Output**

During backpropagation, each layer receives its gradient from the layer after it. The gradient is calculated using the **chain rule**, so many derivatives are multiplied together.

For example, imagine the gradient contains:

**0.5 × 0.5 × 0.5 × 0.5 × 0.5**

This becomes **0.03125**.

With many more layers, the value can become extremely close to **0**.

As a result:

1. The output layer gets a useful gradient.
2. The gradient becomes smaller as it moves backward.
3. Early layers receive an extremely small gradient.
4. Their weights barely change during training.
5. These layers learn **very slowly or effectively stop learning**.

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

---

---

---

# 2. Data Analytics and System Optimization

# 2.1 Data Analysis — Importance and Methods

> **Explain the bias-variance trade-off in deep learning. How do overfitting and underfitting manifest, and what techniques can be used to address each? (Fall 2025)**

**Data analysis** is the process of inspecting, cleaning, transforming, and modeling data to discover useful information, draw conclusions, and support decision-making. In deep learning, data analysis is performed before model building to understand the structure, quality, and distribution of the dataset.

**Importance of Data Analysis:**

- **Quality assurance:** Identifies missing values, duplicates, outliers, and inconsistencies that can degrade model performance.
- **Feature understanding:** Reveals data types, ranges, distributions, and inter-feature correlations that guide preprocessing choices.
- **Class distribution:** Detects class imbalance in classification tasks, which affects loss function selection and sampling strategy.
- **Data sufficiency:** Determines whether the dataset is large and diverse enough to train a deep network without severe overfitting.

**Methods of Data Analysis:**

**1. Descriptive Statistics:** Summarizes the central tendency (mean, median, mode), dispersion (variance, standard deviation, range), and shape (skewness, kurtosis) of each feature. Helps detect outliers and understand value ranges.

**2. Exploratory Data Analysis (EDA):** Uses visualizations — histograms (distribution of individual features), box plots (outlier detection), scatter plots (pairwise relationships), heatmaps (correlation matrices) — to reveal patterns, trends, and anomalies. EDA is typically the first step before any modeling.

**3. Correlation Analysis:** Measures linear (Pearson) or rank-based (Spearman) relationships between features. Highly correlated features may be redundant, and removing them reduces dimensionality without losing much information.

**4. Dimensionality Reduction:** Techniques like PCA (Principal Component Analysis) and t-SNE reduce high-dimensional data to fewer dimensions for visualization and noise removal while retaining the most important variance.

**5. Data Profiling:** Automated examination of data to determine data types, uniqueness, null percentages, and value distributions for each column. Tools like pandas-profiling generate comprehensive reports.

---

# 2.2 Data Augmentation and Normalization

> **Design a complete data processing pipeline for an image classification task. Include steps for data collection, augmentation, normalization, and validation strategy. (Fall 2025)**

## 2.2.1 Data Augmentation

**Data augmentation** artificially increases the size and diversity of the training dataset by applying label-preserving transformations to existing samples. It acts as an implicit regularizer — the model sees more variations, learns invariant features, and generalizes better.

**Why augmentation is needed:** Deep networks have millions of parameters and require large datasets to avoid overfitting. Collecting and labeling real data is expensive and time-consuming. Augmentation fills this gap by creating synthetic training examples from existing data.

**Image Augmentation Techniques:**

- **Geometric transformations:** Horizontal/vertical flipping, rotation (±15°, ±30°), random cropping, scaling (zoom in/out), shearing, translation (shifting image position).
- **Color/Photometric transformations:** Brightness adjustment, contrast change, saturation modification, hue shift, adding Gaussian noise, color jittering.
- **Spatial transformations:** Elastic deformation (locally distorts the image), cutout/random erasing (masks out random rectangular regions, forcing the model to learn from partial information).

**Text Augmentation:** Synonym replacement, random insertion/deletion/swap of words, back-translation (translate to another language and back).

**Audio Augmentation:** Time stretching, pitch shifting, adding background noise, time masking, frequency masking (SpecAugment).

## 2.2.2 Normalization

**Normalization** scales input features or intermediate activations to a standard range, ensuring stable and faster training.

**Why normalization is needed:** Features with vastly different scales (e.g., pixel values 0–255 vs. a binary feature 0–1) cause the loss surface to be elongated, making gradient descent oscillate and converge slowly. Normalization creates a more spherical loss surface, enabling larger learning rates and faster convergence.

**Types of Data Normalization:**

**1. Min-Max Normalization:** Scales values to [0, 1]:

$
x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
$

**2. Z-Score Standardization:** Transforms to zero mean and unit variance:

$
x' = \frac{x - \mu}{\sigma}
$

where $\mu$ is the mean and $\sigma$ is the standard deviation of the feature. This is the most commonly used method for neural network inputs.

**3. Batch Normalization (BN):** Normalizes the activations within each mini-batch at each layer during training.

**4. Layer Normalization:** Normalizes across all features within a single sample (not across the batch). Used in RNNs and Transformers where batch statistics are unreliable due to variable sequence lengths.

**5. Instance Normalization:** Normalizes each sample and each channel independently. Used in style transfer tasks.

**6. Group Normalization:** Divides channels into groups and normalizes within each group. Works well with small batch sizes where Batch Normalization fails.

---

# 2.3 Data Processing Pipeline

> **Design a complete data processing pipeline for an image classification task. Include steps for data collection, augmentation, normalization, and validation strategy. (Fall 2025)**

A **data processing pipeline** is an organized sequence of steps that transforms raw data into a format suitable for training a deep learning model. A well-designed pipeline ensures reproducibility, efficiency, and data quality.

**Complete Pipeline for Image Classification:**

**Step 1 — Data Collection:** Gather images from public datasets (ImageNet, CIFAR-10), web scraping, APIs, or manual capture. Ensure diversity in classes, backgrounds, lighting conditions, and viewpoints. Aim for balanced class distribution.

**Step 2 — Data Cleaning:** Remove corrupted files, duplicate images, and mislabeled samples. Verify image format consistency (JPEG, PNG). Handle missing labels. Remove irrelevant or low-quality images (blurry, occluded).

**Step 3 — Data Splitting:** Divide the dataset into three disjoint subsets:

- **Training set (70–80%):** Used to train the model — the network learns parameters from this data.
- **Validation set (10–15%):** Used during training to tune hyperparameters and monitor overfitting. Not used for weight updates.
- **Test set (10–15%):** Used only once after training is complete to evaluate final model performance. Never used during training or tuning.

The split must be stratified (each subset preserves the class distribution of the full dataset) and random. Data leakage (test data appearing in training) must be strictly avoided.

**Step 4 — Data Augmentation:** Apply transformations (flipping, rotation, cropping, color jitter, etc.) to the training set only. The validation and test sets must remain unaugmented to provide an unbiased performance estimate. Augmentation is typically applied on-the-fly during training (not stored) to save disk space and increase randomness.

**Step 5 — Normalization/Preprocessing:** Resize all images to a fixed resolution (e.g., 224×224 for ResNet). Normalize pixel values — either scale to [0, 1] by dividing by 255, or standardize using the ImageNet mean ([0.485, 0.456, 0.406]) and standard deviation ([0.229, 0.224, 0.225]) per channel. Apply the same normalization parameters (computed from training set) to validation and test sets.

**Step 6 — Data Loading:** Use efficient data loaders (e.g., PyTorch DataLoader, TensorFlow tf.data) with batching, shuffling (training set only), prefetching, and parallel data loading (multiple workers) to keep the GPU fully utilized.

**Step 7 — Validation Strategy:** Evaluate the model on the validation set after every epoch. Track validation loss and accuracy. Use early stopping (halt training when validation loss stops improving). After selecting the final model, evaluate on the test set once.

---

# 2.4 Data Security and Concerns

Deep learning models require large volumes of data, often containing sensitive personal information. This raises critical security and privacy concerns throughout the data lifecycle.

**1. Data Privacy:** Training data may contain personally identifiable information (PII) — names, medical records, financial data, biometric data. Unauthorized access or data breaches expose individuals to identity theft and discrimination. Regulations like GDPR (EU) and CCPA (California) mandate strict handling of personal data, including the right to data deletion.

**2. Data Poisoning Attacks:** An adversary deliberately introduces malicious samples into the training dataset to corrupt the model's learned behavior. A backdoor attack embeds a trigger pattern (e.g., a small patch) in training images, causing the model to misclassify any input containing the trigger at inference time while performing normally on clean inputs.

**3. Model Inversion Attacks:** An attacker queries a trained model and uses the outputs to reconstruct the training data. For example, given a facial recognition model, the attacker can generate approximate face images of individuals in the training set.

**4. Membership Inference Attacks:** An adversary determines whether a specific data point was used in the training set by analyzing the model's confidence scores. Overfitted models are more vulnerable because they respond differently to training vs. unseen data.

**5. Differential Privacy:** A mathematical framework that provides formal privacy guarantees. During training, calibrated random noise is added to gradients (DP-SGD), ensuring that the model's output is statistically indistinguishable whether or not any single individual's data was included. The privacy budget $\epsilon$ controls the trade-off — smaller $\epsilon$ gives stronger privacy but may reduce model accuracy.

**6. Federated Learning:** A decentralized training paradigm where the model is trained across multiple devices (phones, hospitals, edge devices) without centralizing the data. Each device trains locally on its own data and sends only the model updates (gradients/weights) to a central server for aggregation. Raw data never leaves the device.

**7. Data Anonymization:** Techniques like k-anonymity, l-diversity, and data masking remove or generalize identifying attributes before using data for training.

**8. Secure Computation:** Homomorphic encryption allows computation on encrypted data without decryption. Secure multi-party computation enables multiple parties to jointly train a model without revealing their individual data.

---

# 2.5 Model Evaluation and Cross-Validation

> **Explain the bias-variance trade-off in deep learning. How do overfitting and underfitting manifest, and what techniques can be used to address each? (Fall 2025)**

## 2.5.1 Evaluation Metrics

**For Classification Tasks:**

**Confusion Matrix:** A table that compares predicted labels against actual labels. For binary classification:

|                     | Predicted Positive  | Predicted Negative  |
| :------------------ | :------------------ | :------------------ |
| **Actual Positive** | True Positive (TP)  | False Negative (FN) |
| **Actual Negative** | False Positive (FP) | True Negative (TN)  |

**Accuracy:** Overall fraction of correct predictions:

$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$

Misleading when classes are imbalanced (e.g., 95% accuracy on a dataset where 95% belong to one class is trivial).

**Precision:** Of all samples predicted positive, how many are actually positive:

$
\text{Precision} = \frac{TP}{TP + FP}
$

High precision is critical when the cost of false positives is high (e.g., spam detection — marking a legitimate email as spam).

**Recall (Sensitivity):** Of all actual positives, how many are correctly identified:

$
\text{Recall} = \frac{TP}{TP + FN}
$

High recall is critical when the cost of false negatives is high (e.g., cancer detection — missing a positive case).

**F1 Score:** Harmonic mean of precision and recall, balancing both:

$
F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
$

**ROC Curve and AUC:** The Receiver Operating Characteristic curve plots True Positive Rate (recall) vs. False Positive Rate at various classification thresholds. AUC (Area Under the Curve) summarizes overall performance — AUC = 1.0 is perfect, AUC = 0.5 is random.

**For Regression Tasks:**

- **MSE (Mean Squared Error):** $\frac{1}{n} \sum (y_i - \hat{y}_i)^2$ — penalizes large errors heavily.
- **MAE (Mean Absolute Error):** $\frac{1}{n} \sum |y_i - \hat{y}_i|$ — more robust to outliers.
- **R² Score:** Proportion of variance explained by the model (1.0 is perfect fit, 0 is baseline).

## 2.5.2 Cross-Validation

**Hold-Out Validation:** Split data into training and validation sets (e.g., 80/20). Simple but the performance estimate depends heavily on which specific samples fall into which split.

**K-Fold Cross-Validation:** Divides the dataset into K equal folds. The model is trained K times — each time, one fold is used as the validation set and the remaining K−1 folds are used for training. The final performance is the average across all K runs.

- Typical value: K = 5 or K = 10.
- Every data point is used for validation exactly once.
- Provides a more robust and less biased performance estimate than a single hold-out.

**Stratified K-Fold:** Ensures each fold preserves the class distribution of the full dataset. Essential for imbalanced datasets.

**Leave-One-Out Cross-Validation (LOOCV):** K = N (number of samples). Each sample is used once as the validation set. Provides an almost unbiased estimate but is computationally prohibitive for large datasets.

**Cross-validation in deep learning:** Due to the high computational cost of training deep networks, K-fold cross-validation is often replaced by a single train/validation/test split. Cross-validation is more common in traditional ML or when the dataset is small.

---

# 2.6 Hyperparameter Optimization

> **Compare at least four hyperparameter optimization strategies (e.g., grid search, random search, Bayesian optimization). Discuss which is most suitable for large-scale deep learning models and why. (Fall 2025)**

**Hyperparameters** are configuration settings that are fixed before training begins and are not learned from data. They control the learning process and model architecture. Examples: learning rate, batch size, number of layers, number of neurons per layer, dropout rate, weight decay coefficient, optimizer choice.

**Parameters vs. Hyperparameters:**

| Aspect           | Parameters                   | Hyperparameters                    |
| :--------------- | :--------------------------- | :--------------------------------- |
| **Learned from** | Training data (via backprop) | Set before training                |
| **Examples**     | Weights, biases              | Learning rate, batch size, dropout |
| **Updated by**   | Optimizer (SGD, Adam)        | Human or search algorithm          |
| **Stored in**    | Model file                   | Configuration file                 |

## 2.6.1 Grid Search

Defines a discrete set of values for each hyperparameter and evaluates every possible combination exhaustively.

- Example: learning rate ∈ {0.001, 0.01, 0.1}, batch size ∈ {32, 64, 128} → 3 × 3 = 9 combinations, each trained and evaluated.
- **Advantage:** Thorough — guarantees that the best combination within the grid is found.
- **Disadvantage:** Computationally explosive — the number of evaluations grows exponentially with the number of hyperparameters (curse of dimensionality). With 5 hyperparameters and 4 values each, 4⁵ = 1024 evaluations are needed.

## 2.6.2 Random Search

Samples hyperparameter combinations randomly from specified distributions for a fixed budget of evaluations.

- Instead of trying every point on a grid, it randomly selects N configurations and evaluates them.
- **Advantage:** More efficient than grid search — empirically shown (Bergstra & Bengio, 2012) that random search finds good configurations faster because it samples more distinct values of each hyperparameter. In grid search, if one hyperparameter is unimportant, many evaluations are wasted on varying it.
- **Disadvantage:** No guarantee of finding the optimal combination; results depend on the sampling budget.

## 2.6.3 Bayesian Optimization

Builds a probabilistic surrogate model (typically a Gaussian Process) of the objective function and uses it to intelligently select the next hyperparameter configuration to evaluate.

**Working:**

1. Evaluate a few random initial configurations.
2. Fit a surrogate model to the observed (configuration, performance) pairs.
3. Use an acquisition function (e.g., Expected Improvement) to select the next configuration that maximizes the expected improvement over the current best.
4. Train the model with the selected configuration, observe the result, update the surrogate model, and repeat.

- **Advantage:** Sample-efficient — finds good configurations with fewer evaluations by learning from past results. The surrogate model captures the relationship between hyperparameters and performance.
- **Disadvantage:** Computationally expensive to update the surrogate model as the number of observations grows. Does not parallelize easily. Less effective in very high-dimensional spaces.

## 2.6.4 Halving / Successive Halving

Allocates a small budget (few epochs) to a large number of random configurations, evaluates them, discards the worst-performing half, doubles the budget for the surviving configurations, and repeats until one configuration remains.

- **Advantage:** Efficient early elimination of bad configurations. Allocates more resources to promising candidates.
- **Disadvantage:** Early performance may not correlate with final performance (some models need more training to show their potential).

## 2.6.5 Hyperband

Combines random search with successive halving by running multiple rounds of successive halving with different initial budgets, balancing the exploration-exploitation trade-off automatically.

- **Advantage:** Robust — does not require tuning the trade-off between number of configurations and budget per configuration.

## 2.6.6 Population-Based Training (PBT)

Trains a population of models in parallel. Periodically, poorly performing models copy the weights and hyperparameters of better-performing models (exploit) and then perturb the hyperparameters (explore). This allows hyperparameters to be adapted during training rather than fixed.

**Comparison:**

| Strategy                  | Evaluations Needed     | Intelligence  | Parallelizable | Best For                        |
| :------------------------ | :--------------------- | :------------ | :------------- | :------------------------------ |
| **Grid Search**           | Exponential            | None (brute)  | Yes            | Few hyperparameters, small grid |
| **Random Search**         | Fixed budget           | None (random) | Yes            | Moderate search spaces          |
| **Bayesian Optimization** | Low (sample-efficient) | High (learns) | Limited        | Expensive-to-evaluate models    |
| **Hyperband**             | Adaptive               | Moderate      | Yes            | Large-scale deep learning       |
| **PBT**                   | Adaptive               | High          | Yes            | Very large-scale training       |

**Most suitable for large-scale deep learning:** Hyperband and Population-Based Training are most suitable because they efficiently allocate compute by eliminating poor configurations early and adapting hyperparameters dynamically. Bayesian optimization is effective when each evaluation is expensive but does not scale well to highly parallel setups. Grid search is impractical due to exponential cost. Random search is a strong baseline but lacks the adaptive resource allocation of Hyperband.

---

# 2.7 Overfitting, Underfitting, and Bias-Variance Trade-Off

> **Explain the bias-variance trade-off in deep learning. How do overfitting and underfitting manifest, and what techniques can be used to address each? (Fall 2025)**

## 2.7.1 Bias-Variance Trade-Off

The **total error** of a model on unseen data (generalization error) can be decomposed into three components:

$
\text{Total Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Noise}
$

**Bias** is the error due to overly simplistic assumptions in the model. A high-bias model fails to capture the true relationship in the data. It systematically deviates from the correct output. Example: fitting a linear model to highly non-linear data.

**Variance** is the error due to the model's sensitivity to fluctuations in the training data. A high-variance model fits the training data very closely (including noise) and produces very different predictions when trained on different subsets of data.

**Irreducible noise** is the inherent randomness in the data that no model can eliminate (e.g., measurement errors, inherent stochasticity).

**The trade-off:** As model complexity increases, bias decreases (the model can capture more complex patterns) but variance increases (the model becomes more sensitive to training data). The optimal model minimizes the sum of bias² and variance.

| Aspect      | High Bias              | High Variance           |
| :---------- | :--------------------- | :---------------------- |
| **Model**   | Too simple             | Too complex             |
| **Fits**    | Neither train nor test | Train well, test poorly |
| **Problem** | Underfitting           | Overfitting             |
| **Example** | Linear model for XOR   | Deep net on 100 samples |

## 2.7.2 Overfitting

**Overfitting** occurs when the model learns the training data too well — it memorizes the noise and specific patterns of the training set rather than learning the generalizable underlying relationship. The model achieves very low training error but high validation/test error.

**Signs of overfitting:**

- Training loss continues to decrease while validation loss starts increasing.
- Large gap between training accuracy and validation accuracy.
- The model performs exceptionally on training data but fails on new, unseen data.

**Techniques to address overfitting:**

**1. Regularization — L1 and L2:**

- **L2 Regularization (Weight Decay):** Adds a penalty proportional to the square of the weights to the loss function:

$
L_{\text{total}} = L_{\text{original}} + \lambda \sum_{i} w_i^2
$

This discourages large weights, smoothing the learned function. The hyperparameter $\lambda$ controls the regularization strength.

- **L1 Regularization (Lasso):** Adds a penalty proportional to the absolute value of weights:

$
L_{\text{total}} = L_{\text{original}} + \lambda \sum_{i} |w_i|
$

L1 drives some weights to exactly zero, producing sparse models and performing implicit feature selection.

**2. Dropout:** During each training iteration, randomly sets a fraction p (typically 0.2–0.5) of neuron activations to zero. This prevents neurons from co-adapting — each neuron must learn useful features independently, since it cannot rely on any specific other neuron being present. At test time, all neurons are active but outputs are scaled by (1 − p) to maintain expected values. Dropout can be interpreted as training an ensemble of 2^n sub-networks (where n is the number of neurons).

**3. Early Stopping:** Monitor the validation loss during training. Stop training when the validation loss has not improved for a specified number of epochs (patience). This prevents the model from continuing to memorize the training data after it has already learned the generalizable patterns.

**4. Data Augmentation:** Increasing the effective size and diversity of the training data through transformations (as described in Section 2.2.1) reduces overfitting by exposing the model to more variations.

**5. Reducing Model Complexity:** Use fewer layers, fewer neurons per layer, or simpler architectures. A smaller model has fewer parameters and is less capable of memorizing noise.

**6. Batch Normalization:** Acts as a mild regularizer because the normalization introduces noise through mini-batch statistics, which slightly varies from batch to batch.

## 2.7.3 Underfitting

**Underfitting** occurs when the model is too simple to capture the underlying patterns in the data. Both training and validation errors are high.

**Signs of underfitting:**

- High training error (the model cannot even fit the training data well).
- Training and validation errors are both high and close to each other.

**Techniques to address underfitting:**

- **Increase model complexity:** Add more layers, more neurons, or switch to a more expressive architecture.
- **Train longer:** The model may not have converged — increase the number of epochs.
- **Reduce regularization:** If regularization is too strong (large $\lambda$, high dropout), the model is overly constrained.
- **Feature engineering:** Provide more informative features or use better data representations.
- **Decrease learning rate:** A learning rate that is too high may cause the optimizer to overshoot minima, preventing convergence.

## 2.7.4 Bias-Variance in Deep Learning

Deep neural networks have a unique relationship with the bias-variance trade-off. Classical theory predicts that very complex models (like deep networks with millions of parameters) should overfit badly. However, in practice, deep networks often generalize well due to **implicit regularization** from:

- **SGD with mini-batches:** The noise in stochastic gradient descent acts as a regularizer, preventing the model from settling into sharp minima.
- **Overparameterization:** Modern deep networks operate in the "interpolation regime" where they can fit the training data perfectly yet still generalize — a phenomenon described by the **double descent curve**. Beyond the classical U-shaped bias-variance curve, increasing model size past the interpolation threshold causes test error to decrease again.
- **Architecture choices:** Skip connections (ResNet), batch normalization, and weight sharing (CNNs) provide structural regularization.

The practical recipe for deep learning: use a large model (low bias), then control variance through dropout, weight decay, data augmentation, and early stopping.

---

---

---

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

| Feature            | Vanilla RNN       | LSTM                      | GRU                    | Bi-RNN                     |
| :----------------- | :---------------- | :------------------------ | :--------------------- | :------------------------- |
| **Gates**          | None              | 3 (forget, input, output) | 2 (reset, update)      | Depends on base unit       |
| **Memory**         | Hidden state only | Cell state + hidden       | Hidden state only      | Forward + backward states  |
| **Parameters**     | Fewest            | Most (~4× vanilla)        | Moderate (~3× vanilla) | 2× base unit               |
| **Long-range**     | Poor              | Excellent                 | Good                   | Excellent (with LSTM/GRU)  |
| **Training speed** | Fastest           | Slowest                   | Moderate               | ~2× base unit              |
| **Best for**       | Short sequences   | Complex long sequences    | General sequences      | Tasks needing full context |

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

| Feature                  | RNN/LSTM/GRU                          | Transformer                    |
| :----------------------- | :------------------------------------ | :----------------------------- |
| **Processing**           | Sequential (step by step)             | Parallel (all tokens at once)  |
| **Training speed**       | Slow (cannot parallelize)             | Fast (fully parallelizable)    |
| **Long-range deps**      | Struggles (vanishing gradient)        | Excellent (direct attention)   |
| **Memory mechanism**     | Hidden state (bottleneck)             | Attention over all positions   |
| **Position info**        | Implicit (from sequential processing) | Explicit (positional encoding) |
| **Complexity per layer** | $O(T \cdot d^2)$                      | $O(T^2 \cdot d)$               |
| **Inductive bias**       | Strong (sequential)                   | Weak (needs more data)         |

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

---

---

# 4. Computer Vision

# 4.1 CNN Fundamentals — Properties of CNN, CNN vs MLP

> **Explain the fundamental differences between CNNs and MLPs for image processing tasks. Why are CNNs preferred for visual data, and what properties make them effective? (Fall 2025)**

A **Convolutional Neural Network (CNN)** is a specialized neural network designed to process data with grid-like topology — most notably images (2D grids of pixels) and video (3D grids). CNNs exploit the spatial structure of visual data through three key properties that MLPs lack.

**1. Local Connectivity (Sparse Interactions):** In an MLP, every neuron in a layer is connected to every neuron in the previous layer (fully connected). For a 224×224×3 image, the input has 150,528 values — a single hidden neuron in an MLP would need 150,528 weights. In a CNN, each neuron connects only to a small local region of the input (e.g., a 3×3 patch), called the **receptive field**. This drastically reduces parameters and captures the fact that nearby pixels are more correlated than distant ones.

**2. Weight Sharing (Parameter Sharing):** In an MLP, each connection has its own unique weight. In a CNN, the same filter (set of weights) slides across the entire input — the same 3×3 filter is applied to every spatial position. If a feature (e.g., a vertical edge) is useful at one location, it is useful everywhere. A single 3×3 filter on 3-channel input has only 3×3×3 + 1 = 28 parameters, regardless of image size.

**3. Translation Equivariance:** Because the same filter is applied everywhere, if an object shifts in the image, the corresponding feature map shifts by the same amount. Pooling layers further provide **translation invariance** — the network detects the presence of a feature regardless of its exact position.

**Why MLPs fail for images:**

- **Enormous parameter count:** A 224×224×3 image with a hidden layer of 1000 neurons requires 150 million weights in the first layer alone — leading to severe overfitting and impractical computation.
- **No spatial awareness:** Flattening a 2D image into a 1D vector destroys spatial relationships between pixels.
- **No shift invariance:** An MLP trained to recognize a cat in the top-left must learn the same pattern independently for every position.

| Property              | MLP                                | CNN                                  |
| :-------------------- | :--------------------------------- | :----------------------------------- |
| **Connectivity**      | Fully connected                    | Locally connected (sparse)           |
| **Weight sharing**    | No (unique weights per connection) | Yes (shared filters)                 |
| **Spatial structure** | Input flattened to 1D vector       | Preserves 2D/3D structure            |
| **Parameters**        | Very high                          | Very low (due to sharing)            |
| **Translation**       | Not invariant                      | Equivariant (invariant with pooling) |
| **Suitable for**      | Tabular / structured data          | Images, video, spatial data          |

---

# 4.2 Convolution, Pooling, Padding, Flattening, Fully Connected Layer

## 4.2.1 Convolution Operation

The **convolution** operation slides a small learnable filter (kernel) across the input, computing the element-wise product and sum at each position to produce a **feature map** (activation map).

For a 2D input $I$ and kernel $K$ of size $k \times k$:

$
(I * K)[i, j] = \sum_{m=0}^{k-1} \sum_{n=0}^{k-1} I[i+m, j+n] \cdot K[m, n]
$

**Output size formula:** For input size $n$, kernel size $k$, padding $p$, and stride $s$:

$
\text{output size} = \left\lfloor \frac{n - k + 2p}{s} \right\rfloor + 1
$

**Stride:** The step size by which the filter moves. Stride = 1 moves one pixel at a time; stride = 2 skips every other position, reducing the output size by half.

**Multi-channel convolution:** For an input with $C$ channels (e.g., RGB with $C=3$), each filter has dimensions $k \times k \times C$. The filter produces a single 2D feature map. Multiple filters (e.g., 64 filters) produce 64 feature maps, giving an output with 64 channels.

## 4.2.2 Padding

**Padding** adds extra pixels (usually zeros) around the border of the input before convolution.

- **Valid padding (no padding):** $p = 0$. The output shrinks with each convolution. Pixels at the edges contribute to fewer output values than center pixels.
- **Same padding:** $p = \lfloor k/2 \rfloor$. The output has the same spatial dimensions as the input. Ensures all input pixels are treated equally.

## 4.2.3 Pooling

**Pooling** reduces the spatial dimensions of feature maps, decreasing computational cost, reducing parameters, and providing a degree of translation invariance.

**Max Pooling:** Takes the maximum value in each pooling window. Retains the strongest activation (most prominent feature). Most commonly used — typical configuration: 2×2 window, stride 2 (halves spatial dimensions).

**Average Pooling:** Takes the mean of values in each pooling window. Retains average feature presence. Smoother than max pooling.

**Global Average Pooling (GAP):** Computes a single average value for each feature map across the entire spatial extent. Converts a feature map of size $H \times W$ to a single value. Eliminates the need for fully connected layers before the output — reduces parameters dramatically and prevents overfitting. Used in modern architectures like GoogLeNet and ResNet.

## 4.2.4 Flattening

**Flattening** reshapes the 3D feature map (height × width × channels) into a 1D vector. This is the bridge between convolutional layers and fully connected layers. A feature map of size 7×7×512 is flattened to a vector of 25,088 elements.

## 4.2.5 Fully Connected (Dense) Layer

After convolution and pooling extract spatial features, one or more **fully connected layers** combine these features for the final prediction. Every neuron is connected to every element of the input vector. The output layer uses softmax (multi-class classification) or sigmoid (binary classification) activation.

**Typical CNN pipeline:** Input → [Conv → ReLU → Pool] × N → Flatten → FC → FC → Softmax → Output

---

# 4.3 Convolution Variants

> **Describe five convolution variants — standard, transpose, dilated, separable, and deformable — and provide a real-world use case where each variant would be most appropriate. (Fall 2025)**

## 4.3.1 Standard Convolution

The basic convolution described in Section 4.2.1. A $k \times k \times C_{in}$ filter slides across the input, producing one feature map. $C_{out}$ filters produce $C_{out}$ feature maps. Computational cost: $O(k^2 \cdot C_{in} \cdot C_{out} \cdot H \cdot W)$.

**Use case:** General-purpose feature extraction in all CNN architectures (classification, detection, segmentation).

## 4.3.2 Transpose Convolution (Deconvolution)

**Transpose convolution** performs the reverse spatial transformation of a standard convolution — it **upsamples** the feature map to a larger spatial resolution. It inserts zeros between input elements and then applies a standard convolution, or equivalently, maps each input pixel to a $k \times k$ region in the output.

Output size: $\text{output} = (n - 1) \times s - 2p + k$

**Important:** Transpose convolution uses **learnable** upsampling (the weights are trained), unlike fixed methods like bilinear interpolation.

**Artifact:** Can produce checkerboard patterns due to uneven overlap when stride > 1.

**Use case:** Decoder in semantic segmentation networks (U-Net, FCN) to recover spatial resolution; generator in GANs to upsample from latent vectors to full images.

## 4.3.3 Dilated (Atrous) Convolution

**Dilated convolution** inserts gaps (holes) between kernel elements, expanding the receptive field without increasing the number of parameters or reducing spatial resolution.

A dilation rate $r$ means the kernel elements are spaced $r$ apart. A 3×3 kernel with dilation rate 2 has an effective receptive field of 5×5 but still has only 9 parameters.

$
(I *_r K)[i, j] = \sum_{m} \sum_{n} I[i + r \cdot m, j + r \cdot n] \cdot K[m, n]
$

**Advantage:** Captures multi-scale context without pooling (which loses spatial information) and without increasing parameters.

**Use case:** Semantic segmentation (DeepLab) where dense, pixel-level predictions require large receptive fields while maintaining high spatial resolution.

## 4.3.4 Separable Convolution

**Depthwise Separable Convolution** decomposes a standard convolution into two steps:

**Step 1 — Depthwise Convolution:** Applies a single $k \times k$ filter to each input channel independently. $C_{in}$ filters produce $C_{in}$ feature maps. No cross-channel interaction.

**Step 2 — Pointwise Convolution:** Applies a $1 \times 1 \times C_{in}$ convolution to combine information across channels. $C_{out}$ pointwise filters produce $C_{out}$ output channels.

**Cost comparison:** Standard convolution: $k^2 \cdot C_{in} \cdot C_{out}$. Depthwise separable: $k^2 \cdot C_{in} + C_{in} \cdot C_{out}$. Reduction factor ≈ $1/C_{out} + 1/k^2$. For a 3×3 filter with 256 output channels, this is ~8–9× fewer computations.

**Use case:** Lightweight mobile architectures (MobileNet, Xception) where computational efficiency is critical for deployment on edge devices and smartphones.

## 4.3.5 Grouped Convolution

**Grouped convolution** divides the input channels into $G$ groups, performs independent convolution within each group, and concatenates the outputs. Each group has $C_{in}/G$ input channels and $C_{out}/G$ filters.

**Cost reduction:** $G \times$ fewer parameters and computations compared to standard convolution.

**Use case:** Parallel GPU training (originally in AlexNet, which split channels across 2 GPUs); efficient architectures (ResNeXt uses 32 groups for improved accuracy with similar cost).

## 4.3.6 Deformable Convolution

**Deformable convolution** learns 2D offsets for each sampling position in the kernel, allowing the grid to deform and adapt to the geometric shape of objects.

$
y[p_0] = \sum_{p_n \in R} w[p_n] \cdot x[p_0 + p_n + \Delta p_n]
$

where $\Delta p_n$ is the learned offset for position $p_n$. Since the offset positions are typically fractional, **bilinear interpolation** is used to sample the input.

The offsets are produced by a separate convolutional layer applied to the same input feature map — making the deformation data-dependent and learnable end-to-end.

**Use case:** Object detection and instance segmentation where objects have irregular shapes, varying scales, and non-rigid deformations (e.g., detecting humans in different poses).

---

# 4.4 CNN Architectures

> **Trace the evolution of CNN architectures from AlexNet to DenseNet. Highlight the key architectural innovation introduced in each (VGG, GoogLeNet, ResNet, DenseNet). (Fall 2025)**

## 4.4.1 AlexNet (Krizhevsky et al., 2012)

**Innovation:** Demonstrated that deep CNNs trained on GPUs could dramatically outperform traditional computer vision methods. Won ImageNet 2012 with a top-5 error of 15.3% (vs. 26.2% for the runner-up).

**Architecture:** 5 convolutional layers + 3 fully connected layers. ~60 million parameters.

**Key contributions:**

- **ReLU activation:** First large-scale use of ReLU instead of tanh/sigmoid — 6× faster training.
- **GPU training:** Split the network across 2 GPUs for parallel computation.
- **Dropout:** Applied dropout (p=0.5) in fully connected layers to reduce overfitting.
- **Data augmentation:** Random cropping, horizontal flipping, and PCA-based color augmentation.
- **Local Response Normalization (LRN):** Normalized activations across adjacent channels (later replaced by Batch Normalization).

## 4.4.2 VGGNet (Simonyan & Zisserman, 2014)

**Innovation:** Showed that network depth is critical for performance by using a very simple, uniform architecture.

**Architecture:** VGG-16 (16 layers) and VGG-19 (19 layers). ~138 million parameters.

**Key contribution — Small filters, more depth:** Replaced large filters (11×11 in AlexNet) with stacks of 3×3 filters. Two 3×3 convolutions have the same receptive field as one 5×5 but with fewer parameters ($2 \times 3^2 = 18$ vs. $5^2 = 25$) and more non-linearity (two ReLU activations instead of one). Three 3×3 layers = one 7×7 layer.

**Limitation:** Very high parameter count (mostly from fully connected layers) — memory-intensive.

## 4.4.3 GoogLeNet / Inception (Szegedy et al., 2014)

**Innovation:** Introduced the **Inception module** — "go wider, not just deeper." Won ImageNet 2014 with only ~5 million parameters (27× fewer than VGG).

**Inception Module:** Applies multiple filter sizes in parallel within the same layer:

- 1×1 convolution (captures channel correlations)
- 3×3 convolution (captures small spatial patterns)
- 5×5 convolution (captures larger spatial patterns)
- 3×3 max pooling (captures dominant features)

Outputs are concatenated along the channel dimension.

**1×1 convolution (bottleneck):** Used before 3×3 and 5×5 convolutions to reduce the number of input channels, dramatically cutting computational cost. A 1×1 conv with $C_{out}$ filters on $C_{in}$-channel input reduces the channel dimension from $C_{in}$ to $C_{out}$.

**Auxiliary classifiers:** Added at intermediate layers to inject gradient signal deeper into the network, combating vanishing gradients (removed at inference).

**Global Average Pooling:** Replaced fully connected layers with GAP, reducing parameters significantly.

## 4.4.4 ResNet (He et al., 2015)

**Innovation:** Introduced **skip connections (residual connections)** that enable training of extremely deep networks (50, 101, 152 layers). Won ImageNet 2015 with 3.57% top-5 error (surpassing human performance ~5.1%).

**The degradation problem:** Simply stacking more layers beyond a certain depth causes training accuracy to decrease (not just test accuracy) — deeper networks paradoxically perform worse. This is not overfitting but an optimization difficulty — deeper networks are harder to optimize.

**Residual Block:** Instead of learning the desired mapping $H(x)$ directly, the network learns the residual $F(x) = H(x) - x$:

$
H(x) = F(x) + x
$

The input $x$ is added to the output of the convolutional layers via a **shortcut connection** (identity mapping). If the optimal mapping is close to identity, it is easier to learn $F(x) \approx 0$ than to learn $H(x) \approx x$ from scratch.

**Gradient flow:** During backpropagation, the gradient through a residual block is:

$
\frac{\partial L}{\partial x} = \frac{\partial L}{\partial H} \cdot \left(1 + \frac{\partial F}{\partial x}\right)
$

The "1" term ensures the gradient flows directly through the skip connection without vanishing, even in very deep networks.

**Bottleneck block (for deeper ResNets):** Uses 1×1 → 3×3 → 1×1 convolutions. The 1×1 layers reduce and then restore dimensionality, keeping the 3×3 layer computationally efficient.

## 4.4.5 DenseNet (Huang et al., 2016)

**Innovation:** Introduced **dense connections** — each layer receives feature maps from all preceding layers within a block and passes its own feature maps to all subsequent layers.

**Dense Block:** For a block with $L$ layers, layer $l$ receives the concatenation of feature maps from layers $0, 1, ..., l-1$:

$
x_l = H_l([x_0; x_1; ...; x_{l-1}])
$

where $[...]$ denotes concatenation. This differs from ResNet, which uses addition.

**Growth Rate ($k$):** Each layer produces $k$ feature maps. Layer $l$ has $k_0 + k \times (l-1)$ input channels (where $k_0$ is the initial channels). Typical $k$ = 12 or 32 — much smaller than traditional channel counts.

**Transition Layers:** Between dense blocks, 1×1 convolution + 2×2 average pooling reduce spatial dimensions and channel count.

**Advantages:**

- **Feature reuse:** All layers can access features from all previous layers, encouraging maximum feature reuse.
- **Parameter efficiency:** Much fewer parameters than ResNet for similar performance.
- **Stronger gradients:** Direct connections to all preceding layers ensure strong gradient flow.
- **Implicit deep supervision:** Each layer receives gradient signals from the loss via all subsequent layers.

**Architecture Evolution Summary:**

| Architecture   | Year | Depth       | Parameters | Top-5 Error | Key Innovation                   |
| :------------- | :--- | :---------- | :--------- | :---------- | :------------------------------- |
| **AlexNet**    | 2012 | 8 layers    | 60M        | 15.3%       | ReLU, GPU training, dropout      |
| **VGG-16**     | 2014 | 16 layers   | 138M       | 7.3%        | Small 3×3 filters, depth         |
| **GoogLeNet**  | 2014 | 22 layers   | 5M         | 6.7%        | Inception module, 1×1 bottleneck |
| **ResNet-152** | 2015 | 152 layers  | 60M        | 3.6%        | Skip connections                 |
| **DenseNet**   | 2016 | 121+ layers | 8M         | ~5.5%       | Dense connections, feature reuse |

---

# 4.5 CNN Design, Forward and Backward Propagation

## 4.5.1 CNN Design Principles

**Architecture design decisions:**

- **Filter sizes:** Small filters (3×3) are preferred — they require fewer parameters, allow deeper networks, and provide more non-linearity through additional activation layers.
- **Number of filters:** Typically doubles when spatial dimensions are halved (e.g., 64 → 128 → 256 → 512). Early layers detect low-level features (few filters needed); deeper layers need more filters for complex patterns.
- **Downsampling:** Use stride-2 convolutions or pooling to progressively reduce spatial resolution.
- **Depth:** Deeper networks learn more abstract features. Use skip connections (ResNet) to train very deep networks.
- **Final layers:** Global average pooling (replacing FC layers) reduces overfitting. Softmax for classification; linear for regression.

## 4.5.2 Forward Propagation in CNN

**Forward pass** computes the output layer by layer:

1. **Convolution:** $Z^l = W^l * A^{l-1} + b^l$ (filter slides across input, produces feature map).
2. **Activation:** $A^l = \text{ReLU}(Z^l)$ (applies non-linearity).
3. **Pooling:** Reduces spatial dimensions by selecting max or average values.
4. **Flatten:** Converts 3D tensor to 1D vector.
5. **Fully connected:** $Z = WA + b$, followed by activation.
6. **Output:** Softmax converts logits to probabilities.
7. **Loss:** Compare predictions with ground truth — cross-entropy for classification.

## 4.5.3 Backward Propagation in CNN

**Backward pass** computes gradients of the loss with respect to all learnable parameters (filter weights and biases) and updates them using gradient descent.

**Gradient through convolution:** The gradient with respect to the filter weights is computed by convolving the input with the upstream gradient:

$
\frac{\partial L}{\partial W^l} = A^{l-1} * \frac{\partial L}{\partial Z^l}
$

The gradient with respect to the input (for propagation to the previous layer) is computed using a **full convolution** (convolution with the flipped filter):

$
\frac{\partial L}{\partial A^{l-1}} = \frac{\partial L}{\partial Z^l} *_{\text{full}} \text{rot180}(W^l)
$

**Gradient through max pooling:** The gradient passes only to the position that had the maximum value in the forward pass. All other positions receive zero gradient.

**Gradient through ReLU:**

$
\frac{\partial L}{\partial Z^l} = \frac{\partial L}{\partial A^l} \odot \mathbb{1}(Z^l > 0)
$

The gradient is passed through where the pre-activation was positive, and zeroed where it was negative or zero.

---

# 4.6 Transfer Learning and Fine-Tuning

> **Explain transfer learning and fine-tuning in the context of CNNs. Describe a scenario where you would fine-tune only the last few layers versus retraining the entire network. (Fall 2025)**

**Transfer learning** is the practice of using a model pre-trained on a large dataset (e.g., ImageNet with 1.4M images, 1000 classes) as the starting point for a new task with limited data. The pre-trained model has already learned general visual features (edges, textures, shapes) that are useful across many vision tasks.

**Why it works:** Early CNN layers learn universal low-level features (edges, corners, color blobs) that are similar across all image domains. Middle layers learn mid-level features (textures, patterns). Only the deeper layers learn task-specific high-level features (object parts, specific classes). The universal features transfer well to new tasks.

## 4.6.1 Feature Extraction (Frozen Backbone)

Remove the original classification head and use the pre-trained CNN as a fixed feature extractor. Freeze all convolutional layer weights (no gradient updates). Add a new classifier (one or more FC layers + softmax) on top and train only the new classifier.

**When to use:** Small target dataset that is similar to the original dataset (e.g., ImageNet → different object categories). Training the full network would overfit on small data.

## 4.6.2 Fine-Tuning

Unfreeze some or all pre-trained layers and retrain with a **small learning rate** to adapt features to the new task while preserving previously learned representations.

**Strategy — which layers to fine-tune:**

- **Scenario 1 — Small dataset, similar domain:** Fine-tune only the last few layers (higher-level features). Freeze early and middle layers. Example: ImageNet → dog breed classification (both are natural image classification).
- **Scenario 2 — Large dataset, different domain:** Fine-tune the entire network with a small learning rate. All layers need adaptation. Example: ImageNet → medical X-ray classification (visual domain is fundamentally different — textures, structures, and semantics differ).
- **Scenario 3 — Small dataset, different domain:** Use feature extraction only (freeze all layers). Fine-tuning would overfit. Alternatively, fine-tune only the last 1–2 layers.

**Practical guidelines:**

- Use a learning rate 10–100× smaller than training from scratch (e.g., 1e-4 or 1e-5 instead of 1e-2).
- Freeze batch normalization layers when fine-tuning with small batches (batch statistics become unreliable).
- Use differential learning rates — lower rates for early layers, higher rates for later layers.

---

# 4.7 Looking Inside Deep Neural Networks

Understanding what a CNN has learned and why it makes specific predictions is critical for debugging, trust, and interpretability.

## 4.7.1 Feature Map Visualization

Visualize the output (activation) of each filter at each layer. Early layers show edge detectors (horizontal, vertical, diagonal), color detectors, and gradient detectors. Middle layers show texture patterns, corners, and basic shapes. Deep layers show high-level semantic features (dog faces, wheels, text).

## 4.7.2 Activation Maximization

Generate a synthetic input image that maximally activates a specific neuron or filter. Start with random noise, fix network weights, and perform **gradient ascent** on the input pixels to maximize the target neuron's activation:

$
x^* = \arg\max_x \, a_k(x) - \lambda \|x\|^2
$

where $a_k$ is the activation of neuron $k$ and $\lambda$ is a regularization term to keep the image realistic. The resulting image reveals what pattern the neuron is "looking for."

## 4.7.3 Saliency Maps

Compute the gradient of the output class score with respect to each input pixel:

$
S = \left| \frac{\partial y_c}{\partial x} \right|
$

Pixels with large gradient magnitude are the ones that most influence the prediction if changed — they highlight the most "salient" regions of the input for a given class.

## 4.7.4 Grad-CAM (Gradient-weighted Class Activation Mapping)

Produces a coarse heatmap highlighting important regions for a specific class prediction.

1. Compute the gradient of the class score $y^c$ with respect to the feature maps $A^k$ of the last convolutional layer.
2. Global average pool the gradients to get importance weights: $\alpha_k^c = \frac{1}{Z} \sum_i \sum_j \frac{\partial y^c}{\partial A_{ij}^k}$
3. Compute weighted combination: $L_{\text{Grad-CAM}}^c = \text{ReLU}\left(\sum_k \alpha_k^c A^k\right)$

ReLU is applied because we are interested only in features that have a positive influence on the class of interest. The result is a heatmap that can be overlaid on the original image.

## 4.7.5 Occlusion Sensitivity

Systematically cover different regions of the input with a grey/black patch and observe the change in prediction probability. Regions where occlusion causes the largest drop in confidence are the most important for the prediction. This is model-agnostic — it works for any architecture.

---

# 4.8 Neural Style Transfer

Neural style transfer generates a new image that preserves the **content** of one image while adopting the **artistic style** of another (e.g., rendering a photograph in the style of Van Gogh's Starry Night).

**Method (Gatys et al., 2015):** Uses a pre-trained CNN (typically VGG-19) as a fixed feature extractor. The network weights are frozen — instead, the pixel values of the generated image are optimized.

**Content Representation:** The feature maps at a deep layer $l$ capture the content (spatial structure, objects) of an image. The **content loss** measures the difference between feature maps of the content image $C$ and the generated image $G$:

$
L_{\text{content}} = \frac{1}{2} \sum_{i,j} (F_{ij}^l - P_{ij}^l)^2
$

where $F^l$ and $P^l$ are the feature maps of the generated and content images at layer $l$.

**Style Representation — Gram Matrix:** Style is captured by the correlations between filter responses. The **Gram matrix** $G^l$ at layer $l$ with $N_l$ filters and feature maps of size $M_l$:

$
G_{ij}^l = \sum_k F_{ik}^l F_{jk}^l
$

The Gram matrix captures which features tend to co-occur — e.g., if "blue color" and "swirly texture" activations are correlated, the style includes blue swirls. Spatial information is discarded.

**Style Loss:**

$
L_{\text{style}} = \sum_l w_l \frac{1}{4 N_l^2 M_l^2} \sum_{i,j} (G_{ij}^l - A_{ij}^l)^2
$

where $G^l$ and $A^l$ are Gram matrices of the generated and style images, and $w_l$ is the weight for layer $l$. Multiple layers are used to capture style at different scales.

**Total Loss:**

$
L_{\text{total}} = \alpha \cdot L_{\text{content}} + \beta \cdot L_{\text{style}}
$

The ratio $\alpha/\beta$ controls the balance — higher $\beta/\alpha$ produces more stylized images. The generated image is initialized (random noise or content image) and iteratively updated using gradient descent on the pixel values.

---

# 4.9 Image Captioning System

> **Design an image captioning system by combining CNN and sequence modeling components. Explain the role of each component and how training is performed end-to-end. (Fall 2025)**

An **image captioning system** automatically generates a natural language description of an image. It combines a CNN (for visual understanding) with an RNN/LSTM (for language generation) in an **encoder-decoder** framework.

## 4.9.1 Architecture

**Encoder — CNN:** A pre-trained CNN (e.g., ResNet, VGG) extracts visual features from the input image. The final fully connected layer (classification head) is removed. The output is either a single feature vector (from the layer before FC) or a grid of spatial feature vectors (from the last convolutional layer, e.g., 14×14×2048 for ResNet).

**Decoder — LSTM:** An LSTM generates the caption word by word, conditioned on the visual features and the previously generated words.

**Basic pipeline (Show and Tell — Vinyals et al., 2015):**

1. Pass image through CNN encoder → obtain feature vector $v$.
2. Feed $v$ as the initial input to the LSTM (or use it to initialize the hidden state).
3. At each time step $t$, the LSTM receives the embedding of the previous word $w_{t-1}$ and produces a probability distribution over the vocabulary for the next word $w_t$.
4. Generation continues until the model produces an \<END\> token.

## 4.9.2 Attention Mechanism (Show, Attend and Tell — Xu et al., 2015)

Instead of compressing the entire image into a single vector (information bottleneck), the attention mechanism allows the decoder to focus on different image regions while generating each word.

**Spatial features:** The CNN encoder produces a set of $L$ annotation vectors $a_1, a_2, ..., a_L$ (e.g., from a 14×14 feature map, $L = 196$ spatial locations).

**At each decoder time step $t$:**

1. Compute attention weights $\alpha_{t,i}$ — how relevant each spatial region $i$ is for generating word $w_t$:

$
e_{t,i} = f_{\text{att}}(h_{t-1}, a_i) \quad;\quad \alpha_{t,i} = \frac{\exp(e_{t,i})}{\sum_j \exp(e_{t,j})}
$

2. Compute the context vector — weighted sum of spatial features:

$
z_t = \sum_{i=1}^{L} \alpha_{t,i} \cdot a_i
$

3. Feed $z_t$ and the word embedding of $w_{t-1}$ to the LSTM to produce $h_t$ and predict $w_t$.

**Result:** When generating "dog," the model attends to the dog region; when generating "grass," it attends to the grass region.

## 4.9.3 Training

**Dataset:** Image-caption pairs (e.g., MS COCO — each image has 5 human-written captions).

**Training process:**

1. The CNN encoder is typically pre-trained on ImageNet (transfer learning). It may be frozen or fine-tuned with a small learning rate.
2. At each training step, the ground-truth caption is used with **teacher forcing** — the LSTM receives the correct previous word $w_{t-1}$ (not its own prediction) as input at each time step.
3. The loss is the **cross-entropy** between the predicted word distribution and the ground-truth word at each time step, summed over the sequence:

$
L = -\sum_{t=1}^{T} \log p(w_t | w_1, ..., w_{t-1}, I)
$

4. Gradients flow through the LSTM decoder and (if unfrozen) through the CNN encoder, enabling end-to-end training.

**Inference:** At test time, the model generates words autoregressively — using its own predicted word as input to the next step. **Beam search** (maintaining top-$k$ candidate sequences at each step) is used instead of greedy decoding to find higher-quality captions.

**Evaluation Metrics:** BLEU (n-gram precision), METEOR (considers synonyms and stemming), CIDEr (consensus-based, TF-IDF weighted), ROUGE (recall-oriented).

---

---

---

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

| Approach                  | How It Works                                                   | Strength                                        |
| :------------------------ | :------------------------------------------------------------- | :---------------------------------------------- |
| **Frame-level (2D CNN)**  | Apply a 2D CNN to each frame independently, then aggregate     | Simple; leverages pretrained image models       |
| **Clip-level (3D CNN)**   | Apply 3D convolutions to short clips of stacked frames         | Learns spatiotemporal features jointly          |
| **Recurrent (CNN + RNN)** | Extract per-frame features with CNN, feed sequence to RNN/LSTM | Captures long-range temporal dependencies       |
| **Two-stream**            | Separate spatial (RGB) and temporal (optical flow) streams     | Explicitly models appearance and motion         |
| **Transformer-based**     | Apply self-attention over spatial and temporal tokens          | Captures global dependencies without recurrence |

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

| Property                | FlowNet / FlowNet 2.0             | RAFT                                  |
| :---------------------- | :-------------------------------- | :------------------------------------ |
| **Architecture**        | Encoder-decoder (stacked cascade) | Correlation volume + recurrent GRU    |
| **Flow estimation**     | Single forward pass (or cascade)  | Iterative refinement ($N$ iterations) |
| **Accuracy**            | Good baseline                     | State-of-the-art on benchmarks        |
| **Large displacements** | FlowNet 2.0 handles via stacking  | Handles via all-pairs correlation     |
| **Generalization**      | Moderate                          | Strong cross-dataset generalization   |

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

| Property           | 2D Convolution                                | 3D Convolution                                           |
| :----------------- | :-------------------------------------------- | :------------------------------------------------------- |
| **Kernel shape**   | $k_h \times k_w$                              | $k_t \times k_h \times k_w$                              |
| **Input**          | Single frame $H \times W \times C$            | Clip of $T$ frames $T \times H \times W \times C$        |
| **Output**         | 2D feature map                                | 3D feature volume (preserves temporal dim)               |
| **Motion capture** | None (spatial only)                           | Yes (temporal patterns across frames)                    |
| **Parameters**     | $C_{in} \times k_h \times k_w \times C_{out}$ | $C_{in} \times k_t \times k_h \times k_w \times C_{out}$ |
| **Computation**    | Lower                                         | $k_t$ times higher                                       |

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

| Architecture           | Temporal Range       | Spatial Awareness  | Pretraining         | Computation |
| :--------------------- | :------------------- | :----------------- | :------------------ | :---------- |
| **2D CNN (per-frame)** | None                 | Full               | ImageNet            | Low         |
| **3D CNN (C3D/I3D)**   | Short (16–64 frames) | Full               | Kinetics / Inflated | High        |
| **CNN + LSTM**         | Long (entire video)  | Via CNN features   | CNN: ImageNet       | Moderate    |
| **ConvLSTM**           | Long                 | Preserved in gates | Limited             | Moderate    |
| **Two-stream**         | Short–Medium         | Full (two paths)   | ImageNet + flow     | High        |

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

| Method         | Input           | Motion Modeling                | Requires Optical Flow | Strength                         |
| :------------- | :-------------- | :----------------------------- | :-------------------- | :------------------------------- |
| **Two-Stream** | RGB + Flow      | Explicit (optical flow stream) | Yes                   | Strong motion features           |
| **C3D / I3D**  | RGB clips       | Implicit (3D convolutions)     | No (optional)         | End-to-end spatiotemporal        |
| **CNN + LSTM** | Frame features  | Sequential (recurrence)        | No                    | Long-range dependencies          |
| **SlowFast**   | RGB (dual rate) | Implicit (fast pathway)        | No                    | No flow needed; state-of-the-art |
| **R(2+1)D**    | RGB clips       | Factorized 3D convolution      | No                    | Efficient; more nonlinearities   |

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

| Method       | Type | Core Mechanism                   | Handles Occlusion | Speed     |
| :----------- | :--- | :------------------------------- | :---------------- | :-------- |
| **SORT**     | MOT  | Kalman filter + Hungarian (IoU)  | Poor              | Very fast |
| **DeepSORT** | MOT  | SORT + CNN appearance embeddings | Good              | Fast      |
| **SiamFC**   | SOT  | Siamese cross-correlation        | Moderate          | Real-time |

---

---

---

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

| Feature             | Representation           | Information Retained           | Typical Use                         |
| :------------------ | :----------------------- | :----------------------------- | :---------------------------------- |
| **Raw waveform**    | 1D signal                | Everything                     | End-to-end models (WaveNet, 1D CNN) |
| **Spectrogram**     | 2D (time × frequency)    | Full spectral detail           | General analysis                    |
| **Mel spectrogram** | 2D (time × Mel bins)     | Perceptually weighted spectrum | CNN-based classification            |
| **MFCC**            | 2D (time × coefficients) | Spectral envelope only         | Traditional ML, compact models      |

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

| Architecture          | Input               | Strength                                       | Limitation                         |
| :-------------------- | :------------------ | :--------------------------------------------- | :--------------------------------- |
| **2D CNN**            | Mel spectrogram     | Simple, effective, pretrained models available | Limited temporal context           |
| **1D CNN**            | Raw waveform        | No hand-crafted features needed                | Needs more data; longer training   |
| **CRNN**              | Mel spectrogram     | Captures long-range temporal structure         | More complex; slower training      |
| **AST (Transformer)** | Spectrogram patches | Global attention; state-of-the-art accuracy    | High compute; needs large datasets |

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

| Method            | Domain           | Architecture             | Phase Handling         | SDR (vocals) |
| :---------------- | :--------------- | :----------------------- | :--------------------- | :----------- |
| **Open-Unmix**    | Frequency (STFT) | FC + Bi-LSTM             | Reuses mixture phase   | ~6.3 dB      |
| **Wave-U-Net**    | Time (waveform)  | 1D U-Net                 | Learned implicitly     | ~5.7 dB      |
| **Hybrid Demucs** | Both             | Dual U-Net + Transformer | Learned (both domains) | ~8.1 dB      |

---

# 6.3 Sound Event Detection

> **Explain sound event detection as a deep learning task. How is it different from audio classification, and what network architectures and training strategies are commonly used? (Fall 2025)**

## 6.3.1 Task Definition and Difference from Audio Classification

**Audio classification (audio tagging)** assigns one or more labels to an **entire audio clip** — the output is a set of clip-level labels. It answers: **what** sounds are present? Example: given a 10-second recording, output "dog bark, car horn."

**Sound event detection (SED)** identifies **what** sounds are present **and when** they occur — the output includes the onset (start time) and offset (end time) of each event. It answers: **what** sounds and **when**? Example: "dog bark from 2.1s to 3.4s, car horn from 5.0s to 5.8s."

**Polyphonic SED** further requires detecting **multiple overlapping events** at the same time — e.g., a dog barking while a car horn is blowing simultaneously.

| Property                  | Audio Classification         | Sound Event Detection                             |
| :------------------------ | :--------------------------- | :------------------------------------------------ |
| **Output granularity**    | Clip-level labels            | Frame-level labels with timestamps                |
| **Temporal localization** | No                           | Yes (onset + offset)                              |
| **Overlapping events**    | Multi-label (present/absent) | Multi-label per time frame                        |
| **Annotation**            | Weak labels (clip-level)     | Strong labels (frame-level timestamps)            |
| **Evaluation metric**     | Accuracy, mAP                | Event-based F1, segment-based F1, ER (error rate) |

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
