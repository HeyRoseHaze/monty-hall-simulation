import random

def pick_reward(boxes_count: int) -> int:
    return random.randint(1, boxes_count)

def get_alternative_box(boxes_count: int, box_reward: int, user_choice: int) -> int:
    if user_choice == box_reward:
        # the player succeeded on the first try
        available = [i for i in range(1, boxes_count+1) if i !=user_choice]
        return random.choice(available)
    else:
        # The player missed
        return box_reward

def check_win(box_reward: int, user_choice:int, decision: str) -> bool:
    if decision == 'yes':
        return box_reward != user_choice
    return box_reward == user_choice

