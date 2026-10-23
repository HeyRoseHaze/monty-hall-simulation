import pytest
from logic import pick_reward, box_reject, check_win


def test_pick_reward():
    for i in range(100):
        reward = pick_reward()
        assert reward in (1, 2, 3)


def test_box_reject():
    for box_reward in (1, 2, 3):
        for user_choice in (1, 2, 3):
            rejected = box_reject(box_reward, user_choice)
            assert rejected in (1, 2, 3)
            assert rejected != box_reward
            assert rejected != user_choice


@pytest.mark.parametrize(
        "box_reward, user_choice, decision, expected",
        [
            (1, 1, "no", True),
            (2, 1, "no", False),

        ]
)


def test_check_win(box_reward, user_choice, decision, expected):
    assert check_win(box_reward, user_choice, decision) is  expected
