"""
house_edge.py

Compute expected value (EV) and house edge for common European roulette bets.
Assumes a single-zero wheel with 37 numbers (0–36) and standard casino payouts.
"""

from dataclasses import dataclass

WHEEL_SIZE = 37  # European wheel: 0–36

@dataclass(frozen=True)
class Bet:
    name: str
    win_count: int
    payout_net: int  # payout “to-1”

def win_probability(win_count):
    return win_count / WHEEL_SIZE

def expected_value(payout_net, p_win):
    p_lose = 1 - p_win
    return payout_net * p_win - 1 * p_lose

def house_edge_percent(ev):
    return -ev * 100

def main():
    bets = [
        Bet("Straight-up (single number)", 1, 35),
        Bet("Split (two numbers)", 2, 17),
        Bet("Street (three numbers)", 3, 11),
        Bet("Corner (four numbers)", 4, 8),
        Bet("Six line (six numbers)", 6, 5),
        Bet("Dozen (12 numbers)", 12, 2),
        Bet("Even-money (18 numbers)", 18, 1),
    ]

    header = f"{'Bet':35}  {'Win prob':>8}  {'Payout':>8}  {'EV/£1':>10}  {'House edge':>11}"
    print(header)
    print("-" * len(header))

    for b in bets:
        p = win_probability(b.win_count)
        ev = expected_value(b.payout_net, p)
        he = house_edge_percent(ev)
        print(f"{b.name:35}  {p:8.5f}  {b.payout_net:8d}  £{ev:>9.4f}  {he:>10.2f}%")

    print("\nNote: All standard European roulette bets have ≈ 2.70% house edge.")

if __name__ == "__main__":
    main()
