import numpy as np
import scipy.stats as st

mean = 0.2
var=0.0004
sd = var**0.5

def z(data):
    z = (data-mean)/sd
    return z

def std(z):
    std_data = z*sd
    return std_data

def batas_nilai(x):
    return x*sd + mean

def mean_data(prob):
    mean_data = batas_nilai(prob)-(1-prob)*sd
    return mean_data

def prob_xy(x,y):
    probx = (abs(st.norm.sf(z(x))-st.norm.cdf(z(x))))/2
    proby = (abs(st.norm.sf(z(y))-st.norm.cdf(z(y))))/2
    return (probx+proby)*100



no2a = prob_xy(0.18,0.22)
no2b = st.norm.cdf(z(0.15))
no2c = std(st.norm.cdf(z(0.15)))
no2d = mean_data(1-z(0.15))

print(no2dS)