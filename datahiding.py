"""
Dieser Code dient dem Erlebnis der Auswirkungen des data hiding.
Die Übung basiert auf zwei Klassen, nämlich BankAccountWell und BankAccountUgly.

Mit beiden Klassen wird je eine Einzahlung in auf das Konto sowie 2 Bezüge aus dem Konto
realisiert.
Massgebend ist der Unterschied der beiden Klassen in ihrem verhalten.
Diesen Unterschied zu beschreiben, ist der Sinn der Aufgabe.
"""


class BankAccountWell:
    """
    Well constructed BankAccount

    Attributes
    ----------
    _balance: float
    """

    def __init__(self, starting_amount):
        """
        Constructor creating an account with a starting amount
        :param starting_amount:
        """
        self._balance = starting_amount

    def get_money(self, value):
        """
        Gets the requested amount ensuring the balance won't be negative
        :param value:
        :return:
        """
        if value < self._balance:
            self._balance -= value
            return value
        return 0

    @property
    def balance(self):
        """
        Returns the current account balance
        :return: balance (float)
        """
        return self._balance


class BankAccountUgly:
    """
    Badly implemented BankAccount

    Attributes
    ----------
    _balance: float
    """
    balance = 0.0

    def __init__(self, starting_amount):
        """
        Constructor creating an account with a starting amount
        :param starting_amount:
        """
        self.balance = starting_amount


if __name__ == "__main__":
    # Create a bank account that works well.
    account1 = BankAccountWell(1000.0)
    print('vom Bankkonto Nr. 1 mit Saldo ' + str(account1.balance) + ' wird 300.0 abgehoben')
    money_drawn = account1.get_money(300.0)
    print('neuer Saldo = ' + str(account1.balance))
    print('vom Bankkonto Nr. 1 mit Saldo ' + str(account1.balance) + ' wird 900.0 abgehoben')
    money_drawn = account1.get_money(900.0)
    print('neuer Saldo = ' + str(account1.balance), 'da der Bezug ' + str(money_drawn) + ' liefert')
    print(
        '-----------------------------------------------------------------------------------------')
    # Creat a bank account that is badly implemented
    account2 = BankAccountUgly(1000)
    print('vom Bankkonto Nr. 2 mit Saldo ' + str(account2.balance) + ' wird 300.0 abgehoben')
    account2.balance -= 300
    print('neuer Saldo = ' + str(account2.balance))
    print('vom Bankkonto Nr. 2 mit Saldo ' + str(account2.balance) + ' wird 900.0 abgehoben')
    account2.balance -= 900
    print('neuer Saldo = ' + str(account2.balance), 'da der Bezug 900.0 liefert')
