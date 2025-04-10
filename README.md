 Transformer Translation Model

A neural machine translation model built using the Transformer architecture for English to Italian translation.

 Overview

This project implements a transformer model as described in the "Attention is All You Need" paper by Vaswani et al. It uses the OPUS Books dataset to train an English to Italian translation system.

 Model Architecture

- **Encoder-Decoder Transformer** with 6 layers
- **Multi-head Attention** with 8 heads
- **Model Dimension**: 512
- **Feed-Forward Dimension**: 2048

 Dataset

The model is trained on the OPUS Books corpus which contains parallel texts from books in multiple languages.

 Training

The model can be trained using:
```python
python train.py
