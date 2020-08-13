def siguiente_mayor(Lista):
    k = 0
    for i in range(len(Lista)):
        x= Lista[i]
        k+=1 
        for j in range(k,len(Lista)):
            if x < Lista[j]:
                Lista[i] = Lista[j]
                Lista[j] = x
                break
    Lista[len(Lista) - 1] = - 1           
    return(Lista)

