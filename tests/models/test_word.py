from unittest import TestCase
from app.database.models.word import Word


class TestWord(TestCase):
    _id = None
    _word = None
    _definition = None
    _language_id = None
    _out = None

    def setUp(self):
        self._id = 999
        self._word = "foo"
        self._definition = "bar"
        self._language_id = 2
        self._out = Word(id=self._id, word=self._word,
                         definition=self._definition,
                         language_id=self._language_id)

    def test_attr_definition_is_str(self):
        self.assertIsInstance(self._definition, str)

    def test_attr_id_is_int(self):
        self.assertIsInstance(self._id, int)

    def test_attr_word_is_str(self):
        self.assertIsInstance(self._word, str)

    def test_as_dict(self):
        expected = {
            "id": self._id,
            "word": f'{self._word}',
            "definition": f'{self._definition}',
            "language_id": self._language_id}
        self.assertDictEqual(expected, self._out.as_dict())

    def test__repr__(self):
        expected = (f'<Word id={self._id}, ' +
                    f'word={self._word}, ' +
                    f'definition={self._definition}, ' +
                    f'language_id={self._language_id}>')
        self.assertEqual(expected, self._out.__repr__())
