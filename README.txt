# Amenitiz Technical Challenge

## Overview

This is a cash register application built to meet the requirements of a technical test for Amenitiz. The app allows users to add products to a cart and compute the total price, taking into account special conditions and discounts.

## Technical Requirements

Built using Python 3.9+
Covered by unit tests using the unittest framework
Follows Test-Driven Development (TDD) methodology
Products and Pricing

### The app supports the following products:

Product Code	Name	Price
GR1	    Green Tea	    3.11€
SR1	   Strawberries	  5.00€
CF1    	Coffee	      11.23€

### Special Conditions

The app applies the following special conditions:

Buy-one-get-one-free offer on Green Tea (GR1)
Discounted price of 4.50€ for bulk purchases of Strawberries (SR1) (3 or more items)
Discounted price of 2/3 of the original price for bulk purchases of Coffee (CF1) (3 or more items)

## Installation and Usage

### Backend
Clone the repository: 
```
git clone https://github.com/your-username/amenitiz-technical-challenge.git
```
Navigate to the backend directory: 
```
cd backend
```
Install the required dependencies: 
```
pip install -r requirements.txt
```
Run the backend server: 
```
python app.py
```
### Frontend

Navigate to the frontend directory: 
```
cd frontend
```
Install the required dependencies: 
```
npm install
```
Start the frontend server: 
```
npm start
```
### Testing
## Backend
Navigate to the backend directory: 
```
cd backend
```
Run the unit tests: 
```
python -m unittest discover
```
### Frontend
Navigate to the frontend directory: 
```
cd frontend
```
Run the unit tests: 
```
npm test
```
### API Endpoints
The backend API has one endpoint:
```
POST /algo: Calculates the total price of the items in the cart.
Example Request

{
  "GR1": 2,
  "SR1": 3,
  "CF1": 1
}
```

```
Example Response
json
Edit
Copy code
{
  "total": 26.61,
  "items": [
    {
      "product_code": "GR1",
      "name": "Green Tea",
      "quantity": 2,
      "price_per_item": 3.11,
      "discount": "Buy-One-Get-One-Free",
      "total": 3.11
    },
    {
      "product_code": "SR1",
      "name": "Strawberries",
      "quantity": 3,
      "price_per_item": 5.00,
      "discount": "Price Drop",
      "total": 13.50
    },
    {
      "product_code": "CF1",
      "name": "Coffee",
      "quantity": 1,
      "price_per_item": 11.23,
      "discount": "Not Elegible",
      "total": 11.23
    }
  ]
}
```


###Acknowledgments :
This app was built as a technical evaluation for Amenitiz.
