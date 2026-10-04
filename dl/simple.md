## 4.3.1 Standard Convolution

This is the normal, basic convolution. A small filter (say 3×3) slides across the image, does multiply-and-add at every position, and produces a new image called a **feature map** (a map that highlights certain features like edges).

If we use many filters, we get many feature maps — each one detecting a different pattern.

**Where is it used?** Everywhere in CNNs — image classification (is this a cat or dog?), object detection (where is the car?), segmentation (color each pixel by its object).

---

## 4.3.2 Transpose Convolution (Deconvolution)

Standard convolution usually makes images **smaller**. Transpose convolution does the **opposite** — it makes images **bigger**.

**How does it work?** Imagine you have a tiny 2×2 image. Transpose convolution inserts zeros (empty spaces) between the pixels to stretch it out, then applies a normal convolution on top. The result is a larger image.

**Where is it used?**

- In **semantic segmentation** (U-Net, FCN) — the network first shrinks the image to understand it, then uses transpose convolution to blow it back up to original size and label every pixel.
- In **GANs** (Generative Adversarial Networks) — the generator uses it to create full images from a small random input.

---

## 4.3.3 Dilated (Atrous) Convolution

Normal 3×3 filter looks at a 3×3 patch of the image. But what if we want to see a **bigger area** without using a bigger filter (which would need more parameters and more computation)?

**Solution:** Put **gaps (holes)** between the filter elements.

A dilation rate $r$ means the kernel elements are spaced $r$ apart.

- A 3×3 filter with dilation rate 1 → normal 3×3 view.
- A 3×3 filter with dilation rate 2 → the filter elements are spaced 2 apart, so it covers a 5×5 area, but still only has 9 numbers (parameters).
- Dilation rate 3 → covers 7×7 area, still 9 parameters.

**Why is this useful?** It sees a bigger picture without losing detail (no pooling needed) and without increasing computation.

**Where is it used?** In **DeepLab** (a segmentation model) where you need to understand both fine details and big-picture context at the same time.

---

## 4.3.4 Separable Convolution

A standard convolution uses 3x3x3 filters for R,G,B channels.

**Separable convolution breaks this into two cheaper steps:**

**Step 1 — Depthwise Convolution:** Apply a separate small filter (e.g., 3×3) to each channel independently. If the input has 3 channels, use 3 separate filters. No mixing between channels yet.

**Step 2 — Pointwise Convolution:** Apply a 1×1×3 filter across all channels to mix them together.

**Why do this?** It is **much cheaper** computationally. For a 3×3 filter with 256 output channels, separable convolution uses roughly **8–9× fewer calculations** than standard convolution. The results are almost as good.

**Where is it used?** In **MobileNet** and **Xception** — lightweight models designed to run fast on phones and small devices.

---

## 4.3.5 Grouped Convolution

Instead of one big convolution across all channels, we **split the channels into G groups** and do independent convolutions in each group. Then we stick (concatenate) the results back together.

**Example:** If input has 64 channels and we use G = 4 groups, each group processes 64/4 = 16 channels independently.

**Benefit:** G times fewer parameters and computations.

**Where is it used?**

- **AlexNet** (2012) originally used 2 groups to split work across 2 GPUs.
- **ResNeXt** uses 32 groups for better accuracy without increasing cost.

---

## 4.3.6 Deformable Convolution

In standard convolution, the filter always looks at a **fixed, rectangular grid** of pixels. But real-world objects are not always rectangular — a person can be standing, sitting, or bending.

**Deformable convolution** lets each point in the filter **shift** to a different position. The network **learns** these shifts (offsets) during training. So the filter can stretch, squeeze, or bend to match the shape of the object it is looking at.

Since the shifted positions may land between pixels (fractional positions), **bilinear interpolation** is used to estimate the pixel value.

> **Bilinear interpolation** = a way to estimate a value at a point between known pixels, by taking a weighted average of the 4 nearest pixels.

**Where is it used?** Object detection and instance segmentation where objects have irregular shapes — like detecting people in different poses or animals in unusual positions.

