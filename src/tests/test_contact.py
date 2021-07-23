import pytest
from Contact import Contact


def test_contacto():
    contacto = Contact("Juan Perez", "juanito", 57, 123456, "juan@mail.com", "cra100", "email")
    datos = {
        "name": contacto.name,
        "id": contacto.contactId,
        "nickname": contacto.nickname,
        "contactInfo": contacto.contactInfo,
        "preferred": contacto.preferred
    }
    expectativa = {
        "name": "Juan Perez",
        "id": 1,
        "nickname": "juanito",
        "contactInfo": [57, 123456, "juan@mail.com", "cra100"],
        "preferred": "email"
    }
    assert datos == expectativa
