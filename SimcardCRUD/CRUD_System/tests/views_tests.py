import pytest

from django.urls import reverse

from django.contrib.auth import get_user_model


def test_main_view_login_requirement(client):
    response = client.get(reverse("main-page"))

    assert "/login/" in response.url

    assert response.status_code == 302


@pytest.mark.django_db
def test_authenticated_main_page(client):
    User = get_user_model() 

    auth_user = User.objects.create_user(
        username="Igor",
        password="test-password-1234"
    )

    client.force_login(auth_user)


    response = client.get(reverse("main-page"))

    assert response.status_code == 200