class Agenda:
	contactos = []

	def addContacto(self, a):
		self.contactos.append(a)

	def buscarContacto(self, a):
		for contacto in contactos:
			if contacto.getPreferredInfo() == a and contactos.len() > 0:
				return contacto
			else:
				print ("No es posible buscar el contacto solicitado")