from .template import LevelTemplate
import random
import time

class Level2(LevelTemplate):
    
    def __init__(self, debug: bool = False):
        super().__init__(debug)
        self.coefficient = 6

    def play(self):
        """
        Introduces and controls the Level
        """

        print(f"Time to test your speed.")
        time.sleep(3)
        print("You will be given arithmetical questions. Answer them correctly to gain points.")
        time.sleep(4)
        print("You have 60 seconds.")

        # 3, 2, 1, GO!
        for i in range(3, 0, -1):
            print(f"Starting in {i} seconds")
            time.sleep(1)
        
        print("GO!")

        start_time = time.time()
        answer_time = 60 if not self.debug else 80

        while time.time() < start_time + answer_time:

            if self.ask_math():
                self.current_score += self.coefficient
        
        print("Time is up!")



    def ask_math(self) -> bool:
        """
        Gives a math question and asks for an answer.
        Then returns whether or not it was the correct answer.

        Output:
            - Returns True if the guess is correct otherwise False
        """
        numb1 = random.randint(11,50)
        numb2 = random.randint(11,50)
        answer = numb1 + numb2
        print(f"What is {numb1} + {numb2}?")
                
        if self.debug:
            print(f"Answer: {answer}")

        user_input = self.get_number()

        is_correct = user_input == answer
        if not is_correct:
            print("Incorrect")
            return False
        
        print("Correct!")
        return True
