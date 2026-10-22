class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
        

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for value in self.ledger:
            balance = balance + value['amount']
        return balance
    
    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {destination.name}')
            destination.deposit(amount,f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        budget = f"{self.name:*^30}"

        for item in self.ledger:
            budget += f"\n{item['description'][:23]:<23}{item['amount']:>7.2f}"

        budget += f"\nTotal: {self.get_balance():.2f}"  
        return budget   

def create_spend_chart(categories):
    spent = []
    percent = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total += -item['amount']
        spent.append(total)
    
    total_spent = sum(spent)

    for each in spent:
         percent.append((each/total_spent * 100)//10 * 10)

    chart = 'Percentage spent by category'

    for i in range(100,-1,-10):
        row = f'{i:>3}|'
        for p in percent:
            if p >= i:
                row += ' o '
            else:
                row += '   '
        row += ' '
        chart += "\n" + row
    chart += "\n"+"    "+"-"*(3*len(categories)+1)
    longest = max(len(c.name) for c in categories)

    for j in range(longest):
        row = '    '
        for c in categories:
            if j < len(c.name):
                row += " " + c.name[j] + " "
            else:
                row += '   '
        row += "   "
        chart += "\n" + row
    return chart

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
clothing.withdraw(42,'Belt')
food.transfer(50, clothing)
print(food)

print(create_spend_chart([food,clothing]))
print("\n\nMade By : Sudhir Shah\nCopyright")
