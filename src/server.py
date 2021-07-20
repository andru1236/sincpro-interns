from Agenda import Agenda
from flask import Flask, jsonify
from Grupo import Grupo
from Contact import Contact

app = Flask(__name__)

nuevaAgenda = Agenda()
nuevaAgenda.addContacto('Luis')

newContact = Contact('jairo', 'jairo_5', 'programer', 'iso')
## []

@app.route("/")
def home():
    return jsonify(newContact.get)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
