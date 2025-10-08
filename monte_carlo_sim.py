"""
monte_carlo_sim.py

Monte Carlo simulation of European roulette betting sessions.
Generates multiple simulated sessions and plots the distribution
of total returns for 100 £1 bets.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# --- Parameters ---
bets_per_session = 100
sessions = 10000
wheel_size = 37

def simulate_session(bets: int) -> float:
    """Simulate one session of roulette: +35 for win, -1 for loss."""
    outcomes = np.random.choice([35, -1], size=bets, p=[1/wheel_size, 36/wheel_size])
    return np.sum(outcomes)

# --- Run simulation ---
results = np.array([simulate_session(bets_per_session) for _ in range(sessions)])

# --- Summary stats ---
mean_return = np.mean(results)
std_return = np.std(results)
expected_ev = bets_per_session * ((35*(1/wheel_size)) - (36/wheel_size))

print(f"Simulated mean result: £{mean_return:.2f}")
print(f"Theoretical expected result: £{expected_ev:.2f}")
print(f"Standard deviation: £{std_return:.2f}")

# --- Plot histogram ---
plt.figure(figsize=(8,5))
plt.hist(results, bins=40, color='skyblue', edgecolor='white')
plt.axvline(expected_ev, color='red', linestyle='--', linewidth=2, label='Theoretical mean')
plt.title("Distribution of Returns - 100 £1 Roulette Bets")
plt.xlabel("Net Return (£)")
plt.ylabel("Frequency")
plt.legend()

# --- Save plot ---
os.makedirs("images", exist_ok=True)
output_path = os.path.join("images", "roulette_distribution.png")
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.close()

print(f"\nHistogram saved to: {output_path}")
