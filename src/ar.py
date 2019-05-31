import numpy as np


class YW_AR():

    def __init__(self, p):
        self.p = p

    def __repr__(self):
        return "AR({}) object".format(self.p)

    def fit(self, y):
        length = len(y)
        p = self.p
        inv_r = np.linalg.inv(
            np.corrcoef([y[i:length - p + i + 1] for i in range(p)]))
        r_2 = np.corrcoef([y[i:length - p + i] for i in range(p + 1)])[:, 0][
              1:]
        self.params = np.dot(inv_r, r_2)
        self.mu = np.mean(y) - np.dot(self.params,
                                      [np.mean(y[:length - i]) for i in
                                       range(p)])
        self.v_hat = np.mean([(y[i] - self.mu - np.dot(
            np.array([y[i - j] for j in range(1, p + 1)]), self.params)) ** 2
                              for i in range(p, length)])

    def show_model(self):
        st = "y[t] = {:.2f}".format(self.mu)
        for i in range(1, self.p + 1):
            st += " + {:.2f} * y[t{}]".format(self.params[i - 1], -i)
        st += " + e      e ~ N(0,{:.2f})".format(self.v_hat)
        print(st)
