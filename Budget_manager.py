

class Transaction:
    def __init__(self, amount, category, date, t_type):
        self.amount = amount
        self.category = category
        self.date = date
        self.t_type = t_type






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
    elif opcja == 2:
        print('xyz')
    elif opcja == 3:
        print('xyz')
    elif opcja == 4:
        print('xyz')
    else:
        print('Podano nieprawidłową opcję')



