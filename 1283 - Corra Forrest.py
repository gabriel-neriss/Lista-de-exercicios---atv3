# entrada os tempos das corridas que estão nos papeis
#  calcule a média aritmética dos tempos gastos
#  exibir todos os tempos de corrida abaixo dessa média


def media ():
    
    tempo_corrida = int(input ('Tempo de corrida?'))
    cont = media = tempo_total = 0
    lista = []
    while tempo_corrida > 0:
        lista.append(tempo_corrida)
        cont +=1
        tempo_total += tempo_corrida
        media = tempo_total / cont
        tempo_corrida = int(input ('Tempo de corrida?'))
    print ('MEDIA:', '{:.2f}'.format(media))
    for tempos in lista:
        if tempos < media:
            print (tempos)


media ()

