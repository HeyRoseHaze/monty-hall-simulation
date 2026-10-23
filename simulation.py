from lmd import user_choice, get_player_decision
from logic import box_reject, pick_reward, check_win

def run_game():
    win_count = 0
    lose_count = 0

    while True:
        reward = pick_reward()
        choice = user_choice()

        rejected = box_reject(reward, choice)
        print(f"Box {rejected} is empty.")

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