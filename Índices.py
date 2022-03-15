
from time import sleep
s = input("Qual é o seu nome? ")
print("Olá {}, é bom ter você aqui".format(s))
sleep(2)
print("Então {}, vamos começar ".format(s))
sleep(2)
print("Abaixo você me passará uns valores relacionados ao balanço patrimonial da empresa a qual quer examinar!")
sleep(3)
di = 0
while di != 4:
    print( '''
    [1]Índice de Liquidez
    [2]Índice de Atividade
    [3]Índice de Endividamento
    [4]Ìndice de Eentabilidade''')
    int(input("Qual índice deseja calcular? "))
    if di == 1:
        print("Índice de liquidez selecionado. ")
        n1 = int(input("O ativo circulante total da empresa: R$"))
        n2 = int(input("O Passivo circulante total da empresa: R$"))
        n3 = int(input("O Valor do estoque da empresa: R$"))
        n4 = int(input("O valor imediato em bancos: R$"))
        n5 = int(input("O valor imediato em caixa: R$"))
        n6 = int(input("O valor imediato pra resgate financeiro: R$"))
        n7 = int(input("O ativo realizavel a longo prazo: R$"))
        n8 = int(input("O passivo de longo prazo: R$"))

        lc = n1 / n2
        ls = ((n1 - n3) / n2) * 100
        li = ((n4+n5+n6) / n2) * 100
        lg = ((n1 + n7) / (n2 + n8)) * 100

        print("Bom {}, tenho algumas informações para te passar a respeito de sua empresa".format(s))
        sleep(3)
        print("Em seu índice de Liquidez corrente:")
        print("Para cada 1 real de divida a empresa detem de R${:.2f} para saldar suas dividas".format(lc))
        sleep(8)
        print("Em seu índice de Liquidez seca:")
        print("Os ativos circulantes, Líquidos dos estoques tem o potencial de {:.2f}%, para cobrir todas as dívidas de curto prazo ".format(ls))
        sleep(8)
        print("Em seu índice de Liquidez imediata:")
        print("A empresa possui hoje {:.2f}% do valor necessário para cobrir suas dividas no momento".format(li))
        sleep(8)
        print("Em seu índice de liquidez geral:")
        print("A empresa possuí {:.2f}% do valor necessário para arcar com todas as suas obrigações.".format(lg))
        if (li>=100) :
            print("Pagamento a curto prazo consideraado bom")
        else:
            print("Pagamento a curto prazo considerado ruim")
        sleep(5)
        if lg >=100:
            print("Pagamento a longo prazo considerado bom")
        else:
            print("Pagamento a longo prazo considerado ruim")
        sleep(5)
    if di == 2:
        print()





