from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app.extensions import db


class Word(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    word: so.Mapped[str] = so.mapped_column(
        sa.String(128), index=True, unique=True)
    definition: so.Mapped[Optional[str]] = so.mapped_column(
        sa.String(128), index=True, unique=False)
    sa.UniqueConstraint(
        word, definition, name="uq_word_definition")
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))

    def as_dict(self):
        """
        Casts Word object to dict

        :return: dict
        """
        return {
            "id": self.id,
            "word": self.word,
            "definition": self.definition,
            "language_id": self.language_id
        }

    def __repr__(self):
        return (f'<{self.__class__.__name__} ' +
                f'id={self.id}, ' +
                f'word={self.word}, ' +
                f'definition={self.definition}, ' +
                f'language_id={self.language_id}>')

