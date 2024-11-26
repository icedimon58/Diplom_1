from data import BUN_NAME, SOUSE_NAME, BUN_COST
from praktikum.burger import Burger


class TestBurger:
    def test_set_bun_positive(self, mock_bun):
        burger = Burger()
        burger.bun = mock_bun
        burger.set_buns(burger.bun)
        assert burger.bun.get_name() == BUN_NAME and burger.bun.get_price() == BUN_COST

    def test_append_ingredients_positive(self, mock_ingredient):
        burger = Burger()
        burger.bun = mock_ingredient
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 2

    def test_remove_ingredients_positive(self, mock_ingredient):
        burger = Burger()
        burger.bun = mock_ingredient
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        count = len(burger.ingredients)
        burger.remove_ingredient(0)
        assert count - 1 == 2

    def test_get_price_positive(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.get_price()
        assert burger.get_price() == 900

    def test_get_receipt_positive(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_data = burger.get_receipt()
        assert SOUSE_NAME in expected_data and BUN_NAME in expected_data
