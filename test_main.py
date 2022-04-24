import unittest
import main


class TestMain(unittest.TestCase):
    def test_user(self):
        user = main.User()
        name = user.login_user
        self.assertEqual(name, 'hussein')
        password = user.login_password
        self.assertEqual(password, '5868')

#
# if __name__ == '__main__':
#     unittest.main()
