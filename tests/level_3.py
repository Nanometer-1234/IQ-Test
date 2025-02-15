from .template import LevelTemplate
import random
import time

class Level3(LevelTemplate):

    def __init__(self, debug: bool = False):
        super().__init__(debug)
        self.coefficient = 25

    def play(self, numbers):
        """
        Logic for Level 3
        """
        print("Time to test your memory.")
        time.sleep(3)
        print("Now you will have to recall the numbers you saw at the beginning.")

        for i in range(0, len(numbers)):

            current_number = numbers[i]
            
            print(f"Please guess number {i + 1}")
            if self.debug:
                print(f"Number {i + 1} is {current_number}")
            
            guess = self.get_number()

            if current_number == guess:
                self.current_score += self.coefficient
                print("You guessed correctly!")
            else:
                print("Incorrect guess...")


    
    def generate_numbers(self, n: int = 5) -> list[int]:
        """
        Gives the user random numbers to memorize

        Parameters:
            - n - how many numbers the user should memorize
        """
        numbers = [random.randint(100, 999) for i in range(n)]
        
        print("To start, I will give you five three digit numbers.")
        time.sleep(3)
        print("You will have ten seconds to memorize them.")
        time.sleep(3)
        print("For every number you remember at the end, you will receive points.")
        time.sleep(4)
        print("The numbers are. . .")
        time.sleep(3)
        print(numbers)
        time.sleep(10)
        self.clear_terminal_window()
        print("Done!!!\n")
        time.sleep(3)

        if self.debug:
            print(f"Numbers:\t{numbers}")

        return numbers