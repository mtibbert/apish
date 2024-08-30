import os
from unittest import TestCase
from app import url_prefix
import json

from run import app

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
        # print(f'-{seed_fn}')
        # print(f'+{seed_fqn}')
        self.data_provider = load_json(seed_fqn)
        self.url_prefix = url_prefix
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    # Test /language

    def test_language_route_is_200(self):
        response = self.client.get(f'{url_prefix}/language')
        self.assertEqual(200, response.status_code)

    # Test /language/id

    def test_language_id_route_valid_is_200(self):
        idx = self.data_provider[0]["id"]
        response = self.client.get(f'{url_prefix}/language/{idx}')
        self.assertEqual(200, response.status_code)

    def test_language_id_route_invalid_is_404(self):
        idx = "0"
        response = self.client.get(f'{url_prefix}/language/{idx}')
        self.assertEqual(404, response.status_code)
