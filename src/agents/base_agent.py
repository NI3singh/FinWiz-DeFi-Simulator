# src/agents/base_agent.py

from typing import Dict, Any

class BaseAgent:
    """
    A base class for all trading agents in the simulation.
    This defines the essential properties and methods every agent must have.
    """
    def __init__(self, agent_id: str, wallet: Dict[str, float]):
        """
        Initializes a new agent.

        Args:
            agent_id (str): A unique identifier for the agent.
            wallet (Dict[str, float]): The agent's initial holdings of different assets.
                                       Example: {'ETH': 10.0, 'USDC': 50000.0}
        """
        self.agent_id = agent_id
        self.wallet = wallet

    def step(self, market_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        The core decision-making function of the agent.
        This method will be called at each step of the simulation.

        Args:
            market_state (Dict[str, Any]): The current state of the market,
                                            provided by the MarketEnvironment.

        Returns:
            Dict[str, Any]: An action dictionary. For now, we'll return an empty
                            action, but this will later be {'action': 'BUY', ...}
        """
        # Base agent does nothing by default. Subclasses will override this.
        print(f"Agent {self.agent_id} is observing the market.")
        return {} # Return an empty action

    def __repr__(self) -> str:
        """
        A string representation of the agent for easy debugging.
        """
        return f"Agent(id={self.agent_id}, wallet={self.wallet})"