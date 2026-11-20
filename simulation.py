from cli import user_choice, get_player_decision, game_parameters
from logic import get_alternative_box, pick_reward, check_win

def run_game() -> None:
    win_count = 0
    lose_count = 0

    while True:
        boxes_count = game_parameters()

        reward = pick_reward(boxes_count)
        choice = user_choice(boxes_count)

        alternative_box = get_alternative_box(boxes_count, reward, choice)
        print(f"You can change to box number {alternative_box} .")

        decision = get_player_decision()
        win = check_win(reward, choice, decision)

        if win:
            win_count +=1
            print("You win!")
        else:
            lose_count +=1
            print(f"You lose. Reward was in box {reward}")

        print(f"Wins: {win_count}\nLosses: {lose_count}\n")

        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            break

if __name__ == "__main__":
    run_game()