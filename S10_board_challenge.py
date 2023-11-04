# Desafio 01: Palindromos con pilas
# complejidad de tiempo O(2n)
# complejidad de espacio O(n)
def palidromo_pila(cadena):
    pila = []
    pila2 = []
    mitad1 = ""
    mitad2 = ""
    if cadena == "":
        raise Exception("Error: Cadena vacia.")

    for s in cadena: # o(n)
        pila.append(s)

    if len(cadena) % 2 == 0: # si o(n)
        num_ite = len(cadena) // 2
        for n in range(num_ite):
            pila2.append(pila.pop(-1))
        for n in range(num_ite):
            mitad1 = mitad1 + pila.pop(-1)
        for m in range(num_ite):
            mitad2 = mitad2 + pila2.pop(-1)
        return mitad1 == mitad2

    else: # si o(n)
        num_ite = len(cadena) // 2
        for n in range(num_ite):
            pila2.append(pila.pop(-1))
        pila.pop(-1)
        for n in range(num_ite):
            mitad1 = mitad1 + pila.pop(-1)
        for m in range(num_ite):
            mitad2 = mitad2 + pila2.pop(-1)
        return mitad1 == mitad2


string1 = "hola"
string2 = "abcba"

print(palidromo_pila(string2))

# Desafio 2: Caracteres unicos (diccionarios)

def caracteres_unicos():
    pass

# Desafio 3: Balanceo de parentesis(pila)


# Desafio 4: Texto en reversa(pila)