import os
class Piramide:
    num = 0

    def __init__(self, a):
        self.num = a
    
    def generarPiramide(self):
        i=1
        while i <= self.num:
            print("*"*i)
            i+=1

def main():
    os.system('cls')
    print("Piramide")
    num=int(input("Ingresa el numero del tamaño: "))
    obj=Piramide(num)
    obj.generarPiramide()

if __name__ == "__main__":
    main()
