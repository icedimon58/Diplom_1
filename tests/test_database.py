from praktikum.database import Database


class TestDatabase:

    def test_get_name_of_ingridients_positive(self):
        database = Database()
        expected_ingridients = len(database.available_ingredients())
        assert expected_ingridients == 6

    def test_get_name_of_bun_positive(self):
        database = Database()
        expected_ingridients = len(database.available_buns())
        assert expected_ingridients == 3
