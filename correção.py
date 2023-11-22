'''
1)	Crie uma função que recebe uma frase de parâmetro, verifica e obriga o
 usuário a digitar somente números.
'''
def verifica_numero(msg,msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    return int(num)
'''
3)	Crie uma função que recebe de parâmetro uma frase e uma lista com opções
 e pede que o usuário digite uma opção. Ela deve retornar esta opção somente quando
  o usuário digita algo dentro dasopções cadastradas.
'''
def forca_opcao(msg,lista_opcoes):
    apresenta_opcoes(lista_opcoes)
    opcao = input(msg)
    while opcao not in lista_opcoes:
        apresenta_opcoes(lista_opcoes)
        print("Deve ser uma opcao cadastrada!")
        opcao = input(msg)
    return opcao
'''
4)	Crie duas funções, uma que acha o maior valor dentro de uma lista, e outra
 que acha o menor e retornam os índices.
'''
def acha_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior

def acha_menor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i
    return indice_menor
'''
5)	Faça uma função que acha o valor médio de uma lista.
'''
def media(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma/len(lista)
def apresenta_opcoes(lista_opcoes):
    print('Essas são nossas opcoes : ')
    for opcao in lista_opcoes:
        print(opcao)
    return
def acha_indice(lista,alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return False
print("boas vindas")

'''
2)	Crie uma lista com vinhos e outra com os preços correspondentes.
'''
vinhos = ['suave','tinto','branco','italiano','jundiaiense']
precos = [10,20,30,25,15]
valor_total = 0
qtd_tipos = [0,0,0,0,0]
endereco = input("Diga seu endereco : ")
ano = verifica_numero("Diga seu ano de nascimento: ","Tem que ser inteiro!")
if ano >2005:
    print("mto feio n pode")
else:
    while True:
        local_mais_caro = acha_maior(precos)
        print(f"O vinho mais caro é o {vinhos[local_mais_caro]} e custa R${precos[local_mais_caro]},00")
        local_mais_barato = acha_menor(precos)
        print(f"O vinho mais barato é o {vinhos[local_mais_barato]} e custa R${precos[local_mais_barato]},00")
        preco_medio = media(precos)
        print(f"O preço médio de um vinho aqui é R${preco_medio:.2f}")
        escolha = forca_opcao('Qual vinho vc prefere ? ',vinhos)
        local_escolha = acha_indice(vinhos,escolha)
        qtd = verifica_numero(f"Diga quantas garrafas de {escolha} vc quer : ","Tem que ser int")
        qtd_tipos[local_escolha] += qtd
        valor_total += qtd * precos[local_escolha]
        encerrar = forca_opcao("O que voce deseja fazer ? ",['encerrar','continuar'])
        if encerrar == 'encerrar':
            break
    frete = 10
    msg = f'Frete de R${frete},00'
    if valor_total > 500:
        msg = 'Frete grátis'
        frete = 0
    print(msg)
    valor_total += frete
    garrafas = ''
    for i in range(len(qtd_tipos)):
        if qtd_tipos[i] != 0:
            garrafas += f"{qtd_tipos[i]} de {vinhos[i]}, "
    print(f"Obrigado por comprar na Vinheria. Voce comprou {garrafas}totalizando "
          f"R${valor_total},00 e será entregue em {endereco}")



