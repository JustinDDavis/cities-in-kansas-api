from unittest import TestCase
from start import app

class TestFlaskApp(TestCase):
    def setUp(self) -> None:
        print("Setup environment for tests")
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self) -> None:
        print("Tear down testing")

    def test_homepage_is_reachable(self):
        response = self.app.get('/')
        assert "200 OK" == response.status
