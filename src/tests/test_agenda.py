import pytest

from Agenda import Agenda

def test_agenda():
    agenda_x = Agenda()
    agenda_x.add_contact(1)
    a = agenda_x.find_contact(1)
    assert 1 == a

def test_agenda_find():
    agenda = Agenda()
    contact = {
        "name": "selena",
        "nickname": "selena32",
        "group": "trabajo"
    }
    agenda.add_contact(contact)
    x = agenda.find_contact('1')
    assert x == contact
    

def test_equals_2():
    assert 3 == 3
    