import pytest
from automatic_game import parse_args, simulate_strategy, run_simulation

# Tests for argparse

def test_parse_args_default(monkeypatch):
    monkeypatch.setattr("sys.argv", ["automatic_game.py"])
    args = parse_args()

    assert args.games == 10000
    assert args.boxes == 3

def test_parse_args_custom_values(monkeypatch):
    monkeypatch.setattr("sys.argv", ["automatic_game.py", "-g", "500", "-b", "10"])
    args = parse_args()

    assert args.games == 500
    assert args.boxes == 10


# Tests for strategy

def test_strategy_correct_data():
    games = 100
    boxes = 3

    wins, history = simulate_strategy('yes', games, boxes)

    assert len(history) == games 
    assert 0 <= wins <= games

    assert isinstance(wins, int)
    assert isinstance(history, list) 

# Tests for simulation games

def test_simulation_games_invalid_games(capsys):
    run_simulation(0, 3)

    captured = capsys.readouterr()
    assert captured.out == "Error: The number of games must be greater than 0.\n"

def test_simulation_games_invalid_boxes(capsys):
    run_simulation(10, 2)

    captured = capsys.readouterr()
    assert captured.out == "Error: The number of boxes cannot be less than 3.\n"