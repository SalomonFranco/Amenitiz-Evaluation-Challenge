# Offer class is a base class for all the offers
# It has a method apply which is implemented by the child classes
class Offer
    def apply(quantity, price)
      raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
    end
  
  # This class handles applying an offer when purchasing x items and receiving y at no cost.
  # Examples:
  # - Purchase 1 green tea and receive 1 free (which means buying a bundle of 2 for the cost of 1)
  # - Purchase 3 oranges and receive 2 free (which is equivalent to buying a bundle of 5 for the cost of 3)
    class VolumeDiscountOffer < Offer
      def initialize(offer_quantity, free_quantity)
        super()
        @offer_quantity = offer_quantity
        @free_quantity = free_quantity
      end
  
      def apply(quantity, price)
        ((quantity / @offer_quantity) * (@offer_quantity - @free_quantity) * price) +
          ((quantity % @offer_quantity) * price)
      end
    end
  
    # This class handles applying a price reduction when purchasing more than x items.
    # Example: Purchase 3 or more strawberries and pay only $4.50 per item
    class QuantityThresholdDiscount < Offer
      def initialize(offer_amount, offer_price)
        super()
        @offer_amount = offer_amount
        @offer_price = offer_price
      end
  
      def apply(quantity, price)
        quantity >= @offer_amount ? quantity * @offer_price : quantity * price
      end
    end
  end