def main():
    #escribe tu código abajo de esta línea

     caracter= int(input())
    y=0
    for numero in range (caracter):
        y=y+1
        if numero%2==0:
            print(str(y)+"-#")
        else:
            print(str(y)+"-%")

   
