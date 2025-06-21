from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from yhkee0404.example_database import Base


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    content: Mapped[str] = mapped_column(String, unique=False)
