from flask import Flask, jsonify, request
from Contact import Contact
from Agenda import Agenda

app = Flask(__name__)
agenda1 = Agenda()

@app.route('/user')
def get_contacts():
    return jsonify({
        "Data": [agenda1.contactos]
    })

@app.route('/user/<string:atributo>', methods=['GET'])
def get_contact(atributo):
    foundContact = agenda1.find_contact(atributo)
    return jsonify(foundContact) 

@app.route('/user', methods=['POST'])
def create_contact():
    newContact = {
        "id": len(agenda1.contactos) + 1,
        "contactInfo": request.json['contactInfo'],
        "name": request.json['name'],
        "nickname": request.json['nickname'],
        "preferred": request.json['preferred']
    }

    contacto3 = Contact(newContact['name'], newContact['nickname'], newContact['contactInfo'][0], newContact['contactInfo'][1], newContact['contactInfo'][2], newContact['contactInfo'][3], newContact['preferred'])
    data = contacto3.conver_data()
    print(newContact['contactInfo'][0])
    agenda1.add_contact(data)

    return jsonify(agenda1.contactos)

@app.route('/user/<string:id>', methods=['DELETE'])
def delete_products(id):
    contactDelete = agenda1.delete_contact(id)
    return jsonify(contactDelete)

@app.route('/user/<string:id>', methods=['PUT'])
def edit_contacts(id):
        foundContact = agenda1.find_contact(id)
        foundContact[0]['name'] = request.json['name']
        foundContact[0]['nickname'] = request.json['nickname']
        foundContact[0]['preferred'] = request.json['preferred']
        
        return jsonify(foundContact[0])

if __name__ == "__main__":
    app.run(debug=True)

