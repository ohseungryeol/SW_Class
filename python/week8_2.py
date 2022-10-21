class Bank:
    money=0

    @classmethod
    def change_money(cls,money):
        cls.money+=money
    @classmethod
    def print_money(cls):
        print(cls.money)

Bank.change_money(1000)
Bank.print_money()

