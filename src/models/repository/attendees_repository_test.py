from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='Novo registro em banco de dados')
def test_insert_attendee():
    attendees_info = {
        'id': 'meu_uuid-e-nois-attendee',
        'name': 'attendee name',
        'email': 'email@email.com',
        'event_id': '123456'
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)

@pytest.mark.skip(reason='...')
def test_get_attendee_badge_by_id():
    attendee_id = 'meu_uuid-e-nois-attendee'
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendee_id)

    print(attendee)