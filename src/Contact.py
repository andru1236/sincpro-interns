# Clase de contacto

class Contact:

    countContactId = 0

    def __init__(self, name, nickname, code, phone, email, address, preferred):
        Contact.countContactId += 1
        self.__contactId = Contact.countContactId
        self.__name = name
        self.__nickname = nickname
        self.__contactInfo = list((code, phone, email, address))
        self.__preferred = preferred

    @property
    def contactId(self):
        return self.__contactId

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname):
        self.__nickname = nickname

    @property
    def contactInfo(self):
        return self.__contactInfo

    @contactInfo.setter
    def contactInfo(self, contactInfo):
        self.__contactInfo = contactInfo

    @property
    def preferred(self):
        return self.__preferred

    @preferred.setter
    def preferred(self, preferred):
        self.preferred = preferred


        Contacto: idContacto={self.contactId},
        nombre={self.name},
        apodo={self.nickname},
        telefono={self.contactInfo[0]},
        email={self.contactInfo[1]},
        email={self.contactInfo[2]},
        direccion={self.contactInfo[3]},
        preferido={self.preferred}
        
    def conver_data(self):
        return {
            "name": self.__name,
            "id": self.__contactId,
            "nickname": self.__nickname,
            "contactInfo": self.__contactInfo,
            "preferred": self.__preferred
        }
        