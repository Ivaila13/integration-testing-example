# order_module.py

from product_module import get_product
from discount_module import apply_discount

def calculate_total_price(order_items):
    """
    Изчислява общата цена на поръчка с отстъпка.
    order_items е списък от tuples (product_id, quantity).
    """
    total = 0
    for product_id, quantity in order_items:
        product = get_product(product_id)
        if product:
            total += product["price"] * quantity

    print(f"Обща цена без отстъпка: {total}")  # Печати за дебъгване
    total_with_discount = apply_discount(total)
    print(f"Цена с отстъпка: {total_with_discount}")  # Печати за дебъгване
    return total_with_discount

