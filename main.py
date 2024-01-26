from flask import Flask, request, render_template

app=Flask(__name__)
def index():
    return render_template("layout.html")

@app.route("/")
def index():
    return render_template("formulario.html")

'''
@app.route("/multiplica/",methods=["GET", "POST"])
def mult():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")

        return "<h1>El resultado es : {}</h1>".format(str(int(num1)*int(num2)))
    else:
        return 
            
            <form action="/multiplica"method="POST">
                <label>N1: </label>
                <input type="text" name="n1"/>
                <label>N2: </label>
                <input type="text" name="n2"/>
                <input type="submit">
            </form>
            

'''

'''
@app.route("/formulario")
def calculo():
    return render_template("formulario.html")


'''

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


if __name__ == "__main__":
    app.run(debug=True)