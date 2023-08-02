import pytest


@pytest.mark.django_db
def test_retrieve_ad(client, ad, user_token_and_object):
    token, _ = user_token_and_object

    expected_response = {
        "pk": ad.pk,
        "image": ad.image,
        "title": ad.title,
        "price": ad.price,
        "phone": ad.author.phone,
        "description": ad.description,
        "author_first_name": ad.author.first_name,
        "author_last_name": ad.author.last_name,
        "author_id": ad.author_id
    }

    response = client.get(f'/api/ads/{ad.pk}/', HTTP_AUTHORIZATION=f"Bearer {token}")

    assert response.data == expected_response
    assert response.status_code == 200


@pytest.mark.django_db
def test_retrieve_ad_unauthorized(client, ad):
    response = client.get(f"/api/ads/{ad.pk}/")

    assert response.data == {"detail": "Authentication credentials were not provided."}
    assert response.status_code == 401
