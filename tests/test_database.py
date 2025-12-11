import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import TestDataBase


class TestDatabase:
    
    def test_available_buns_returns_list_with_correct_buns(self, database):
        """Проверяем, что метод available_buns возвращает корректные данные"""
        buns = database.available_buns()
        
        # Проверяем количество и структуру данных
        assert len(buns) == 3
        
        # Проверяем каждую булочку через её методы
        for i, expected_bun in enumerate(TestDataBase.database_buns):
            bun = buns[i]
            assert bun.get_name() == expected_bun[1]
            assert bun.get_price() == expected_bun[2]

    def test_available_ingredients_returns_list_with_correct_ingredients(self, database):
        """Проверяем, что метод available_ingredients возвращает корректные данные"""
        ingredients = database.available_ingredients()
        
        # Проверяем количество
        assert len(ingredients) == 6
        
        # Проверяем структуру и данные через методы ингредиентов
        for i, expected_ingredient in enumerate(TestDataBase.database_ingredients):
            ingredient = ingredients[i]
            assert ingredient.get_type() == expected_ingredient[1]
            assert ingredient.get_name() == expected_ingredient[2]
            assert ingredient.get_price() == expected_ingredient[3]

    def test_available_ingredients_has_correct_types_distribution(self, database):
        """Проверяем распределение типов ингредиентов"""
        ingredients = database.available_ingredients()
        
        sauces = [ingredient for ingredient in ingredients 
                 if ingredient.get_type() == INGREDIENT_TYPE_SAUCE]
        fillings = [ingredient for ingredient in ingredients 
                   if ingredient.get_type() == INGREDIENT_TYPE_FILLING]
        
        assert len(sauces) == 3
        assert len(fillings) == 3

    def test_available_methods_return_valid_objects(self, database):
        """Проверяем, что методы возвращают валидные объекты"""
        buns = database.available_buns()
        ingredients = database.available_ingredients()
        
        # Проверяем, что объекты имеют ожидаемые методы
        for bun in buns:
            assert hasattr(bun, 'get_name')
            assert hasattr(bun, 'get_price')
            assert callable(bun.get_name)
            assert callable(bun.get_price)
            
        for ingredient in ingredients:
            assert hasattr(ingredient, 'get_type')
            assert hasattr(ingredient, 'get_name')
            assert hasattr(ingredient, 'get_price')
            assert callable(ingredient.get_type)
            assert callable(ingredient.get_name)
            assert callable(ingredient.get_price)
            
        
                