# discount_module.py

def apply_discount(total_price):
    """
    Прилага отстъпки според правилата:
    - 10% отстъпка за обща цена над 1000.
    - 5% отстъпка за обща цена над 500, но под или равна на 1000.
    - Без отстъпка за обща цена до 500.
    """
    if total_price > 1000:
        return total_price * 0.90  # 10% отстъпка
    elif total_price > 500:
        return total_price * 0.95  # 5% отстъпка
    else:
        return total_price  # Няма отстъпка
