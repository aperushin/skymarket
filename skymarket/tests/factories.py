import factory
from datetime import datetime

from users.models import User, UserRoles
from ads.models import Ad, Comment


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    first_name = factory.Faker('name')
    last_name = factory.Faker('name')
    phone = factory.Faker('phone_number')
    role = UserRoles.USER
    image = None
    is_active = True


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    title = factory.Faker('word')
    price = 2
    description = 'ad description'
    author = factory.SubFactory(UserFactory)
    created_at = datetime.now()
    image = None


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    text = factory.Faker('text')
    author = factory.SubFactory(UserFactory)
    ad = factory.SubFactory(AdFactory)
    created_at = datetime.now()
