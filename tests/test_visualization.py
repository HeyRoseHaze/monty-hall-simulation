import os 
from pathlib import Path
from visualization import plot_results

def test_plot_results_creates_files(tmp_path: Path) -> None:
    switch_history = [50.0, 66.7, 75.0]
    stay_history = [50.0, 33.3, 25.0]

    temp_file = tmp_path / "test_plot.png"

    saved_file = plot_results(
        switch_history, 
        stay_history, 
        boxes_count=3, 
        output_filename=str(temp_file))

    assert saved_file == str(temp_file)
    assert os.path.exists(saved_file)

    