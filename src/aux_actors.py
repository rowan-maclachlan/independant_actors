import random as r

def get_w_uniform_dist(mid, var):
    low = mid - var
    high = mid + var
    return int(r.uniform(low, high))

def get_w_normal_dist(mu, var):
    return int(r.gauss(mu, sqrt(var)))
