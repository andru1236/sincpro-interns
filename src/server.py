from Agenda import Agenda
from flask import Flask
from flask_restful import Resource, Api
from Grupo import Grupo

app = Flask(__name__)

nuevaAgenda = Agenda()
nuevaAgenda.addContacto('Luis')
## []

@app.route("/")
def home():
    return {"hola" : nuevaAgenda.contactos}

if __name__ == '__main__':
    app.run(host='0.0.0.0')
