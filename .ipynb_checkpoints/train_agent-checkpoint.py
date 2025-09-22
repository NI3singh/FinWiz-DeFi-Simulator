# train_agent.py

import torch
from stable_baselines3 import PPO
from src.market.rl_environment import TradingEnv

print("--- Starting RL Agent Training ---")

# 1. Setup the Environment
initial_wallet = {'ETH': 5, 'USDC': 15000}
initial_prices = {'ETH_USDC': 3000.0}
env = TradingEnv(initial_wallet=initial_wallet, initial_prices=initial_prices)

# 2. Set the Device (Crucial for using the MI300X!)
# We use "cuda" as the device name because ROCm uses PyTorch's CUDA interface.
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")
if device == "cuda":
    print(f"Device name: {torch.cuda.get_device_name(0)}")

# 3. Instantiate the PPO Agent
# We pass our environment and tell the model to use the GPU.
# The "MlpPolicy" is a standard neural network policy.
model = PPO(
    "MlpPolicy",
    env,
    verbose=1,  # This will print training progress
    device=device
)

# 4. Train the Agent
# The agent will run simulations for 20,000 "timesteps" to learn.
# This is where the GPU will be heavily used.
print("\n--- Training started ---")
model.learn(total_timesteps=20000)
print("--- Training finished ---")

# 5. Save the Trained Model
model_path = "models/ppo_trading_agent.zip"
model.save(model_path)
print(f"Trained model saved to {model_path}")