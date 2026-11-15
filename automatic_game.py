from logic import pick_reward, check_win
import random
import argparse

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
   return parser.parse_args()
   
def strategy(decision: str, games_count: int, boxes_count: int)  -> int:
    wins = 0
    for _ in range(games_count):
        reward = pick_reward(boxes_count)
        user_choice = random.randint(1, boxes_count)
        if check_win(reward, user_choice, decision):
            wins +=1
    return wins

def simulation_games(games_count: int, boxes_count: int) -> None:
   if games_count <= 0:
      print("Error: The number of games must be greater than 0.")
      return
   if boxes_count < 3:
      print("Error: The number of boxes cannot be less than 3.")
      return

   print(f"Number of boxes in the game: {boxes_count}")
   for decision in ("yes", "no"):
    wins = strategy(decision, games_count, boxes_count)
    losses = games_count - wins
    win_rate = (wins / games_count) * 100

    
    print(f"\nResults for decision: '{decision}' (Played: {games_count})")
    print(f"Wins: {wins} ({win_rate:.2f}%)")
    print(f"Losses: {losses}")


if __name__=="__main__":
    args = parse_args()
    simulation_games(args.games, args.boxes)


        