import unittest
from Examples import Example

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Seting up the Test Environment")

    @classmethod
    def tearDownClass(cls):
        print("Resuming the Test Environment")

    def setUp(self):
        print("Starting the setup for test cycle")

    def tearDown(self):
        print("Finishing the test cycle")

    def test_add_pass(self):
        result = Example.add(self, 5, 6)
        # Passing
        self.assertEqual(result, 11)

    def test_add_fail(self):
        result = Example.add(self, 5, 6)
        # Fail
        self.assertEqual(result, 17)

    def test_sub_pass(self):
        result = Example.sub(self, 15, 6)
        # Passing
        self.assertEqual(result, 9)

    def test_sub_fail(self):
        result = Example.sub(self, 15, 6)
        # Fail
        self.assertEqual(result, 17)


if __name__ == '__main__':
    unittest.main()
