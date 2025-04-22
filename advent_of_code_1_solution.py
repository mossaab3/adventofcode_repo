import numpy as np

### ---- Extracting data from the csv file
data = np.loadtxt("advent_1_data.csv")  
data_1 = data[:, 0]  # first column
data_2 = data[:, 1]  # second column

### ---- Keeping it lists so that it is the most general case altough numpy is faster 
data_1 = list(data_1)
data_2 = list(data_2)

### calculating similarity score between two lists
### ---- This function calculates the total distance between a list of tuples
def calculate_total_difference(list_of_tuples) -> float:
    total_distance = 0
    for i in range(len(list_of_tuples)):
        total_distance += abs(list_of_tuples[i][0] - list_of_tuples[i][1])
    
    print("The total distance is:", total_distance)
    return total_distance

### ---- This function matches two lists of the same size and returns a list of tuples
def match_lists(input_1, input_2) -> list:

    ## asserting input_1 and input_2 are of the same size to be matched and their size is bigger than 0
    assert(len(input_1) > 0) and len(input_2), "Input lists must be of size greater than 0."
    assert len(input_1) == len(input_2), "Input lists must be of the same length."

    ## here we create a list of tuples with the values of the two lists
    size = len(input_1)

    matched_list_of_tuples = []
    for i in range(size):
        minimum_input_1 = min(input_1)
        minimum_input_2 = min(input_2)
        index_input_1 = input_1.index(minimum_input_1)
        index_input_2 = input_2.index(minimum_input_2)
        matched_list_of_tuples.append((minimum_input_1, minimum_input_2))
        input_1.pop(index_input_1)
        input_2.pop(index_input_2)
    
    return matched_list_of_tuples


def similarity_score(input_1, input_2) -> float:
    ## asserting input_1 and input_2 are of the same size to be matched and their size is bigger than 0
    assert(len(input_1) > 0) and len(input_2) > 0, "Input lists must be of size greater than 0."
    assert len(input_1) == len(input_2), "Input lists must be of the same length."

    size = len(input_1)
    similarity_score = 0
    for i in range(size):
        for j in range(size):
            if(input_2[j] == input_1[i]):
                similarity_score+=input_1[i]

    return similarity_score



# ### ---- Test for advent_1_data.csv
if __name__=="__main__":
    user_input = float(input("which part do you need ? \n 0 for part I or 1 for part II "))
    if(user_input) == 0.0:
        matched_list = match_lists(data_1, data_2)
        calculate_total_difference(matched_list)
    else:
        print("\033[92m" + "similarity score is : \033[0m", similarity_score(data_1, data_2)) 


