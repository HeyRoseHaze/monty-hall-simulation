from logic import pick_reward, check_win
import random
import argparse
from visualization import plot_results

def parse_args() -> argparse.Namespace:
   parser = argparse.ArgumentParser(
      description="Monty Hall paradox simulator"
   )
   parser.add_argument(
    "-g", "--games",
    type=int,
    default=10000,
    help="Number of games to simulate for each strategy (default: 10000)"    
   )
   parser.add_argument(
    "-b", "--boxes",
    type=int,
    default=3,
    help="Number of boxes (default: 3)"
   )
   parser.add_argument(
      "--plot",
      action="store_true",
      help="Generate and save a plot as a PNG file"
   )
   return parser.parse_args()
   
def strategy(decision: str, games_count: int, boxes_count: int)  -> tuple[int, list[float]]:
    wins = 0
    history: list[float] = []

    for game in range(1, games_count + 1):
        reward = pick_reward(boxes_count)
        user_choice = random.randint(1, boxes_count)
        if check_win(reward, user_choice, decision):
            wins +=1
        history.append((wins / game) * 100) 
    return wins, history

def simulation_games(games_count: int, boxes_count: int, plot: bool = False) -> None:
   if games_count <= 0:
      print("Error: The number of games must be greater than 0.")
      return
   if boxes_count < 3:
      print("Error: The number of boxes cannot be less than 3.")
      return

   print(f"Number of boxes in the game: {boxes_count}")
   histories: dict[str, list[float]] = {}

   for decision in ("yes", "no"):
      wins, history = strategy(decision, games_count, boxes_count)
      histories[decision] = history

      losses = games_count - wins
      win_rate = (wins / games_count) * 100

    
      print(f"\nResults for decision: '{decision}' (Played: {games_count})")
      print(f"Wins: {wins} ({win_rate:.2f}%)")
      print(f"Losses: {losses}")

   if plot:
      saved_file = plot_results(
         win_rates_switch=histories["yes"],
         win_rates_stay=histories["no"],
         boxes_count=boxes_count,
      )
      print(f"\nPlot saved to: {saved_file}")


if __name__=="__main__":
    args = parse_args()
    simulation_games(args.games, args.boxes, plot=args.plot)


        