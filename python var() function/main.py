
class Customer:
    def __init__(self, products = 'POS System', budget ='$4000', nationality = 'Indian', buying_behavior = 'Frequent buyer'):
        self.Products = products
        self.Budget = budget
        self.Nationality = nationality
        self.Buying_behavior = buying_behavior

my_object = Customer()
print('Our Cudtomer Dictionary has:', vars(my_object))