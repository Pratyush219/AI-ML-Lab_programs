import random
from math import exp

def init_network(n_inputs, n_hidden, n_outputs):
    network = []
    hidden = [{'weights': [random.random() for i in range(n_inputs + 1)]} for j in range(n_hidden)]
    output = [{'weights': [random.random() for i in range(n_hidden + 1)]} for j in range(n_outputs)]
    network = [hidden, output]
    return network

def activate(weights, inputs):
    result = weights[-1]
    for i in range(len(inputs)):
        result += weights[i] * inputs[i]
    return result

def sigmoid(x):
    return 1/(1 + exp(-x))

def sigmoid_deriative(x):
    return x * (1 - x)

def forward_propagate(network, data):
    inputs = data
    for layer in network:
        new_input = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = sigmoid(activation)
            new_input.append(neuron['output'])
        inputs = new_input
    return inputs

def backward_propagate(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        if i == len(network) - 1:
            for j in range(len(layer)):
                neuron = layer[j]
                neuron['delta'] = (expected[j] - neuron['output']) * sigmoid_deriative(neuron['output'])
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                error = 0
                for nextNeuron in network[i + 1]:
                    error += nextNeuron['weights'][j] * nextNeuron['delta']
                neuron['delta'] = error * sigmoid_deriative(error)

def update_weights(network, l_rate, data):
    inputs = data
    for i in range(len(network)):
        layer = network[i]
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i - 1]]
        for neuron in layer:
            for j in range(len(inputs)):
                neuron['weights'][j] += l_rate * inputs[j] * neuron['delta']
            neuron['weights'][-1] += l_rate * neuron['delta']

def train_network(dataset, l_rate, n_epochs, n_inputs, n_hidden, n_outputs):
    network = init_network(n_inputs, n_hidden, n_outputs)
    for epoch in range(n_epochs):
        sum_error = 0
        for data in dataset:
            obtained = forward_propagate(network, data[:-1])
            expected = [i for i in range(n_outputs)]
            sum_error += sum([(expected[i] - obtained[i]) for i in range(n_outputs)])
            backward_propagate(network, expected)
            update_weights(network, l_rate, data)
        print(f'epoch={epoch}, l_rate={l_rate:.3f}, sum_error={sum_error:.3f}')
    for layer in network:
        print(layer)

dataset = [[random.uniform(0, 4) for i in range(2)] for i in range(10)]
for data in dataset:
    data.append(random.randint(0, 1))
n_inputs = len(dataset[0]) - 1
n_hidden = 2
n_outputs = len(set([data[-1] for data in dataset]))
train_network(dataset, 0.5, 20, n_inputs, n_hidden, n_outputs)