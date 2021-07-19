# Clase de contacto

class Contact():

    countContactId = 0

    def __init__(self, name, nickname, contactInfo, preferred):
        Contact.countContactId += 1
        self.__contactId = Contact.countContactId
        self.__name = name
        self.__nickname = nickname
        self.__contactInfo = contactInfo
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
    def contactoInfo(self):
        return self.__contactInfo
    
    @contactInfo.setter
    def contactInfo(self, contactInfo):
        self.__contactInfo = contactInfo
    
    @property
    def preferred(self):
        return self.__preferred
    
    @preferred.setter
    def prefered(self, preferred):
        self.__preferred = preferred