import pytest
from product_module import add_product
from order_module import calculate_total_price

# Фикстура за настройка на тестовите данни
@pytest.fixture
def setup_products():
    add_product(1, "Laptop", 1200)
    add_product(2, "Mouse", 20)

# Тест 1: Поръчка без отстъпка
def test_order_without_discount(setup_products):
    order_items = [(2, 3)]  # 3x Mouse (20 * 3 = 60)
    total_price = calculate_total_price(order_items)
    assert total_price == 60  # Без отстъпка

# Тест 2: Поръчка с 5% отстъпка
def test_order_with_5_percent_discount(setup_products):
    order_items = [(2, 30)]  # 30x Mouse (20 * 30 = 600)
    total_price = calculate_total_price(order_items)
    assert total_price == 570  # 600 - 5% отстъпка

# Тест 3: Поръчка с 10% отстъпка
def test_order_with_10_percent_discount(setup_products):
    order_items = [(1, 2), (2, 1)]  # 2x Laptop (1200 * 2 = 2400) + 1x Mouse (20) = 2420
    total_price = calculate_total_price(order_items)
    assert total_price == 2178  # Очаквана стойност след 10% отстъпка (2420 * 0.90 = 2178)


# Тест 4: Поръчка с несъществуващ продукт
def test_order_with_invalid_product(setup_products):
    order_items = [(99, 1)]  # Несъществуващ продукт
    total_price = calculate_total_price(order_items)
    assert total_price == 0  # Няма такъв продукт, цената е 0
