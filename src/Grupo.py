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
                    "elemento": contacto
                }
        return {"message": "El contacto no se encuentra en este grupo"}

    def list_group(self):
        pass

    def conver_group(self):
        return {"list": self.__lista}


FAMILIA = Grupo("Familia")
AMIGOS = Grupo("Amigos")
TRABAJO = Grupo("Trabajo")


if __name__ == "__main__":
    contacto1 = Contact("Juan Z", "juan", 57, 123456, "juan@mail.com", "cra78", True)
    contacto2 = Contact("Carlos P", "carlos", 591, 123456, "carlos@mail.com", "cra78", True)
    contacto3 = Contact("Leidy G", "lady", 1, 123456, "lady@mail.com", "cra78", True)
    contacto4 = Contact("Javier N", "javi", 591, 123456, "javi@mail.com", "cra78", True)
    contacto5 = Contact("Marcela A", "marce", 52, 123456, "marce@mail.com", "cra78", True)

    FAMILIA.add_contact_group(contacto1)
    FAMILIA.add_contact_group(contacto2)
    AMIGOS.add_contact_group(contacto1)
    AMIGOS.add_contact_group(contacto5)
    TRABAJO.add_contact_group(contacto3)

    print(FAMILIA.conver_group())
    print(AMIGOS.conver_group())
    print(TRABAJO.conver_group())

    FAMILIA.remove_contact_group(2)
    print(FAMILIA.conver_group())

