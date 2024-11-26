import pytest

from praktikum.ingredient import Ingredient
from data import TEST_INGRIDIENT_1, TEST_INGRIDIENT_2


class TestIngridient:

    @pytest.mark.parametrize('type_ingrid,name,price', [TEST_INGRIDIENT_1, TEST_INGRIDIENT_2])
    def test_get_name_of_ingridient_positive(self, type_ingrid, name, price):
        ingridient = Ingredient(type_ingrid, name, price)
        assert ingridient.get_name() == name

    @pytest.mark.parametrize('type_ingrid,name,price', [TEST_INGRIDIENT_1, TEST_INGRIDIENT_2])
    def test_get_price_of_ingridient_positive(self, type_ingrid, name, price):
        ingridient = Ingredient(type_ingrid, name, price)
        assert ingridient.get_price() == price

    @pytest.mark.parametrize('type_ingrid,name,price', [TEST_INGRIDIENT_1, TEST_INGRIDIENT_2])
    def test_type_of_ingridient_positive(self, type_ingrid, name, price):
        ingridient = Ingredient(type_ingrid, name, price)
        assert ingridient.get_type() == type_ingrid
