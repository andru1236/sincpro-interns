# Clase agenda
from Contact import Contact

class Agenda:

	contactos = []

	def agregarContacto(self, contacto):
		self.contactos.append(contacto)

	def borrarContacto(self, id):
		for contacto in self.contactos:
			if contacto.contactId == id:
				self.contactos.remove(contacto)
				print("Se ha eliminado el contacto")
				break

	def buscarContacto(self, buscar):
		for contacto in self.contactos:
			if contacto.nickname == buscar:
				return f"Resultado de la busqueda: {contacto}"
			else:
				return "No se encontró el contacto solicitado"

	def __str__(self):
		agenda_str = ""
		for contacto in self.contactos:
			agenda_str += contacto.__str__()
		return agenda_str

if __name__ == "__main__":
	contacto1 = Contact("Juan Diaz", "Juan", 57, 123456, "juan@mail.com", "cra78", True)
	contacto2 = Contact("Carlos Perez", "Charles", 591, 123456, "carlos@mail.com", "cra78", True)
	contacto3 = Contact("Leidy Martinez", "Lady", 52, 123456, "leidy@mail.com", "cra78", False)
	agenda1 = Agenda()
	agenda1.agregarContacto(contacto1)
	agenda1.agregarContacto(contacto2)
	agenda1.agregarContacto(contacto3)
	print(agenda1)
	agenda1.borrarContacto(1)
	print(agenda1)