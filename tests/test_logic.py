import pytest
import random
from logic import pick_reward, get_alternative_box, check_win

def test_pick_reward():
    # check whether the reward is in the range (1, boxes_count)
    for _ in range(100):
        number = random.randint(1, 10**5)
        reward = pick_reward(number)
        assert reward in range(1, number+1)


def test_get_alternative_box():
    for boxes_count in range(3, 16):
        for box_reward in range(1, boxes_count+1):
            for user_choice in range(1, boxes_count+1):
                alternative = get_alternative_box(boxes_count, box_reward, user_choice)

                assert alternative != user_choice
                assert  1 <= alternative <= boxes_count+1

                
                if user_choice != box_reward:
                    assert alternative == box_reward

@pytest.mark.parametrize(
    "box_reward, user_choice, decision, expected",
    [
        (1, 1, "no", True),
        (2, 1, "no", False),
        (1, 1, "yes", False),
        (2, 1, "yes", True),
        (2, 3, "yes", True),
        (100, 50, "no", False),
        (100, 50, "yes", True)
    ]
)
def test_check_win(box_reward, user_choice, decision, expected):
    assert check_win(box_reward, user_choice, decision) is expected