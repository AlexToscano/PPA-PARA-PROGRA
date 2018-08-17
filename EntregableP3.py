import os

class alumno:

    def __init__(self,Nombre,Promedio,Grupo):
        self.Nombre=Nombre
        self.Promedio=Promedio
        self.Grupo=Grupo

    def __str__(self):
        return "%s , %s , %s"%(self.Nombre,self.Promedio,self.Grupo)

    def alfabeto():
        Alumnos={}
        list=[]
        listOB =[]
        Archivo = "Estudiantes.txt"
        with open(Archivo,'r') as file:
            print("Opened "+ Archivo)
            for line in file.readlines():
                list=[]
                list.append(line)
                list=' '.join(list)
                list=list.split(",")
                Alumnos[list[0]] = list[1]
                listOB.append(alumno(list[0],list[1],list[2]))
           
            listOB.sort(key=lambda Alumno:Alumno.Nombre)
           
            for i in listOB:
                Texto=open("Oren por alfabeto.txt",'a+')
                Texto.write(str(i))
                Texto.close
            print("Archivo por ALfabeto Creado")  

    def promedio():
        Alumnos={}
        list=[]
        listOB =[]
        Archivo = "Estudiantes.txt"
        with open(Archivo,'r') as file:
            print("Opened "+ Archivo)
            for line in file.readlines():
                list=[]
                list.append(line)
                list=' '.join(list)
                list=list.split(",")
                Alumnos[list[0]] = list[1]
                listOB.append(alumno(list[0],list[1],list[2]))
            
            listOB.sort(key=lambda Alumno:Alumno.Promedio,reverse=True)
            for i in listOB:
                Texto=open("Oren por promedio.txt",'a+')
                Texto.write(str(i))
                Texto.close
            print("Archivo por promedio creado")
               

def main():
   
    x=(int(input("Escoga como quiere ordenar a los alumnos:\n 1.-Alfabetico\n 2.-Promedio\n")))

    if(x==1):
        alumno.alfabeto()
    if(x==2):
        alumno.promedio()


if __name__=="__main__":
    main()
