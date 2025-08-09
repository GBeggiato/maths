import numpy as np
import matplotlib.pyplot as plt


def one_moving_average(arr, w):
    '''one-sided moving average of an array, using a window of w values from the past'''
    return np.convolve(arr, np.ones(w), 'valid')*(1/w)


def two_moving_average(arr, k):
    '''two-sided moving average of an array, using k values around the observed one'''
    if k%2==0:
        k+=1# k needs to be odd, to have symmetry around the observed value
    fin = np.empty(shape=len(arr)-k+1)
    a = int(k/2)
    for i, t in enumerate(range((k-1-a), (len(arr)-a))):
        fin[i] = np.mean(arr[t-a:t+a+1])
    return fin


def exp_ma(arr, lda=1, look_back=1):
    '''returns exponential moving average of the array arr
    @lda -> exponential param (0->returns the data, 1->simple one-sided m.a.)
    @look_back -> obs window'''
    # default checks, any exeption returns the data
    if lda<=0 or lda>1:
        return arr
    if look_back>(len(arr)-1) or look_back<1:
        return arr
    if lda==1 and look_back==1:
        return arr
    if lda==1:
        return np.convolve(arr, np.ones(look_back), 'valid')*(1/look_back)
    fin = np.empty(shape=len(arr)-look_back+1)
    # exponential coeffs
    ldas = np.power(lda, np.arange(look_back-1, -1, -1))
    # computations
    for t in range(look_back, len(arr)+1):
        f = t-look_back
        fin[f] = np.average(a=arr[f:t], weights=ldas)
    return fin


def main():

    rand = np.random.RandomState()
    rand.seed(43251)

    tot = 100
    x = np.arange(tot)
    values = np.ndarray(shape=tot)
    values[0] = 0
    values[1:] = rand.normal(size=tot-1).cumsum()

    lb = 2
    y = exp_ma(values, lda=1, look_back=lb)
    plt.plot(x, values)
    plt.plot(x[lb-1:], y, linewidth=.5)
    plt.show()

        
if __name__=="__main__":
    main()       

