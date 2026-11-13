import pytest
import random
from logic import pick_reward

def test_pick_reward():
    for _ in range(100):
        number = random.randint(1, 10**5)
        reward = pick_reward(number)
        assert reward in range(1, number+1)