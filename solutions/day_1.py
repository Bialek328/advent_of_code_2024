import pandas as pd
from pathlib import Path
import os

INPUTS_PATH = Path("inputs")

def load_input() -> pd.DataFrame:
    """ Look for input file for the task and load the data into pandas DataFrame """
    input = "{}/{}".format(INPUTS_PATH, "day_1.csv")
    print(f"Searching for: {input}")
    if os.path.exists(input):
        with open(input, "r") as file:
            data = pd.read_csv(file)
            return data
    else:
        raise FileNotFoundError("No input for this task!")

def clean_data(data: pd.DataFrame):
    """ After loading the csv there are semicolons in the data,
    this code removes redundant semicolons and splits the data into two columns as intended """
    data['Table 1'] = data['Table 1'].apply(lambda x: x[1:-4])
    data[['Left', 'Right']] = data['Table 1'].str.split(";", n=1, expand=True)
    clean_data = data.drop('Table 1', axis=1)
    clean_data = clean_data.drop(0, axis=0)
    return clean_data

def quicksort(array, left, right):
    """ Implement quicksort algorithm to sort recieved data """
    if left < right:
        p = _split(array, left, right)
        quicksort(array, left, p - 1)
        quicksort(array, p + 1, right)
    return array

def _split(target, left, right):
    """ Used in quicksort to find where to split the array """
    pivot = target[right]
    i = left
    j = right - 1
    while i < j:
        while i < right and target[i] < pivot:
            i += 1
        while j > left and target[j] >= pivot:
            j -= 1
        if i < j:
            target[i], target[j] = target[j], target[i]
    if target[i] > pivot:
        target[i], target[right] = target[right], target[i]

    return i

if __name__ == "__main__":
    input_data = load_input()
    cleaned_data = clean_data(input_data)
    # ensure value in the columns are int and extract them into list 
    left_list = cleaned_data['Left'].apply(lambda x: int(x)).to_list()
    right_list = cleaned_data['Right'].apply(lambda x: int(x)).to_list()

    # sort the obtained lists
    sorted_left = quicksort(left_list, 0, len(left_list) - 1)
    sorted_right = quicksort(right_list, 0, len(right_list) - 1)

    # calculate difference between elements to find the solution to the riddle
    diffs = []
    for a, b in zip(sorted_left, sorted_right):
        diffs.append(abs(a -b))
    print("Solution:", sum(diffs))

