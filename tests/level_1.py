from .template import LevelTemplate
import random
import time

class Level1(LevelTemplate):

    def __init__(self, debug: bool = False):
        super().__init__(debug)
        self.coefficient = 150

    def play(self):
        """
        Logic for level 1

        Uses the guess_logic function to run level 1.

        """
        print("Time to test your strategy;")
        time.sleep(3)
        print("We will be doing number guessing.\n")
        time.sleep(3)

        total = 3
        total_tries = 0

        for i in range(0, total):
            total_tries += self.guess_logic()

        self.current_score = (total / total_tries) * self.coefficient

    def guess_logic(self) -> int:
        """
        Implementation of a single guesss

        Ask the user for a number. If the number is incorrect
        then they will get a hint if they should guess a higher
        or a lower number.

        Output:
            - the total number of tries
        """

        correct = random.randint(1, 100)
        try_count = 0

        if self.debug:
            print(f"Correct number: {correct}")
        
        print("There is a number that is between 1 and 100. Try to guess it!")

        while True:
            
            if self.debug:
                print(f"Current try: {try_count+1}")
            
            answer = self.get_number()
            try_count += 1

            if answer == correct:
                print(f"Congrats! The right answer was {correct}. It took you {try_count} guesses.")
                print()
                break

            elif answer < correct:
                print("Wrong. Guess higher.")
            
            elif answer > correct:
                print("Wrong. Guess lower.")
        
        return try_count