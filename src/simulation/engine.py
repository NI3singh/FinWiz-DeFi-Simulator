# src/simulation/engine.py

from tqdm import tqdm
from typing import List
from src.agents.base_agent import BaseAgent
from src.market.environment import MarketEnvironment

class SimulationEngine:
    """The main engine to run the agent-based simulation."""
    def __init__(self, market: MarketEnvironment, agents: List[BaseAgent]):
        self.market = market
        self.agents = agents
        self.price_history = [] # New: To store price history
        print(f"SimulationEngine initialized with {len(self.agents)} agents.")

    def run(self, num_steps: int):
        """Runs the simulation and tracks price history."""
        print(f"Starting simulation for {num_steps} steps...")

        for step in tqdm(range(num_steps), desc="Simulating Market"):
            # 1. Get market state and record the price
            market_state = self.market.get_market_state()
            self.price_history.append(market_state['prices']['ETH_USDC'])

            # 2. Let each agent act
            for agent in self.agents:
                action = agent.step(market_state)
                self.market.execute_trade(agent.agent_id, action)

        print("Simulation finished.")
        # New: Print the final price
        final_price = self.price_history[-1]
        print(f"Initial ETH Price: {self.price_history[0]:.2f} USDC")
        print(f"Final ETH Price:   {final_price:.2f} USDC")