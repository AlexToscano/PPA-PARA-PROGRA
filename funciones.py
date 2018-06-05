#funcion para saludar
def saludar():
	print("Hola bienvenido a mi primer programa con funciones :)")
#Funcion para sumar
def sumados(numx,numy):
	if(type(numx) != int or type(numy) != int ):
		print("Ese tipo de dato es incorrecto")
		return
	result = numx + numy
	return result
#Funcion para restar
def resta(numx,numy):
	if(type(numx) != int or type(numy) != int ):
		print("Ese tipo de dato es incorrecto")
		return
	result= numx - numy
	return result
#Funcion para multiplicar
def multi(numx, numy):
	if(type(numx) != int or type(numy) != int ):
		print("Ese tipo de dato es incorrecto")
		return
	result = numx * numy
	return result
#funcion para dividir
def div(numx,numy):
	if(type(numx) != int or type(numy) != int ):
		print("Ese tipo de dato es incorrecto")
		return
	result = numx / numy
	return result
#funcion potencia
def pot(numx, numy):
	if(type(numx) != int or type(numy) != int ):
		print("Ese tipo de dato es incorrecto")
		return
	for i in range(numy):
		result = numx * numx
	return result 

#Funcion principal del programa
def main():
	saludar()
	print("Que desea hacer??:")
	opcion = int(input("1.Suma\n2.Resta\n3.Multiplicar\n4.Dividir\n5.Potencia\n"))
	if(opcion == 1):
		num1 = int(input("Escribe un numero"))
		num2 = int(input("Escribe otro numero"))
		result = sumados(num1,num2)
		print("El resultado es:"+ str(result))
	if(opcion==2):
		num1 = int(input("Escribe un numero"))
		num2 = int(input("Escribe otro numero"))
		result = resta(num1,num2)
		print("El resultado es:"+ str(result))
	if(opcion == 3):
		num1 = int(input("Escribe un numero"))
		num2 = int(input("Escribe otro numero"))
		result = multi(num1,num2)
		print("El resultado es:"+ str(result))
	if(opcion == 4):
		num1 = int(input("Escribe un numero"))
		num2 = int(input("Escribe otro numero"))
		result = div(num1,num2)
		print("El resultado es:"+ str(result))
	if(opcion == 5):
		num1 = int(input("Escribe un numero"))
		num2 = int(input("Escribe otro numero"))
		result = pot(num1,num2)
		print("El resultado es:"+ str(result))

if __name__ == '__main__':
	main()