import matplotlib.pyplot as plt

def plot_results(
        win_rates_switch: list[float],
        win_rates_stay: list[float],
        boxes_count: int = 3,
        output_filename: str | None = None,
        show_plot: bool = True,
) -> str:
    if not win_rates_switch or not win_rates_stay:
        raise ValueError("The lists containing the results cannot be empty.")

    plt.figure(figsize=(10, 6))
    plt.plot(win_rates_switch, label="Change of selection ('yes')", color="#2ecc71", linewidth=2)
    plt.plot(win_rates_stay, label="Stick with the choice ('no')", color="#e74c3c", linewidth=2)

    expected_stay = (1 / boxes_count) * 100
    expected_switch = ((boxes_count - 1)/ boxes_count) * 100
    plt.axhline(expected_switch, color="#27ae60", linestyle="--", alpha=0.6, label=f"Theory 'yes' ({expected_switch:.1f}%)")
    plt.axhline(expected_stay, color="#c0392b", linestyle="--", alpha=0.6, label=f"Theory 'no' ({expected_stay:.1f}%)")


    plt.title(f"The Monty Hall Paradox - results ({boxes_count} boxes)", fontsize=14)
    plt.xlabel("Number of games played", fontsize=12)
    plt.ylabel("Win percentage (%)", fontsize=12)
    plt.ylim(0, 100)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="center right")
    plt.tight_layout()

    filename = output_filename or f"monty_hall_{boxes_count}_boxes.png"
    plt.savefig(filename, dpi=300)
    plt.close()

    if show_plot:
        pass

    return filename