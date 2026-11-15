import pytest
from automatic_game import parse_args, simulation_games

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


# Test for simulation games

def test_simulation_games_invalid_games(capsys):
    simulation_games(0, 3)

    captured = capsys.readouterr()
    assert captured.out == "Error: The number of games must be greater than 0.\n"

def test_simulation_games_invalid_boxes(capsys):
    simulation_games(10, 2)

    captured = capsys.readouterr()
    assert captured.out == "Error: The number of boxes cannot be less than 3.\n"