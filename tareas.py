def factorial(n):
    if (n == 1):
        return 1
    else:
         
        return n  * factorial(n - 1)
def fibonacci(n,x,num,num2):
    num2 += 1
    if(num2 != num):
        print(n)
        n = n + x
        x = n - x
        
        fibonacci(n,x,num,num2)
		
def multix(num,m,n):
    n = n + 1
    if(n == m):
      return num
    if(n <= m):
      num = num + 3
      return multix(num,m,n)

   
def pascal():


	

         
def main():
    seguir=True
    while(seguir):
        opcion=int(input("escoja una opcion:\n 1.-Factorial\n 2.-Fibonacci\n 3.-multiplo de 3\n 4.-triangulo de pascal\n 5.-salir\n"))

        if(opcion==1):
            x=6
            print("Opcion 1")
            print("Resultado del facotrial de 6: ", factorial(x))
        if(opcion==2):
            num = int(input("Numeros que quieres en el fibonacci: "))
            print(0)
            fibonacci(1,0,num,0)
        if(opcion==3):
            x=int(input("Elige un multiplo de 3: "))
            print("Multiplo de 3 :" , multix(3,x,0))
        
        if(opcion==4):

        if(opcion==5):
            seguir=False
if __name__=="__main__":
    main()
   

    
