# Amenitiz-Technical-Challenge

This project is a command-line application developed as a solution to the Amenitiz technical challenge. It implements a cash register system that allows users to add products to a virtual cart, calculate the total price, and apply dynamic discounts based on predefined pricing rules.


Features

- Add products to a cart
- Compute the total price with special discount rules:
 Buy-one-get-one-free for Green Tea
 Bulk discount for Strawberries (price drops to 4.50€ if you buy 3 or more)
 Bulk discount for Coffee (price drops to 2/3 of the original price if you buy 3 or more)
- Flexible and easily extendable pricing rules

Technical Requirements

- Ruby
- Bundler for managing dependencies
- RSpec for testing


Setup Instructions

Prerequisites

- Ruby (version 2.5.11 or higher)
- Bundler

Installation

1. Clone the repository:
```
git clone <repository-url>
cd Amenitiz-Evaluation-Challenge
```
2. Install dependencies:
```
bundle install
```
Running the Application

1. Navigate to the backend directory:
```
cd backend
```
2. Start the application:
```
ruby lib/cash_register.rb start
```
Running Tests

1. Navigate to the backend directory:
```
cd backend
```
2. Run the tests using RSpec:
```
bundle exec rspec
```

Key Information

Products Registered

- Green Tea (GR1) 3.11€
- Strawberries (SR1) 5.00€
- Coffee (CF1) 11.23€

Special Conditions

- Green Tea (GR1): Buy-one-get-one-free
- Strawberries (SR1): Price drops to 4.50€ if you buy 3 or more
- Coffee (CF1): Price drops to 2/3 of the original price if you buy 3 or more

Test Data

- GR1 , GR1	= 3.11€
- SR1 , SR1 , GR1 , SR1	= 16.61€
- GR1 , CF1 , SR1 , CF1 , CF1	= 30.57€

Future Improvements

- Frontend Implementation: Develop a web or mobile frontend to interact with the cash register system.
- Database Integration: Store product and transaction data in a database for persistence.
- User Authentication: Implement user authentication to manage different user roles (e.g., admin, cashier).
- Enhanced Discount Rules: Add more complex discount rules and promotions.
- Reporting: Generate sales reports and analytics.

