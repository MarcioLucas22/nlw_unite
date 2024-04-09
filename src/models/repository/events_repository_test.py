import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='Novo registro em banco de dados')
def test_insert_events():
    event = {
        "uuid": "123456",
        "title": "meu-title",
        "slug": "meu-slug4",
        "maximum_attendees": 30,
    }

    events_repository = EventsRepository()
    reponse = events_repository.insert_event(event)
    print(reponse)

@pytest.mark.skip(reason='Não necessita')
def test_get_event_by_id():
    event_id = "meu_uuid-e-nois33"

    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)