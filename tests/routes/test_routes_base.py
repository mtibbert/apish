from unittest import TestCase
from app import db
import json
import os

from app.database.models.language import Language
from run import app


class TestRoutesBase(TestCase):

    # MODEL = None
    SEED_FILE = f"{Language.__name__.lower()}.seed.json"
    SEED_DIR = "database/seeds"
    SEED_FQN = os.path.join(app.root_path, SEED_DIR, SEED_FILE)
    TEST_ENTITY_PREFIX = "~~"

    # Helpers

    @staticmethod
    def load_json(file_name) -> dict:
        """
        Load test data file

        :param file_name:
        :return: dict
        """
        # Open JSON seed file
        f = open(file_name)
        data = json.load(f)
        f.close()
        return data

    @staticmethod
    def remove_test_data(model, col) -> None:
        """
        Delete all database rows where the

        :param col: Column to search for entities starting with TEST_ENTITY_PREFIX
        :return: None
        """
        items = (model.query.filter(
            col.startswith(TestRoutesBase.TEST_ENTITY_PREFIX)))
        for item in items:
            db.session.delete(item)
        db.session.commit()

    @staticmethod
    def random_str(prefixed: bool = True, size: int = 7) -> str:
        import string
        import random
        # using random.choices() generating random strings
        rand_str = ''.join(
            random.choices(
                string.ascii_letters,
                k=size))  # initializing size of string
        if prefixed:
            rand_str = f'{TestRoutesBase.TEST_ENTITY_PREFIX}{rand_str}'
        return rand_str
