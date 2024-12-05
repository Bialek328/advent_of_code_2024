from utils import load_input

import pandas as pd

def clean_data(data: pd.DataFrame):
    cleaned = data["Table 1"].apply(lambda x: x[:-1].split(" "))
    cleaned = cleaned.apply(lambda x: [int(val) for val in x])
    print(cleaned)
    return cleaned
   
def check_first_condition(input: list) -> bool:
    """ List must be either descending or ascending """
    res1 = check_descending(input)
    res2 = check_ascending(input)
    return res1 or res2

def check_second_condition(input: list) -> bool:
    res = False
    for i in range(len(input)):
        if i + 1 >= len(input):
            break
        if 1 <= abs(input[i] - input[i + 1]) <=3:
            res = True
        else:
            return False
    return res

def check_descending(input: list) -> bool:
    res = False
    for i in range(len(input)):
        if i + 1 >= len(input):
            break
        if input[i] > input[i + 1]:
            res = True
        else:
            return False
    return res

def check_ascending(input: list) -> bool:
    res = False
    for i in range(len(input)):
        if i + 1 >= len(input):
            break
        if input[i] < input[i + 1]:
            res = True
        else:
            return False
    return res

if __name__ == "__main__":
    data = load_input(2)
    cleaned_data = clean_data(data)
    data_list = cleaned_data.tolist()

    # Solution Part 1
    counter = 0
    for line in data_list:
        if check_first_condition(line) and check_second_condition(line):
            counter += 1
    print("Solution: ", counter)

