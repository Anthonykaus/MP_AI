
#### `architecture/hybrid_neural_network.py`
```python
import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, LSTM

class HybridNeuralNetwork(tf.keras.Model):
    def __init__(self, input_shape=(64, 64, 3), num_classes=10):
        super(HybridNeuralNetwork, self).__init__()
        # CNN layers
        self.conv1 = Conv2D(32, (3, 3), activation='relu', input_shape=input_shape)
        self.pool1 = MaxPooling2D((2, 2))
        self.conv2 = Conv2D(64, (3, 3), activation='relu')
        self.pool2 = MaxPooling2D((2, 2))
        self.flatten = Flatten()
        # RNN layers
        self.lstm1 = LSTM(64)
        # Dense layer
        self.dense1 = Dense(num_classes, activation='softmax')

    def call(self, inputs):
        x = self.conv1(inputs)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.pool2(x)
        x = self.flatten(x)
        x = self.lstm1(tf.expand_dims(x, 1))  # Add time dimension for LSTM
        return self.dense1(x)

    def summary(self):
        inputs = tf.keras.Input(shape=(64, 64, 3))
        outputs = self.call(inputs)
        model = tf.keras.Model(inputs=inputs, outputs=outputs)
        print(model.summary())
