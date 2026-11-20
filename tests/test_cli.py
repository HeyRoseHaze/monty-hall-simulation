import pytest
from cli import get_player_decision, user_choice, game_parameters

# Tests game parameters
def test_game_parameters(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "100")
    assert game_parameters() == 100

def test_game_parameters_series(monkeypatch: pytest.MonkeyPatch) -> None:
    inputs = iter(["five", "100"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert game_parameters() == 100

# Test user choice
def test_user_choice(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "2" )
    assert user_choice(100) == 2

def test_user_choice_series(monkeypatch: pytest.MonkeyPatch) -> None:
    inputs = iter(["no", "0", "5", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert user_choice(100) == 5

# Test player decision
def test_get_player_decision_uppercase(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "    YES   ")
    assert get_player_decision() == "yes"


def test_get_player_decision_series(monkeypatch: pytest.MonkeyPatch) -> None:
    inputs = iter(["co", "2", "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_player_decision() == "yes"







