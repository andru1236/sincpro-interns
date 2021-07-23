from Contact import Contact

class Grupo:
    
    def __init__(self, group_name):
        self.__group_name = group_name
        self.__lista = []

    def add_contact_group(self, contact):
        self.__lista.append(contact)

    def remove_contact_group(self, id):
        for contacto in self.__lista:
            if contacto.contactId == id:
                self.__lista.remove(contacto)
                return {
                    "message": "Contacto removido del grupo",
                    "element": contacto
                }
        return {"message": "El contacto no se encuentra en este grupo"}

    def list_group(self):
        pass

    def conver_group(self):
        return {"list": self.__lista}

    def return_list(self):
        return self.__lista




