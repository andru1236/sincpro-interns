import pytest
from Grupo import Grupo
from Contact import Contact


def test_add_contact_group():
    FAMILIA = Grupo("Familia")
    AMIGOS = Grupo("Amigos")
    contacto1 = Contact("Juan Perez", "juanito", 57, 123456,
                        "juan@mail.com", "cra100", "email")
    contacto2 = Contact("Leidy Martinez", "lady", 52, 789456,
                        "lady@mail.com", "cra50", "telefono")
    FAMILIA.add_contact_group(contacto1)
    AMIGOS.add_contact_group(contacto1)
    FAMILIA.add_contact_group(contacto2)
    AMIGOS.add_contact_group(contacto2)

    assert isinstance(FAMILIA.lista[0], Contact) == True
    assert isinstance(FAMILIA.lista[1], Contact) == True
    assert isinstance(AMIGOS.lista[0], Contact) == True
    assert isinstance(AMIGOS.lista[1], Contact) == True


def test_remove_contact_group():
    FAMILIA = Grupo("Familia")
    FAMILIA.lista = [Contact("Juan Perez", "juanito", 57, 123456, "juan@mail.com", "cra100", "email"),
                     Contact("Leidy Martinez", "lady", 52, 789456, "lady@mail.com", "cra50", "telefono")]
    tam_original = len(FAMILIA.lista)
    delete = FAMILIA.lista[0].contactId
    FAMILIA.remove_contact_group(delete)
    assert len(FAMILIA.lista) == tam_original - 1


def test_conver_group():
    FAMILIA = Grupo("Familia")
    FAMILIA.lista = [Contact("Juan Perez", "juanito", 57, 123456, "juan@mail.com", "cra100", "email"),
                     Contact("Leidy Martinez", "lady", 52, 789456, "lady@mail.com", "cra50", "telefono")]
    assert isinstance(FAMILIA.conver_group()["list"][0], Contact)
    assert isinstance(FAMILIA.conver_group()["list"][1], Contact)
