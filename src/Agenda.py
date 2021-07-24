
class Agenda:

	contactos = []

	def add_contact(self, a):
		self.contactos.append(a)
	
	def delete_contact(self, id):
			delete_contact = [contact for contact in self.contactos if contact['id'] == int(id)]
			if len(delete_contact) > 0:
				self.contactos.remove(delete_contact[0])
				return self.contactos
			return {"messaje": "Contact not found"}

	def find_contact(self, a):
			if(len(self.contactos) > 0):
				return self.contactos[int(a)-1]
			return {"mensaje": "not found"}
            
