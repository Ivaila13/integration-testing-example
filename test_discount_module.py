import pytest
from discount_module import apply_discount

# Тест 1: Без отстъпка
def test_no_discount():
    total_price = 400
    assert apply_discount(total_price) == 400

# Тест 2: С 5% отстъпка
def test_5_percent_discount():
    total_price = 600
    assert apply_discount(total_price) == 570  # 600 * 0.95 = 570

# Тест 3: С 10% отстъпка
def test_10_percent_discount():
    total_price = 1200
    assert apply_discount(total_price) == 1080  # 1200 * 0.9 = 1080
