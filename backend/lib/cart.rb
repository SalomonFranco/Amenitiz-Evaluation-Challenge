# This class handles managing the products in the cart and computing the total cost.
class Cart
    attr_reader :items
  
    def initialize
      @items = {}
    end
  
    def add(product)
      raise ArgumentError, 'Product cannot be nil' unless product
  
      @items[product.code] ||= { product:, quantity: 0 }
      @items[product.code][:quantity] += 1
    end
  
    def total
      @items.values.reduce(0) do |total, item|
        total + item[:product].calculate_price_for(item[:quantity])
      end
    end
  
    def empty?
      @items.empty?
    end
  end