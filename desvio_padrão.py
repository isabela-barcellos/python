def acha_media(lista): #achando media
    soma =0
    for elem in lista:
        soma+=elem
    return soma/len(lista)

def std(lista): #std(devio padrão em inglês)
    soma=0
    media = acha_media(lista)
    for elem in lista:
        soma += (elem - media)**2 #aqi vai pegar cada elem menos o resultado da média e eleva esse resultado a 2 e ai fazendo isso a cada elemento da lista
    soma/=len(lista)
    soma **=0.5
    return soma
print(std([1,2,3,4]))