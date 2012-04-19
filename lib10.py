def f10(x,y):
    """hace una suma y calcula si el resultado es primo"""

    suma=x+y
    actual=2
    es_primo=True
    while actual<suma:
        if x%actual==0:
            es_primo=False
        actual=actual+1
    if es_primo:
        return "x es primo"
    else:
        return "no es primo"
