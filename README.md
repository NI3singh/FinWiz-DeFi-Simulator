# Echo: A DeFi Economic Simulator with AI Agents

**Echo** is a high-performance market simulation engine designed to model the complex and emergent behaviors of Decentralized Finance (DeFi) ecosystems. Instead of relying on flawed historical backtesting, this project builds a "digital twin" of a crypto market, populated by intelligent AI agents that learn and execute trading strategies.

This project was developed for the **Mercer | Mettl FinWiz 1.0 Hackathon**.



---

## 🚀 Core Achievement: From Simulation to a Learning AI

The key accomplishment of this project is the end-to-end creation of a sophisticated Reinforcement Learning (RL) agent capable of developing its own trading strategies.

1.  **Custom Simulation Engine:** We built a dynamic market environment from scratch in Python where agent actions (BUY/SELL) directly impact asset prices, creating a realistic feedback loop.
2.  **Intelligent Agent Development:** We progressed from simple random and rule-based (Momentum) agents to a true AI.
3.  **Advanced Reinforcement Learning:** Using the powerful **AMD MI300X GPU**, we successfully trained a **Proximal Policy Optimization (PPO)** agent. This agent was not given any explicit strategy; it learned purely through trial and error, with the goal of maximizing its portfolio value.
4.  **Emergent Strategy:** The trained agent developed a unique, non-obvious, and profitable short-term trading strategy, demonstrating true emergent behavior—a hallmark of a complex adaptive system.

---

## 🛠️ Technology Stack

* **Core Language:** Python 3.12
* **AI & Machine Learning:**
    * **PyTorch (on ROCm):** The foundational deep learning framework, accelerated by the AMD GPU.
    * **Stable-Baselines3:** A high-level library for implementing and training state-of-the-art Reinforcement Learning algorithms.
    * **Gymnasium:** The standard toolkit for building RL environments.
* **Data & Visualization:**
    * **NumPy & Pandas:** For high-performance numerical operations.
    * **Plotly:** For creating interactive data visualizations to analyze simulation results.
* **Compute:**
    * **AMD Instinct MI300X GPU (192 GB VRAM):** The core hardware that made the intensive RL training process feasible.

---

## 🏁 How to Run

This project is structured into modular Python scripts.

### 1. Setup

Clone the repository and install the required dependencies:
```bash
git clone <your-repo-url>
cd Finwiz_project
pip install -r requirements.txt  # (You would create this file)
```

### 2. Check the RL Environment

Verify that the custom trading environment is compatible with the RL libraries.
```bash
python3 check_env.py
```

### 3. Train the AI Agent

Run the training script. This will use the GPU and save the trained model to the `models/` directory.
```bash
python3 train_agent.py
```

### 4. Evaluate the Trained Agent

Load the saved model and run an evaluation simulation. This will generate an interactive chart named `final_evaluation_chart.html`.
```bash
python3 evaluate_agent.py
```
