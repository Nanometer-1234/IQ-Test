import os

class LevelTemplate:

    def __init__(self, debug: bool = False):
        
        self.current_score = 0
        self.debug = debug

        mode = "debug" if self.debug else "prod"
        #print(f"Current mode is: {mode}")

    def get_number(self) -> int:
        """
        Get the user's input and validate it.
        If the user does not enter a number, they
        will be asked to try again.

        Output:
            - A valid integer
        """
        number = None
        while True:

            try:
                user_input = input("Enter a number: ")
                number = int(user_input)
                break
            except Exception as e:
                print(f"Please try again!\nError message: {e}\n")
                
        return number
    

    def clear_terminal_window(self):
        """
        This function clears the terminal.
        """
        os.system("cls")



    def play(self):
        """
        This function must be implemmented by a level
        """
        raise Exception("Please implement logic in the function...")
