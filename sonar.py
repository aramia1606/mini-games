import random
import math

INSTRUCTIONS = """Instructions:
You are the captain of the Simon, a treasure-hunting ship. Your mission is to find three sunken treasure chests using sonar devices. Your sonar only detects distance, not direction.

Enter the coordinates to drop a sonar device. The ocean map will show how far the nearest chest is or an 'X' if it's beyond range.

For example, the 'C' marks the chests:
                     1         2         3
           012345678901234567890123456789012
         0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
         1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
         2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
         3 ````````~~~`````~~~`~`````~`~``~` 3
         4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4
           012345678901234567890123456789012
                     1         2         3

Press Enter to continue..."""

class Table:
    def __init__(self, chests, sonar, sonar_left, chests_left):
        self.chests = chests
        self.sonar = sonar
        self.sonar_left = sonar_left
        self.chests_left = chests_left

TENS = "".join(" " * 9 + str(i + 1) for i in range(5))
UNITS = "".join(str(i) for _ in range(6) for i in range(10))

def get_distance_to_chest(x, y):
    return str(min(round(math.sqrt((x - cx) ** 2 + (y - cy) ** 2)) for cx, cy in current_table.chests))

def print_table(table):
    sonar_positions = set(table.sonar)
    print(" " * 4, TENS)
    print(" " * 3, UNITS)
    
    for y in range(15):
        row_display = f"{y:2} "
        skip = 0
        for x in range(60):
            if (x, y) in sonar_positions:
                distance = get_distance_to_chest(x, y)
                row_display += distance if int(distance) > 0 else "X"
                skip = 1 if int(distance) > 9 else 0
            else:
                row_display += random.choice("~`") if skip == 0 else ""
                skip = max(skip - 1, 0)
        print(row_display, y)
    
    print(" " * 3, UNITS)
    print(" " * 4, TENS)

def print_state():
    print(f"You have {current_table.sonar_left} sonar device(s) left. {current_table.chests_left} treasure chest(s) remaining.")
    print("Where do you want to drop the next sonar device? (0-59 0-14) (or type 'quit')")

def is_input_valid(user_input):
    user_input = user_input.strip()
    if user_input.lower() == "quit":
        return "quit"
    try:
        x, y = map(int, user_input.split())
        return (x, y) if 0 <= x < 60 and 0 <= y < 15 else None
    except ValueError:
        return None

def add_to_sonar(position):
    current_table.sonar.append(position)
    current_table.sonar_left -= 1
    if position in current_table.chests:
        current_table.chests_left -= 1
        print("You found a chest!")
    else:
        print(f"Treasure detected at a distance of {get_distance_to_chest(*position)} from the sonar device.")

def check_game_status():
    if current_table.chests_left == 0:
        print("IT'S A WIN!")
        return True
    if current_table.sonar_left == 0:
        print("We've run out of sonar devices! Game over.")
        print("The remaining chests were at:", " ".join(map(str, (c for c in current_table.chests if c not in current_table.sonar))))
        return True
    return False

# Main game loop
is_playing = True
while is_playing:
    print("S O N A R !\n")
    
    while True:
        try:
            nb_chests = int(input("How many chests do you want to find?\n"))
            if nb_chests > 0:
                break
        except ValueError:
            pass
        print("Invalid input. Please enter a positive integer.")
    
    current_table = Table(
        chests=[(random.randint(0, 59), random.randint(0, 14)) for _ in range(nb_chests)],
        sonar=[],
        sonar_left=15,
        chests_left=nb_chests
    )
    
    if input("Would you like to view the instructions? (Y/N)\n").strip().upper() == "Y":
        input(INSTRUCTIONS)
    
    while is_playing:
        print_table(current_table)
        print_state()
        
        while True:
            user_input = input().strip()
            valid_input = is_input_valid(user_input)
            if valid_input == "quit":
                is_playing = False
                break
            elif valid_input:
                add_to_sonar(valid_input)
                break
            print("Invalid input. Try again.")
        
            break
    
    if input("Do you want to play again? (Y/N)\n").strip().upper() != "Y":
        is_playing = False
        print("Thanks for playing! See you next time.")
