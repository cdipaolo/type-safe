import numpy as np

class LogReg():

    #Uses logistic regression and gradient decent to optimize a weight vector

    def __init__(self, data, tags, alpha=0.05, maxIter=100):
        """
        The training vector is stored in two parts, the data and the tags.
        The data will be converted into numpy array from a list

        >>> model = LogReg([-10, -10, -10, -10, 10, 10, 10, 10], \
                           [0, 0, 0, 0, 1, 1, 1, 1], alpha=0.01, maxIter=100)
        >>> model.train()
        >>> model.predict(10)
        1
        >>> model.predict(-10)
        0
        """
        self._data = np.array(data)

        # add a column of 1s for the y offset feature
        self._data = np.hstack(([[1]]*self._data.shape[0], self._data))

        self._tags = np.array(tags)

        self._weights = np.array([]*self._data.shape[0])

        self._alpha = alpha

        self._costs = []

        self._maxIter = maxIter


    def predict(self, x):
        """
        Takes the dot product of one feature and the weight vector
        and returns the result of them entered into the sigmoid function

        >>> LogReg.predict()
        """
        dot_p = np.dot(x, self._weight)

        return (1 / (1 - np.exp(-1 * dot_p)))

        
    def train(self):
        """ trains the weight vector on the training data
        """
        alpha = self._alpha
        tempw = np.copy(self._weight)
        
        # going through the training data _maxIter times
        for iter in range(_maxIter):
        
            # moving through the training data
            for i in range(self._data.size):
                xi = self._data[i]
                # the predicted value
                y_hat = self.predict(xi)
                # the target value
                yi = self._tags[i]
                
                # calculating the delta by which to adjust this particular weight
<<<<<<< HEAD:logistic_regression.py
                grad = alpha * (y_hat - yi) * xi
        
=======
                delta = alpha * (hxi - yi) * xi

                self._weight[k] -= delta

>>>>>>> 1a4c5f84434cd1a5172ee0a622b802588307073e:logisticRegression.py
                # adjusting the ith weight by this delta
                tempw -= delta
                
        self._weight = tempw


    def __repr__(self):
        """used for making the terminal look pretty. :)
        gives how many iterations there are, n dimensions, cost over time
        LogRegtrains and shit. Idk actually but we'll see. yikers.

        >>> print repr(LogReg([[1, 2, 3], [0, 0, 0]], [1, 0, 0], .25, 100))
        's'

        """
        s = 'This has been trained for %i iterations.' + '\n' +'There are %i data points.' + '\n' +'Cost overflow bullshit.' %(self._maxIter, self._data.shape[0]*self._data.shape[1])
        return s 