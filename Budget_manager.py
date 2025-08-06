import json

class Transaction:
    def __init__(self, amount, category, date, t_type):
        self.amount = amount
        self.category = category
        self.date = date
        self.t_type = t_type


class BudgetManager:

    def __init__(self):
        self.transaction = []

    def add_transaction(self, transaction):
        self.transaction.append(transaction)

    def get_balance(self):
        income = sum(t.amount for t in self.transaction if t.t_type == 'income')
        expense = sum(t.amount for t in self.transaction if t.t_type == 'expense')
        return income - expense

    def list_transaction(self):
        for t in self.transaction:
            print(f"{t.date} | {t.category} | {t.amount} | {t.t_type}")


while True:
    print('Opcja 1')
    print('Opcja 2')
    print('Opcja 3')
    print('Opcja 4')

    opcja = int(input("Wybierz opcję "))

    if opcja == 1:
        amount = float(input('Kwota: '))
        category = input('Kategoria: ')
        date = input('Data: ')
        t_type = input('Rodzaj transakcji (dochody/wydatki): ')
        transaction = Transaction(amount, category, date, t_type)

    elif opcja == 2:
        print('xyz')
    elif opcja == 3:
        print('xyz')
    elif opcja == 4:
        print('xyz')
    else:
        print('Podano nieprawidłową opcję')



