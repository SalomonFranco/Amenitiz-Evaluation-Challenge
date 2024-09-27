Cash Register App

Overview
This is a cash register application built to meet the requirements of a technical test for Amenitiz. The app allows users to add products to a cart and compute the total price, taking into account special conditions and discounts.

Technical Requirements
Built using Python 3.9+
Covered by unit tests using the unittest framework
Follows Test-Driven Development (TDD) methodology
Products and Pricing
The app supports the following products:

Product Code	Name	Price
GR1	Green Tea	3.11€
SR1	Strawberries	5.00€
CF1	Coffee	11.23€
Special Conditions
The app applies the following special conditions:

Buy-one-get-one-free offer on Green Tea (GR1)
Discounted price of 4.50€ for bulk purchases of Strawberries (SR1) (3 or more items)
Discounted price of 2/3 of the original price for bulk purchases of Coffee (CF1) (3 or more items)
Test Data
The app has been tested with the following scenarios:

Cart	Total Price Expected
GR1, GR1	3.11€
SR1, SR1, GR1, SR1	16.61€
GR1, CF1, SR1, CF1, CF1	30.57€
Code Structure and Flow
The app is structured into the following modules:

app.py: The main application module, responsible for handling user input and calculating the total price.
products.py: Defines the product classes and their respective prices.
special_conditions.py: Defines the special conditions and discounts applied to each product.
tests.py: Contains unit tests for the app.
Commit History
The commit history is available in the Git repository and follows standard professional guidelines.

Best Practices
The app follows best practices for coding, including:

Clear and concise variable names
Proper use of functions and modules
Consistent coding style
Thorough testing
Facility to Make Changes
The app is designed to be flexible and easy to modify. New products and special conditions can be added by modifying the products.py and special_conditions.py modules, respectively.

Installation and Usage
To run the app, simply execute the app.py file using Python:

bash
Edit
Copy code
python app.py
License
This app is licensed under the MIT License.

Contributing
Contributions are welcome! Please submit a pull request with your changes and a clear description of what you've modified.

Acknowledgments
This app was built as a technical evaluation for Amenitiz.