palavra = input('Digite uma palavra: ').lower()
contador_vogais = 0

for letra in palavra:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        contador_vogais += 1
print(palavra.replace('a', '').replace('e', '').replace(
    'i', '').replace('o', '').replace('u', ''))
print('Esta palavra tinha ', contador_vogais, ' vogais')
