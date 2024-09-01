from unittest import TestCase
from app import url_prefix
from run import app
import json
import os

import app.routes.language.language_bp as bp

seed_file = "language.seed.json"
seed_dir = "database/seeds"
seed_fqn = os.path.join(app.root_path, seed_dir, seed_file)


def load_json(file_name):
    # Open JSON seed file
    f = open(file_name)
    data = json.load(f)
    f.close()
    return data


class TestLanguageBP(TestCase):

    def setUp(self):

        self.data_provider = load_json(seed_fqn)
        self.url_prefix = url_prefix
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    # Test do_get_languages()

    def test_do_get_languages_content_type_is_json(self):
        response = bp.do_get_languages()
        self.assertEqual("application/json", response.content_type)

    def test_do_get_languages_contains_seeds(self):
        response = bp.do_get_languages()
        actual_json = response.json
        for i in range(0, len(self.data_provider)):
            with self.subTest(language=self.data_provider[i]["language"]):
                self.assertIn(self.data_provider[i], actual_json)

    # Test do_get_language_by_id(id)

    def test_do_get_language_by_id(self):
        for i in range(0, len(self.data_provider)):
            idx = self.data_provider[i]["id"]
            actual = bp.do_get_language_by_id(idx)
            with self.subTest(id=idx):
                self.assertEqual(self.data_provider[i], actual.json)
