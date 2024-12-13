from datetime import datetime
from typing import List, Optional

class Transaction:
    def __init__(self, amount: float, t_type: str, category: str, date: Optional[datetime] = None):
        if t_type not in ('income', 'expense'):
            raise ValueError("Transaction type must be 'income' or 'expense'.")
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        
        self.amount = amount
        self.type = t_type
        self.category = category
        self.date = date or datetime.now()

    def __repr__(self):
        return f"Transaction(amount={self.amount}, type='{self.type}', category='{self.category}', date={self.date})"

class Account:
    def __init__(self):
        self.balance = 0.0
        self.transactions: List[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        if transaction.type == 'income':
            self.balance += transaction.amount
        elif transaction.type == 'expense':
            self.balance -= transaction.amount
        self.transactions.append(transaction)

    def remove_transaction(self, transaction: Transaction):
        if transaction not in self.transactions:
            raise ValueError("Transaction not found in account.")
        if transaction.type == 'income':
            self.balance -= transaction.amount
        elif transaction.type == 'expense':
            self.balance += transaction.amount
        self.transactions.remove(transaction)

    def get_balance(self) -> float:
        return self.balance

    def generate_report_by_category(self) -> dict:
        report = {}
        for transaction in self.transactions:
            if transaction.category not in report:
                report[transaction.category] = 0.0
            if transaction.type == 'income':
                report[transaction.category] += transaction.amount
            elif transaction.type == 'expense':
                report[transaction.category] -= transaction.amount
        return report

class TaxCalculator:
    TAX_RATE = 0.13

    @staticmethod
    def calculate_tax(transactions: List[Transaction]) -> float:
        total_income = sum(t.amount for t in transactions if t.type == 'income')
        return total_income * TaxCalculator.TAX_RATE

    @staticmethod
    def calculate_net_profit(transactions: List[Transaction]) -> float:
        total_income = sum(t.amount for t in transactions if t.type == 'income')
        total_expenses = sum(t.amount for t in transactions if t.type == 'expense')
        return total_income - total_expenses