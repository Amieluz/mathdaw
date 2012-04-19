def f11(x,y):
    """Una lista con todos los valores enteros entre ellos (incluyendo x e y)"""
    lista = [];
    aux = 0;
    if x > y:
        for i in range(y,x+1):
            lista.append(i)
        return lista;
    else:
        for i in range(x,y+1):
            lista.append(i)
        return lista;