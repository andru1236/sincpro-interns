from flask import Flask, jsonify, request
from Contact import Contact
from Agenda import Agenda
from Grupo import Grupo

app = Flask(__name__)
agenda = Agenda()

familia = Grupo("Familia")
amigos = Grupo("Amigos")
trabajo = Grupo("Trabajo")


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
        "preferred": request.json['preferred'],
        "group": request.json['group']
    }    

    contacto = Contact(new_contact['name'], new_contact['nickname'], new_contact['contactInfo'][0], new_contact['contactInfo'][1], new_contact['contactInfo'][2], new_contact['contactInfo'][3], new_contact['preferred'])
    data = contacto.conver_data()
    agenda.add_contact(data)
    
    if new_contact['group'] == "familia":
        familia.add_contact_group(data)
        
    if new_contact['group'] == "trabajo":
        trabajo.add_contact_group(data)    

    if new_contact['group'] == "amigos":
        amigos.add_contact_group(data)

    return jsonify(agenda.contactos)

@app.route('/user/<string:id>', methods=['DELETE'])
def delete_products(id):
    contact_delete = agenda.delete_contact(id)
    return jsonify(contact_delete)

@app.route('/user/<string:id>', methods=['PUT'])
def edit_contacts(id):
        found_contact: Contact = agenda.find_contact(id)
        contact_info = request.json['contactInfo']
        
        found_contact['contactInfo'][0] = contact_info[0]
        found_contact['contactInfo'][1] = contact_info[1]
        found_contact['contactInfo'][2] = contact_info[2]
        found_contact['contactInfo'][3] = contact_info[3]

        found_contact['name'] = request.json['name']
        found_contact['nickname']= request.json['nickname']
        found_contact['preferred'] = request.json['preferred']
        
        return jsonify(found_contact)

@app.route('/user/group')
def get_groups():
    return jsonify({
        "familia": [familia.return_list()],
        "trabajo": [trabajo.return_list()],
        "amigos": [amigos.return_list()]
    })

@app.route('/user/group/<string:group>')
def get_group(group):
    if group == "familia":
        return jsonify(familia.return_list())
        
    if group == "trabajo":
        return jsonify(trabajo.return_list())  

    if group == "amigos":
        return jsonify(amigos.return_list())

if __name__ == "__main__":
    app.run(debug=True)

    