---

---

# 4.4 CNN Architectures (The Evolution of CNN Designs)

## 4.4.1 AlexNet (2012)

> The network that started the deep learning revolution.

**What happened?** AlexNet won the ImageNet competition in 2012 by a huge margin — 15.3% error vs. 26.2% for the second-best method. It proved that deep CNNs trained on GPUs can crush traditional methods.

> **ImageNet** = a massive dataset with millions of labeled images in 1000 categories. A yearly competition challenges teams to build the best image classifier.
>
> **Top-5 error** = the model is wrong if the correct label is NOT in its top 5 guesses.

**Structure:** 5 convolutional layers + 3 fully connected layers. About 60 million parameters.

**Key ideas AlexNet introduced:**

| Idea                  | What it means                                                                                                                                      |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ReLU activation**   | Used ReLU (output = max(0, x)) instead of older functions like sigmoid. This made training **6× faster**.                                          |
| **GPU training**      | Split the network across 2 GPUs to speed up training.                                                                                              |
| **Dropout**           | Randomly turned off 50% of neurons during training to prevent **overfitting** (memorizing the training data instead of learning general patterns). |
| **Data augmentation** | Created extra training images by randomly cropping, flipping, and changing colors — so the model sees more variety.                                |

---

## 4.4.2 VGGNet (2014)

> The lesson: **deeper is better**, but keep it simple.

**Main idea:** Use only **small 3×3 filters** and stack many layers deep (16 or 19 layers).

**Why small filters?** A stack of two 3×3 filters sees the same area as one 5×5 filter, but:

- Uses **fewer parameters**: 2 × 9 = 18 vs. 25.
- Adds **more non-linearity**: two ReLU activations instead of one, so the network can learn more complex patterns.

Three 3×3 layers = same view as one 7×7 filter, but cheaper and more powerful.

**Problem:** VGG-16 has **138 million parameters** (mostly in the fully connected layers at the end) — very heavy on memory.

---

## 4.4.3 GoogLeNet / Inception (2014)

> The lesson: **go wider, not just deeper.**

**Main idea:** Instead of choosing one filter size (3×3 or 5×5), use **all of them at the same time** in a single layer. This is called the **Inception Module**.

**What is an Inception Module?** At each layer, run these in parallel:

- 1×1 convolution → captures channel relationships
- 3×3 convolution → captures small patterns
- 5×5 convolution → captures bigger patterns
- 3×3 max pooling → captures dominant features

Then **concatenate** (join together) all the outputs along the channel dimension.

**Clever trick — 1×1 bottleneck convolution:** Before the 3×3 and 5×5 convolutions, use a 1×1 convolution to **reduce the number of channels**. This drastically cuts computation.

**Other ideas:**

- **Global Average Pooling (GAP):** Instead of expensive fully connected layers at the end, just take the average of each feature map. This reduces parameters hugely.
- **Auxiliary classifiers:** Extra small classifiers attached at middle layers to help gradients reach deep layers during training (removed after training).

**Result:** Only ~5 million parameters (27× fewer than VGG!) but better accuracy.

---

## 4.4.4 ResNet (2015)

> The lesson: **skip connections solve the depth problem.**

**The problem:** When you stack too many layers, the network actually gets **worse** — even on training data! This is called the **degradation problem**. It's not overfitting — it's the network struggling to optimize so many layers.

**The solution — Residual Block (Skip Connection):**

Instead of asking a block of layers to learn the full output H(x), ask it to learn only the **difference** (residual) F(x) = H(x) - x. Then add the input back:

$$H(x) = F(x) + x$$

The input **skips over** the convolutional layers through a **shortcut connection** and gets added directly to the output.

**Why does this work?**

- If the layers don't need to change anything, they can simply learn F(x) = 0, and the output becomes just x (identity). Learning "do nothing" is easy.
- During backpropagation, the gradient flows **directly through the skip connection**, so it doesn't vanish even in 100+ layer networks.

