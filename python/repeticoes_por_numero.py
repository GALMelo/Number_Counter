listaDeNumeros = []
dicionario = {}

# pega a quantidade de numeros
quantidade = int(input("Digite quantos valores sua lista possui: "))

# pega os valores que serao digitados
def getValues(n, value):
    
    listaDeNumeros.append(value)
    if n == 1:
        return 0
    
    getValues(n-1, int(input()))

getValues(quantidade, int(input()))

# adiciona os valores digitados em um dicionario com suas quantidades
def addToDict(listaLocal):
    if len(listaLocal) == 0:
        return 0
    if dicionario.__contains__(listaLocal[0]):
        dicionario[listaLocal[0]] += 1
    else:
        dicionario.update({listaLocal[0]: 1})

    #print(d)

    addToDict(listaLocal[1:])

addToDict(listaDeNumeros)

# pega os valores do dicionario com repeticoes
def getCountValues(dicionarioLocal):
    
    if dicionarioLocal == {}:
        return ""
    copiaDicionarioLocal = dicionarioLocal.copy()

    copiaDicionarioLocal.pop([*copiaDicionarioLocal][0],
                             copiaDicionarioLocal.get([*copiaDicionarioLocal][0]))
    
    return "O numero {} repetiu {} vezes\n".format(
        [*dicionarioLocal][0],
        dicionarioLocal[[*dicionarioLocal][0]]) + getCountValues(copiaDicionarioLocal) 

# imprime valores 
print(getCountValues(dicionario))
