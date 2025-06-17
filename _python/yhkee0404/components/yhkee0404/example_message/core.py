import json

from yhkee0404 import example_kafka as kafka
from yhkee0404.example_database import Session
from yhkee0404.example_database.message import crud
from yhkee0404.example_dictionaries import pick
from yhkee0404.example_schema import Message


def notify(message: Message) -> None:
    data = pick(vars(message), {"id", "content"})

    key = str(data["id"])
    value = json.dumps(data)

    kafka.producer.produce("message", key, value)


def create(content: str) -> int:
    with Session.begin() as session:
        data = crud.create(session, content)

        notify(data)

        return data.id


def read(message_id: int):
    with Session.begin() as session:
        return vars(crud.read(session, message_id))


def update(message_id: int, content: str) -> None:
    with Session.begin() as session:
        existing = crud.read(session, message_id)

        if not existing:
            raise ValueError()

        return crud.update(session, existing, content)


def delete(message_id: int) -> None:
    with Session.begin() as session:
        return crud.delete(session, message_id)
