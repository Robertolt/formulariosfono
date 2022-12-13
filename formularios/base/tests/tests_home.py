import pytest
from django.test import Client
from django.urls import reverse

from formularios.base.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_home_titulo(resp):
    assert_contains(resp, '<title>Formulários</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("home")}">Formulários')
