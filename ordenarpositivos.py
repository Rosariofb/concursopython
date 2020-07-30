def ordena_positivos(lista):
    positivos=list(sorted(filter(lambda x: x > 0, lista)))
    nueva_lista=lista
    l=len(lista)
    j=0
    for i in range(l):
        if lista[i] > 0:
            nueva_lista[i]=positivos[j] 
            j+=1 
    return(nueva_lista)

