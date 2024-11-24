import numpy as np

def normalize_data(data):
    return data / 255.0

def augment_data(images, labels):
    augmented_images = []
    augmented_labels = []

    for image, label in zip(images, labels):
        # Example augmentation: horizontal flip
        flipped_image = np.fliplr(image)
        augmented_images.extend([image, flipped_image])
        augmented_labels.extend([label, label])

    return np.array(augmented_images), np.array(augmented_labels)

# Example usage
if __name__ == "__main__":
    (x_train, y_train), (_, _) = tf.keras.datasets.mnist.load_data()
    normalized_images = normalize_data(x_train)
    augmented_images, augmented_labels = augment_data(normalized_images, y_train)
    print(augmented_images.shape, augmented_labels.shape)
