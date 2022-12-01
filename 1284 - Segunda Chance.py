def notas_finais (originais, novas):
    finais = []
    for i in range (len(originais)):
        if novas[i] == 10 and originais[i] < 10:
            finais.append(min(originais[i] + 2, 10))
        else:
            finais.append (originais[i])
    return finais

def notas_alteradas (originais, finais):
    qtd_alteradas = 0
    for i in range (len(originais)):
        if originais[i] != finais[i]:
            qtd_alteradas += 1
    return qtd_alteradas

def exibe (originais, finais, qtd_alteradas):
    print (f'NOTAS ALTERADAS: {qtd_alteradas}')

    for i in range(len(originais)):
        alterou = ('*' if originais [i] != finais[i] else '-')
        print (f'{alterou} ({i+1:30}) original: {originais[i]:05.2f} | final: {final[i]:05.2f}')

n = int(input())
originais = coleta_notas(n)
novas = coleta_notas(n)
finais = notas_finais (originais, novas)
qtd_alteradas = notas_alteradas(originais, finais)
exibi(originais, finais, qtd_alteradas)
