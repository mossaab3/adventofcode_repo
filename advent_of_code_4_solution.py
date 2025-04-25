import math


the_word = "XMAS"
# the_phrase = "MMMSXXMASMMSAMXMSMSAAMXSXMAAMMMSAMASMSMXXMASAMXAMMXXAMMXXAMASMSMSASXSSSAXAMASAAAMAMMMXMMMMMXMXAXMASX"
the_word_length = len(the_word)

with open("advent_4_data.txt", "r") as file:
    the_phrase = file.read()

## the phrase must be a square 
phrase_size = len(the_phrase)
phrase_square_side_size = int(math.sqrt(phrase_size))

def is_word_valid(four_letter_word):
    if len(four_letter_word) != 4:
        # print("\033[91mThe word contains more than 4 letters\033[0m")
        return False
    # check if four_letter_word string == the_word and check its inverse as well

    if four_letter_word == the_word or four_letter_word == the_word[::-1]:
        return True
    else:
        return False

def compute_xmas_words(phrase):

    number_of_xmas_words = 0.0
    for i in range(len(phrase)):
        if (phrase_square_side_size - i%phrase_square_side_size)>=the_word_length: 
            horizontal_word = phrase[i] + phrase[i+1] + phrase[i+2] + phrase[i+3]
        else:
            horizontal_word = ""

        if i <= len(phrase) - 3*phrase_square_side_size - 1: 
            vertical_word = phrase[i] + phrase[i+phrase_square_side_size] + phrase[i+2*phrase_square_side_size] + phrase[i + 3*phrase_square_side_size]
        else:
            vertical_word = ""

        first_diagonal_condition_forward_right = ((phrase_square_side_size - i%phrase_square_side_size)>=the_word_length)
        second_diagonal_condition_forward_right = i <= phrase_size-(the_word_length -1)*phrase_square_side_size - the_word_length # this has been found using experimentation 
        if (first_diagonal_condition_forward_right and second_diagonal_condition_forward_right): 
            diagonal_word_forward_right = phrase[i] + phrase[i+phrase_square_side_size+1] + phrase[i+2*phrase_square_side_size+2] + phrase[i+3*phrase_square_side_size+3]
        else:
            diagonal_word_forward_right = ""
        
        first_diagonal_condition_backwards_right = ((i%phrase_square_side_size) >= (the_word_length-1))
        second_diagonal_condition_backwards_right= (i <= phrase_size - 3 *phrase_square_side_size - 1)

        if (first_diagonal_condition_backwards_right and second_diagonal_condition_backwards_right):
            diagonal_word_backwards_right = phrase[i] + phrase[i+phrase_square_side_size-1] + phrase[i+2*phrase_square_side_size-2] + phrase[i+3*phrase_square_side_size-3]
        else:
            diagonal_word_backwards_right = ""

        print("iteration is :", i)
        # print("\033[92miteration number :\033[0m", i)
        print("the horizontal word is :", horizontal_word)
        print("the vertical word is :", vertical_word)
        print("the diagonal word forward right is :", diagonal_word_forward_right)
        print("the diagonal word backwards right is :", diagonal_word_backwards_right)
        is_horizontal_word_valid = is_word_valid(horizontal_word)
        is_vertical_word_valid = is_word_valid(vertical_word)
        is_diagonal_word_forward_right_valid = is_word_valid(diagonal_word_forward_right)
        is_diagonal_word_backwards_right_valid = is_word_valid(diagonal_word_backwards_right)
        
        if is_horizontal_word_valid:
            number_of_xmas_words += 1
            print("is horizontal word valid :", horizontal_word)
            print("\033[92mnumber of xmas words is :\033[0m", number_of_xmas_words)
        if is_vertical_word_valid:
            number_of_xmas_words += 1
            print("vertical word valid :", vertical_word)
            print("\033[92mnumber of xmas words is :\033[0m", number_of_xmas_words)

        if is_diagonal_word_forward_right_valid:
            number_of_xmas_words += 1
            print("diagonal word valid :", diagonal_word_forward_right)
            print("\033[92mnumber of xmas words is :\033[0m", number_of_xmas_words)
        if is_diagonal_word_backwards_right_valid:
            number_of_xmas_words += 1
            print("diagonal word backwards right valid :", diagonal_word_backwards_right)
            print("\033[92mnumber of xmas words is :\033[0m", number_of_xmas_words)
        # print("the number of xmas words is :", number_of_xmas_words)
        # input("")

    return number_of_xmas_words

if __name__ == "__main__":
    print(compute_xmas_words(the_phrase))