def f20(x,y):
    lista=[]
    if x<=y:
        num = x;
        while num <= y:
            lista.append(num);
            num+=5
        return lista;
    else:
        print "El primer numero ha de ser menor que el segundo, para poder operar";

