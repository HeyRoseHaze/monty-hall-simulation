from logic import box_reject, pick_reward, check_win
import random
import simulation_settings

def simulation_games():
    win_count_yes = 0
    lose_count_yes = 0
    win_count_no = 0
    lose_count_no = 0
    decision = "yes"

    for _ in range(simulation_settings.number):
        reward = pick_reward()
        user_choice = random.randint(1,3)
        win = check_win(reward, user_choice, decision)

        if win:
            win_count_yes += 1
        else:
            lose_count_yes +=1

    decision = "no"

    for _ in range(simulation_settings.number):
        reward = pick_reward()
        user_choice = random.randint(1,3)
        win = check_win(reward, user_choice, decision)

        if win:
            win_count_no += 1
        else:
            lose_count_no += 1

    print(f"Played: {simulation_settings.number}")
    print(f"Results for decision: {decision}")
    print(f"Wins: {win_count_yes}")
    print(f"Losses: {lose_count_yes}")
    print(f"\nResults for decision: {decision}")
    print(f"Wins: {win_count_no}")
    print(f"Losses: {lose_count_no}")


if __name__=="__main__":
    simulation_games()


        