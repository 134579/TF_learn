import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

plt.imshow(mnist.train.images[0].reshape([28, 28]), cmap=plt.get_cmap("Greys"))
plt.show()



