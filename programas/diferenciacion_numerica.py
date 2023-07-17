def metodo_euler(f, x0, y0, tn, n):
    x = [x0]
    y = [y0]
    for i in range(n-1):
        y.append(y[-1] + tn * f(x[-1], y[-1]))
        x.append(x[-1] + tn)
    return {'x': x, 'y': y}
