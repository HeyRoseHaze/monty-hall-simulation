
def game_parameters() -> int:
    while True:
        try:
            boxes_count = int(input("Choose a number of boxes: ") )
            if boxes_count < 3:
                print("The number of boxes cannot be less than 3.")
            else:
                print(f'Number of boxes: {boxes_count}')
                return boxes_count
        except ValueError:
            print("This is not a number. Enter a number.")

def user_choice(boxes_count: int) -> int:
    while True:
        try:
            choice = int(input(f"Choose a box (1-{boxes_count}): "))
            if 1 <= choice <= boxes_count:
                print(f"Selected: {choice}")
                return choice           
            print(f"You entered {choice}. The number must be in the range 1-{boxes_count}.\nYou need to enter it again.")
                
        except ValueError:
            print(f"This is not a number, Enter a number in the range 1-{boxes_count}")

def get_player_decision() -> str:
    while True:
        decision = input("Are you changing the box? (yes/no) ").strip().lower()
        if decision in ("yes", "no"):
            return decision
        print("Wrong! You have to enter yes/no")
        
