const { useState, useEffect } = React;
const { render } = ReactDOM;

function App() {
  const initialCart = { GR1: 0, SR1: 0, SF1: 0 };
  const initialItems =[
        {
            "discount": "Not Elegible",
            "name": "Green Tea",
            "price_per_item": 3.11,
            "product_code": "GR1",
            "quantity": 0,
            "total": 0.0
        },
        {
            "name": "Strawberries",
            "product_code": "SR1",
            "quantity": 0
        },
        {
            "name": "Coffee",
            "product_code": "CF1",
            "quantity": 0
        }
    ]
  const [cart, setCart] = useState(initialCart);
  const [total, setTotal] = useState(0);
  const [items,setItems] = useState(initialItems);

  // Function to handle incrementing the quantity of an item
  const addItem = (item) => {
    setCart({ ...cart, [item]: cart[item] + 1 });
  };

  // Function to handle decrementing the quantity of an item
  const removeItem = (item) => {
    if (cart[item] > 0) {
      setCart({ ...cart, [item]: cart[item] - 1 });
    }
  };

  // Function to handle resetting the cart
  const resetCart = () => {
    setCart(initialCart);
  };

  // Function to calculate the total price based on the cart
  const calculateTotal = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/algo', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ cart }),
      });

      const result = await response.json();
      setTotal(result.total);
      setItems(result.items);
    } catch (error) {
      console.error('Error calculating total:', error);
    }
  };

  // Update total whenever the cart changes
  useEffect(() => {
    calculateTotal();
  }, [cart]);

  return (
    <div style={{ backgroundColor: '#f0f0f0', padding: 20 }}>
      <div style={{ display: 'flex', justifyContent: 'center' }}>
        <h1 style={{ color: '#00698f', fontSize: 36, fontWeight: 'bold' }}>Cash Register</h1>
      </div>
      <div className="products" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', backgroundColor: '#ffffff', padding: 20, borderRadius: 10, boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)' }}>
        <div className="product" style={{ display: 'flex', justifyContent: 'space-between', width: '100%', padding: 10, borderBottom: '1px solid #ccc' }}>
          <span style={{ fontSize: 18, fontWeight: 'bold' }}> ☕ Coffee - CF1</span>
          <span style={{ display: 'flex' }}>
            <button onClick={() => removeItem('SF1')} style={{ backgroundColor: 'red', color: '#ffffff', border: 'none', padding: 9, borderRadius: 5, cursor: 'pointer', width: 38, height: 38, fontSize: 22, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>-</button>
            <span style={{ margin: '0 10px', fontSize: 18 }}>{cart.SF1}</span>
            <button onClick={() => addItem('SF1')} style={{ backgroundColor: '#4CAF50', color: '#ffffff', border: 'none', padding: 9, borderRadius: 5, cursor: 'pointer', width: 38, height: 38, fontSize: 22, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>+</button>
          </span>
        </div>
        <div className="product" style={{ display: 'flex', justifyContent: 'space-between', width: '100%', padding: 10, borderBottom: '1px solid #ccc' }}>
          <span style={{ fontSize: 18, fontWeight: 'bold' }}> 🍵 Green Tea - GR1</span>
          <span style={{ display: 'flex' }}>
            <button onClick={() => removeItem('GR1')} style={{ backgroundColor: 'red', color: '#ffffff', border: 'none', padding: 9, borderRadius: 5, cursor: 'pointer', width: 38, height: 38, fontSize: 22, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>-</button>
            <span style={{ margin: '0 10px', fontSize: 18 }}>{cart.GR1}</span>
            <button onClick={() => addItem('GR1')} style={{ backgroundColor: '#4CAF50', color: '#ffffff', border: 'none', padding: 9, borderRadius: 5, cursor: 'pointer', width: 38, height: 38, fontSize: 22, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>+</button>
          </span>
        </div>
        <div className="product" style={{ display: 'flex', justifyContent: 'space-between', width: '100%', padding: 10 }}>
          <span style={{ fontSize: 18, fontWeight: 'bold' }}> 🍓 Strawberries - SR1</span>
          <span style={{ display: 'flex' }}>
            <button onClick={() => removeItem('SR1')} style={{ backgroundColor: 'red', color: '#ffffff', border: 'none', padding: 9, borderRadius: 5, cursor: 'pointer', width: 38, height: 38, fontSize: 22, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>-</button>
            <span style={{ margin: '0 10px', fontSize: 18 }}>{cart.SR1}</span>
            <button onClick={() => addItem('SR1')} style={{ backgroundColor: '#4CAF50', color: '#ffffff', border: 'none', padding: 9, borderRadius: 5, cursor: 'pointer', width: 38, height: 38, fontSize: 22, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>+</button>
          </span>
        </div>
      </div>

      <div className="summary" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', backgroundColor: '#ffffff', padding: 20, borderRadius: 10, boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)', marginTop: 20 }}>
        <h2 style={{ color: '#00698f', fontSize: 24, fontWeight: 'bold' }}>Summary</h2>
        <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
          {items.map((item) => (
            item.quantity > 0 && (
              <li key={item.product_code} style={{ fontSize: 18, padding: 10, borderBottom: '1px solid #ccc' }}>
                {item.name} - {item.quantity} x ${item.price_per_item.toFixed(2)} (Discount: {item.discount})
              </li>
            )
          ))}
        </ul>
        <h3 style={{ color: '#00698f', fontSize: 24, fontWeight: 'bold' }}>Total: ${total.toFixed(2)}</h3>
      </div>

      <button onClick={resetCart} style={{ backgroundColor: '#4CAF50', color: '#ffffff', border: 'none', padding: 10, borderRadius: 5, cursor: 'pointer', display: 'block', margin: '20px auto' }}>Reset</button>
    </div>
  );
}
