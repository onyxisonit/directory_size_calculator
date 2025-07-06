import unittest
from file_system import File, Directory
from example import build_example_filesystem
from main import handle_cd, handle_size

class TestFileSystem(unittest.TestCase):

    def setUp(self):
        self.root = build_example_filesystem()

    def test_docs_directory_size(self):
        docs = self.root.subdirectories[0]  # "docs"
        self.assertEqual(docs.name, "docs")
        expected_size = 120 + 122 + 91 + 192 + 333
        self.assertEqual(handle_size(docs), expected_size)

    def test_nested_directory_size(self):
        media = self.root.subdirectories[2]  # "media"
        expected = 5900 + 900 + 250 + 266
        self.assertEqual(handle_size(media), expected)

    def test_total_root_size(self):
        total_size = handle_size(self.root)
        expected = (
            120 + 122 + 91 + 192 + 333 +         # docs
            91 + 86 + 91 + 50 + 72 +             # desktop/screenshots + text
            5900 + 900 + 250 + 266               # media/music + images
        )
        self.assertEqual(total_size, expected)


    def test_handle_cd_valid_and_invalid(self):
        curr = self.root
        path = ["root"]

        curr, path = handle_cd("docs", curr, path)
        self.assertEqual(curr.name, "docs")

        curr, path = handle_cd("..", curr, path)
        self.assertEqual(curr.name, "root")

        curr, path = handle_cd("not_a_folder", curr, path)
        self.assertEqual(curr.name, "root")  # invalid directory, should not change

    def test_handle_cd_deep_nesting(self):
        curr = self.root
        path = ["root"]

        #test handling of single directory path
        curr, path = handle_cd("desktop", curr, path)
        curr, path = handle_cd("screenshots", curr, path)
        self.assertEqual(curr.name, "screenshots")

        curr, path = handle_cd("..", curr, path)
        self.assertEqual(curr.name, "desktop")

        curr, path = handle_cd("..", curr, path)
        self.assertEqual(curr.name, "root")

        # test handling of multiple directory path
        curr, path = handle_cd("desktop/screenshots", curr, path)
        self.assertEqual(curr.name, "screenshots")

        curr, path = handle_cd("../../media/images/../../docs", curr, path)
        self.assertEqual(curr.name, "docs")

    def test_empty_directory(self):
        new_dir = Directory("empty")
        new_dir.parent = None  # simulate root
        self.assertEqual(handle_size(new_dir), 0)

        # no parent, path shouldn't change
        curr, path = handle_cd("..", new_dir, ["empty"])
        self.assertEqual(curr.name, "empty")
        self.assertEqual(path, ["empty"])


if __name__ == '__main__':
    unittest.main()

