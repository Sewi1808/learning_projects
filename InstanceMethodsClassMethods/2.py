class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    @classmethod
    def margherita(cls):
        return cls(['cheese', 'tomatoes'])

    @classmethod
    def ham(cls):
        return cls(['cheese', 'tomatoes', 'ham'])

    @classmethod
    def classic(cls):
        return cls(['cheese', 'tomatoes', 'ham', 'mushrooms'])

print(Pizza.ham())