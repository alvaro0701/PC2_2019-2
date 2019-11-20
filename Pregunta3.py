import os
os.system("cls")

nombre=[]
edad=[]
sexo=[]
datos=[nombre,edad,sexo]
a=0
h=0
m=0
while len(nombre)<5:
    n=input("Ingrese nombre de la persona:")
    nombre.append(n)
    while True:
        s=input("Ingrese sexo de la persona:")
        sexo.append(s)
        if s=="Masculino"or s=="masculino":
            h=h+1
            break
        elif s=="Femenino"or s=="femenino":
            m=m+1
            break
        else:
            print("Ingrese sexo (Masculino/Femenino)")

    while True:
        e=int(input("Ingrese edad:"))
        if e>5 and e<17:
            a=a+e
            edad.append(e)
            break
        else:
            print("Ingrese edad entre 5 y 17")
b=a/5
print("*************Registro********************")
print("Personas registradas")
print(datos)
print("cantidad de Mujeres:",m)
print("Camtidad de Homnres:",h)
print("El promedio de las edades es:",b)




    



