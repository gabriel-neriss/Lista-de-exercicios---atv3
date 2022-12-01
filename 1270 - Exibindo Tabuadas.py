def exibindo_tabuadas():

    n1 = int(input('n'))
    n2 = int(input('n'))
    i = 0
    
    if (n1 > n2):
      print('Nenhuma tabuada no intervalo!')
    else:
      for x in range(n1, n2 + 1): 
        for i in range(1, 11): 
          print( x,'x' ,i, '=', x * i)
        print('----------')
    
exibindo_tabuadas()
