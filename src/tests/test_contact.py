import pytest
from Contact import Contact


def test_contacto():
    contacto = Contact("Juan Perez", "juanito", 57, 123456, "juan@mail.com", "cra100", "email")
    expectativa = {
        "name": "Juan Perez",
        "id": 1,
        "nickname": "juanito",
        "contactInfo": [57, 123456, "juan@mail.com", "cra100"],
        "preferred": "email"
    }
    assert contacto.conver_data() == expectativa
