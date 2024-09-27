from flask import Flask, render_template,request
from flask_cors import CORS, cross_origin
import json
app = Flask(__name__)
cors = CORS(app, resources={r"/ap.js": {"origins": "*"}})
CORS(app, support_credentials=True)


def isDiscountGreenTea(quantity):
    if quantity > 1:
        return 'Buy-One-Get-One-Free'
    else:
        return 'Not Elegible'
    
def calculateGreenTea(quantity,price,discount):
    if discount =='Not Elegible':
        return quantity*price
    else:
        if quantity%2==0:
            return ((quantity/2)*price)
        else:
            return ((((quantity-1)/2))*price) + price

def isDiscountStrawberry(quantity):
    if quantity > 3:
        return 'Price Drop'
    else:
        return 'Not Elegible'
    
def calculateStrawberry(quantity,price,discount):
    if discount =='Not Elegible':
        return quantity*price
    else:
        price=4.50
        return quantity*price

# Coffee discount check
def isDiscountCoffee(quantity):
    if quantity >= 3:
        return '2/3 Price Discount'
    else:
        return 'Not Elegible'

# Coffee price calculation
def calculateCoffee(quantity, price, discount):
    if discount == 'Not Elegible':
        return quantity * price
    else:
        discounted_price = (2 / 3) * price
        return quantity * discounted_price
        
    
@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/algo',methods=['POST'])
def handleCart():
    data = request.data
    cart = json.loads(data)
    
    grtea= cart.get('cart','').get('GR1','') #Cantidad de Green Tea
    strberry=cart.get('cart','').get('SR1','') #Cantidad de Strawberry
    coffee=cart.get('cart','').get('SF1','') #Cantidad de Cafe

    priceGreenTea=3.11
    discountGreenTea=isDiscountGreenTea(grtea)
    totalGreenTea=calculateGreenTea(grtea,priceGreenTea,discountGreenTea)

    priceStrberry=5.00
    discountStrBerry=isDiscountGreenTea(grtea)
    totalStrBerry=calculateGreenTea(grtea,priceStrberry,discountStrBerry)

    # Coffee pricing
    priceCoffee = 11.23
    discountCoffee = isDiscountCoffee(coffee)
    totalCoffee = calculateCoffee(coffee, priceCoffee, discountCoffee)


    totalPrice=totalGreenTea+totalStrBerry+totalCoffee

    itemsList =[]
    greenTeaNode= {
        'product_code':'GR1',
        'name':'Green Tea',
        'quantity':grtea,
        "price_per_item": priceGreenTea,
        "discount": discountGreenTea,
        "total": round(totalGreenTea, 2)

    }

    strberryNode={
        'product_code':'SR1',
        'name':'Strawberries',
        'quantity':strberry,
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
    
    cart['items']=itemsList
    cart['total']=totalPrice

    updatedJson= json.dumps(cart)

    return cart

if __name__ == "__main__":
    app.run()