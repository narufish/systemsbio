
import numpy as np

# diplays choices for output reference
print("1: [0,0,1,1]")
print("2: [0,1,1,0]")
print("4: [0,1,0,1]")

# Input for user to choose which output reference to use
while True:
    choice = input("Choose which output to use as reference [1,2,3]:")
    try: #if the user entered a non-integer or integer which are not in the range 1<= x <=3, then user is asked to input again
        choice = int(choice)
        if choice>=1 and choice<=3:
            break
        else:
            print("Please enter valid integer input")
    except ValueError:
        print("Please enter integer input")

# random seed set to 1
np.random.seed(1)

# sigmoid function is used for the activation function in training
def sigmoid(x):
    y = 1/(1 + np.exp(-x))
    return y

# Calculate the slope by using derivative of the sigmoid function
def sigmoidSlope(x):
    return x*(1-x)

# randomly initialize the weights for the synapses connecting input and output layer
# mean of 0
weights01 = 2*np.random.random((3,1)) - 1

# the input data and reference output is initialized
x = [[0,0,1],
     [0,1,1],
     [1,0,1],
     [1,1,1]]

# depending on the user's choice, the different reference output is set
# this is based on the exercise 4
if choice==1: y = [0,0,1,1]
elif choice==2: y = [0,1,1,0]
elif choice==3: y = [0,1,0,1]

# create numpy array from the initialized input and output
inputData = np.array(x)
referenceOutput = np.atleast_2d(y).T

# number of iterations for training
# the number of iterations for the model to reach the reference output value is 37000
trainingNumber = 900

# training process
for i in range(trainingNumber):
    inputLayer = inputData
    # calculates the predicted output from the current training model
    outputPerceptionLayer = sigmoid(np.dot(inputLayer, weights01))
    # calculates the error which is difference from actual output to predicted output from the model
    # error = y - a, where a is predicted output
    outputError = referenceOutput - outputPerceptionLayer
    # calculates the loss slope (derivative), dw, of the predicted error
    # loss slope find the point of minimum loss from the loss function
    # we use te chain rule to get the loss slope
    # loss slope, dz = sigmoid error x loss slope
    #                  = (y-a) x [a x (1-a)]
    outputDelta = outputError * sigmoidSlope(outputPerceptionLayer)
    # dw = dz * x
    # w = w + dw
    # whereby, x = input, w = weights, dw = weight derivative
    weights01 += np.dot(inputLayer.T, outputDelta)

# prints the output from the network after undergoing the specified number of training iterations
print("Output values after " + str(trainingNumber) + " training iterations:")
print(np.round(outputPerceptionLayer,decimals=2))








