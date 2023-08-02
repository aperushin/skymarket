import pytest


@pytest.mark.django_db
def test_ad_list(client, ad):
    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
            "pk": ad.pk,
            "image": ad.image,
            "title": ad.title,
            "price": ad.price,
            "description": ad.description
        }]
    }

    response = client.get("/api/ads/")

    assert response.data == expected_response
    assert response.status_code == 200
