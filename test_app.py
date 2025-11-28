import unidiff
from app import say_hello


class TestApp(unidiff.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello("AWS"), "Hello, AWS!")
        
if __name__ == "__main__":
    unidiff.main()