from pytest_factoryboy import register

from tests.factories import AdFactory, UserFactory, CommentFactory

pytest_plugins = 'tests.fixtures'

register(AdFactory)
register(UserFactory)
register(CommentFactory)
