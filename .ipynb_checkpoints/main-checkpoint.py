# main.py

from src.market.environment import MarketEnvironment
from src.agents.simple_agents import RandomAgent
from src.agents.strategy_agents import MomentumAgent
from src.simulation.engine import SimulationEngine
from visualize import plot_price_history # <-- IMPORT OUR NEW FUNCTION

if __name__ == "__main__":
    print("--- Setting up DeFi Simulation ---")

    market = MarketEnvironment(initial_prices={'ETH_USDC': 3000.0}, price_impact_factor=50)

    agents = [
        RandomAgent(agent_id="random_1", wallet={'ETH': 5, 'USDC': 15000}),
        MomentumAgent(agent_id="momentum_1", wallet={'ETH': 5, 'USDC': 15000})
    ]

    simulation = SimulationEngine(market=market, agents=agents)

    # Run the simulation
    simulation.run(num_steps=100)

    # --- NEW: VISUALIZE THE RESULTS ---
    # After the simulation is done, get the price history and plot it.
    price_history = simulation.price_history
    plot_price_history(price_history)

    print("--- Simulation Complete ---")