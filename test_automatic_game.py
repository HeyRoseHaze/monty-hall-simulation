import pytest
from automatic_game import parse_args

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