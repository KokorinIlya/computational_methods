def dx_dt(t, x, y, z, sigma, b, r):
    return sigma * (y - x)


def dy_dt(t, x, y, z, sigma, b, r):
    return x * (r - z) - y


def dz_dt(t, x, y, z, sigma, b, r):
    return x * y - b * z


sigma = 10
b = 8/3
rs = [0.5, 10, 24.06, 30, 100]
dt = 0.001
max_t = 20
