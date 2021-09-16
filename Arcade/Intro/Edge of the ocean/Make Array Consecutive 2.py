def makeArrayConsecutive2(statues):
    statues.sort()
    primer_valor = (statues[0])
    ultimo_valor = (statues[-1])
    lista = list(range(primer_valor, ultimo_valor + 1))
    x = len(statues)
    y = len(lista)
    return (y - x)