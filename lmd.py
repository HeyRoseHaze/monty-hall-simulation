
def user_choice() -> int:
    while True:
        try:
            choice = int(input("Choose a box (1-3): "))
            if 1 <= choice <= 3:
                print(f"Selected: {choice}")
                return choice           
            print(f"You entered {choice}. The number must be in the range 1-3.\nYou need to enter it again.")
                
        except ValueError:
            print("This is not a number, Enter a number in the range 1-3")

def get_player_decision() -> str:
    while True:
        decision = input("Are you changing the box? (yes/no) ").strip().lower()
        if decision in ("yes", "no"):
            return decision
        print("Wrong! You have to enter yes/no")
        
