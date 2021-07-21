from flask import Flask, jsonify, request
from Contact import Contact
from Agenda import Agenda

app = Flask(__name__)

agenda1 = Agenda()

contacto3 = Contact("Juan Diaz", "Juan", 57, 123456, "juan@mail.com", "cra78", True)
data = contacto3.converData()

agenda1.addContact(data)

@app.route('/user')
def getContacts():
    return jsonify({
        "Data": [agenda1.contactos]
    })

@app.route('/user/<string:atributo>', methods=['GET'])
def getContact(atributo):
    foundContact = agenda1.findContact(atributo)
    return jsonify(foundContact) 

@app.route('/user', methods=['POST'])
def createContact():
    newContact = {
        "id": request.json['contactId'],
        "contactInfo": request.json['contactInfo'],
        "name": request.json['name'],
        "nickname": request.json['nickname'],
        "preferred": request.json['preferred']
    }
    agenda1.addContact(newContact)

    return jsonify(agenda1.contactos)

@app.route('/user/<string:id>', methods=['DELETE'])
def deleteProduct(id):
    contactDelete = agenda1.DeleteContact(id)
    return jsonify(contactDelete)


if __name__ == "__main__":
    app.run(debug=True)
