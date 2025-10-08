# Gambling Analysis (Python & R)

Statistical exploration of the mathematics behind gambling — combining Python and R to model house edge, simulate random betting outcomes, and analyse theoretical distributions of returns.  
Developed as part of a 2024 research project at IDAD, blending quantitative modelling and probability theory.

---

## 🎯 Overview
This repository investigates:
- The **house edge** of European roulette using probability-weighted expected value models.
- The **distribution of returns** from 100 £1 bets using both theoretical and Monte Carlo simulation.
- **Random walk modelling** to illustrate long-run player losses and operator profitability.
- Comparisons between simulated and theoretical outcomes using visualisation and summary statistics.

---

## 🧮 Key Files
| File | Language | Description |
|------|-----------|-------------|
| `house_edge.py` | Python | Calculates expected value (EV) and house edge for various roulette bets |
| `roulette_simulation.R` | R | Simulates 100 £1 bets × 10,000 runs and compares to theoretical mean |
| `monte_carlo_sim.py` | Python | Monte Carlo simulation that generates and saves a histogram of returns |

---

## 📊 Example Output
After running `monte_carlo_sim.py`, a histogram of returns is saved automatically:
