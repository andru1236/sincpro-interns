class Agenda:
	contactos = []

	def addContacto(a):
		contactos.append(a)

	def buscarContacto(a):
		for contacto in contactos:
			if contacto.getPreferredInfo() == a and contactos.len() > 0:
				return contacto
			else:
				print "No es posible buscar el contacto solicitado"