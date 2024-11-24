import tensorflow as tf
from architecture.spiking_neural_network import SpikingNeuralNetwork

class LocalTrainingPipeline:
    def __init__(self, model):
        self.model = model

    def prepare_data(self):
        (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0
        return (x_train, y_train), (x_test, y_test)

    def train(self, epochs=10):
        (x_train, y_train), (x_test, y_test) = self.prepare_data()
        self.model.build_model()
        self.model.compile_model()
        self.model.train(x_train, y_train, epochs=epochs)
        return self.model.evaluate(x_test, y_test)

# Example usage
if __name__ == "__main__":
    snn = SpikingNeuralNetwork()
    pipeline = LocalTrainingPipeline(snn)
    evaluation_results = pipeline.train(epochs=5)
    print(evaluation_results)
