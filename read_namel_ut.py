"""
    This defines the unit tests for read_namel.py.
"""
__author__ = "Nicholas Geyer"
__credits__ = ["Nicholas Geyer"]
__license__ = "GNU GPLv3.0"
__version__ = "1.0.0"
__maintainer__ = "Nicholas Geyer"
__email__ = "nicholas.geyer@colostate.edu"
__status__ = "Production"

import unittest

from read_namel import *

class MyTestCase(unittest.TestCase):
    def test_valid_namelist(self):
        self.assertEqual(type(read_namel('./unit_testing_input/namel_sibdrv')),type({}))

    def test_invalid_namelist(self):
        with self.assertRaises(ValueError) as context:
            read_namel('./unit_testing_input/namel_sibdrv_bogus')
        self.assertTrue('Check your namelist. A pbp value does not have a valid lon-lat pair',context.exception)

if __name__ == '__main__':
    unittest.main()
