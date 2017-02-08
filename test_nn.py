import numpy as np


def sigmoid(x):
    return 1 / (1+np.exp(-x))


def sigmoid_derivative(x):
    return x*(1-x)


def normalize(v):
    norm = np.linalg.norm(v, ord=1)
    if norm == 0:
        norm = np.finfo(v.dtype).eps
    return v/norm, norm


class Train:
    def __init__(self):
        self.weights = 2 * np.random.random((2, 1)) - 1

    def train(self, inputs, outputs, iterations):
        for i in xrange(iterations):
            res = self.think(inputs)
            error = outputs - res
            adjustment = np.dot(inputs.T, error*sigmoid_derivative(res))
            self.weights += adjustment

    def think(self, inputs):
        return sigmoid(np.dot(inputs, self.weights))

"""
input_set = np.array(
    [[0, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1]]
)
"""

input_set = np.array(
    [[3, 4],
     [4, 5],
     [1, 2],
     [1, 1]]
)

output_set = np.array([
    [5, 6.40, 2.236, 1.414]
]).T

np.random.seed(1)


t = Train()

normal_inputs, norm1 = normalize(input_set)
normal_outputs, norm2 = normalize(output_set)


#print t.weights
t.train(normal_inputs, normal_outputs, 1000)

normal_test, norm_test = normalize(np.array([3, 4]))

print np.dot(normal_test, t.weights)
#print t.weights
#print t.think(np.array([1, 0, 0])), np.dot(np.array([1,1,1]), t.weights)