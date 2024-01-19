lista=[]
listaPar=[]
listaInpar=[]

import os
class ListaNumeros:
    tam = 0
    num = 0

    def __init__(self, a):
        self.tam = a

    def ordenarLista(self):
        for i in range(self.tam):
            self.num=int(input(""))
            lista.append(self.num)
            if self.num % 2 == 0:
                listaPar.append(self.num)
            else:
                listaInpar.append(self.num)
        lista.sort()
        listaPar.sort()
        listaInpar.sort()
        print(lista)
        print(listaPar)
        print(listaInpar)

def main():
    os.system('cls')
    print("Lista")
    tam=int(input("Ingresa el tamaño de la lista: "))
    obj=ListaNumeros(tam)
    obj.ordenarLista()

if __name__ == "__main__":
    main()
