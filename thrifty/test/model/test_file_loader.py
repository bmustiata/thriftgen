import unittest
import os

from thrifty.model.file_loader import load_model_from_file
from thrifty.model import ThriftyEnum


class TestFileLoader(unittest.TestCase):
    """
    Test creating models from thrift files.
    """
    def test_file_loading(self):
        """
        Test the basic echo thrift file loading.
        """
        file_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data/echo.thrift')

        model = load_model_from_file(file_name)
        self.assertEqual(4, len(model.file_items),
                         "There should be an exception, a struct, an enum and a service")

        first_item: ThriftyEnum = model.file_items[0]
        self.assertTrue(isinstance(first_item, ThriftyEnum))
        self.assertEqual("ProcessState", first_item.name)


if __name__ == '__main__':
    unittest.main()
