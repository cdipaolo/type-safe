import logistic_regression
import unittest
import numpy as np

class TestLogisticRegression1(unittest.TestCase):
    def __init__(self):
        X = []
        Y = []
        for i in range(-10, 10, 0.1):
            for j in range(-10, 10, 0.1):
                if j > i:
                    X += [i, j]
                    Y += 1
                else:
                    X += [i, j]
                    Y += 0
        self.model = LogReg(X, Y, 0.1, 100)
        model.train()

    def test_predicts_correctly(self):
        for i in range(-25, 25, 0.5):
            for j in range(-25, 25, 0.5):
                if j > i:
                    self.assertEqual(self.model.predict([i, j + 0.5]), 1, msg="Model should predict 1 when y > x")
                else:
                    self.assertEqual(self.model.predict([i, j - 0.5]), 0, msg="model should predict 0 when y < x")

class TestLogisticRegression2(unittest.TestCase):
    def __init__(self):
        X = []
        Y = []
        for i in range(-10, 10, 0.5):
            for j in range(-10, 10, 0.5):
                for k in range(-10, 10, 0.5):
                    if i + 3*j - 2*k > 0:
                        X += [i, j, k]
                        Y += 1
                    else:
                        X += [i, j, k]
                        Y += 0
        self.model = LogReg(X, Y, 0.1, 100)
        model.train()

    def test_predicts_correctly(self):
        for i in range(-10, 10, 0.5):
            for j in range(-10, 10, 0.5):
                for k in range(-10, 10, 0.5):
                    if i + 3*j - 2*k > 0:
                        self.assertEqual(self.model.predict([i + 0.5, j + 0.5, k]), 1, msg="Model should predict 1 when x + 3y - 2z > 0")
                    else:
                        self.assertEqual(self.model.predict([i - 0.5, j - 0.5, k]), 0, msg="model should predict 0 when x + 3y - 2z < 0")

if __name__ == '__main__':
    unittest.main()
        
