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

| Property               | MLP                              | CNN                                  |
| :--------------------- | :------------------------------- | :----------------------------------- |
| **Connectivity**       | Fully connected                  | Locally connected (sparse)           |
| **Weight sharing**     | No (unique weights per connection)| Yes (shared filters)                |
| **Spatial structure**  | Input flattened to 1D vector     | Preserves 2D/3D structure            |
| **Parameters**         | Very high                        | Very low (due to sharing)            |
| **Translation**        | Not invariant                    | Equivariant (invariant with pooling) |
| **Suitable for**       | Tabular / structured data        | Images, video, spatial data          |

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

| Architecture   | Year | Depth     | Parameters | Top-5 Error | Key Innovation                  |
| :------------- | :--- | :-------- | :--------- | :---------- | :------------------------------ |
| **AlexNet**    | 2012 | 8 layers  | 60M        | 15.3%       | ReLU, GPU training, dropout     |
| **VGG-16**     | 2014 | 16 layers | 138M       | 7.3%        | Small 3×3 filters, depth        |
| **GoogLeNet**  | 2014 | 22 layers | 5M         | 6.7%        | Inception module, 1×1 bottleneck|
| **ResNet-152** | 2015 | 152 layers| 60M        | 3.6%        | Skip connections                |
| **DenseNet**   | 2016 | 121+ layers| 8M        | ~5.5%       | Dense connections, feature reuse|

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
