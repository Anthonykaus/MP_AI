import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

class ArchitectureGenerator:
    def __init__(self):
        self.generator = self._build_generator()

    def _build_generator(self):
        inputs = Input(shape=(100,))
        x = Dense(256, activation='relu')(inputs)
        x = Dense(512, activation='relu')(x)
        outputs = Dense(28*28, activation='sigmoid')(x)  # Example output for an image
        model = Model(inputs=inputs, outputs=outputs)
        return model

    def generate(self):
        noise = tf.random.normal([1, 100])
        generated_architecture = self.generator(noise)
        return generated_architecture.numpy().reshape(28, 28)  # Example reshaping

# Example usage
if __name__ == "__main__":
    arch_gen = ArchitectureGenerator()
    new_arch = arch_gen.generate()
    print(new_arch.shape)
