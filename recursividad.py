#recursividad: es el hecho de que una funcion se llame a si misma , 
#esto con el proposito de dividir el problema en una  version mas pequeña de el.
#Debe tener una condicion  de terminacion para evitar que se vuelva infinita

def sum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
         return numlist[0] + sum(numlist[1:])
if __name__=="__main__":
    mylist=[1, 2, 3, 4, 5, 6, 7]
    print(sum(mylist))