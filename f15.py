#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ALUMNO
#
# Created:     19/04/2012
# Copyright:   (c) ALUMNO 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
def f15(x,y):
    cadena=""
    if (x>24):
        print "Error, el primer numero debe estar entre 0 y 24"
    elif (x<0):
        print "Error, el primer numero debe estar entre 0 y 24"
    elif (y<0):
        print "Error, el segundo numero debe estar entre 0 y 60"
    elif (y>60):
        print "Error, el segundo numero debe estar entre 0 y 60"
    else:
        print "Son las %d:%d"(x,y)



def main():
    f15(13,13)

if __name__ == '__main__':
    main()
