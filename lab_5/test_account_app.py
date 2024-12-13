import pytest
from datetime import datetime

from accounting_app import Transaction, Account, TaxCalculator


def test_transaction_creation():
    transaction = Transaction(100, 'income', 'salary')
    assert transaction.amount == 100
    assert transaction.type == 'income'
    assert transaction.category == 'salary'
    assert isinstance(transaction.date, datetime)

def test_account_add_transaction():
    account = Account()
    transaction = Transaction(500, 'income', 'bonus')
    account.add_transaction(transaction)
    assert account.get_balance() == 500

def test_account_remove_transaction():
    account = Account()
    transaction = Transaction(200, 'income', 'salary')
    account.add_transaction(transaction)
    account.remove_transaction(transaction)
    assert account.get_balance() == 0

def test_account_generate_report():
    account = Account()
    account.add_transaction(Transaction(1000, 'income', 'salary'))
    account.add_transaction(Transaction(200, 'expense', 'groceries'))
    report = account.generate_report_by_category()
    assert report['salary'] == 1000
    assert report['groceries'] == -200

def test_tax_calculation():
    transactions = [Transaction(1000, 'income', 'salary'), Transaction(200, 'income', 'bonus')]
    tax = TaxCalculator.calculate_tax(transactions)
    assert tax == pytest.approx(156.0)

def test_net_profit_calculation():
    transactions = [
        Transaction(1000, 'income', 'salary'),
        Transaction(500, 'expense', 'rent'),
        Transaction(200, 'expense', 'utilities')
    ]
    net_profit = TaxCalculator.calculate_net_profit(transactions)
    assert net_profit == 300

@pytest.mark.parametrize("transactions,expected_tax", [
    ([Transaction(1000, 'income', 'salary')], 130.0),
    ([Transaction(500, 'income', 'bonus'), Transaction(500, 'income', 'freelance')], 130.0),
    ([], 0.0)
])
def test_parametrized_tax_calculation(transactions, expected_tax):
    tax = TaxCalculator.calculate_tax(transactions)
    assert tax == pytest.approx(expected_tax)
