from aplic import get_doc_owner_name, delete_doc, add_new_doc
import unittest


class TestControlPanelUnitTest(unittest.TestCase):

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name("11-2"), "Геннадий Покемонов")

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('4545', 'passport', 'Ivan', 3), 3)

    def test_delete_doc(self):
        self.assertTrue(delete_doc('2207 876234'))