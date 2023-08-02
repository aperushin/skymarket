import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_partial_update_ad(client, user_token_and_object):
    token, user = user_token_and_object
    ad = AdFactory.create(author=user)

    data = {"title": "altered title"}

    expected_response = {
        "pk": ad.pk,
        "image": ad.image,
        "title": "altered title",
        "price": ad.price,
        "phone": user.phone,
        "description": ad.description,
        "author_first_name": user.first_name,
        "author_last_name": user.last_name,
        "author_id": user.id
    }

    response = client.patch(
        f"/api/ads/{ad.pk}/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION=f"Bearer {token}",
    )

    assert response.data == expected_response
    assert response.status_code == 200


@pytest.mark.django_db
def test_partial_update_ad_unauthorized(client, ad):
    data = {"title": "altered title"}

    response = client.patch(
        f"/api/ads/{ad.pk}/",
        data,
        content_type='application/json',
    )

    assert response.data == {"detail": "Authentication credentials were not provided."}
    assert response.status_code == 401


@pytest.mark.django_db
def test_partial_update_ad_not_owner(client, ad, user_token_and_object):
    token, _ = user_token_and_object

    data = {"title": "altered title"}

    response = client.patch(
        f"/api/ads/{ad.pk}/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION=f"Bearer {token}",
    )

    assert response.data == {"detail": "You do not have permission to perform this action."}
    assert response.status_code == 403


@pytest.mark.django_db
def test_partial_update_ad_admin(client, ad, admin_token_and_object):
    token, admin_user = admin_token_and_object

    data = {"title": "altered title"}

    expected_response = {
        "pk": ad.pk,
        "image": ad.image,
        "title": "altered title",
        "price": ad.price,
        "phone": ad.author.phone,
        "description": ad.description,
        "author_first_name": ad.author.first_name,
        "author_last_name": ad.author.last_name,
        "author_id": ad.author.id
    }

    response = client.patch(
        f"/api/ads/{ad.pk}/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION=f"Bearer {token}",
    )

    assert admin_user != ad.author
    assert response.data == expected_response
    assert response.status_code == 200
