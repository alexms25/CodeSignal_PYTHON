def adjacentElementsProduct(inputArray):
    datomayor = len(inputArray)
    datomenor = datomayor - 1
    lista = []
    for x in inputArray:
        datomayor -= 1
        datomenor -= 1
        z = (inputArray[datomayor])
        y = (inputArray[datomenor]) 
        x = z*y
        if datomayor >= 1:
            lista.append(x)
        else:
            lista.sort()
            lista.reverse()
            return (lista[0])
        