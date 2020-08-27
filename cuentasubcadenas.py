# Implementa una función cuenta_subcadenas_ax(cadena) que devuelva el número de 
# subcadenas contenidas en el string cadena que comienzan por la letra A 
# y terminan por la letra X.

def cuenta_subcadenas_ax(cadena):
    nro_cad=0
    for i in range(len(cadena)):
        if 'A' == cadena[i]:
            subcadena=cadena[i+1:len(cadena)]
            cont=0
            while cont<len(subcadena):
                if subcadena[cont]=='X':
                    nro_cad+=1
                cont+=1    
    return(nro_cad)

