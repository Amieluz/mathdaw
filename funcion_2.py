#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Beatriz Vidal
#
# Created:     19/04/2012
# Copyright:   (c) ALUMNO 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
def calcularDistancia(x,y):
    distancia=x-y;
    return distancia;

def main():
   distancia1=20;
   distancia2=13;
   resultado=calcularDistancia(distancia1,distancia2);
   print "la distancia entre los dos puntos es %d" %resultado+ " metos";

if __name__ == '__main__':
    main()
