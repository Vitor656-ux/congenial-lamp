def media(lista):
    
    total = 0
    for i in lista:

         total += i

    media = total / len(lista)
    return total
    
numeros = [6, 8, 9, 5]

print(media(numeros))
