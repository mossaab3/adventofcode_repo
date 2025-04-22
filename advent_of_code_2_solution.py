import numpy as np 


### declaring reports :
# reports = np.array([
#     [7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9]
# ])

## read a csv file that looks like this : 

data = []
with open('advent_2_data.csv', 'r') as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        data.append(row)

reports = np.array(data, dtype=object)



def how_many_safe_reports(reports):

    nbr_of_reports = len(reports)

    number_of_safe_reports = 0
    safe_reports = []
    for i in range(nbr_of_reports):
        sign_ = np.sign(reports[i][1] - reports[i][0])
        length_of_the_report = len(reports[i])
        is_safe = True

        for j in range(length_of_the_report - 1):
            if sign_ != np.sign(reports[i][j+1] - reports[i][j]):
                is_safe = False
                break
            if np.abs(reports[i][j+1] - reports[i][j]) < 1 or np.abs(reports[i][j+1] - reports[i][j]) > 3 : 
                is_safe = False
                break
        if is_safe:
            number_of_safe_reports+=1.0

    print(number_of_safe_reports)
    return number_of_safe_reports

if __name__ == "__main__":
    how_many_safe_reports(reports)