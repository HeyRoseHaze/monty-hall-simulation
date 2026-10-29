from logic import box_reject, pick_reward, check_win
import random
import simulation_settings

def simulation_games():
    win_count = 0
    lose_count = 0
    decision = simulation_settings.decision

    for _ in range(simulation_settings.number):
        reward = pick_reward()
        user_choice = random.randint(1,3)
        win = check_win(reward, user_choice, decision)

        if win:
            win_count += 1
        else:
            lose_count +=1

    print(f"Played: {simulation_settings.number}")
    print(f"Decision: {simulation_settings.decision}")
    print(f"Wins: {win_count}")
    print(f"Losses: {lose_count}")


if __name__=="__main__":
    simulation_games()


        