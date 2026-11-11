import random
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

suits = ["clubs (♣)", "diamonds (♦)", "hearts (♥)", "spades (♠)"]
ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

suit = random.choice(suits)
rank = random.choice(ranks)
print(f"{rank} of {suit}")
