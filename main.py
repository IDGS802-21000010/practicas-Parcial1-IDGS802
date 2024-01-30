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

if __name__ == "__main__":
    app.run(debug=True)