> **Vanishing gradient** = gradients become extremely tiny as they travel back through many layers, so early layers stop learning.

**Bottleneck block:** In deeper ResNets (50+ layers), each block uses 1×1 → 3×3 → 1×1 convolutions. The 1×1 layers squeeze and then expand the channels, keeping the middle 3×3 layer cheap.

**Result:** ResNet-152 (152 layers!) achieved 3.57% top-5 error — **better than humans** (~5.1% error).

---

## 4.4.5 DenseNet (2016)

> The lesson: **connect every layer to every other layer.**

**Main idea — Dense Connections:** In a **Dense Block**, every layer receives the feature maps from **all previous layers** (joined by concatenation, not addition like ResNet).

If a block has 5 layers, then:

- Layer 2 gets input from Layer 1.
- Layer 3 gets input from Layer 1 AND Layer 2.
- Layer 4 gets input from Layer 1, 2, AND 3.
- ...and so on.

> **Concatenation vs. Addition:**
>
> - ResNet **adds** the skip connection to the output (same size, element-wise sum).
> - DenseNet **concatenates** — stacks all previous feature maps together (channels keep growing).

**Growth Rate (k):** Each layer produces only a small number of feature maps (e.g., k = 12 or 32). Since all previous maps are available, there's no need for each layer to produce many maps on its own.

> **Growth rate** = how many new feature maps each layer adds.

**Transition Layers:** Between dense blocks, a 1×1 convolution + 2×2 average pooling layer is used to reduce the size and number of channels (otherwise things would get too big).

**Why is DenseNet good?**

| Advantage            | Explanation                                                                               |
| :------------------- | :---------------------------------------------------------------------------------------- |
| **Feature reuse**    | Every layer can use features from all previous layers — nothing is wasted.                |
| **Fewer parameters** | Much smaller than ResNet for similar performance, because each layer produces fewer maps. |
| **Strong gradients** | Every layer has a direct connection to the loss, so gradients stay strong.                |
| **Deep supervision** | Each layer gets gradient signals through many short paths, not just one long path.        |

---

## Architecture Evolution Summary

| Architecture   | Year | Depth       | Parameters | Top-5 Error | Key Innovation                   |
| :------------- | :--- | :---------- | :--------- | :---------- | :------------------------------- |
| **AlexNet**    | 2012 | 8 layers    | 60M        | 15.3%       | ReLU, GPU training, dropout      |
| **VGG-16**     | 2014 | 16 layers   | 138M       | 7.3%        | Small 3×3 filters, go deeper     |
| **GoogLeNet**  | 2014 | 22 layers   | 5M         | 6.7%        | Inception module, 1×1 bottleneck |
| **ResNet-152** | 2015 | 152 layers  | 60M        | 3.6%        | Skip connections                 |
| **DenseNet**   | 2016 | 121+ layers | 8M         | ~5.5%       | Dense connections, feature reuse |

**The story in one line:** AlexNet proved deep learning works → VGG showed deeper is better → GoogLeNet showed wider is smarter → ResNet solved the depth limit with skip connections → DenseNet maximized feature reuse with dense connections.

---

# 4.5 CNN Design, Forward and Backward Propagation

## 4.5.1 CNN Design Principles

When building a CNN, you need to make some design choices — like choosing the right ingredients before cooking. Here are the main decisions:

- **Filter size:** Use small 3×3 filters. They need fewer numbers (parameters) to store, let you build deeper networks, and since each layer adds a ReLU activation, the network can learn more complex patterns.

- **Number of filters:** As the image shrinks (spatial dimensions reduce), increase the number of filters. A common pattern: 64 → 128 → 256 → 512. Early layers detect simple things (edges, colors) so they need fewer filters. Deeper layers detect complicated things (faces, objects) and need more filters.

- **Downsampling** (making the image smaller): Use **stride-2 convolution** (the filter jumps 2 pixels instead of 1) or **pooling** (taking the max or average of a small region) to gradually shrink the image.

