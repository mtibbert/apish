from app import url_prefix
from app.database.models.language import Language
from run import app
from tests.routes.test_routes_base import TestRoutesBase


class TestLanguageBP(TestRoutesBase):

    def setUp(self):
        self.data_provider = self.load_json(self.SEED_FQN)
        self.url_prefix = url_prefix
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    # Test /language DELETE

    def test_do_delete_invalid_id_status_msg_contains_id(self):
        language_id = 0
        url = f'{self.url_prefix}/language/{language_id}'
        # Update db item
        delete_response = self.client.delete(url)
        # Check response
        expected = f'Unprocessable Content: Invalid Language id ({language_id}).'
        actual = delete_response.json["message"]
        # check result from server with expected data
        self.assertEqual(422, delete_response.status_code)
        self.assertEqual(expected, actual)

    def test_do_delete_json_is_updated(self):
        exp_language = self.random_str()
        exp_description = self.random_str(False, 15)
        item_data = {"language": exp_language,
                     "description": exp_description}
        url = f'{self.url_prefix}/language'
        # Create item to modify
        post_response = self.client.post(url, json=item_data)
        # Grab new entity id
        item_id = post_response.headers["location"]
        url = f'{url}/{item_id}'  # Update for Delete request
        # Delete db item
        delete_response = self.client.delete(url)
        item_data["id"] = int(item_id)  # Add ID and compare to updated entity
        self.assertEqual(item_data, delete_response.json)
        self.remove_test_data(Language, Language.language)

    def test_do_delete_status_is_200(self):
        # noinspection DuplicatedCode
        exp_language = self.random_str()
        exp_description = self.random_str(False, 15)
        item_data = {"language": exp_language,
                     "description": exp_description}
        url = f'{self.url_prefix}/language'
        # Create item to delete
        post_response = self.client.post(url, json=item_data)
        url = f'{url}/{post_response.headers["location"]}'
        # Delete db item
        delete_response = self.client.delete(url)
        # check result from server with expected data
        self.assertEqual(200, delete_response.status_code)
        self.remove_test_data(Language, Language.language)

    def test_do_delete_not_found_id_status_is_404(self):
        language_id = 9223372036854775807  # SQLite max int
        url = f'{self.url_prefix}/language/{language_id}'
        # Update db item
        delete_response = self.client.delete(url)
        # check result from server with expected data
        expected = f'Not Found: {language_id}'
        actual = delete_response.json["message"]
        # check result from server with expected data
        self.assertEqual(404, delete_response.status_code)
        self.assertEqual(expected, actual)

    def test_do_delete_invalid_id_status_is_422(self):
        language_id = 0
        url = f'{self.url_prefix}/language/{language_id}'
        # Delete db item
        delete_response = self.client.delete(url)
        # check result from server with expected data
        self.assertEqual(422, delete_response.status_code)
        self.assertEqual("422 UNPROCESSABLE ENTITY",
                         delete_response.status.upper())

    # Test /language GET

    def test_language_route_is_200(self):
        response = self.client.get(f'{url_prefix}/language')
        self.assertEqual(200, response.status_code)

    # Test /language/id GET

    def test_language_id_route_valid_is_200(self):
        idx = self.data_provider[0]["id"]
        response = self.client.get(f'{url_prefix}/language/{idx}')
        self.assertEqual(200, response.status_code)

    def test_language_id_route_invalid_is_404(self):
        idx = "0"
        response = self.client.get(f'{url_prefix}/language/{idx}')
        self.assertEqual(404, response.status_code)

    # Test /language POST GET

    def test_post_header_location_matches(self):
        exp_language = self.random_str()
        exp_description = self.random_str(False, 15)
        data = {"language": exp_language,
                "description": exp_description}
        post_response = self.client.post(
            f'{self.url_prefix}/language',
            json=data
        )
        # check response from server with expected data
        lang_id = int(post_response.headers["location"])
        post_response = self.client.get(f'{url_prefix}/language/{lang_id}')
        expected = {"id": lang_id,
                    "language": exp_language,
                    "description": exp_description}
        self.assertDictEqual(post_response.json, expected)
        self.remove_test_data(Language, Language.language)

    def test_do_post_status_is_201(self):
        exp_language = self.random_str()
        exp_description = self.random_str(False, 15)
        data = {"language": exp_language,
                "description": exp_description}
        post_response = self.client.post(
            f'{self.url_prefix}/language',
            json=data
        )
        # check result from server with expected data
        self.assertEqual(post_response.status_code, 201)
        self.remove_test_data(Language, Language.language)

    # Test /language/id PUT

    def test_do_put_invalid_id_status_msg_contains_id(self):
        language_id = 0
        url = f'{self.url_prefix}/language/{language_id}'
        exp_description = self.random_str()
        item_data = {"description": exp_description}
        # Update db item
        put_response = self.client.put(url, json=item_data)
        # Check response
        expected = f'Unprocessable Content: Invalid Language id ({language_id}).'
        actual = put_response.json["message"]
        # check result from server with expected data
        self.assertEqual(422, put_response.status_code)
        self.assertEqual(expected, actual)

    def test_do_put_json_is_updated(self):
        exp_language = self.random_str()
        exp_description = self.random_str(False, 15)
        item_data = {"language": exp_language,
                     "description": exp_description}
        url = f'{self.url_prefix}/language'
        # Create item to modify
        post_response = self.client.post(url, json=item_data)
        # Modify description
        item_data["description"] = item_data["description"][::-1]
        # Grab new entity id
        item_id = post_response.headers["location"]
        url = f'{url}/{item_id}'  # Update for PUT request
        # Update db item
        put_response = self.client.put(url, json=item_data)
        item_data["id"] = int(item_id)  # Add ID and compare to updated entity
        self.assertEqual(item_data, put_response.json)
        self.remove_test_data(Language, Language.language)

    def test_do_put_status_is_200(self):
        # noinspection DuplicatedCode
        exp_language = self.random_str()
        exp_description = self.random_str(False, 15)
        item_data = {"language": exp_language,
                     "description": exp_description}
        url = f'{self.url_prefix}/language'
        # Create item to modify
        post_response = self.client.post(url, json=item_data)
        url = f'{url}/{post_response.headers["location"]}'
        item_data["description"] = item_data["description"][::-1]
        # Update db item
        put_response = self.client.put(url, json=item_data)
        # check result from server with expected data
        self.assertEqual(200, put_response.status_code)
        self.remove_test_data(Language, Language.language)

    def test_do_put_not_found_id_status_is_404(self):
        language_id = 9223372036854775807  # SQLite max int
        url = f'{self.url_prefix}/language/{language_id}'
        item_data = {"description": "foo"}
        # Update db item
        put_response = self.client.put(url, json=item_data)
        # check result from server with expected data
        expected = f'Not Found: {language_id}'
        actual = put_response.json["message"]
        # check result from server with expected data
        self.assertEqual(404, put_response.status_code)
        self.assertEqual(expected, actual)

    def test_do_put_invalid_id_status_is_422(self):
        language_id = 0
        url = f'{self.url_prefix}/language/{language_id}'
        exp_description = self.random_str()
        item_data = {"description": exp_description}
        # Update db item
        put_response = self.client.put(url, json=item_data
                                       )
        # check result from server with expected data
        self.assertEqual(422, put_response.status_code)
        self.assertEqual("422 UNPROCESSABLE ENTITY",
                         put_response.status.upper())
