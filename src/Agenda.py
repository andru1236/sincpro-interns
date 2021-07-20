# Clase agenda
from Contact import Contact

class Agenda:

	contactos = []

	def agregarContacto(self, contacto):
		self.contactos.append(contacto)

	def buscarContacto(self, buscar):
		for contacto in contactos:
			if contacto.nickname == buscar:
				return contacto
			else:
				print ("No se encuentra el contacto solicitado")

	def __str__(self):
		agenda_str = ""
		for contacto in self.contactos:
			agenda_str += contacto.__str__()
		return agenda_str

if __name__ == "__main__":
	contacto1 = Contact("Juan Diaz", "Juan", 57, 123456, "juan@mail.com", "cra78", True)
	contacto2 = Contact("Juan Diaz", "Juan", 57, 123456, "juan@mail.com", "cra78", True)
	contacto3 = Contact("Juan Diaz", "Juan", 57, 123456, "juan@mail.com", "cra78", True)
	agenda1 = Agenda()
	agenda1.agregarContacto(contacto1)
	agenda1.agregarContacto(contacto2)
	agenda1.agregarContacto(contacto3)
	print(agenda1)