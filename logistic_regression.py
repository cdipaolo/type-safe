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

        assert _data.shape[0] == _tags.size, "Number of tags not equal to number of data sets"

        self._weights = np.array([69]*self._data.shape[0])

        self._alpha = alpha

        self._costs = []

        self._maxIter = maxIter

        self._current_iterations = 0

    def predict(self, x):
        """
        Takes the dot product of one feature and the weight vector
        and returns the result of them entered into the sigmoid function

        >>> logReg = LogReg([[1, 2, 3], [0, 0, 0]], [1, 0], .25, 100)
        >>> logReg.predict([1, 2, 3])
        0.5
        """
        dot_p = np.dot(x, self._weight)

        return (1 / (1 + np.exp(-1 * dot_p)))

        
    def train(self):
        """ trains the weight vector on the training data
        """
        alpha = self._alpha
        j_save_iteration = 5

        # going through the training data _maxIter times
        for iter in range(_maxIter):
            # initialize the gradient at 0
            grad = [0] * (len(self._data[0]))
            # moving through the training data
            for i in range(self._data.size):
                xi = self._data[i]
                # the predicted value
                hxi = self.predict(xi)
                # the target value
                yi = self._tags[i]
                
                grad += np.multiply((hxi - yi),xi)
            
            weightchange = np.multiply(grad, alpha)
            self._weight = np.subtract(self._weight, weightchange)
            
            # incrementing the number of iterations
            self._current_iterations += 1
            
            if iter % j_save_iteration == 0:
                self._costs.append(self.cost())
        
    def cost():
        """ calculates the sum of the squared residuals of a particular weight vector
            >>> a = LogReg([],[])
            >>> a._weights = [0,0,0]
            >>> a._data = [0,0,0]
            >>> a._tags = [1,1,1]
            >>> assert a.cost() > 0
        """
        sum = 0
        
        for i in range(self._data.size):
            y_hat = predict(self._data[i])
            y = self._tags[i]
            
            sum += (y_hat - y)**2
        
        sum /= self._data.size
        
        return sum
        
    def costs():
        """ returns all previous costs after some number of iterations
        """
        return self._costs

    def __repr__(self):
        """used for making the terminal look pretty. :)
        gives how many iterations there are, n dimensions, cost over time
        LogRegtrains and shit. Idk actually but we'll see. yikers.

        >>> logReg = LogReg([[1, 2, 3], [0, 0, 0]], [1, 0, 0], .25, 100)
        >>> logReg._costs = [4, 3, 6]
        >>> print repr(logReg)
        This has been trained for 0 iterations.
        There are 8 data points.
        Some cost values are: 4, 3, 6.

        """
        datapoints = self._data.shape[0]*self._data.shape[1]
        cost_middle = self._costs[len(self._costs)/2]
        s = 'This has been trained for %i iterations.' \
            '\nThere are %i data points.' \
            '\nSome cost values are: %i, %i, %i.' \
            % (self._current_iterations, datapoints, self._costs[0], cost_middle, self._costs[-1])
        
        return s 
