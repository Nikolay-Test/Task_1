from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class BunTestData1:
    """
    Тестовые данные для первой булочки и связанных ингредиентов.
    Используется для тестирования классов Bun, Ingredient и Burger.
    """
    # Данные для булочки
    bun_name = 'Краторная булка N-200i'
    bun_price = 1255
    
    # Данные для соуса
    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'Соус Spicy-X'
    sauce_price = 90
    
    # Данные для начинки
    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'Мини-салат Экзо-Плантаго'
    filling_price = 4400
    
    # Ожидаемая итоговая стоимость бургера
    burger_final_cost = bun_price * 2 + sauce_price + filling_price


class BunTestData2:
    """
    Тестовые данные для второй булочки и связанных ингредиентов.
    Используется для тестирования классов Bun, Ingredient и Burger.
    """
    # Данные для булочки
    bun_name = 'Флюоресцентная булка R2-D3'
    bun_price = 988
    
    # Данные для соуса
    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'Соус фирменный Space Sauce'
    sauce_price = 80
    
    # Данные для начинки
    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'Мясо бессмертных моллюсков Protostomia'
    filling_price = 1337
    
    # Ожидаемая итоговая стоимость бургера
    burger_final_cost = bun_price * 2 + sauce_price + filling_price


class TestDataBase:
    """
    Тестовые данные для тестирования базы данных.
    Содержит ожидаемые данные о булочках и ингредиентах.
    """
    
    # Ожидаемые данные о булочках в базе данных
    # Формат: [индекс, название, цена]
    database_buns = [
        [0, 'black bun', 100],
        [1, 'white bun', 200],
        [2, 'red bun', 300]
    ]
    
    # Ожидаемые данные об ингредиентах в базе данных
    # Формат: [индекс, тип, название, цена]
    database_ingredients = [
        [0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100],
        [1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200],
        [2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300],
        [3, INGREDIENT_TYPE_FILLING, 'cutlet', 100],
        [4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200],
        [5, INGREDIENT_TYPE_FILLING, 'sausage', 300]
    ]
    
    @staticmethod
    def get_bun_by_index(index: int):
        """Получить данные о булочке по индексу"""
        if 0 <= index < len(TestDataBase.database_buns):
            return TestDataBase.database_buns[index]
        return None
    
    @staticmethod
    def get_ingredient_by_index(index: int):
        """Получить данные об ингредиенте по индексу"""
        if 0 <= index < len(TestDataBase.database_ingredients):
            return TestDataBase.database_ingredients[index]
        return None
    
    @staticmethod
    def get_all_sauces():
        """Получить все соусы из тестовых данных"""
        return [ing for ing in TestDataBase.database_ingredients 
                if ing[1] == INGREDIENT_TYPE_SAUCE]
    
    @staticmethod
    def get_all_fillings():
        """Получить все начинки из тестовых данных"""
        return [ing for ing in TestDataBase.database_ingredients 
                if ing[1] == INGREDIENT_TYPE_FILLING]


class BurgerTestData:
    """
    Тестовые данные для тестирования класса Burger.
    """
    
    @staticmethod
    def get_burger_price_test_cases():
        """
        Возвращает тестовые случаи для проверки расчета цены бургера.
        Формат: (цена_булочки, список_цен_ингредиентов, ожидаемая_общая_цена)
        """
        return [
            (100.0, [50.0, 80.0], 330.0),  # 2*100 + 50 + 80
            (0.0, [10.0, 20.0], 30.0),     # 2*0 + 10 + 20
            (50.0, [], 100.0),             # Только булочки
            (75.5, [25.5, 30.0], 206.5),   # 2*75.5 + 25.5 + 30
        ]
    
    @staticmethod
    def get_ingredient_move_test_cases():
        """
        Возвращает тестовые случаи для проверки перемещения ингредиентов.
        Формат: (начальный_индекс, новый_индекс)
        """
        return [
            (0, 1),    # Переместить первый элемент на вторую позицию
            (2, 0),    # Переместить третий элемент на первую позицию
            (1, 3),    # Переместить второй элемент на четвертую позицию
        ]


class IngredientTestData:
    """
    Тестовые данные для параметризованного тестирования ингредиентов.
    """
    
    @staticmethod
    def get_all_test_cases():
        """
        Возвращает все тестовые случаи для ингредиентов.
        Формат: (тип_ингредиента, название, цена)
        """
        return [
            (BunTestData1.sauce_type, BunTestData1.sauce_name, BunTestData1.sauce_price),
            (BunTestData1.filling_type, BunTestData1.filling_name, BunTestData1.filling_price),
            (BunTestData2.sauce_type, BunTestData2.sauce_name, BunTestData2.sauce_price),
            (BunTestData2.filling_type, BunTestData2.filling_name, BunTestData2.filling_price)
        ]
    
    @staticmethod
    def get_sauce_test_cases():
        """
        Возвращает тестовые случаи для соусов.
        """
        return [
            (BunTestData1.sauce_type, BunTestData1.sauce_name, BunTestData1.sauce_price),
            (BunTestData2.sauce_type, BunTestData2.sauce_name, BunTestData2.sauce_price)
        ]
    
    @staticmethod
    def get_filling_test_cases():
        """
        Возвращает тестовые случаи для начинок.
        """
        return [
            (BunTestData1.filling_type, BunTestData1.filling_name, BunTestData1.filling_price),
            (BunTestData2.filling_type, BunTestData2.filling_name, BunTestData2.filling_price)
        ]


class BunTestData:
    """
    Тестовые данные для параметризованного тестирования булочек.
    """
    
    @staticmethod
    def get_all_test_cases():
        """
        Возвращает все тестовые случаи для булочек.
        Формат: (название, цена)
        """
        return [
            (BunTestData1.bun_name, BunTestData1.bun_price),
            (BunTestData2.bun_name, BunTestData2.bun_price)
        ]