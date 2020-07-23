def mayoria_absoluta(votos):
    dicvotos={}
    for opcion in votos:
        if opcion not in dicvotos:
            contador=1
        else:
            contador=dicvotos.get(opcion)
            contador+=1
        dicvotos[opcion] = contador

    mital_total=sum(dicvotos.values())/2   
    mayor=None
    for k,v in dicvotos.items():
        if v > mital_total:
            mayor=k;break
    return(mayor)   


