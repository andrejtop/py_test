from ya_api_folder import creating_new_folder_yandex_disk, delete_folder_yandex_disk
import unittest


class TestCreateFolderUnitTest(unittest.TestCase):

    def test_creating_new_folder_yandex_disk(self):
        self.assertEqual(creating_new_folder_yandex_disk("test"), 201)

    def test_delete_folder_yandex_disk(self):
        self.assertEqual(delete_folder_yandex_disk('test'), 204)