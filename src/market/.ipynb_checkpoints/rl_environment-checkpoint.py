# src/market/rl_environment.py

import gymnasium as gym
from gymnasium import spaces
import numpy as np
from typing import Dict

from src.market.environment import MarketEnvironment

class TradingEnv(gym.Env):
    """
    A custom Gymnasium environment for our trading simulation.
    This acts as a wrapper around our MarketEnvironment to make it
    compatible with Stable-Baselines3.
    """
    def __init__(self, initial_wallet: Dict[str, float], initial_prices: Dict[str, float]):
        super(TradingEnv, self).__init__()

        # Store initial state for resets
        self.initial_wallet = initial_wallet
        self.initial_prices = initial_prices
        
        # Internal state
        self._market = MarketEnvironment(initial_prices.copy())
        self._wallet = initial_wallet.copy()
        self._portfolio_value = 0
        
        # 1. Define the Action Space
        # The agent can choose one of 3 discrete actions:
        # 0: HOLD, 1: BUY, 2: SELL
        self.action_space = spaces.Discrete(3)

        # 2. Define the Observation Space
        # What the agent sees at each step. We'll give it 3 pieces of info:
        # - Current ETH Price
        # - Amount of ETH in wallet
        # - Amount of USDC in wallet
        self.observation_space = spaces.Box(
            low=0, high=np.inf, shape=(3,), dtype=np.float32
        )

    def _get_observation(self):
        """Constructs the observation array from the current state."""
        obs = np.array([
            self._market.prices['ETH_USDC'],
            self._wallet['ETH'],
            self._wallet['USDC']
        ], dtype=np.float32)
        return obs

    def _calculate_portfolio_value(self):
        """Calculates the total value of the agent's assets."""
        return (self._wallet['ETH'] * self._market.prices['ETH_USDC']) + self._wallet['USDC']

    def reset(self, seed=None):
        """Resets the environment to its initial state for a new episode."""
        super().reset(seed=seed)
        
        self._market = MarketEnvironment(self.initial_prices.copy())
        self._wallet = self.initial_wallet.copy()
        self._portfolio_value = self._calculate_portfolio_value()
        
        info = {} # info dict, required by Gymnasium
        return self._get_observation(), info

    def step(self, action):
        """Executes one time step within the environment."""
        # Map the discrete action (0, 1, 2) to a trade action
        trade_action = {}
        if action == 1: # BUY
            # Simple logic: use 10% of USDC to buy ETH
            usdc_to_spend = self._wallet['USDC'] * 0.1
            eth_to_buy = usdc_to_spend / self._market.prices['ETH_USDC']
            self._wallet['USDC'] -= usdc_to_spend
            self._wallet['ETH'] += eth_to_buy
            trade_action = {'action': 'BUY', 'asset': 'ETH', 'amount': eth_to_buy}
        elif action == 2: # SELL
            # Simple logic: sell 10% of ETH
            eth_to_sell = self._wallet['ETH'] * 0.1
            usdc_gained = eth_to_sell * self._market.prices['ETH_USDC']
            self._wallet['ETH'] -= eth_to_sell
            self._wallet['USDC'] += usdc_gained
            trade_action = {'action': 'SELL', 'asset': 'ETH', 'amount': eth_to_sell}
        
        # Execute the trade in the underlying market to trigger price impact
        if trade_action:
            self._market.execute_trade("rl_agent", trade_action)

        # Calculate reward
        new_portfolio_value = self._calculate_portfolio_value()
        reward = new_portfolio_value - self._portfolio_value
        self._portfolio_value = new_portfolio_value

        # For this simple case, we'll say an episode never 'terminates' on its own
        terminated = False
        # And it's not 'truncated' (cut short)
        truncated = False
        
        info = {}
        
        return self._get_observation(), reward, terminated, truncated, info