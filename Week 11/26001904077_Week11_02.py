import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)# set random seed to 42

# sigmoid function as activation function
def sigmoid(x):
    return 1/(1+np.exp(-x))

# derivative of the sigmoid function to get the minimum loss
def sigmoidSlope(x):
    return x*(1-x)

# initialization of input(x) and target output(y)
x = [[0,0,1],
     [0,1,1],
     [1,0,1],
     [1,1,1]]

inputData = np.array(x)

probNum = 0 #problem number is initialized to 0

# sets the target output to y based on problem number variable (probNum)
def targetOutput(probNum):
    if probNum == 0:# problem 1
        y = [0, 0, 1, 1] # referenceOutput 1
    elif probNum == 1: # problem 2
        y = [0, 1, 1, 0] # referenceOutput 2
    return y

# function to plot the subgraph for each of the four variables
def plotSubgraph(meanOutputError,trainingIter,index,title):
    plt.subplot(2, 2, index)
    plt.plot([i for i in range(trainingIter)], meanOutputError)
    plt.title(title)
    plt.xlabel("Number of iterations")
    plt.ylabel("Mean output error")

trainingNumber = 900 #number of iterations for training

# loops to do training process for both single and multi layered networks for both problem 1 and 2
while probNum<2:
    # Initialization of the target output(y), first referenceOutput 1 is chosen then referenceOutput 2
    y = targetOutput(probNum)
    referenceOutput = np.atleast_2d(y).T
    # initialization of the weights for input layer(weights01) and hidden layer(weights02)
    weights01 = 2 * np.random.random((3, 1)) - 1

    #initialize the meanOutputErrorList for storing the mean output error values during training
    meanOutputErrorList = []
    # training procedure for single-layer neural network
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
        meanOutputError = np.mean(np.abs(outputError))
        meanOutputErrorList.append(meanOutputError)
    #prints the output result after training the network
    print("Single-layer neural network - problem["+ str(probNum+1) + "]")
    print("Output values after " + str(trainingNumber) + " training iterations:")
    print(np.round(outputPerceptionLayer, decimals=2))
    # plot the graph for single-layered network for each problem of the mean output error
    plotSubgraph(meanOutputErrorList,trainingNumber,2*probNum+1,"Single-layer network - problem ["+str(probNum+1)+ "]" )

    # reinitialize weights for multi-layer network
    weights01 = 2 * np.random.random((3, 4)) - 1
    weights02 = 2 * np.random.random((4, 1)) - 1

    # empty the meanOutputErrorList for multi layered network training
    meanOutputErrorList = []
    # the multi-layer neural network training procedure for fixed number of iterations (trainingNumber)
    for j in range(trainingNumber):
        #set the input data for all layers as forward propogation
        inputLayer = inputData
        hiddenLayer = sigmoid(np.dot(inputLayer, weights01))
        outputPerceptronLayer = sigmoid(np.dot(hiddenLayer, weights02))

        # the difference between the output perceptron layer and the reference output
        outputError = referenceOutput - outputPerceptronLayer

        # the divergence from the reference output (outputError) multipltied
        # by the slope of the sigmoid function at value of the output perceptron layer
        outputDelta = outputError * sigmoidSlope(outputPerceptronLayer)

        # start of backpropagation
        hiddenLayerError = outputDelta.dot(weights02.T)

        # Error contributed in the hidden layer (hiddenLayerError) multiplied
        # by the slope of the sigmoid function at value of the hidden layer
        hiddenLayerDelta = hiddenLayerError * sigmoidSlope(hiddenLayer)

        # update the weights to approach the weights which produce least error
        weights02 += hiddenLayer.T.dot(outputDelta)
        weights01 += inputData.T.dot(hiddenLayerDelta)
        meanOutputError = np.mean(np.abs(outputError))
        meanOutputErrorList.append(meanOutputError)

    # prints the output result after training the network
    print("Multi-layer neural network - problem["+ str(probNum+1) + "]")
    print("Output values after " + str(trainingNumber) + " training iterations:")
    print(np.round(outputPerceptronLayer))
    # plot the graph for multi-layered network for each problem of the mean output error
    plotSubgraph(meanOutputErrorList, trainingNumber, 2*probNum + 2,
                 "Multi-layer network - problem [" + str(probNum+1) + "]")

    probNum += 1# increment problem number by 1

plt.show() #show the final graph including all four variables



























