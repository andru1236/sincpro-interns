from flask import Flask, jsonify, request
from Contact import Contact
from Agenda import Agenda

app = Flask(__name__)
agenda = Agenda()

@app.route('/user')
def get_contacts():
    return jsonify({
        "Data": [agenda.contactos]
    })

@app.route('/user/<string:atributo>', methods=['GET'])
def get_contact(atributo):
    found_contact = agenda.find_contact(atributo)
    return jsonify(found_contact) 

@app.route('/user', methods=['POST'])
def create_contact():
    new_contact = {
        "id": len(agenda.contactos) + 1,
        "contactInfo": request.json['contactInfo'],
        "name": request.json['name'],
        "nickname": request.json['nickname'],
        "preferred": request.json['preferred']
    }

    contacto = Contact(new_contact['name'], new_contact['nickname'], new_contact['contactInfo'][0], new_contact['contactInfo'][1], new_contact['contactInfo'][2], new_contact['contactInfo'][3], new_contact['preferred'])
    data = contacto.conver_data()
    agenda.add_contact(data)

    return jsonify(agenda.contactos)

@app.route('/user/<string:id>', methods=['DELETE'])
def delete_products(id):
    contact_delete = agenda.delete_contact(id)
    return jsonify(contact_delete)

@app.route('/user/<string:id>', methods=['PUT'])
def edit_contacts(id):
        found_contact = agenda.find_contact(id)
        found_contact[0]['name'] = request.json['name']
        found_contact[0]['nickname'] = request.json['nickname']
        found_contact[0]['preferred'] = request.json['preferred']
        
        return jsonify(found_contact[0])

if __name__ == "__main__":
    app.run(debug=True)

