import random

def pick_reward() -> int:
    return random.randint(1,3)

def box_reject(box_reward: int, user_choice: int) -> int:
    available = [i for i in (1, 2, 3) if i != box_reward and i != user_choice]
    print(available)
    return random.choice(available)

def final(box_reward, user_choice, decision):
    if decision == "no":
        if box_reward == user_choice:
            print("You win")
            return True
        else: 
            print(f"You lose. Reward was in the box {box_reward}")
            return False
    if decision == "yes":
        if box_reward == user_choice:
            print(f"You lose. Reward was in the box {box_reward}")
            return False
        else: 
            print("You win")
            return True
