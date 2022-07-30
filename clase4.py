#Ejercicio A
def decorador(function):

    def funcion_de_retorno():
        print('Hola')
        function()
        print('Chau')

    return funcion_de_retorno

@decorador
def decir ():
    print("Esto es Programación Avanzada")
    
decir()


#Ejercicio B
def decorador2(function):
    
    def funcion_de_retorno(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ZeroDivisionError:
            return "No se puede dividir por 0!"
    return funcion_de_retorno

@decorador2
def dividir(a,b):
    return a/b

print(dividir(9,8))
print(dividir(2,0))


