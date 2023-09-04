from review import Review
class Customer:
    all_customers=[]
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def getnew_given_name(self, new_given_name):
        self.given_name = new_given_name

    def getnew_family_name(self, new_family_name):
        self.family_name = new_family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    @classmethod
    def all(cls):
        return cls.all_customers
    
    def restaurants(self):
        return list(set([review.get_restaurant() for review in self.reviews]))
    
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.add_review(review)
    def num_reviews(self):
        return len(self.reviews)
    
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None
    
    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.get_given_name() == given_name]

    def restaurants(self):
        return list(set([review.get_restaurant() for review in self.reviews]))