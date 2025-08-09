import matplotlib.pyplot as plt
import numpy as np
from scipy.special import binom


def bezier(control_points, curve_points=30):
    '''
    given the control points, returns a bezier curve with N 'curve_points'
    as x-y values. control_points is a matrix of shape Nx2
    '''
    t = np.linspace(0, 1, curve_points)
    n, _ = control_points.shape # npoints
    bern = np.empty(shape=(n, curve_points))
    n -= 1 # curve degree
    for i in range(n+1):
        bern[i] = binom(n, i)*np.power(1-t, n-i)*np.power(t, i)
    return np.dot(bern.T, control_points.astype(np.float64))


def main():
    rand = np.random.RandomState(seed=4628)
    # create and organize control points (deg 1 to 4)
    i = 2
    n = 2
    control_points = rand.randint(n, size=(n, 2))
    idx = np.argsort(control_points[:, 0])
    control_points = control_points[idx]
    bezier_points = bezier(control_points)
    plt.figure()
    plt.subplot(2, 2, i-1)
    plt.scatter(control_points[:, 0], control_points[:, 1], s=9, label='control points')
    plt.plot(control_points[:, 0], control_points[:, 1], linewidth=.4)
    plt.plot(bezier_points[:, 0], bezier_points[:, 1], color="r", linewidth=.6, label='bezier curve')
    plt.title("Bezier curve of degree %d"%(len(control_points)-1))
    plt.legend()

    i += 1
    n += 1
    control_points = rand.randint(10, size=(n, 2))
    idx = np.argsort(control_points[:, 0])
    control_points = control_points[idx]
    bezier_points = bezier(control_points)   
    plt.subplot(2, 2, i-1)
    plt.scatter(control_points[:, 0], control_points[:, 1], s=9, label='control points')
    plt.plot(control_points[:, 0], control_points[:, 1], linewidth=.4)
    plt.plot(bezier_points[:, 0], bezier_points[:, 1], color="r", linewidth=.6, label='bezier curve')
    plt.title("Bezier curve of degree %d"%(len(control_points)-1))

    i += 1
    n += 1
    control_points = rand.randint(10, size=(n, 2))
    idx = np.argsort(control_points[:, 0])
    control_points = control_points[idx]
    bezier_points = bezier(control_points)
    plt.subplot(2, 2, i-1)
    plt.scatter(control_points[:, 0], control_points[:, 1], s=9, label='control points')
    plt.plot(control_points[:, 0], control_points[:, 1], linewidth=.4)
    plt.plot(bezier_points[:, 0], bezier_points[:, 1], color="r", linewidth=.6, label='bezier curve')
    plt.title("Bezier curve of degree %d"%(len(control_points)-1))

    i += 1
    n += 1
    control_points = rand.randint(10, size=(n, 2))
    idx = np.argsort(control_points[:, 0])
    control_points = control_points[idx]
    bezier_points = bezier(control_points)
    plt.subplot(2, 2, i-1)
    plt.scatter(control_points[:, 0], control_points[:, 1], s=9, label='control points')
    plt.plot(control_points[:, 0], control_points[:, 1], linewidth=.4)
    plt.plot(bezier_points[:, 0], bezier_points[:, 1], color="r", linewidth=.6, label='bezier curve')
    plt.title("Bezier curve of degree %d"%(len(control_points)-1))
    #---    
    plt.show()


if __name__=="__main__":
    main()






    
