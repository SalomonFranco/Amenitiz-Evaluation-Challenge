require 'thor'
require 'tty-prompt'
require_relative 'cart'
require_relative 'item'
require_relative 'promotion'

#CashRegisterApp is a command-line tool for a cash register system
class CashRegisterApp < Thor
  def initialize(args = [], local_options = {}, config = {})
    super
    load_products_sample_data
    @cart = Cart.new
  end

  desc 'start', 'Start the cash register'
  def start
    prompt_for_products
    print_cart_total
  end

  private

  def load_products_sample_data
    green_tea_offer = Offer::VolumeDiscountOffer.new(2, 1)
    strawberries_offer = Offer::QuantityThresholdDiscount.new(3, 4.50)
    coffee_offer = Offer::QuantityThresholdDiscount.new(3, 11.23 * 2 / 3)

    @products = [
      Product.new('GR1', 'Green Tea', 3.11, green_tea_offer),
      Product.new('SR1', 'Strawberries', 5.00, strawberries_offer),
      Product.new('CF1', 'Coffee', 11.23, coffee_offer)
    ]
  end

  def prompt_for_products
    prompt = TTY::Prompt.new
    loop do
      input = prompt.ask('Enter the product code: (empty to finish)', default: '')
      break if input.empty?

      handle_product_input(input)
    end
  end

  def handle_product_input(input)
    product = fetch_product(input)
    if product
      @cart.add(product)
      puts "Current total: #{format('%.2f', @cart.total)}€"
    else
      puts "Product #{input} not found"
    end
  end

  def fetch_product(code)
    @products.find { |prod| prod.code == code }
  end

  def print_cart_total
    puts "\nCart Summary:"
    @cart.items.each do |code, item|
      puts "#{item[:quantity]} x #{item[:product].name} (#{item[:product].code}): #{format('%.2f', item[:product].calculate_price_for(item[:quantity]))}€"
    end
    puts "\nFinal total: #{format('%.2f', @cart.total)}€"
  end
end

CashRegisterApp.start(ARGV)