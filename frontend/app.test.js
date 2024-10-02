import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react';
import { App } from './ap';

describe('App', () => {
  it('adds item to cart', () => {
    const { getByText } = render(<App />);
    const addItemButton = getByText('Add Item');
    fireEvent.click(addItemButton);
    expect(getByText('Item added to cart')).toBeInTheDocument();
  });

  it('removes item from cart', () => {
    const { getByText } = render(<App />);
    const removeItemButton = getByText('Remove Item');
    fireEvent.click(removeItemButton);
    expect(getByText('Item removed from cart')).toBeInTheDocument();
  });

  it('calculates total price correctly', () => {
    const { getByText } = render(<App />);
    const calculateTotalButton = getByText('Calculate Total');
    fireEvent.click(calculateTotalButton);
    expect(getByText('Total price: 10.00')).toBeInTheDocument();
  });

  it('handles errors correctly', () => {
    const { getByText } = render(<App />);
    const calculateTotalButton = getByText('Calculate Total');
    fireEvent.click(calculateTotalButton);
    expect(getByText('Error: Unable to calculate total price')).toBeInTheDocument();
  });
});