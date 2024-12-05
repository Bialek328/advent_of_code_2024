from pathlib import Path
import os
import pandas as pd

INPUTS_PATH = Path("inputs")

def load_input(day: int) -> pd.DataFrame:
    """ Look for input file for the task and load the data into pandas DataFrame """
    input = "{}/{}".format(INPUTS_PATH, f"day_{day}.csv")
    print(f"Searching for: {input}")
    if os.path.exists(input):
        with open(input, "r") as file:
            data = pd.read_csv(file)
            return data
    else:
        raise FileNotFoundError("No input for this task!")
