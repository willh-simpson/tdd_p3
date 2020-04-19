import pytest
from invoice import Invoice


@pytest.fixture()
def products():
    products = {
        'Pen': {'qnt': 10, 'unit price': 3.75, 'discount': 5},
        'Notebook': {'qnt': 5, 'unit price': 7.5, 'discount': 10}
    }

    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()

    return invoice


def test_can_calculate_total_impure_price(invoice, products):
    invoice.total_impure_price(products)

    assert invoice.total_impure_price(products) == 75


def test_can_calculate_total_discount(invoice, products):
    invoice.total_discount(products)

    assert invoice.total_discount(products) == 5.62


def test_can_calculate_total_pure_price(invoice, products):
    invoice.total_pure_price(products)

    assert invoice.total_pure_price(products) == 69.38
