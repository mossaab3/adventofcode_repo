

# corrupted_text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
with open("advent_3_data.txt", "r") as file:
    corrupted_text = file.read()

print("Original text:", corrupted_text)
print("type is ", type(corrupted_text))
print("len is ", len(corrupted_text))

# corrupted_text = 

def correct_text(corrupted_text):
    uncorrupted_text = ""
    total_mul = 0.0
    for i in range(len(corrupted_text)):
        if corrupted_text[i] == 'm' and corrupted_text[i+1] == 'u' and corrupted_text[i+2] == 'l':
            ##check if the next character is (

            if corrupted_text[i+3] == '(':
                # find the first closing parenthesis
                closing_parenthesis = corrupted_text.find(')', i+3)
                comma = corrupted_text.find(",", i+3, closing_parenthesis)

                if(corrupted_text[i+4:comma].isdigit() and corrupted_text[comma+1:closing_parenthesis].isdigit()):
                    uncorrupted_text += "mul(" + corrupted_text[i+4:comma] + "," + corrupted_text[comma+1:closing_parenthesis] + ")"
                    total_mul += float(corrupted_text[i+4:comma]) * float(corrupted_text[comma+1:closing_parenthesis])

    return uncorrupted_text, total_mul



if __name__ == "__main__":
    print("Original text:", corrupted_text)
    uncorrupted_text, total_mul = correct_text(corrupted_text)
    print("Uncorrupted text:", uncorrupted_text, " and total multiplication :", total_mul)