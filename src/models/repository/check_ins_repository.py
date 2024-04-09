from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError

db_connection_handler.connect_to_db()

class CheckInRepository:
    def insert_check_in(self, attendeeId: str) -> str:
        with db_connection_handler as database:
            try:
                check_in = (
                    CheckIns(
                        attendeeId = attendeeId
                    )
                )
                database.session.add(check_in)
                database.session.commit()

                return attendeeId
            except IntegrityError:
                raise Exception('Check-in já cadastrado.')
            except Exception as exception:
                db_connection_handler.session.rollback()
                raise exception