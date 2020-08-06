def acumulado(Lista):
    Listasuma=[]
    suma=0
    for i in Lista:
        suma+=i
        Listasuma.append(suma)
    return(Listasuma)

