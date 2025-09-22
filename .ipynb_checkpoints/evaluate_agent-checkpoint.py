# evaluate_agent.py

from stable_baselines3 import PPO
from src.market.rl_environment import TradingEnv
from visualize import plot_evaluation_results

print("--- Evaluating Trained Agent for Final Demo ---")

# 1. Setup the evaluation environment
initial_wallet = {'ETH': 5, 'USDC': 15000}
initial_prices = {'ETH_USDC': 3000.0}
env = TradingEnv(initial_wallet=initial_wallet, initial_prices=initial_prices)

# 2. Load the trained model
model_path = "models/ppo_trading_agent.zip"
model = PPO.load(model_path, env=env)
print(f"Model loaded from {model_path}")

# 3. Run a single, clean episode for the demo
obs, info = env.reset()
price_history = [env._market.prices['ETH_USDC']]
portfolio_history = [env._portfolio_value]

# Set max steps for the episode
max_steps = 200
for i in range(max_steps):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)

    price_history.append(env._market.prices['ETH_USDC'])
    portfolio_history.append(env._portfolio_value)

    # Stop if the episode is over
    if terminated or truncated:
        print(f"Episode finished after {i+1} steps.")
        break

print("--- Evaluation Finished ---")

# 4. Plot the results
plot_evaluation_results(price_history, portfolio_history, filename="final_evaluation_chart.html")