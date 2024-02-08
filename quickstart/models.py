from django.db import models


class MyAppModel(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=255, default="")

    @property
    def is_empty(self):
        return not bool(self.content)


import pytest


@pytest.fixture
def test_model():
    return MyAppModel


@pytest.mark.django_db
def test_app_is_empty(test_model):
    model = test_model(title="test")
    assert model.is_empty


@pytest.mark.django_db
def test_app_isnot_empty(test_model):
    model = test_model(title="test", content="test")
    assert not model.is_empty
