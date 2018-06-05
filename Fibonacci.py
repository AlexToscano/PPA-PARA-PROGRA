num = int(input("Escoje un numero entre 5 y 15\n"))
if(num >= 5 and num <= 15):
	a=1
	b=0
	c=0
	for i in range(num):
		print("Secuencia: "+ str(c))
		c=a+b
		a=b
		b=c
		
else:
	print("El numero es incorrecto")

