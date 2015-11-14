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



