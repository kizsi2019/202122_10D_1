kutya {
    'Neve': 'Bodri '
    'Életkor':12
    'Fajtája':'Goldi'
    'Oltás': True


}
print(kutya)
# szótár elemeinek elérése kulcs alapján
print(kutya['eletkor'])
print(kutya.get('eletkor'))

    # nem létező kulcsra való hivatkozás -> KeyError
    # print(diak['osztaly'])

    # nem létező kulcsra hivatkozunk a .get metódussal, 
    # ilyenkor a megadott alapértékkel tér vissza
print(kutya.get('kollegista', 'nem'))

    # ellenőrzés, hogy létezik-e a kulcs
print('keresztnev' in kutya)