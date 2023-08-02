import pytest


@pytest.mark.django_db
def test_create_ad(client, user_token_and_object):
    token, user = user_token_and_object

    data = {
        "image": "",
        "title": "Ad title",
        "price": 2,
        "description": "string"
    }

    expected_response = {
        "image": None,
        "title": "Ad title",
        "price": 2,
        "phone": user.phone,
        "description": "string",
        "author_first_name": user.first_name,
        "author_last_name": user.last_name,
        "author_id": user.id
    }

    response = client.post(
        "/api/ads/",
        data,
        format="json",
        HTTP_AUTHORIZATION=f"Bearer {token}",
    )

    response.data.pop("pk")

    assert response.data == expected_response
    assert response.status_code == 201


@pytest.mark.django_db
def test_create_ad_unauthorized(client):
    data = {
        "image": "",
        "title": "Ad title",
        "price": 2,
        "description": "string"
    }

    response = client.post(
        "/api/ads/",
        data,
        format="json"
    )

    assert response.data == {"detail": "Authentication credentials were not provided."}
    assert response.status_code == 401
