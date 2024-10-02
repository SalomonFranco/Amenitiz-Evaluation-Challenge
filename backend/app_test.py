import unittest
from unittest.mock import patch, MagicMock
from backend.app import handle_cart

class TestHandleCart(unittest.TestCase):
    def test_process_cart_data(self):
        cart_data = {'GR1': 2, 'SR1': 3}
        response = handle_cart(cart_data)
        self.assertEqual(response['total'], 16.61)

    def test_handle_invalid_input_data(self):
        cart_data = {'invalid_product': 2}
        response = handle_cart(cart_data)
        self.assertEqual(response['error'], 'Invalid input data')

    def test_handle_error(self):
        with patch('app.calculate_total') as mock_calculate_total:
            mock_calculate_total.side_effect = Exception('Error calculating total')
            cart_data = {'GR1': 2, 'SR1': 3}
            response = handle_cart(cart_data)
            self.assertEqual(response['error'], 'Error calculating total')

    def test_handle_cart_with_no_items(self):
        cart_data = {}
        response = handle_cart(cart_data)
        self.assertEqual(response['total'], 0.0)

    def test_handle_cart_with_single_item(self):
        cart_data = {'GR1': 1}
        response = handle_cart(cart_data)
        self.assertEqual(response['total'], 5.0)

    def test_handle_cart_with_multiple_items(self):
        cart_data = {'GR1': 2, 'SR1': 3, 'CF1': 1}
        response = handle_cart(cart_data)
        self.assertEqual(response['total'], 26.61)

if __name__ == '__main__':
    unittest.main()