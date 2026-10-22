import random

def pick_reward() -> int:
    return random.randint(1,3)

def box_reject(box_reward: int, user_choice: int) -> int:
    available = [i for i in (1, 2, 3) if i != box_reward and i != user_choice]
    return random.choice(available)


def check_win(box_reward: int, user_choice:int, decision: str) -> bool:
    if decision == 'yes':
        return box_reward != user_choice
    return box_reward == user_choice


