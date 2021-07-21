
class Agenda:

	contactos = []

	def addContact(self, a):
		self.contactos.append(a)
	
	def DeleteContact(self, id):
			DeleteContact = [contact for contact in self.contactos if contact['id'] == int(id)]
			if len(DeleteContact) > 0:
				self.contactos.remove(DeleteContact[0])
				return DeleteContact
			else:
				return {"messaje": "Contact not found"}

	def findContact(self, from Contact import Contacta):
			found = [item for item in self.contactos if item['id'] == int(a)]
			if(len(found) > 0):
				return found
			else: 
				print(type(a))
				return {"mensaje": "not found"}

