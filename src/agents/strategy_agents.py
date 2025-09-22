# src/agents/strategy_agents.py

from typing import Dict, Any
from src.agents.base_agent import BaseAgent

class MomentumAgent(BaseAgent):
    """
    An agent that implements a simple momentum strategy.
    It buys if the price is rising and sells if the price is falling.
    """
    def __init__(self, agent_id: str, wallet: Dict[str, float]):
        super().__init__(agent_id, wallet)
        self.last_observed_price = 0.0 # Agent's memory of the last price

    def step(self, market_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Implements the momentum logic.
        """
        current_price = market_state['prices']['ETH_USDC']
        action = {} # Default action is to do nothing

        # We need at least one previous price to calculate momentum
        if self.last_observed_price > 0:
            if current_price > self.last_observed_price:
                # Price is rising (upward momentum), so we BUY
                action = {'action': 'BUY', 'asset': 'ETH', 'amount': 0.1}
            elif current_price < self.last_observed_price:
                # Price is falling (downward momentum), so we SELL
                action = {'action': 'SELL', 'asset': 'ETH', 'amount': 0.1}

        # Update the agent's memory with the current price for the next step
        self.last_observed_price = current_price

        return action