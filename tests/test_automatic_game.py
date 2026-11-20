import pytest
from automatic_game import parse_args, simulate_strategy, run_simulation
from unittest.mock import MagicMock, patch

#dodac type - mypy 

# testy plot


# Tests for argparse

def test_parse_args_default(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("sys.argv", ["automatic_game.py"])
    args = parse_args()

    assert args.games == 10000
    assert args.boxes == 3
    assert args.plot == False

def test_parse_args_custom_values(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("sys.argv", ["automatic_game.py", "-g", "500", "-b", "10", "--plot"])
    args = parse_args()

    assert args.games == 500
    assert args.boxes == 10
    assert args.plot == True


# Tests for simulate strategy

def test_simulate_strategy_correct_data() -> None:
    games = 100
    boxes = 3

    wins, history = simulate_strategy('yes', games, boxes)

    assert len(history) == games 
    assert 0 <= wins <= games
    assert isinstance(wins, int)
    assert isinstance(history, list) 
    assert history[-1] == pytest.approx((wins/games) * 100)

# Tests for run simulation

def test_run_simulation_invalid_games(capsys: pytest.CaptureFixture[str]) -> None:
    run_simulation(0, 3)

    captured = capsys.readouterr()
    assert captured.out == "Error: The number of games must be greater than 0.\n"

def test_run_simulation_invalid_boxes(capsys: pytest.CaptureFixture[str]) -> None:
    run_simulation(10, 2)

    captured = capsys.readouterr()
    assert captured.out == "Error: The number of boxes cannot be less than 3.\n"

@patch("automatic_game.plot_results")
def test_run_simulation_with_plot(
    mock_plot_results: MagicMock,
    capsys: pytest.CaptureFixture[str],
) -> None:
    mock_plot_results.return_value = "test_plot.png"

    run_simulation(10, 3, plot=True)

    mock_plot_results.assert_called_once()
    captured = capsys.readouterr()
    assert "Plot saved to: test_plot.png" in captured.out


@patch("automatic_game.plot_results")
def test_run_simulation_without_plot(mock_plot_results: MagicMock) -> None:
    run_simulation(10, 3, plot=False)

    mock_plot_results.assert_not_called()