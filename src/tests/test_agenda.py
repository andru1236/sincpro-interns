import pytest

from Agenda import Agenda

def test_agenda():
    agenda_x = Agenda()
    agenda_x.add_contact(1)
    a = agenda_x.find_contact(1)
    assert 1 == a


def test_equals_2():
    assert 3 == 3
    