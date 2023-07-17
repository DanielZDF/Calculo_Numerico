def biseccion(F, a, b, Er, N):
    
    def comprobacion(F,a,b):
        return (F(a) * F(b) < 0)

    def error(A,B):
        return abs((A-B)/A)
    
    def calculo(Funcion, V_Actual, IntA, IntB, E, It):
        if(It == 0):
            return V_Actual
        
        if(comprobacion(Funcion, IntA, V_Actual)):
            if(error(V_Actual,IntA) < E):
                return V_Actual
            else:
                V_Sig = (V_Actual + IntA)/2
                return calculo(Funcion, V_Sig, IntA, V_Actual, E, It-1)
                
        if(comprobacion(Funcion, IntB, V_Actual)):
            if(error(V_Actual,IntB) < E):
                return V_Actual
            else:
                V_Sig = (V_Actual + IntB)/2
                return calculo(Funcion, V_Sig, V_Actual, IntB, E, It-1)
                
                     
    ValorActual = (a+b)/2
    if (comprobacion(F,a,b)):
        return calculo(F,ValorActual,a,b,Er,N-1)
    else:
        return None
