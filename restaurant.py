class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def get_reviews(self):
        return self.reviews

    def customers(self):
        return [review.customer for review in self.reviews]
    
    def average_star_rating(self):
        if not self.reviews:
            return 0  
        
        total_rating = sum(review.get_rating() for review in self.reviews)
        return total_rating / len(self.reviews)

