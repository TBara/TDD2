import unittest
from check_pwd import check_pwd

# Must be between 8 and 20 characters (inclusive)
# Must contain at least one lowercase letter
# Must contain at least one uppercase letter
# Must contain at least one digit
# Must contain at least one symbol from: ~`!@#$%^&*()_+-=


class TestCase(unittest.TestCase):

    def test1(self):
        pwd = ''
        expected = False
        self.assertFalse(check_pwd(pwd), expected)


if __name__ == '__main__':
    unittest.main()
