import numpy as np

class LogReg(self):

    #Uses logistic regression and gradient decent to optimize a weight vector

    def __init__(self, data, tags, alpha, maxIter):
        """
        The training vector is stored in two parts, the data and the tags.
        The data will be converted into numpy array
        """
        

        self._data = np.array(data)
        self._data = 1 + self._data

        self._tags = np.array(tags)

        self._weights = np.array()

        self._alpha = alpha

        self._costs = [] 

        self._maxIter = maxIter

    def predict(self, feature, weight):
        """
        Takes the dot product of one feature and the weight vector
        and returns the result of them entered into the sigmoid function
        """



    def __repr__(self):
        """used for making the terminal look pretty. :)
        gives how many iterations there are, n dimensions, cost over time
        LogRegtrains and shit. Idk actually but we'll see. yikers.
        """
        s = 'This has been trained for %05d iterations.' + '\n' +'There are %05d data points.' + '\n' +'Cost overflow bullshit.' % (self.maxIter, self.data)
        return s 