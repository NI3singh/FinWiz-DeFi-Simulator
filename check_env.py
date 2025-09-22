# check_env.py

from stable_baselines3.common.env_checker import check_env
from src.market.rl_environment import TradingEnv

print("--- Checking Custom Trading Environment ---")

# We need to define the initial state to create an instance of the environment
initial_wallet = {'ETH': 5, 'USDC': 15000}
initial_prices = {'ETH_USDC': 3000.0}

# Create an instance of our custom environment
env = TradingEnv(initial_wallet=initial_wallet, initial_prices=initial_prices)

# The magic happens here!
# check_env will run a series of tests and raise an error if something is wrong.
try:
    check_env(env)
    print("\n✅ Environment check passed! Your custom environment is compatible with Stable-Baselines3.")
except Exception as e:
    print(f"\n❌ Environment check failed: {e}")