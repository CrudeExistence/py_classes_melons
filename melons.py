"""This file should have our melon-type classes in it."""


melons = [
    ('Watermelon', 'green', False, 'natural', ['Fall', 'Summer']),
    ('Cantaloupe', 'tan', False, 'natural', ['Spring', 'Summer']),
    ('Casaba', 'green', True, 'natural', ['Spring', 'Summer', 'Fall', 'Winter']),
    ('Sharlyn', 'tan', True, 'natural', ['Summer']),
    ('Santa Claus', 'green', True, 'natural', ['Winter', 'Spring']),
    ('Christmas', 'green', False, 'natural', ['Winter']),
    ('Horned Melon', 'yellow', True, 'natural', ['Summer']),
    ('Xigua', 'black', True, 'square', ['Summer']),
    ('Ogen', 'tan', False, 'natural', ['Spring', 'Summer'])
]

# class MelonOrder:
#     def get_base_price(self):
#         return 5.0

class AbstractMelonOrder:
    """comnmon logic for all melons
    
    Not meant to be instatiated directly.
    """

    def __init__(self):
        raise NotImplementedError("Don't make instanaces of me")

    def get_base_price(self):
        return 5.0

    def get_price(self, qty):
        each = self.get_base_price() + self.add_on
        total = each * qty

        if self.imported:
            total = total * 1.5
        
        if self.shape == "square":
            total = total* 2

        return total


class WatermelonOrder(AbstractMelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Fall", "Summer"]

    def get_price(self, qty):
        total = super(WatermelonOrder, self).get_price(qty)
        if qty >= 5:
            total = total * 0.75

        return total



class OgenOrder(AbstractMelonOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    add_on = 1


    

