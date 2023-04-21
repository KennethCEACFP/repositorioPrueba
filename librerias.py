import random as rd
import string as st
# funciones
print("-----------------------Random------------------------")
# random devuelve un valor entre 0-1 con muchos decimales
print(rd.random())
# uniform, lo mismo pero pones los parametros
print(rd.uniform(5,10))

#devuelve un numero sin decimales perteneciente a un rango
print(rd.randrange(10, 20, 2))

# pones que numeros quieres que salga con lista o tuplas, con set no
print(rd.choice([1,2,3,4,5,6,7]))


print(rd.choices([1,2,34,5,6,], [20,20,20,20,20], k=5))


print("----------------------String----------------------")

print("Todas las letras en minusculas y mayusculas", st.ascii_letters)

print("todas las letras en minusculas", st.ascii_lowercase)

print("todas las letras en mayusculas", st.ascii_uppercase)

print("todos los numeros", st.digits)

print("todos los numeros en formato hexadecimal", st.hexdigits)

print("Representar un espacio en blanco", list(st.whitespace))

print("el resto de caracteres en la tala asii", st.punctuation)

texto= "Este es el texto que vamos a separar y vams a poner la primera letra de cada palabra en mayusculas"

print(st.capwords(texto, "e"))

print("String-formatter")

formatter= st.Formatter()

print(formatter.format("El texto{inicio}, otro texto:{medio}, texto final:{fin}", inicio="El texto inicio", medio="el texto medio", fin="el texto final"))

print("String-template")
t= st.Template("Hola, me llamo $name, tengo $age años")
print(t.substitute(name= "kenneth", age=18))