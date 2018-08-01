import unittest
import os

from thrifty.model.file_loader import load_model_from_file
from thrifty.model import \
    ThriftyEnum, \
    ThriftyStruct


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

        # ====================================================
        # Enum reading
        # ====================================================
        first_item: ThriftyEnum = model.file_items[0]
        self.assertTrue(isinstance(first_item, ThriftyEnum))
        self.assertEqual("ProcessState", first_item.name)
        self.assertEqual(3, len(first_item.values))
        self.assertEqual("Just a simple enum.", first_item.comment)

        # ====================================================
        # Struct reading
        # ====================================================
        second_item: ThriftyStruct = model.file_items[1]
        self.assertTrue(isinstance(second_item, ThriftyStruct))
        self.assertEqual("ProcessResult", second_item.name)
        self.assertEqual("Just a very\nvery\nsimple struct.", second_item.comment)
        self.assertEqual(2, len(second_item.attributes))
        self.assertEqual("state", second_item.attributes[0].name)
        self.assertEqual("ProcessState", second_item.attributes[0].attrtype.name)
        self.assertEqual("exitCode", second_item.attributes[1].name)
        self.assertEqual("i32", second_item.attributes[1].attrtype.name)


if __name__ == '__main__':
    unittest.main()