> **Stride** = how many pixels the filter moves each step. Stride 1 = move 1 pixel at a time. Stride 2 = skip every other position, so the output is half the size.

- **Depth** (number of layers): More layers = the network can learn more abstract (high-level) features. But very deep networks are hard to train, so use **skip connections** (shortcuts that let information jump over layers, like in ResNet).

- **Final layers:** Use **Global Average Pooling (GAP)** instead of big fully connected layers — it takes the average of each feature map, giving one number per map. This reduces the number of parameters and prevents overfitting. Then use **Softmax** for classification (picking a category) or a **linear layer** for regression (predicting a number).

> **Overfitting** = when the model memorizes the training data but can't handle new, unseen data.

---

## 4.5.2 Forward Propagation in CNN

**Forward propagation** (also called the **forward pass**) is the process of feeding an input image through the network layer by layer to get a prediction. Think of it like passing a ball through a series of checkpoints — at each checkpoint, something happens to the ball.

Here's what happens step by step:

1. **Convolution:** The filter slides across the input image, does multiply-and-add at each position, and produces a **feature map**. Mathematically: $Z^l = W^l * A^{l-1} + b^l$ (where $W$ is the filter, $A$ is the input, $b$ is the bias, and $*$ means convolution).

2. **Activation (ReLU):** Apply the ReLU function — keep positive values as they are, turn negative values to zero. This adds **non-linearity** (without it, the whole network would behave like a single simple layer). $A^l = \text{ReLU}(Z^l)$

3. **Pooling:** Shrink the feature map by picking the maximum value (max pooling) or average value (average pooling) from small regions (e.g., 2×2 blocks).

4. **Flatten:** The feature maps are 3D (height × width × channels). **Flatten** means stretching them into a single long 1D list of numbers, so they can be fed into a regular (fully connected) layer.

> **Tensor** = a multi-dimensional array. A 1D tensor is a list, 2D is a table, 3D is a cube of numbers.

5. **Fully connected layer:** Every neuron connects to every neuron in the next layer. $Z = WA + b$, then apply activation.

6. **Output (Softmax):** Converts raw scores (**logits**) into **probabilities** that add up to 1. The class with the highest probability is the prediction.

> **Logits** = the raw, unnormalized output scores before converting to probabilities.

7. **Loss:** Compare the prediction with the correct answer (**ground truth**). For classification, we use **cross-entropy loss** — it gives a small loss when the prediction is confident and correct, and a large loss when the prediction is wrong.

---

## 4.5.3 Backward Propagation in CNN

**Backward propagation** is how the network **learns from its mistakes**. After the forward pass gives a prediction, we compute the **loss** (how wrong the prediction was). Then we work backwards through the network, calculating how much each filter weight contributed to the error. Finally, we adjust the weights to reduce the error.

> **Gradient** = a number that tells us "if I increase this weight a little, how much does the loss change?" It points in the direction of steepest increase, so we move in the **opposite direction** to decrease the loss.

Here's how gradients are computed through different layers:

**Through convolution:** To find out how much each filter weight affected the loss, we convolve the input with the upstream gradient (the error signal coming from the layer above):

$$\frac{\partial L}{\partial W^l} = A^{l-1} * \frac{\partial L}{\partial Z^l}$$

**Through max pooling:** During the forward pass, max pooling picked the biggest value in each region. During backprop, the gradient goes **only to that winning position**. All other positions get zero gradient — because changing them wouldn't have changed the output.

**Through ReLU:** ReLU says: if the input was positive, pass the gradient through unchanged. If the input was negative or zero, block the gradient (set it to zero).

After computing all the gradients, we update the weights using **gradient descent**: $W_{\text{new}} = W_{\text{old}} - \eta \cdot \frac{\partial L}{\partial W}$, where $\eta$ is the **learning rate** (a small number that controls how big each update step is).

---

---

# 4.7 Looking Inside Deep Neural Networks

