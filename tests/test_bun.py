import pytest

from praktikum.bun import Bun
from data import TEST_BUN


class TestBun:

    @pytest.mark.parametrize('name,price', [TEST_BUN])
    def test_get_name_of_bun_positive(self, name, price):
        ingridient = Bun(name, price)
        assert ingridient.get_name() == name

    @pytest.mark.parametrize('name,price', [TEST_BUN])
    def test_get_price_of_bun_positive(self, name, price):
        ingridient = Bun(name, price)
        assert ingridient.get_price() == price
