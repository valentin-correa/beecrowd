apariciones = {}

rango = int(input())

for i in range(rango):
    number = int(input())

    if number not in apariciones:
        apariciones[number] = 1
    else:
        apariciones[number] += 1

orden = sorted(apariciones)

for number in orden:
    print(f"{number} aparece {apariciones[number]} vez(es)")