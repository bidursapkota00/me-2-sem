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

# 4.9 Image Captioning System

An **image captioning system** looks at a photo and writes a sentence describing it — like "A dog sitting on green grass near a red ball."

It combines two types of neural networks:

- A **CNN** (to understand the image) — the "eyes"
- An **RNN/LSTM** (to generate the sentence) — the "mouth"

This is called an **encoder-decoder framework**: the CNN **encodes** (compresses) the image into a compact representation, and the LSTM **decodes** (expands) that representation into a sentence.

> **Encoder** = takes raw input and converts it into a meaningful summary.
> **Decoder** = takes the summary and produces the desired output.
>
> **LSTM (Long Short-Term Memory)** = a type of RNN that is good at remembering information over long sequences (sentences, paragraphs).

## 4.9.1 Architecture

**Encoder — CNN:** Take a pre-trained CNN (like ResNet or VGG) and remove the last classification layer. What remains gives us a **feature vector** — a list of numbers that describes the image's visual content. This is like the CNN saying: "I see a dog, grass, a ball, outdoor scene..."

**Decoder — LSTM:** The LSTM generates the caption **one word at a time**. At each step, it looks at:

- The image features (what's in the picture)
- The words it has already generated (what it has said so far)

And predicts the **next word**.

**Basic pipeline (Show and Tell model):**

1. Pass the image through the CNN → get a feature vector $v$.
2. Feed $v$ to the LSTM as the starting input.
3. At each time step $t$, the LSTM receives the **embedding** (numerical representation) of the previous word $w_{t-1}$ and outputs a probability for every word in the vocabulary. The most likely word becomes $w_t$.
4. This continues until the model outputs an **\<END\> token** — a special word that means "I'm done talking."

> **Embedding** = converting a word into a list of numbers that captures its meaning. Similar words (like "dog" and "puppy") get similar numbers.
>
> **Vocabulary** = the set of all words the model knows.

## 4.9.2 Attention Mechanism

The basic model compresses the **entire image** into a single vector — but this is like trying to describe a complex scene after looking at it for one second with your eyes closed. A lot of detail is lost. This is called an **information bottleneck**.

The **attention mechanism** fixes this. Instead of one vector, the CNN produces a **grid of feature vectors** (e.g., 14×14 = 196 vectors, each describing a different region of the image). When generating each word, the LSTM "looks at" (attends to) the most relevant region.

**How it works at each time step $t$:**

1. **Compute attention weights** $\alpha_{t,i}$: For each of the 196 regions, calculate a score saying "how relevant is this region for the word I'm about to generate?" Then normalize these scores using **softmax** so they add up to 1.

$$e_{t,i} = f_{\text{att}}(h_{t-1}, a_i) \quad;\quad \alpha_{t,i} = \frac{\exp(e_{t,i})}{\sum_j \exp(e_{t,j})}$$

> $h_{t-1}$ = the LSTM's previous hidden state (its memory of what it has generated so far).
> $a_i$ = the feature vector for region $i$ of the image.

2. **Compute context vector** $z_t$: Take a **weighted sum** of all region features — regions with higher attention weight contribute more.

$$z_t = \sum_{i=1}^{L} \alpha_{t,i} \cdot a_i$$

3. Feed $z_t$ and the previous word's embedding into the LSTM to generate the next word.

**Example:** When the model generates the word "dog," it pays attention to the part of the image where the dog is. When it generates "grass," it shifts attention to the grass area.

## 4.9.3 Training

**Dataset:** We need thousands of image-caption pairs. A popular dataset is **MS COCO**, where each image comes with 5 different captions written by humans.

**Training process:**

1. The CNN encoder is **pre-trained on ImageNet** (transfer learning — reusing knowledge learned from millions of images). Its weights may be **frozen** (kept fixed) or **fine-tuned** (adjusted slightly with a small learning rate).

2. During training, we use **teacher forcing** — at each time step, we give the LSTM the **correct previous word** (from the human-written caption), not the word it predicted. This is like a teacher correcting a student at every step so they don't go off track.

3. The **loss function** is **cross-entropy loss** — it measures how well the model's predicted word probabilities match the actual correct words, summed over the whole sentence:

$$L = -\sum_{t=1}^{T} \log p(w_t | w_1, ..., w_{t-1}, I)$$

> This says: for each word in the caption, how surprised was the model by the correct answer? Less surprise = lower loss = better model.

4. Gradients flow backward through the LSTM and (if the CNN is not frozen) through the CNN too, allowing **end-to-end training** — the entire system learns together.

> **End-to-end training** = training the whole pipeline (CNN + LSTM) as one system, rather than training each part separately.

**Inference (generating captions for new images):**

At test time, the model generates words **autoregressively** — it uses its own predicted word as input to predict the next word (no teacher forcing, since we don't have the answer).

Instead of just picking the single best word at each step (**greedy decoding**), we use **beam search** — keep the top-$k$ (e.g., top-3) candidate sentences at each step and continue expanding all of them. At the end, pick the best complete sentence. This usually produces better captions.

> **Beam search** = exploring multiple possible sentences simultaneously and choosing the best one. Like considering multiple routes on a GPS before picking the fastest.

**How do we measure caption quality?**

| Metric     | What it measures                                                                                                                                                   |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **BLEU**   | How many n-grams (word chunks of length n) in the generated caption match the reference. Focuses on **precision** (are the generated words correct?).              |
| **METEOR** | Like BLEU, but also considers **synonyms** (words with similar meaning) and **stemming** (treating "running" and "run" as the same).                               |
| **CIDEr**  | Measures consensus — does the generated caption match what **most humans** would say? Uses **TF-IDF** weighting (words that are unique to this image matter more). |
| **ROUGE**  | Focuses on **recall** — how many of the reference words appear in the generated caption?                                                                           |

> **Precision** = of the words I generated, how many are correct?
> **Recall** = of the correct words, how many did I generate?
> **n-gram** = a sequence of n consecutive words. "the dog" is a 2-gram (bigram). "the brown dog" is a 3-gram (trigram).
