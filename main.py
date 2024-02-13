from flask import Flask, request, render_template
import forms
import math
import os
class Distancia:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    res = 0

    def __init__(self, a, b, c, d):
        self.x1 = a
        self.y1 = b
        self.x2 = c
        self.y2 = d
    
    def calcular(self):
        return math.sqrt(((self.x2-self.x1)**2)+((self.y2-self.y1)**2))
         
class CalcularResistencia:
    b1 = ''
    b2 = ''
    b3 = ''
    r = 0
    valor = 0
    vMax = 0
    vMin = 0
    c1 = ''
    c2 = ''
    c3 = ''
    cr = ''

    def __init__(self, z, y, x, w):
        self.b1 = z
        self.b2 = y
        self.b3 = x
        self.r = w
    
    def calR(self):

        colores = {
            'Negro':'#000000', 
            'Cafe':'#A18262', 
            'Rojo':'#FF0000', 
            'Naranja':'#FF8000', 
            'Amarillo':'#FFFF00', 
            'Verde':'#1CF000',
            'Azul':'#0000FF ', 
            'Violeta':'#4C2882',
            'Gris':'#9B9B9B',
            'Blanco':'#FFFFFF',
            'Oro':'#FFBF00 ',
            'Plata':'#E3E4E5'
            }
        
        val1 = {
            'Negro':'0', 
            'Cafe':'1', 
            'Rojo':'2', 
            'Naranja':'3', 
            'Amarillo':'4', 
            'Verde':'5',
            'Azul':'6', 
            'Violeta':'7',
            'Gris':'8',
            'Blanco':'9'
            }
        
        val2 = {
            'Negro':1, 
            'Cafe':10, 
            'Rojo':100, 
            'Naranja':1000, 
            'Amarillo':10000, 
            'Verde':100000,
            'Azul':1000000, 
            'Violeta':10000000,
            'Gris':100000000,
            'Blanco':1000000000,
            'Oro':5,
            'Plata':10
            }
        v=val1[self.b1] + val1[self.b2]
        re=val2[self.r]
        valor = int(v) * val2[self.b3]
        vMax = valor + ((valor*re)/100)
        vMin = valor - ((valor*re)/100)
        c1 = colores[self.b1]
        c2 = colores[self.b2]
        c3 = colores[self.b3]
        cr = colores[self.r]
        return valor, vMax, vMin, c1, c2, c3, cr

app=Flask(__name__)
def index():
    return render_template("layout.html")

@app.route("/")
def index():
    return render_template("formulario.html")

@app.route("/resultado",methods=["GET","POST"])
def opc():
    res = 0
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        op=request.form.get("Ope")
        if op == "S":
            res = str(int(num1)+int(num2))
        elif op == "R":
            res = str(int(num1)-int(num2))
        elif op =="M":
            res = str(int(num1)*int(num2))
        elif op =="D":
            res = str(int(num1)/int(num2))
        return "<h1>El resultado es : {}</h1>".format(res)

@app.route("/calcu",methods=["GET","POST"])
def alumnos():
    os.system('cls')
    res=""
    cal_form=forms.UserForm(request.form)
    if request.method=='POST':
        x1=cal_form.x1.data
        y1=cal_form.y1.data
        x2=cal_form.x2.data
        y2=cal_form.y2.data
        obj=Distancia(x1,y1,x2,y2)
        res = obj.calcular()
        print(res)
    return render_template("distancia.html", form=cal_form, res=res)

@app.route("/resistencia", methods=["GET", "POST"])
def resi():
    os.system('cls')
    valor = 0 
    vMax= 0
    vMin=0
    c1=''
    c2=''
    c3=''
    cr=''
    cal_form=forms.ResistenciaForm(request.form)
    if request.method=='POST':
        b1=cal_form.banda1.data
        b2=cal_form.banda2.data
        b3=cal_form.banda3.data
        r=cal_form.resColor.data
        obj=CalcularResistencia(b1,b2,b3,r)
        valor,vMax,vMin, c1, c2, c3, cr = obj.calR()
    return render_template("resistencia.html", form=cal_form, valor=valor, vMax=vMax, vMin=vMin, c1=c1, c2=c2,c3=c3,cr=cr)


if __name__ == "__main__":
    app.run(debug=True)