km = float(input('Digite a que velocidade você estava? '))
if km <= 80:
    print('Você estava numa velocidade de {:.0f}KM/H ,VELOCIDADE PERMITIDA!'.format(km))
else:
    print('Você ultrapassou o limite de 80 KM/H, ENTÃO SERÁ MULTADO!')
    multa = (km - 80) * 7
    print('A multa será de R${:.2f}, DIRIJA COM CUIDADO!'.format(multa))

