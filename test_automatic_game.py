import pytest
from automatic_game import parse_args

def test_parse_args(monkeypatch):
    monkeypatch.setattr("sys.argv", ["automatic_game.py"])
    args = parse_args()

    assert args.games == 10000
    assert args.boxes == 3