import matplotlib.pyplot as plt
import plotly.graph_objects as go


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


def draw(solver, t0=0, x0=13.41265629, y0=13.46430003, z0=33.46156416):
    for r in rs:
        ts, xs, ys, zs = solver(r, t0, x0, y0, z0)

        print('r = {0}'.format(r))
        plt.plot(ts, xs, 'red')
        plt.show()
        plt.plot(ts, ys, 'green')
        plt.show()
        plt.plot(ts, zs, 'blue')
        plt.show()

        fig = go.Figure(
            data=[
                go.Scatter3d(
                    x=xs,
                    y=ys,
                    z=zs,
                    marker=go.Marker(
                        size=1
                    )
                )
            ]
        )
        fig.show()