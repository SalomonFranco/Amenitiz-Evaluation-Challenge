from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/algo": {"origins": "*"}})

def isDiscountGreenTea(quantity):
    if quantity > 1:
        return 'Buy-One-Get-One-Free'
    else:
        return 'Not Elegible'

def calculateGreenTea(quantity, price, discount):
    if discount == 'Not Elegible':
        return quantity * price
    else:
        if quantity % 2 == 0:
            return ((quantity / 2) * price)
        else:
            return ((((quantity - 1) / 2)) * price) + price

def isDiscountStrawberry(quantity):
    if quantity >= 3:
        return 'Price Drop'
    else:
        return 'Not Elegible'

def calculateStrawberry(quantity, price, discount):
    if discount == 'Not Elegible':
        return quantity * price
    else:
        price = 4.50
        return quantity * price

def isDiscountCoffee(quantity):
    if quantity >= 3:
        return '2/3 Price Discount'
    else:
        return 'Not Elegible'

def calculateCoffee(quantity, price, discount):
    if discount == 'Not Elegible':
        return quantity * price
    else:
        discounted_price = (2 * price) / 3
        return quantity * discounted_price

def handle_cart(cart_data):
    try:
        grtea = cart_data.get('GR1', 0)
        strberry = cart_data.get('SR1', 0)
        coffee = cart_data.get('CF1', 0)

        priceGreenTea = 3.11
        discountGreenTea = isDiscountGreenTea(grtea)
        totalGreenTea = calculateGreenTea(grtea, priceGreenTea, discountGreenTea)

        priceStrberry = 5.00
        discountStrBerry = isDiscountStrawberry(strberry)
        totalStrBerry = calculateStrawberry(strberry, priceStrberry, discountStrBerry)

        priceCoffee = 11.23
        discountCoffee = isDiscountCoffee(coffee)
        totalCoffee = calculateCoffee(coffee, priceCoffee, discountCoffee)

        totalPrice = totalGreenTea + totalStrBerry + totalCoffee

        itemsList = []
        greenTeaNode = {
            'product_code': 'GR1',
            'name': 'Green Tea',
            'quantity': grtea,
            "price_per_item": priceGreenTea,
            "discount": discountGreenTea,
            "total": round(totalGreenTea, 2)
        }

        strberryNode = {
            'product_code': 'SR1',
            'name': 'Strawberries',
            'quantity': strberry,
            "price_per_item": priceStrberry,
            "discount": discountStrBerry,
            "total": round(totalStrBerry, 2)
        }

        coffeeNode = {
            'product_code': 'CF1',
            'name': 'Coffee',
            'quantity': coffee,
            "price_per_item": priceCoffee,
            "discount": discountCoffee,
            "total": round(totalCoffee, 2)
        }

        itemsList.append(greenTeaNode)
        itemsList.append(strberryNode)
        itemsList.append(coffeeNode)

        response = {
            'total': round(totalPrice, 2),
            'items': itemsList
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/algo', methods=['POST'])
def handle_cart_endpoint():
    cart_data = request.get_json()
    return handle_cart(cart_data)

if __name__ == '__main__':
    app.run(debug=True)