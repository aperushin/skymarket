import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_my_ad_list(client, user_token_and_object):
    token, user = user_token_and_object
    my_ad = AdFactory.create(author=user)
    other_ad = AdFactory.create()

    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
            "pk": my_ad.pk,
            "image": my_ad.image,
            "title": my_ad.title,
            "price": my_ad.price,
            "description": my_ad.description
        }]
    }

    response = client.get("/api/ads/me/", HTTP_AUTHORIZATION=f"Bearer {token}")

    assert my_ad.author != other_ad.author
    assert response.data == expected_response
    assert response.status_code == 200
