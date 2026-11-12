from logic import pick_reward, check_win
import random
import simulation_settings

def strategy(decision: str, games_count: int)  -> int:
    wins = 0
    for _ in range(games_count):
        reward = pick_reward()
        user_choice = random.randint(1,3)
        if check_win(reward, user_choice, decision):
            wins +=1
    return wins

def simulation_games():
   total = simulation_settings.number

   for decision in ("yes", "no"):
    wins = strategy(decision, total)
    losses = total - wins
    win_rate = (wins / total) * 100

    print(f"\nResults for decision: '{decision}' (Played: {total})")
    print(f"Wins: {wins} ({win_rate:.2f}%)")
    print(f"Losses: {losses}")


if __name__=="__main__":
    simulation_games()


        