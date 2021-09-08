def main():
    #escribe tu código abajo de esta línea
 
P=float(input())
suma=P
X=0
while P>0:
    P=float(input())
    X=X+1
    if P>0:
     suma=suma+P
if P<=0:
    prd=suma/X
    print(prd)
