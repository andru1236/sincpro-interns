import pytest

from Agenda import Agenda

@pytest.fixture
def clase():
    clase = Agenda()
    contact = {
        "id": 1,
        "name": "selena",
        "nickname": "selena32",
        "group": "trabajo"
    }
    clase.add_contact(contact)
    return clase

def test_agenda_find(clase):
    x = clase.find_contact('1')
    assert x == clase.contactos[0]

def test_agenda_remove(clase):
    b = clase.delete_contact('1')
    assert b == clase.contactos 

"""
def test_agenda_find():
    agenda_x = Agenda()
    contact = {
        "name": "selena",
        "nickname": "selena32",
        "group": "trabajo"
    }
    agenda_x.add_contact(contact)
    a = agenda_x.find_contact(1)
    assert a == contact
"""
    