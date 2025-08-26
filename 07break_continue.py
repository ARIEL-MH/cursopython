# ** Break && Continue

# break termina el ciclo antes de iterarse todos los elementos
# continue salta a la siguiente iteración

# funcionan con for y while

for number in range(1, 11):

    if number % 2 == 0:
        continue  # saltar a la siguiente iteración

    if number == 7:
        break

    print(f'Valor: {number}')
