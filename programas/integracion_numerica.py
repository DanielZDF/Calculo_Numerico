def suma_riemann(f,a,b,n):
    h = (b-a)/n
    At = 0
    for x in range(n+1):
        At = At + (h * f(a+h*x))
    return At

def metodo_trapecio(f,a,b,n):
    h = (b-a)/n
    At = 0
    for x in range(n):
        x1 = a+h*x
        x2 = a+h*(x+1)
        At = At + (h * ((f(x1) + f(x2))/2))
    return At
