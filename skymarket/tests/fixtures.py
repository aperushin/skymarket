import pytest

from users.models import UserRoles


@pytest.fixture
@pytest.mark.django_db
def user_token_and_id(client, django_user_model):
    email = 'test_user@test.com'
    password = '123qWe123123'

    user = django_user_model.objects.create_user(
        email=email,
        password=password,
        role=UserRoles.USER,
        first_name='user',
        last_name='test',
        phone='+35797111111',
    )

    response = client.post(
        '/api/token/',
        {'email': email, 'password': password},
        format='json',
    )

    return response.data['access'], user.id


@pytest.fixture
@pytest.mark.django_db
def admin_token_and_id(client, django_user_model):
    email = 'test_admin@test.com'
    password = '123qWe123123'

    user = django_user_model.objects.create_user(
        email=email,
        password=password,
        role=UserRoles.ADMIN,
        first_name='admin',
        last_name='test',
        phone='+35797111111',
    )

    response = client.post(
        '/api/token/',
        {'email': email, 'password': password},
        format='json',
    )

    return response.data['access'], user.id
