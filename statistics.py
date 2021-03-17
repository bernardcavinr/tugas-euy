import numpy as r
from numpy.linalg import inv

def mean_data(X):
    N = len(X)
    sum_X = 0
    for i in range(N):
        sum_X = sum_X + X[i] 
    avg = sum_X/N 
    return avg

def min_data(X):
    N = len(X)
    min_X = X[0]
    for i in range(1,N):
        if X[i] < min_X :
            min_X = X[i]
    return min_X

def max_data(X):
    N = len(X)
    max_X = X[0]

    for i in range(1,N):
        if X[i] > max_X:
            max_X = X[i]
    return max_X

def var_data(X, mode ='populasi'):
    N = len(X)
    avg_X = mean_data(X)

    sum_X = 0
    for i in range(N):
        sum_X = sum_X + (X[i]-avg_X)**2

    if mode == 'populasi':
        var_X = sum_X/N
    elif mode == 'sampel' :
        var_X = sum_X/(N-1)
    else:
        print('Pastikan hanya memilihmode populasi atau sampel')
    return var_X

def std_data(X):
    var_X = var_data(X, mode='populasi')
    std_X = var_X**(0.5)
    return std_X

def median_data(X):
    X = sorted(X)
    N = len(X)
    if N%2 ==0:
        n = int(N/2 - 1)
        m = int(N/2)
        M = (X[n] + X[m])/2
    else :
        i = int((N)/2)
        M = X[i]
    return M

def cov_data(X,Y):
    N = len(X)
    avg_X = mean_data(X)
    avg_Y = mean_data(Y)
    sum_cov = 0
    for i in range(N):
        sum_cov = sum_cov + (X[i] - avg_X)*(Y[i] - avg_Y)
        cov_XY = sum_cov / (N)

    return cov_XY

def corr_coeff(X,Y):
    cov_XY = cov_data(X,Y)
    std_X = std_data(X)
    std_Y = std_data(Y)

    r_xy = cov_XY / (std_X * std_Y)

    return r_xy

def koefisien_variansi(a):
    koefisien_variansi = (std_data(a)/mean_data(a))*100
    return koefisien_variansi

def auto_corr(Y, lag):
    nn = len(Y) 
    ac = [] 
    arr_lag = [] 
    for i in range(0, lag):
        trace_a = Y[i:nn] 
        trace_b = Y[:(nn-i)]
        ac.append(corr_coeff(trace_a, trace_b)) 
        arr_lag.append(i) 
    return arr_lag, ac

def cross_corr(Y1, Y2, lag):
    Y1_bar = r.mean(Y1)
    Y2_bar = r.mean(Y2)

    T = len(Y1)

    s_y1 = var_data(Y1)
    s_y2 = var_data(Y2)

    lag_k = []
    r_y1y2 = []
    for k in range(-lag, lag+1, 1):
        c_y1y2 = 0
        if k>=0:
            for t in range(T-k):
                c_y1y2 = c_y1y2 + (Y1[t] - Y1_bar) * (Y2[t+k] - Y2_bar)
       
        else:
            for t in range(T+k):
                c_y1y2 = c_y1y2 + (Y2[t] - Y2_bar) * (Y1[t-k] - Y1_bar)
       
        r_y1y2.append(c_y1y2 / (s_y1 * s_y2))
        lag_k.append(k)

    return r_y1y2, lag_k

def lin_reg(X,Y):
    covXY = cov_data(X,Y)
    std_X = std_data(X)
    avg_X = mean_data(X)
    avg_Y = mean_data(Y)

    b_1 = covXY / (std_X ** 2)
    b_0 = avg_Y - b_1* avg_X

    return (b_0, b_1)

def lsq_reg(X,Y):
    N = len(X)

    A = r.ones((N,2))
    A[:,1] = X

    Y = r.transpose(Y)
    b = inv(A.T@A)@A.T@Y
    return b