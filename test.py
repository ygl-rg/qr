import gramm
import linreg
import time
import numpy as np

a = [[1, 2, 3], [1, 1, 1]]

b = time.time()

for i in xrange(1):
    """
    res = linreg.linreg([74.5,
                         74.5,
                         75.9,
                         78.3,
                         77.3,
                         77,
                         76.8],
                        [[10.7],
                         [10.6],
                         [15.8],
                         [14.0],
                         [12.4],
                         [12.1],
                         [12.0]])
    """
    x = np.array(
        [
            [0, 10.8, 82],
        ])
    y = np.array([0, 43.7, 100])
    A = np.vstack([x, np.ones(len(x[0]))]).T
    #X = np.column_stack(x+[1]*len(x[0]))

    res1 = np.linalg.lstsq(A,y)[0]

    #print res
    print res1
print time.time() - b

# for i, d in enumerate(res):
#    print i, d
