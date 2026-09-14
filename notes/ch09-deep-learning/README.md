# Chapter 9: Deep Learning

Transcribed notes from *Data Science and Machine Learning: Mathematical and Statistical Methods* (Kroese, Botev, Taimre, Vaisman), Chapter 9, "Deep Learning" (PDF pages 341-372 / printed pages 323-354).

| File | Section | PDF pages | Description |
|---|---|---|---|
| [9.1-introduction.md](9.1-introduction.md) | 9.1 Introduction | 341-344 | Supervised learning recap, hypothesis space $\mathcal{G}_L$ and the approximation–estimation tradeoff, Kolmogorov's superposition theorem (Theorem 9.1), and the motivation for activation functions. |
| [9.2-feed-forward-neural-networks.md](9.2-feed-forward-neural-networks.md) | 9.2 Feed-Forward Neural Networks | 344-349 | Formal definition of layers, weights/biases, network depth/width, Algorithm 9.2.1 (feed-forward propagation), Examples 9.1-9.3 (regression, multi-logit classification, density estimation), network architecture/sparsity, and convolutional neural networks (CNNs). |
| [9.3-back-propagation.md](9.3-back-propagation.md) | 9.3 Back-Propagation | 349-352 | Training loss and gradient notation, Theorem 9.2 (gradient of training loss) with proof, Algorithms 9.3.1-9.3.2 (back-propagation), ReLU vs. logistic saturation, Example 9.4 (squared-error and cross-entropy loss gradients). |
| [9.4-methods-for-training.md](9.4-methods-for-training.md) | 9.4 Methods for Training (incl. 9.4.1-9.4.4) | 353-359 | Steepest descent & stochastic gradient descent (9.4.1), Levenberg–Marquardt (9.4.2), limited-memory BFGS (9.4.3, Algorithms 9.4.3-9.4.4), and adaptive gradient methods — AdaGrad, Adam (Algorithm 9.4.5), and momentum (9.4.4). |
| [9.5-examples-in-python.md](9.5-examples-in-python.md) | 9.5 Examples in Python (incl. 9.5.1-9.5.2) | 359-367 | Full Python code: (9.5.1) a from-scratch neural network with stochastic gradient descent for polynomial regression; (9.5.2) a PyTorch CNN for Fashion-MNIST image classification. Includes "Further Reading" pointers. |
| [exercises.md](exercises.md) | Exercises | 368-372 | All 17 end-of-chapter exercises (softmax invariance, projection pursuit, SGD with reshuffling, KL divergence/BFGS derivations, QR-based Hessian updates, multi-logit classifier on the seeds dataset, comparisons of training algorithms, etc.). |
