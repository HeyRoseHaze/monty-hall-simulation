import pytest
from logic import pick_reward, box_reject, check_win
from lmd import get_player_decision, user_choice


# Test for logic.py

def test_pick_reward():
    for i in range(100):
        reward = pick_reward()
        assert reward in (1, 2, 3)


def test_box_reject():
    for box_reward in (1, 2, 3):
        for user_choice in (1, 2, 3):
            rejected = box_reject(box_reward, user_choice)
            assert rejected in (1, 2, 3)
            assert rejected != box_reward
            assert rejected != user_choice


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

def test_user_choice(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2" )
    assert user_choice() == 2


def test_user_choice_series(monkeypatch):
    inputs = iter(["no", "0", "5", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert user_choice() == 3


def test_get_player_decision_uppercase(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "    YES   ")
    assert get_player_decision() == "yes"


def test_get_player_decision_series(monkeypatch):
    inputs = iter(["co", "2", "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_player_decision() == "yes"







