def diferenca():
    while True:
        hi = int(input('Digite a hora inicial: '))
        if 0 <= hi > 24:
            print('Hora inválida! Tente novamente! ')
        else:
            break

    while True:
        hf = int(input('Digite a hora final: '))
        if 0 <= hf > 24:
            print('Hora inválida! Tente novamente: ')
        else:
            break


    hor_segundos = (hf * 3600) - (hi * 3600)

    print(f'O total de horas em segundos é: {hor_segundos} ')

    while True:
        mi = int(input('Digite os minutos iniciais: '))
        if mi > 60:
            print('Minutos inválidos! Tente novamente! ')
        else:
            break
    while True:
        mf = int(input('Digite os minutos finais: '))
        if mf > 60:
            print('Minutos inválidos! Tente novamente! ')
        else:
            break

    min_segundos = (mf * 60) - (mi * 60)
    print(f'O total de horas em segundos é: {min_segundos} ')

    while True:
        si = int(input('Digite os segundos iniciais: '))
        if si > 60:
            print('Segundos inválidos! Tente novamente! ')
        else:
            break
    while True:
        sf = int(input('Digite os segundos finais: '))
        if sf > 60:
            print('Segundos inválidos! Tente novamente! ')
        else:
            break

    segundos = (sf - si)
    print(f'O total de horas em segundos é: {segundos} ')

    segundos_totais = (hor_segundos + min_segundos + segundos)

    print(f'A diferença entre os segundos finais e iniciais é: {segundos_totais}')


diferenca()