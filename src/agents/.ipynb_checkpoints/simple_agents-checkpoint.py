# src/agents/simple_agents.py

import random
from typing import Dict, Any
from src.agents.base_agent import BaseAgent

class DoNothingAgent(BaseAgent):
    """A simple agent that observes the market but never takes any action."""
    def __init__(self, agent_id: str, wallet: Dict[str, float]):
        super().__init__(agent_id, wallet)

    def step(self, market_state: Dict[str, Any]) -> Dict[str, Any]:
        # This agent's logic is to do nothing, so it just returns an empty action.
        return {}

class RandomAgent(BaseAgent):
    """An agent that acts randomly, either buying, selling, or doing nothing."""
    def __init__(self, agent_id: str, wallet: Dict[str, float], trade_probability: float = 0.5):
        super().__init__(agent_id, wallet)
        self.trade_probability = trade_probability

    def step(self, market_state: Dict[str, Any]) -> Dict[str, Any]:
        # Decide whether to trade at all based on the trade_probability
        if random.random() < self.trade_probability:
            # If trading, decide randomly between BUY and SELL
            action_type = random.choice(['BUY', 'SELL'])

            # For simplicity, trade a fixed small amount of ETH for USDC
            amount = 0.1 

            return {
                'action': action_type,
                'asset': 'ETH',
                'amount': amount
            }

        # If not trading, do nothing
        return {}