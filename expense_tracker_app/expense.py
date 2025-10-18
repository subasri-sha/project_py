class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        # self.amount = amount
        self.amount = float(str(amount).replace("Rs.", "").replace("₹", "").strip())


    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, {self.amount:.2f} >"
    
    '''
    <expense.Expense object at 0x000001D8F62D7230> to avoid this using def __repr__(self): --> Returns a string representation of the object when you print it. 
    '''
