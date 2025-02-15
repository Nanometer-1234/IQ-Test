from tests.level_1 import Level1
from tests.level_2 import Level2
from tests.level_3 import Level3
from scoring import announce
from intro import introduce
import constants

# This file will run the program
total_score = 0
user_name = introduce()

Level_3 = Level3(constants.DEBUG)
if constants.L3:
    the_numbers = Level_3.generate_numbers()

if constants.L1:
    Level_1 = Level1(constants.DEBUG)
    Level_1.play()
    total_score += Level_1.current_score
    print(Level_1.current_score)

if constants.L2:
    Level_2 = Level2(constants.DEBUG)
    Level_2.play()
    total_score += Level_2.current_score
    print(Level_2.current_score)

if constants.L3:
    Level_3.play(the_numbers)
    total_score += Level_3.current_score
    print(Level_3.current_score)

announce(total_score)