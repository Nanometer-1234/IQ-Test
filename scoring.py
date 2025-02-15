import time

def announce(scored: float):
    """
    Docstrings
    """
    print("Your IQ Test is now done.")
    time.sleep(3)
    print("You scored. . . ")
    time.sleep(3)

    scored = round(scored)

    if scored < 30:
        print(f"{scored}. Oh, wow! You are very stupid.")
            
    elif scored < 60:
        print(f"{scored}. Man! You are dumb!")
            
    elif scored < 113:
        print(f"{scored}. You are ok I guess.")

    elif scored < 125:
        print(f"{scored}! Congrats! You are actually not bad!")
    
    elif scored < 150:
        print(f"{scored}!!! Congratulations! You are very smart!")
        
    elif scored < 200:
        print(f"{scored}!!! Congratulations! You are a genius!")
    
    else:
        print(f"{scored}!!! Ok, let's get things straight. Are you a human or an AI supercomputer?")
    