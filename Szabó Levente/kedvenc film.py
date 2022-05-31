def óra(perc):
    óra = perc // 60
    perc = perc - óra * 60
    return str(óra) + 'óra' + str(perc) + 'perc'
for _ in range(3):
    cím = input('Add meg a film címét! ')
    hossz = int(input('Hány perces a film? '))
    print('A(z)', cím, (hossz), óra, 'hosszú.')