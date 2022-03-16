from ctypes.wintypes import HLOCAL


a=0
for i in range(4):
    a+=1
    print(a)
dato= str(input("ingrese un dato "))
if dato== "hola":
  print("true")
else:
    print("false")

nombre= ("nicolas")
print (type(nombre))
mensaje="""" esto es 
un mensaje
saltadito jeje"""
print(mensaje)

def oracion ():
    print("tengo moto")
oracion()
def suma (n1,n2):
    print(n1+n2)
suma(3,5)
suma(8,380)
suma(345,45)

lista=["nicolas", "ramirez", "villamizar"]
lista.insert(1,"amadado")
print(lista)
#con .append solo puedo agregar un elemento a la lista pero al final
#con .insert(1, "elemento") puedo agregar un nuevc elemento en la posición que quiera
lista.extend(["el ingeniero","mas ingeniero","de todos los ingenieros"])
print(lista[:])
print(lista.index("mas ingeniero"))
#.index sirve para que nos diga el indice en el que se encuentra un elemento dentro de una lista
print("nicolas"in lista)# "elemento que quermos saber si esta en la lista",in= en lista que tengamos creada 
lista.remove("mas ingeniero")#remove para poder remover un elemento de una lista
print(lista[:])
lista.pop()#.pop es para remover el ultimo elemento de una lista
print(lista[:])

#sumar listas
hola=["trabajando""programando""estudiando"] *4 
#si le ponemos a una lista el * seguido de un número ejemplo:*4 me repetirá la lista 4 veces
hello=["cantando""hablando"]
print(hola+hello[:])

tupla=("nicolas",19,3,2004)
print(tupla[0])
tupla_a_lista= list(tupla) #con el metodo list lo que haces es convertir una tupla en una lista
print(tupla_a_lista)

listica=["hacker colacho"]
lista_a_tupla=tuple(listica) # con el metodo tuple convertimos una lista en una tupla
print(lista_a_tupla)
print("hacker colacho" in lista_a_tupla) # comprobamos si un valor esta en la tupla
tupletica= ("osos",)# le ponemos la coma al final para que se sepa que es una tupla con un unico elemento
print(tupletica.count("osos")) #con el .count averiguamos cuantas veces se repite un elemneto en la tupla

print(len(tupletica)) # len lo usamos para saber cuantos elementos tiene una tupla

desempaquetado=("19","marzo",2004)
dia,mes,año= desempaquetado # proceso para desempaquetar una tupla y asignarle un valor a una variable
print(mes)
print(dia)
print(año)