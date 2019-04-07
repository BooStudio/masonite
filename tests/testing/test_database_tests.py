
from masonite.testing import DatabaseTestCase

from config.database import Model


class User(Model):
    pass


class TestDatabase(DatabaseTestCase):

    def setUp(self):
        super().setUp()
        self.make(User, self.users_factory, 20)

    def users_factory(self, faker):
        return {
            'name': faker.name(),
            'email': faker.email(),
            'password': '$2b$12$WMgb5Re1NqUr.uSRfQmPQeeGWudk/8/aNbVMpD1dR.Et83vfL8WAu',  # == 'secret'
        }

    def test_has_records(self):
        self.assertGreater(User.all().count(), 0)
