#Global constant
STEP = 1

def ask_number(question, low, high, step):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response

