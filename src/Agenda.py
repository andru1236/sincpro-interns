
class Agenda:

	contactos = []

	def add_contact(self, a):
		self.contactos.append(a)
	
	def delete_contact(self, id):
			DeleteContact = [contact for contact in self.contactos if contact['id'] == int(id)]
			if len(DeleteContact) > 0:
				self.contactos.remove(DeleteContact[0])
				return DeleteContact
			else:
				return {"messaje": "Contact not found"}

	def find_contact(self, a):
			found = [item for item in self.contactos if item['id'] == int(a)]
			if(len(found) > 0):
				return found
			else: 
				return {"mensaje": "not found"}

