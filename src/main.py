from flask import Flask
app = Flask(__name__)

def suma(a,b):
 return a+b

@app.route("/")
def hello():
        res = suma(13,22)
        return "Hola Jorge, Mario  y Fatima, soy Francisco y la suma de 3 + 2 es  %s" % (res)
if __name__ == "__main__":
        app.run(host='0.0.0.0',port=4000)

