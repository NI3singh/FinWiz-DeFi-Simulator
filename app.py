# app.py

import streamlit as st
import pandas as pd
import time
from stable_baselines3 import PPO
from src.market.rl_environment import TradingEnv

# --- Page Configuration ---
st.set_page_config(
    page_title="DeFi Agent 'Echo' Simulation",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Header and Introduction ---
st.title("🤖 DeFi Agent 'Echo' - A Reinforcement Learning Simulation")
st.markdown("""
This dashboard showcases 'Echo', an AI agent trained using Reinforcement Learning to trade in a simulated DeFi market.
- **The Agent**: Trained using the PPO algorithm for 20,000 timesteps.
- **The Goal**: To learn a strategy that maximizes its portfolio value.
- **The Chart Below**: Shows the agent's performance over a 200-step evaluation episode.
""")

# --- Display the Final Evaluation Chart ---
st.header("Agent Performance Evaluation")
st.write("This chart shows the ETH price evolution (blue) and the agent's corresponding portfolio value (orange).")
try:
    with open("final_evaluation_chart.html", 'r', encoding='utf-8') as f:
        html_string = f.read()
        st.components.v1.html(html_string, height=500)
except FileNotFoundError:
    st.warning("Please run `evaluate_agent.py` first to generate the final chart.")


# --- Live Demo Section ---
st.header("🚀 Live Simulation Demo")
if st.button("Click to Run Live Demo"):
    # Load the trained model
    model = PPO.load("models/ppo_trading_agent.zip")

    # Setup the environment
    initial_wallet = {'ETH': 5, 'USDC': 15000}
    initial_prices = {'ETH_USDC': 3000.0}
    env = TradingEnv(initial_wallet=initial_wallet, initial_prices=initial_prices)
    obs, info = env.reset()

    st.success("Live demo started! Watch the agent's actions below.")

    # Create placeholders for live updates
    col1, col2, col3 = st.columns(3)
    step_placeholder = col1.empty()
    action_placeholder = col2.empty()
    portfolio_placeholder = col3.empty()
    chart_placeholder = st.empty()

    # Live simulation loop
    price_history = [env._market.prices['ETH_USDC']]

    for i in range(200): # Run for 200 steps
        action, _states = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, info = env.step(action)

        # --- Update the UI in real-time ---
        action_map = {0: "HOLD ✊", 1: "BUY 📈", 2: "SELL 📉"}

        step_placeholder.metric("Simulation Step", f"{i + 1}/200")
        action_placeholder.metric("Agent's Action", action_map[action.item()])
        portfolio_placeholder.metric("Current Portfolio Value", f"${env._portfolio_value:,.2f}")

        # Update the chart
        price_history.append(env._market.prices['ETH_USDC'])
        chart_df = pd.DataFrame(price_history, columns=['ETH Price'])
        chart_placeholder.line_chart(chart_df)

        # Small delay to make the simulation watchable
        time.sleep(0.1)

        if terminated or truncated:
            st.success("Episode finished!")
            break

    st.success("Live demo finished!")