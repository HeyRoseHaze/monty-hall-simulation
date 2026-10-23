import pytest
from logic import pick_reward


def test_pick_reward():
    for i in range(100):
        reward = pick_reward()
        assert reward in (1, 2, 3)

    