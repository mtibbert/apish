from unittest import TestCase
from app import url_prefix
from run import app
import app.routes.home.home_bp as bp


class TestHomeBP(TestCase):
    def setUp(self):
        self.url_prefix = url_prefix
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    # Test home_bp

    def test_do_get_home_content_as_text(self):
        expected = "<p>Apish home</p>"
        actual = bp.do_get_home()
        self.assertEqual(expected, actual.get_data(as_text=True))

    def test_do_get_home_response_content_type_is_html(self):
        expected_content_type = "text/html; charset=utf-8"
        actual = bp.do_get_home()
        self.assertEqual(expected_content_type,
                         actual.content_type)
