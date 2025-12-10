import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    
    def test_set_buns_should_set_bun_in_burger(self, burger, mock_bun):
        """Проверяем, что метод set_buns устанавливает булочку"""
        burger.set_buns(mock_bun)
        # Проверяем, что цена бургера корректно рассчитывается с установленной булочкой
        assert burger.get_price() == 200.0  # 100 * 2

    def test_add_ingredient_should_add_to_ingredients_list(self, burger, mock_bun, mock_ingredient_sauce):
        """Проверяем, что метод add_ingredient добавляет ингредиент"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        # Проверяем через расчет цены
        assert burger.get_price() == 250.0  # 100*2 + 50

    def test_remove_ingredient_should_remove_from_list(self, burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        """Проверяем, что метод remove_ingredient удаляет ингредиент"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        
        initial_price = burger.get_price()  # 100*2 + 50 + 80 = 330
        burger.remove_ingredient(0)
        price_after_removal = burger.get_price()  # 100*2 + 80 = 280
        
        assert price_after_removal == 280.0
        assert initial_price != price_after_removal

    def test_move_ingredient_should_change_order(self, burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        """Проверяем, что метод move_ingredient перемещает ингредиент"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)   # Индекс 0
        burger.add_ingredient(mock_ingredient_filling) # Индекс 1
        
        # Получаем чек до перемещения
        receipt_before = burger.get_receipt()
        
        # Перемещаем ингредиент
        burger.move_ingredient(0, 1)
        
        # Получаем чек после перемещения
        receipt_after = burger.get_receipt()
        
        # Чеки должны отличаться (порядок ингредиентов разный)
        assert receipt_before != receipt_after

    def test_get_price_calculates_correct_total(self, burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        """Проверяем расчет общей цены"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        
        # Ожидаемая цена: булочка (100) * 2 + соус (50) + начинка (80) = 330
        expected_price = 100.0 * 2 + 50.0 + 80.0
        assert burger.get_price() == expected_price

    def test_get_receipt_contains_all_required_info(self, burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        """Проверяем формирование чека"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        
        receipt = burger.get_receipt()
        
        # Проверяем обязательные элементы в чеке
        assert "test bun" in receipt
        assert "hot sauce" in receipt
        assert "cutlet" in receipt
        assert "Price:" in receipt
        assert "330.0" in receipt  # Общая цена

    def test_get_receipt_starts_and_ends_with_bun(self, burger, mock_bun):
        """Проверяем, что чек начинается и заканчивается булочкой"""
        burger.set_buns(mock_bun)
        receipt_lines = burger.get_receipt().split('\n')
        
        assert "(==== test bun ====)" == receipt_lines[0]
        assert "(==== test bun ====)" == receipt_lines[1]  # Вторая строка - последняя булочка
        assert receipt_lines[2] == ""  # Пустая строка
        assert "Price: 200.0" in receipt_lines[3]  # Строка с ценой

    def test_remove_ingredient_with_invalid_index_raises_error(self, burger, mock_bun, mock_ingredient_sauce):
        """Проверяем исключение при удалении с невалидным индексом"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)  # Несуществующий индекс

    def test_move_ingredient_with_invalid_index_raises_error(self, burger, mock_bun, mock_ingredient_sauce):
        """Проверяем исключение при перемещении с невалидным индексом"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        
        with pytest.raises(IndexError):
            burger.move_ingredient(5, 0)  # Несуществующий исходный индекс
            