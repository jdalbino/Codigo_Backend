from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicial():
    print("me llamaron!")

    return "Bienvenido a mi API"

@app.route('/api/info')
def info_app():
     return {
         'fecha':'10-10-2021',
         'user':'Juan Diego',
         'lastname': 'Albino Ramos',
     }

app.run(debug=True)

print("yo no me ejecuto")