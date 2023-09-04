from customer import Customer
from restaurant import Restaurant
from review import Review

# if __name__ == "__main__":
    # Create customers
customer1 = Customer("Wambui", "Karanja")
customer2 = Customer("Emmanuel", "Kimani")

# Create restaurants
restaurant1 = Restaurant("Cafe Kilimani")
restaurant2 = Restaurant("Big Square")

# Create reviews
# review1 = Review(customer1, restaurant1, 4)
# review2 = Review(customer2, restaurant1, 8)
# review3 = Review(customer1, restaurant2, 5)
customer1.add_review(restaurant1, 5)
customer2.add_review(restaurant1, 4)
customer2.add_review(restaurant2, 3)

# for average star rating
print(f"{restaurant1.name} Average Star Rating: {restaurant1.average_star_rating()}")
print(f"{restaurant2.name} Average Star Rating: {restaurant2.average_star_rating()}")

# Tests
print("All Customers:")
for customer in Customer.all():
    print(customer.full_name())

print("\nAll Reviews:")
for review in Review.all():
    print(f"{review.customer.full_name()} has  reviewed {review.restaurant.name} and rated it {review.rating} stars.")

print("\nCustomers who reviewed Cafe Kilimani:")
cafe_reviews = restaurant1.reviews
for customer in restaurant1.customers():
    print(customer.full_name())

print("\nAverage rating for Cafe Kilimani:")
ratings = [review.get_rating for review in cafe_reviews]
average_rating = sum(ratings) / len(ratings)
print(f"Average Rating:{average_rating.average_star_rating()}")

# Find a customer by full name
found_customer = Customer.find_by_name("Wambui Karanja")
if found_customer:
    print(f"Found Customer: {found_customer.full_name()}")
else:
    print("Customer not found.")

customers_with_given_name = Customer.find_all_by_given_name("Alice")
print(f"Customers with given name 'Alice': {[customer.full_name() for customer in customers_with_given_name]}")