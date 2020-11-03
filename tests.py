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

    def test2(self):
        pwd = 'pA$swr4'
        expected = False
        self.assertFalse(check_pwd(pwd), expected)

    def test3(self):
        pwd = 'Th1$istoolongofapass_'
        expected = False
        self.assertFalse(check_pwd(pwd), expected)

    def test4(self):
        pwd = 'pA$$w0rd'
        expected = True
        self.assertTrue(check_pwd(pwd), expected)


if __name__ == '__main__':
    unittest.main()
