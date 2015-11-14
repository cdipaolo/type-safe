import numpy as np

class LogReg():

    #Uses logistic regression and gradient decent to optimize a weight vector

    def __init__(self, data, tags, alpha, maxIter):
        """
        The training vector is stored in two parts, the data and the tags.
        The data will be converted into numpy array
        """
        

        self._data = np.array(data)

        # add a column of 1s for the y offset feature
        self._data = np.hstack(([[1]]*self._data.shape[0], self._data))

        self._tags = np.array(tags)

        self._weights = np.array([0]*self._data.shape[0])

        self._alpha = alpha

        self._costs = []

        self._maxIter = maxIter


    def predict(self, x):
        """
        Takes the dot product of one feature and the weight vector
        and returns the result of them entered into the sigmoid function

        >>> logReg = LogReg([[1, 2, 3], [0, 0, 0]], [1, 0, 0], .25, 100)
        >>> logReg.predict([1, 2, 3])

        """
        dot_p = np.dot(x, self._weight)

        return (1 / (1 - np.exp(-1 * dot_p)))

        
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
            
            if iter % j_save_iteration == 0:
                self._costs.append(self.cost())
        
    def cost():
        """ calculates the sum of the squared residuals of a particular weight vector
        """
        sum = 0
        
        for i in range(self._data.size):
            ycaret = predict(self._data[i])
            y = self._tags[i]
            
            sum += (ycaret - y)**2
        
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

        >>> print repr(LogReg([[1, 2, 3], [0, 0, 0]], [1, 0, 0], .25, 100))
        's'

        """
        s = 'This has been trained for %i iterations.' \
            '\nThere are %i data points.' \
            '\nCost overflow bullshit.' % (self._maxIter, self._data.shape[0]*self._data.shape[1])
        
        return s 