A CNN is often called a **"black box"** — you put in an image, it gives a prediction, but you don't know **why**. Understanding what the network has learned is important for **debugging** (finding mistakes), **trust** (believing the model's answers), and **interpretability** (explaining decisions to humans).

> **Interpretability** = the ability to explain, in human-understandable terms, why a model made a certain decision.

Here are some techniques to "look inside" a CNN:

## 4.7.1 Feature Map Visualization

The simplest way: just look at the **feature maps** (outputs of each filter at each layer) as images.

- **Early layers** (close to the input): Show simple patterns — edges (horizontal, vertical, diagonal lines), basic colors, and gradients (smooth changes in brightness).
- **Middle layers**: Show more complex patterns — textures (repeating patterns), corners, and basic shapes.
- **Deep layers** (close to the output): Show high-level **semantic features** — recognizable things like dog faces, car wheels, or text characters.

> **Semantic** = related to meaning. "Semantic features" are features that carry meaning (e.g., "this looks like an eye").

## 4.7.2 Activation Maximization

This answers the question: **"What does a specific neuron want to see?"**

**Method:** Start with a random noise image (just random colored pixels). Then **freeze** (lock) the network's weights and do **gradient ascent** on the pixel values of the image — that is, adjust the pixels to **increase** the activation of a chosen neuron as much as possible.

> **Gradient ascent** = the opposite of gradient descent. Instead of going downhill to minimize something, we go uphill to maximize something.

The resulting image shows the pattern the neuron is "looking for." For example, a neuron in a deep layer might produce an image that looks like a dog face — meaning that neuron fires strongly when it sees dog-like features.

## 4.7.3 Saliency Maps

This answers: **"Which pixels in the input image matter most for the prediction?"**

Compute the **gradient** of the predicted class score with respect to each input pixel:

$$S = \left| \frac{\partial y_c}{\partial x} \right|$$

> **Saliency** = importance, what stands out.

Pixels where the gradient is large are the ones that would change the prediction the most if you modified them. The saliency map highlights these important regions — usually the object that the CNN is classifying.

## 4.7.4 Grad-CAM (Gradient-weighted Class Activation Mapping)

Grad-CAM creates a **heatmap** (a color-coded map where warm colors = important, cool colors = unimportant) showing which parts of the image the CNN focused on when making its prediction.

## 4.7.5 Occlusion Sensitivity

The simplest and most intuitive method. **Cover up** (occlude) different parts of the image with a grey or black patch, one region at a time, and see how the prediction changes.

- If covering a region causes the confidence to **drop a lot**, that region is very important for the prediction.
- If covering a region barely changes the confidence, that region doesn't matter much.

---

---

# 4.8 Neural Style Transfer

