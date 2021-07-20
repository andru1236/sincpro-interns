from flask import Flask, jsonify, request
from Contact import Contact
import json

from Agenda import Agenda

app = Flask(__name__)

agenda1 = Agenda()

contacto3 = Contact("Juan Diaz", "Juan", 57, 123456, "juan@mail.com", "cra78", True)
data = contacto3.converData()

agenda1.agregarContacto(data)

@app.route('/user')
def getContacts():
    return jsonify({
        "Data": [agenda1.contactos]
    })

@app.route('/user/<string:atributo>', methods=['GET'])
def getContact(atributo):
    found = [item for item in agenda1.contactos if item['nickname'] == atributo]
    if(len(found) > 0):
        return jsonify(found)
    return jsonify({"mensaje": "not found"})

@app.route('/user', methods=['POST'])
def createContact():
    newContact = {
        "id": request.json['contactId'],
        "contactInfo": request.json['contactInfo'],
        "name": request.json['name'],
        "nickname": request.json['nickname'],
        "preferred": request.json['preferred']
    }
    agenda1.agregarContacto(newContact)

    return jsonify(agenda1.contactos)

if __name__ == "__main__":
    app.run(debug=True)
