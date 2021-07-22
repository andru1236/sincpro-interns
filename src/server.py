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
    

@app.route('/user/atribute')
def get_contanct_atrubute():

    atribute = request.args.get('info')
    def get_contact(x):
        for item in agenda.contactos:
            for b in item.values():
                if b == x:
                    return item

    found_contact_atribute = get_contact(atribute)

    return jsonify({
        "Data": [found_contact_atribute]
    })


@app.route('/user/<string:atributo>', methods=['GET'])
def get_contact(atributo):
    found_contact = agenda.find_contact(atributo)
    return jsonify(found_contact) 


@app.route('/user', methods=['POST'])
def create_contact():
    new_contact = {
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
        found_contact: Contact = agenda.find_contact(id)
        print(type(found_contact))
        print(found_contact)
        contact_info = request.json['contactInfo']
        print(contact_info[1])
        print(found_contact['contactInfo'][0])
        found_contact['contactInfo'][0] = contact_info[0]
        found_contact['contactInfo'][1] = contact_info[1]
        found_contact['contactInfo'][2] = contact_info[2]
        found_contact['contactInfo'][3] = contact_info[3]

        found_contact['name'] = request.json['name']
        found_contact['nickname']= request.json['nickname']
        found_contact['preferred'] = request.json['preferred']
        
        return jsonify(found_contact)

if __name__ == "__main__":
    app.run(debug=True)

    