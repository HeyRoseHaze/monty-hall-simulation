import pytest
import random
from logic import pick_reward, get_alternative_box, check_win
from lmd import get_player_decision, user_choice, game_parameters


# Test for logic.py

def test_pick_reward():
    for i in range(100):
        number = random.randint(1, 10**5)
        reward = pick_reward(number)
        assert reward in range(1, number+1)



@pytest.mark.parametrize(
    "box_reward, user_choice, decision, expected",
    [
        (1, 1, "no", True),
        (2, 1, "no", False),
        (1, 1, "yes", False),
        (2, 1, "yes", True),
        (2, 3, "yes", True)
    ]
)
def test_check_win(box_reward, user_choice, decision, expected):
    assert check_win(box_reward, user_choice, decision) is expected


# Tests for lmd.py
# Tests game parameters
def test_game_parameters(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "100")
    assert game_parameters() == 100

def test_game_parameters_series(monkeypatch):
    inputs = iter(["five", "100"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert game_parameters() == 100

# Test user choice
def test_user_choice(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2" )
    assert user_choice(100) == 2

def test_user_choice_series(monkeypatch):
    inputs = iter(["no", "0", "5", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert user_choice(100) == 5

# Test player decision
def test_get_player_decision_uppercase(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "    YES   ")
    assert get_player_decision() == "yes"


def test_get_player_decision_series(monkeypatch):
    inputs = iter(["co", "2", "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_player_decision() == "yes"







