import numpy as np

class LogReg:

    #Uses logistic regression and gradient decent to optimize a weight vector

    def __init__(trainingData, trainingTags):
        """
        The training vector is stored in two parts, the data and the tags.
        The data will be converted into numpy array
        """
        

        self._trainingData = np.array(trainingData)
        self._trainingData = 1 + self._trainingData


        self._trainingTags = np.array(trainingTags)



    def sigmoid(feature, weight):
        """
        takes the dot product of one feature and the weight vector
        and returns the result of them entered into the sigmoid function
        """



    def __repr__(self):
        """used for making the terminal look pretty. :)
        gives how many iterations there are, n dimensions, cost over time
        LogRegtrains and shit. Idk actually but we'll see. yikers.
        """
        s = 'This has been trained for %N iterations.' \
        '\n' \
        +'There are %N data points.' \
        '\n' \
        +'Cost overflow bullshit.' %(self.N)
        return s 