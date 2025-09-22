# src/market/environment.py

from typing import Dict, Any

class MarketEnvironment:
    """
    Simulates the DeFi market environment with a dynamic pricing model.
    """
    def __init__(self, initial_prices: Dict[str, float], price_impact_factor: float = 0.01):
        """
        Initializes the market environment.

        Args:
            initial_prices (Dict[str, float]): The starting prices for assets.
            price_impact_factor (float): A factor to determine how much a trade affects the price.
        """
        self.prices = initial_prices
        self.price_impact_factor = price_impact_factor
        print(f"MarketEnvironment initialized with prices: {self.prices}")

    def execute_trade(self, agent_id: str, action: Dict[str, Any]):
        """
        Processes a trade action and updates the market price based on a simple impact model.
        """
        if not action or 'action' not in action:
            return
    
        # --- ADD THIS PRINT STATEMENT BACK IN ---
        print(f"Executing trade for {agent_id}: {action}")
        
        action_type = action.get('action')
        asset = action.get('asset')
        amount = action.get('amount')
        
        if not all([action_type, asset, amount]):
            return
            
        price_key = f"{asset}_USDC"
        if price_key in self.prices:
            current_price = self.prices[price_key]
            
            if action_type == 'BUY':
                price_change = amount * self.price_impact_factor
                self.prices[price_key] += price_change
            elif action_type == 'SELL':
                price_change = amount * self.price_impact_factor
                self.prices[price_key] -= price_change

            # Uncomment the line below if you want to see every single price update
            # print(f"Trade executed: {action_type} {amount} {asset}. New price: {self.prices[price_key]:.4f}")

    def get_market_state(self) -> Dict[str, Any]:
        """
        Returns the current state of the market for agents to observe.
        """
        return {
            'prices': self.prices.copy()
        }