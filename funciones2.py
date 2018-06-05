def potencia(num1,num2 = 2):
	if (num2 == 0):
		return 1
	for x in range(num2 - 1):
		num1 = num1 * num1
	return num1
def main():
	numero = int(input("Escribe un numero:"))
	print("El numero al cuadrado es:"+ str(potencia(numero)))

if __name__ == "__main__":
	main()