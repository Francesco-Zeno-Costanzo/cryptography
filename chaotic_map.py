"""
code for chaotic map
"""
import time
import itertools
import numpy as np
import matplotlib.pyplot as plt


def logistic_key(x0, r, size):
    """
    logistic map

    Parameter
    ---------
    x0 : float
        initial value
    r : float
        parameter of logistic map
    size : int
        number of iteration

    Return
    ------
    x : 1darray
        logistic map
    """
    x = np.zeros(size)
    x[0] = x0

    for n in range(size-1):
        x[n+1] = r * x[n] * (1 - x[n])

    return x


def generalized_logistic_key(x0, p, q, size):
    """
    logistic map

    Parameter
    ---------
    x0 : float
        initial value
    r : float
        parameter of logistic map
    size : int
        number of iteration

    Return
    ------
    x : 1darray
        logistic map
    """
    x = np.zeros(size)
    x[0] = x0

    for n in range(size-1):
        if 0<= x[n] <= p:
            x[n+1] = -q/p**2 *(p - x[n])**2 + q
        elif p < x[n] <= 1 :
            x[n+1] = -q/(1-p)**2 *(p - x[n])**2 + q

    return x


def tent_key(x0, mu, size):
    """
    tent map

    Parameter
    ---------
    x0 : float
        initial value
    r : float
        parameter of tent map
    size : int
        number of iteration

    Return
    ------
    x : 1darray
        tent map
    """
    x = np.zeros(size)
    x[0] = x0

    for n in range(size-1):
        if x[n] < 0.5:
            x[n+1] = mu * x[n]
        else :
            x[n+1] = mu * (1 - x[n])

    return x


def gaussian_key(x0, a, b, size):
    """
    gaussian map

    Parameter
    ---------
    x0 : float
        initial value
    r : float
        parameter of gaussian map
    size : int
        number of iteration

    Return
    ------
    x : 1darray
        gaussian map
    """
    x = np.zeros(size)
    x[0] = x0

    for n in range(size-1):
        x[n+1] = np.exp(- a * x[n]**2) + b

    return x


def bifurcation(f, Param):
    """
    function to create bifurcation diagram
    default we take 400 iteration of map

    Parameters
    ----------
    f : callable
        map
    Param : 2darray
        matrix of parameter range:
        Param[i, 0] = min of i-th parameter
        Param[i, 1] = max of i-th parameter
        Param[i, 2] = numbero of point between min and max

    Return
    ------
    P : 1darray
        value of map
    R : 2darray
        value of parameter used
    """
    M = len(Param[:, 0]) #number of parameter

    par = []             #it will contain the sets of parameter variations
    for i in range(M):
        par.append(np.linspace(Param[i, 0], Param[i, 1], int(Param[i, 2])))

    pars = itertools.product(*par)   #in order not to make n nested cycles,
    pars = [comb for comb in pars]   #first calculate all the combinations
                                     #of the indexes of the cycles,
                                     #i.e. the Cartesian product, and then
                                     #cycle over the combinations

    N = len(pars)                    #length of final cycle

    P = np.zeros(N)
    R = np.zeros((N, M))

    for i, val in enumerate(pars):
        x = f(*val, 400)[-1]
        P[i] = x
        R[i, :] = val

    return P, R



if __name__ == "__main__":

    start = time.time()
    """
    par1 = np.matrix("0.05, 0.95, 500 ; 2, 4, 500")

    x1, p1 = bifurcation(logistic_key, par1)

    plt.figure(1)
    plt.title('Diagramma delle biforcazioni mappa logistica', fontsize=15)
    plt.plot(p1[:, 1], x1, linestyle='', marker='.', color='b', markersize=0.2)
    plt.xlabel('r')
    plt.ylabel('$x_n$')
    plt.grid()
    """
    """
    par2 = np.matrix("0.05, 0.95, 500 ; 1, 2, 500")

    x2, p2 = bifurcation(tent_key, par2)

    plt.figure(2)
    plt.title('Diagramma delle biforcazioni mappa a tenda', fontsize=15)
    plt.plot(p2[:, 1], x2, linestyle='', marker='.', color='b', markersize=0.2)
    plt.xlabel('$\mu$')
    plt.ylabel('$x_n$')
    plt.grid()
    """
    """
    par3 = np.matrix("-1, 1.2, 500 ; 10, 10, 1 ; -1, 1, 500")

    x3, p3 = bifurcation(gaussian_key, par3)

    plt.figure(3)
    plt.title('Diagramma delle biforcazioni mappa di Gauss', fontsize=15)
    plt.plot(p3[:, 2], x3, linestyle='', marker='.', color='b', markersize=0.2)
    plt.xlabel(r'$\beta$')
    plt.ylabel('$x_n$')
    plt.grid()
    """
    """
    par4 = np.matrix("0.05, 0.95, 500 ; 0.05, 0.95, 500 ; 0.9, 0.9, 1")
    #par4 = np.matrix("0.05, 0.95, 500 ; 0.2, 0.2, 1 ; 0.6, 1, 500")
    x4, p4 = bifurcation(generalized_logistic_key, par4)

    plt.figure(3)
    plt.title('Diagramma delle biforcazioni mappa logistica generalizzata', fontsize=15)
    plt.plot(p4[:, 1], x4, linestyle='', marker='.', color='b', markersize=0.2)
    plt.xlabel('p')
    plt.ylabel('$x_n$')
    plt.grid()
    """
    #plt.show()

    end = time.time() - start
    print(f'Elapsed time = {end:.3f} seconds')