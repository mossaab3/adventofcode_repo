import math

the_word = "MAS"
the_word_length = len(the_word)
### --- the phrase is here 
# the_phrase = ".M.S.M......A..MSMS..M.S.MAA....A.ASMSM..M.S.M..............S.S.S.S.S..A.A.A.A..M.M.M.M.M..........."
with open("advent_4_data_part_2.txt", "r") as file:
    the_phrase = file.read()
## ---

phrase_size = len(the_phrase)
phrase_square_side_size = int(math.sqrt(phrase_size))
print(phrase_size)
print(phrase_square_side_size)
## the phrase must be a square 

def is_word_valid(word_to_check, reference_word=the_word):
    if len(word_to_check) != len(reference_word):
        # print("\033[91mThe word contains more than 4 letters\033[0m")
        return False
    # check if four_letter_word string == the_word and check its inverse as well

    if word_to_check == reference_word or word_to_check == reference_word[::-1]:
        return True
    else:
        return False


def is_matrix_of_x_sam_form(word_matrix):
    assert len(word_matrix) == 9, "THE GIVEN MATRIX IS NOT a 9x9 MATRIX"
    first_diagonal_word = ""
    second_diagonal_word = ""
    for i in range(len(the_word)):
        first_diagonal_word += word_matrix[i*(the_word_length+1)]
        second_diagonal_word+= word_matrix[(the_word_length-1)+i*(the_word_length-1)]
    # print("first_diag_word is:", first_diagonal_word)
    # print("second_diag_word is:", second_diagonal_word)
    
    if is_word_valid(first_diagonal_word) and is_word_valid(second_diagonal_word):
        return True
    return False

def computer_number_of_x_sam_form(phrase):
    number_of_x_sam_form = 0.0
    for i in range(phrase_size):
        first_condition = (phrase_square_side_size - i % phrase_square_side_size)>=the_word_length
        second_condition= i <= ( phrase_size - 2*phrase_square_side_size - the_word_length)

        if first_condition and second_condition:
            matrix_i = phrase[i] + phrase[i+1] + phrase[i+2] + phrase[i+phrase_square_side_size] + phrase[i+phrase_square_side_size+1] +phrase[i+phrase_square_side_size+2]+phrase[i+2*phrase_square_side_size] + phrase[i+2*phrase_square_side_size+1] + phrase[i+2*phrase_square_side_size+2]
            if(is_matrix_of_x_sam_form(matrix_i)):
                number_of_x_sam_form+=1.0

    return number_of_x_sam_form

if __name__ == "__main__":
    print("\033[92mnumber of x sam form is : ", computer_number_of_x_sam_form(the_phrase), "\033[0m")
