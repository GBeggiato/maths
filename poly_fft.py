import numpy as np
from numpy import ndarray


def _adj_poly(p1: ndarray, p2: ndarray) -> tuple[ndarray, ndarray]:
    '''takes 2 arrays returns them as 2 arrays where
    len(array) is a power of 2 (the min 2^n such that
    2^n >= max(len1, len2) ). Higher orders filled with 0'''
    L = max(len(p1), len(p2))
    i = 0
    LL = 1<<0
    while 1:
        LL = 1<<i
        if LL>=L:
            break
        else:
            i += 1
    P1 = np.concatenate((p1, np.zeros(shape=LL - len(p1))))
    P2 = np.concatenate((p2, np.zeros(shape=LL - len(p2))))
    return P1, P2


def fft_poly_mult(p1: ndarray, p2: ndarray) -> ndarray:
    '''polynomials multiplication using FFT. p1, p2 are coeff repr'''
    P1, P2 = _adj_poly(p1, p2) # calls above function
    z = np.zeros(shape=len(P1)) # lenP1==lenP2
    pp1 = np.concatenate((P1, z))
    pp2 = np.concatenate((P2, z))
    v1 = np.fft.fft(pp1) # value repr
    v2 = np.fft.fft(pp2)
    # coeff repr of the solution (imag part and higher order coeffs are always 0, discarded)
    return np.real(np.fft.ifft(v1*v2))[:(len(p1)+len(p2)-1)] 


def eval_poly(P: ndarray, x: ndarray) -> ndarray:
    '''evaluates a polynomial P (coeff repr) at x
    P[1, 2, 3] = 1 + 2x + 3x^2 (Horner method)'''
    y = np.full(shape=len(x), fill_value=P[0], dtype=np.double)
    X = np.copy(x)
    for i in range(1, len(P)):
        if P[i]!=0:
            y += P[i]*X
        X *= x 
    return y

