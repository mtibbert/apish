from unittest import TestCase
from run import app


class TestHomeRoutes(TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    # Test /

    def test_route_default_status_is_200(self):
        response = self.client.get(f'/')
        self.assertEqual(200, response.status_code)

    # Test /home

    def test_route_home_status_is_200(self):
        response = self.client.get(f'/home')
        self.assertEqual(200, response.status_code)
