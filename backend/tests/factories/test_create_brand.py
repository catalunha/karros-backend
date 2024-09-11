import pytest
from model_bakery import baker

from backend.factories.models import Brand


@pytest.mark.django_db
class TestCreateBrand:
    def test_create_brand_with_baker(self):
        brand = baker.make(Brand)
        assert brand
        assert isinstance(brand, Brand)
