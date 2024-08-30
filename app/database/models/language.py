from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app.extensions import db


class Language(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    language: so.Mapped[str] = so.mapped_column(
        sa.String(128), index=True, unique=True)
    description: so.Mapped[Optional[str]] = so.mapped_column(
        sa.String(128), index=True, unique=False)
    sa.UniqueConstraint(
        language, description, name="uq_language_description")

    def as_dict(self):
        """
        Casts language object to dict

        :return: dict
        """
        return {
            "id": self.id,
            "language": self.language,
            "description": self.description
        }

    def __repr__(self):
        return (f'<Language ' +
                f'id={self.id}, ' +
                f'language={self.language}, ' +
                f'description={self.description}>')

