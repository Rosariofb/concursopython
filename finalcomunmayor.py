def final_comun_mayor(Lst1,Lst2):
    l=len(Lst1)-1
    j=len(Lst2)-1
    resultado=''
    for i in range(l, -1, - 1):
        if Lst1[i]==Lst2[j]:
            resultado=Lst1[i:l+1]
        else:break  
        j-=1
    return(resultado)
