# evaluate_agent.py

from stable_baselines3 import PPO
from src.market.rl_environment import TradingEnv
from visualize import plot_evaluation_results

print("--- Evaluating Trained Agent ---")

# 1. Setup the evaluation environment (it must be the same as the training env)
initial_wallet = {'ETH': 5, 'USDC': 15000}
initial_prices = {'ETH_USDC': 3000.0}
env = TradingEnv(initial_wallet=initial_wallet, initial_prices=initial_prices)

# 2. Load the trained model
model_path = "models/ppo_trading_agent.zip"
model = PPO.load(model_path, env=env)
print(f"Model loaded from {model_path}")

# 3. Run the evaluation loop
obs, info = env.reset()
price_history = []
portfolio_history = []

for _ in range(200): # Evaluate for 200 steps
    # Use the model to predict the best action
    action, _states = model.predict(obs, deterministic=True)

    # Take the action in the environment
    obs, reward, terminated, truncated, info = env.step(action)

    # Record data for plotting
    price_history.append(env._market.prices['ETH_USDC'])
    portfolio_history.append(env._portfolio_value)

    # If the episode ends, reset it (not likely in our current setup, but good practice)
    if terminated or truncated:
        obs, info = env.reset()

print("--- Evaluation Finished ---")

# 4. Plot the results
plot_evaluation_results(price_history, portfolio_history)