**Neural style transfer** is a technique that takes two images — a **content image** (e.g., a photo of a city) and a **style image** (e.g., Van Gogh's "Starry Night" painting) — and creates a **new image** that has the content (objects, layout) of the first image but painted in the artistic style of the second image.

> Think of it like asking an artist: "Paint my photograph, but make it look like a Van Gogh painting."

**How it works (Gatys et al., 2015):**

Use a pre-trained CNN (usually **VGG-19**) as a **feature extractor**. The CNN's weights are **frozen** (not updated). Instead, we start with a blank (random noise) or copy of the content image and repeatedly adjust its **pixel values** using gradient descent until it looks right.

> **Feature extractor** = a network used only to extract (pull out) useful patterns from images, not to classify them.

### Content Representation

When an image passes through a CNN, the feature maps at **deep layers** capture the **content** — the shapes, objects, and spatial layout of the image (not colors or textures, but "what is where").

The **content loss** measures how different the generated image's features are from the content image's features at a chosen layer $l$.

### Style Representation — Gram Matrix

Style is not about "what" is in the image, but about "how" it looks — the textures, colors, and brush strokes.

To capture style, we use the **Gram matrix**. It measures **correlations** (relationships) between different filter responses.

> **Gram matrix** = a table where each entry tells you how much two filters "fire together." If filter A (which detects blue color) and filter B (which detects swirly shapes) both activate strongly at the same places, the Gram matrix captures this — meaning the style includes "blue swirls."

The Gram matrix throws away spatial information (where things are) and keeps only the style information (what patterns co-occur).

The **style loss** measures how different the generated image's Gram matrix is from the style image's Gram matrix, summed across multiple layers to capture style at different scales — fine textures (early layers) and large patterns (deep layers).

### Total Loss

$$L_{\text{total}} = \alpha \cdot L_{\text{content}} + \beta \cdot L_{\text{style}}$$

- $\alpha$ controls how much to preserve the **content**.
- $\beta$ controls how much to apply the **style**.
- If $\beta$ is much larger than $\alpha$, the result will be very stylized (more like the painting). If $\alpha$ is larger, the result will look more like the original photo.

The generated image starts as random noise (or a copy of the content image) and is updated step by step using **gradient descent on the pixels** — not on the network weights! — until the total loss is small enough.

---

---

# 5.2 Motion Analysis and Optical Flow

> **Explain how optical flow is used for motion analysis in video sequences. Discuss at least two deep learning approaches that estimate optical flow and their comparative strengths. (Tutorial)**

## 5.2.1 Optical Flow

A video is just a sequence of images (called **frames**) shown quickly one after another. When something moves in a video — a car driving, a ball flying, a person walking — the pixels that make up that object shift position from one frame to the next.

**Optical flow** is a way to measure this movement. For every pixel in one frame, optical flow tells us: **"Where did this pixel go in the next frame?"** The answer is a small arrow (a **displacement vector**) with two numbers $(u, v)$:

- $u$ = how far the pixel moved **horizontally** (left/right)
- $v$ = how far the pixel moved **vertically** (up/down)

> **Displacement vector** = a pair of numbers that describe the direction and distance of movement.

If you draw all these little arrows on the image, you get a "flow field" — a picture that shows the direction and speed of motion at every pixel.

### The Brightness Constancy Assumption

The basic idea behind optical flow is simple: **a pixel keeps the same brightness as it moves.** A white dot on a ball stays white whether the ball is on the left of the screen or the right.

In math:

$$I(x, y, t) = I(x + u, y + v, t + 1)$$

This says: the brightness $I$ at position $(x, y)$ in frame $t$ equals the brightness at the **new position** $(x+u, y+v)$ in the **next frame** $t+1$.

From this simple equation, we can derive:

$$I_x u + I_y v + I_t = 0$$

- $I_x$ = how fast brightness changes going **left to right** (spatial gradient in x)
- $I_y$ = how fast brightness changes going **top to bottom** (spatial gradient in y)
- $I_t$ = how fast brightness changes **over time** (temporal gradient)

> **Gradient** = the rate of change. A spatial gradient tells how quickly pixel brightness changes across space. A temporal gradient tells how quickly it changes over time.

**The problem:** We have **one equation** but **two unknowns** ($u$ and $v$). One equation is not enough to solve for two things. This is called the **aperture problem** — like trying to figure out which way a striped pole is moving when you can only see it through a tiny hole (aperture).

> **Aperture problem** = the difficulty of determining the true direction of motion from local information alone.

### Classical (Traditional) Methods

To solve the aperture problem, we need extra assumptions:

- **Lucas-Kanade (1981):** Assumes that all pixels in a small **neighborhood** (e.g., a 5×5 block of pixels) move the same way. This gives us many equations (one per pixel in the block), enough to solve for $u$ and $v$ using **least squares** (a method to find the best-fit answer when you have more equations than unknowns). It produces **sparse** flow — meaning it only computes flow at certain feature points, not every pixel. Works best for small, slow movements.

- **Horn-Schunck (1981):** Assumes that nearby pixels have **similar** flow — the motion should change smoothly, not jump around. It computes flow for **every** pixel (**dense** flow), but is more sensitive to noise (random errors in pixel values).

> **Sparse** = computed only at some selected points. **Dense** = computed at every single pixel.

---

## 5.2.2 Deep Learning Approaches for Optical Flow

We can train a neural network to learn optical flow directly from data. Give the network two frames, and it outputs the flow field. Here are two major deep learning approaches:

### 1. FlowNet (2015) and FlowNet 2.0 (2017)

FlowNet was the **first CNN** (Convolutional Neural Network) trained to predict optical flow from raw image pairs. It has two versions:

- **FlowNetS (Simple):** Takes two frames, stacks them together (so the input has 6 channels — 3 color channels from each frame), and passes them through an **encoder-decoder** network.
  - The **encoder** (compression part) shrinks the images and extracts important features.
  - The **decoder** (expansion part) takes those features and blows them back up to full size, outputting a flow vector at each pixel.

- **FlowNetC (Correlation):** Instead of stacking the two frames, it processes each frame through its **own separate encoder**. Then it computes a **correlation layer** — this layer compares features from the two frames to find which parts match (like playing a "spot the difference" game). After finding matches, the decoder produces the flow field.

**FlowNet 2.0** improved accuracy by **stacking** multiple FlowNets one after another like a chain. The first network handles **big movements**, and the following networks **refine** the result to fix small details.

### 2. RAFT — Recurrent All-Pairs Field Transforms (2020)

RAFT is a newer and more accurate method. Instead of predicting the flow in one shot, it **gradually improves** its guess over many steps — like erasing and redrawing your answer again and again until it's perfect.

**How RAFT works (3 stages):**

1. **Feature extraction:** A CNN processes both frames and turns them into **feature maps** (compact representations that capture important patterns like edges, textures, and shapes).

2. **Correlation volume:** RAFT compares **every** feature in Frame 1 with **every** feature in Frame 2 by computing their **dot product** (a simple math operation that measures similarity). The result is a big 4D table (called a **correlation volume**) that stores how similar any two locations are across the two frames.

3. **Iterative update:** A small recurrent network (using a **GRU** — a type of memory unit) repeatedly looks at the correlation volume, checks "how good is my current flow guess?", and produces a small correction. After many iterations (typically 12–32 rounds), the flow converges to an accurate answer.

### FlowNet vs. RAFT — Comparison

| Property            | FlowNet / FlowNet 2.0            | RAFT                                          |
| :------------------ | :------------------------------- | :-------------------------------------------- |
| **How it works**    | Encoder-decoder (stacked chain)  | Correlation volume + GRU iterative refinement |
| **Flow estimation** | One forward pass (or a chain)    | Many iterations, gradually improving          |
| **Accuracy**        | Good starting point              | Best-in-class (state-of-the-art)              |
| **Large movements** | FlowNet 2.0 handles via stacking | Handles naturally via all-pairs correlation   |
| **Generalization**  | Moderate                         | Works well even on new, unseen datasets       |

> **State-of-the-art** = the best-performing method at the current time.
>
> **Generalization** = the ability to perform well on new data that the model was not trained on.

### Applications of Optical Flow

- **Action recognition:** Optical flow gives the network explicit motion information. For example, a "waving" action creates a specific flow pattern. **Two-stream networks** use one stream for the raw image (appearance) and another stream for optical flow (motion).
- **Video stabilization:** If the camera is shaking, the flow vectors show that shake. Software can use this to cancel out the unwanted movement and produce a smooth video.
- **Object segmentation:** A moving car produces flow arrows that point in a different direction than the still background. This difference helps separate (segment) moving objects from the background.
- **Frame interpolation:** If you have Frame 1 and Frame 3, optical flow can help generate Frame 2 (the in-between frame), creating slow-motion effects.

> **Segmentation** = dividing an image into regions, each belonging to a different object.
>
> **Frame interpolation** = creating new frames between existing ones to make video smoother.

---

---

# 5.3 3D Data and Convolution

> **Describe how 3D convolution differs from standard 2D convolution and explain its role in video-based action recognition. What are the computational trade-offs involved? (Tutorial)**

## 5.3.1 From 2D to 3D Convolution

### Quick Recap: 2D Convolution

In a normal CNN, a small **2D filter** (e.g., 3×3) slides across a **single image** (height × width) and produces a **feature map** — a new image that highlights certain patterns like edges or textures.

When we apply a 2D CNN to a video, it processes **each frame separately**, one at a time. It can see what's happening **within** a frame (spatial features — shapes, objects, colors) but it has **no idea** how things change **across** frames. It cannot learn motion.

> **Spatial** = related to space (height and width of an image).
>
> **Temporal** = related to time (the sequence of frames in a video).

### What is 3D Convolution?

A **3D convolution** adds a **time dimension** to the filter. Instead of a 3×3 filter that looks at one frame, a 3D filter might be **3×3×3** — it covers **3 frames** at once, looking at a 3×3 region **in each of those 3 frames** simultaneously.

As this 3D filter slides across the video (moving in space AND in time), it can detect patterns that happen **over time** — like a hand moving from left to right across multiple frames. These are called **spatiotemporal features** (features that combine both space and time information).

> **Spatiotemporal** = involving both space (where things are) and time (when things happen).

### Why Does 3D Convolution Matter?

Imagine a person waving their hand. In any single frame, you just see a hand in one position. But across 3 frames, you see the hand in three different positions — that's the "waving" pattern. A 2D filter processing frames one by one **cannot** see this pattern. A 3D filter spanning 3 frames **can** detect it directly.

This makes 3D convolution powerful for tasks like **action recognition** — telling the difference between "running" and "walking," or between "clapping" and "waving."

### 2D vs. 3D Convolution — Comparison

| Property               | 2D Convolution             | 3D Convolution                               |
| :--------------------- | :------------------------- | :------------------------------------------- |
| **Filter shape**       | height × width (e.g., 3×3) | time × height × width (e.g., 3×3×3)          |
| **Input**              | One frame at a time        | A clip (stack of multiple frames)            |
| **Output**             | 2D feature map             | 3D feature volume (keeps the time dimension) |
| **Can detect motion?** | No (spatial only)          | Yes (sees patterns across frames)            |
| **Computation cost**   | Lower                      | Higher (roughly $k_t$ times more)            |

> $k_t$ = the size of the filter in the time dimension (e.g., 3 for a filter that spans 3 frames).

### Computational Trade-offs (The Cost of 3D)

3D convolution is more powerful but also more expensive:

- **More parameters (weights):** A 3×3 2D filter has 9 weights. A 3×3×3 3D filter has 27 weights — **3 times more**. More weights means the network is larger and needs more data to train properly.

  > **Parameters** = the learnable numbers (weights) inside a neural network. More parameters = bigger model = more memory needed.

- **More computation (FLOPs):** Since the 3D filter slides across an extra dimension (time), the number of multiply-and-add operations is much higher. A 3D CNN can be **10 to 100 times slower** than a 2D CNN.

  > **FLOPs (Floating Point Operations)** = a count of how many math operations (like multiplications and additions) the network needs to perform. More FLOPs = slower.

- **More memory:** The intermediate feature maps are now 3D volumes (time × height × width × channels) instead of 2D maps. Storing these volumes takes much more memory (RAM/GPU memory).

### How to Reduce the Cost — (2+1)D Convolution

A smart trick called **(2+1)D convolution** (used in a model called **R(2+1)D**) breaks the 3D filter into two simpler steps:

1. First, apply a **spatial-only** filter ($1 × k × k$) — this looks at patterns within each frame (like a normal 2D filter).
2. Then, apply a **temporal-only** filter ($k_t × 1 × 1$) — this looks at how those patterns change over time.

This factorization uses fewer parameters, is computationally cheaper, and often actually **improves** accuracy because it adds an extra **non-linearity** (ReLU activation) between the two steps.

> **Factorization** = breaking one complex operation into two simpler operations that together do the same job.
>
> **Non-linearity** = a mathematical function (like ReLU) that lets the network learn complex, non-straight-line patterns. More non-linearities = the network can learn richer patterns.
