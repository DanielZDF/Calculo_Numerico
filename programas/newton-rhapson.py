import sympy as sp

def new_raph (f,Xo,Er,w):

    def convergencia(f,Xo):
        x = sp.Symbol('x')
        F = sp.sympify(str(f(x)))
        df1 = sp.diff(F, x)
        df2 = sp.diff(df1, x)
        valor = abs((f(Xo) * df2.subs(x, Xo)) / df1.subs(x, Xo)**2)
        return valor < 1

    def error(A,B):
        return abs((A-B)/A)

    def formula(Xi,f,df):
        return Xi - (f(Xi)/df.subs(x, Xi))

    def calculo(f,df,Xi,Er,w):
        Xi2 = formula(Xi,f,df)
        if (error(Xi,Xi2) < Er or w == 0):
            return Xi2
        else:
            return calculo(f,df,Xi2,Er,w-1)
       
    if (convergencia(f,Xo) == True):
        x = sp.Symbol('x')
        df = sp.diff(sp.sympify(str(f(x))), x)
        return calculo(f,df,Xo,Er,w)
    else:
        return None
