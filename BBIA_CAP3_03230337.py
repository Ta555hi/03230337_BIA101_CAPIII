################################
# Github Repo link
# https://github.com/Ta555hi/03230337_BIA101_CAPIII
# Your Name: Tashi Lhamo
# Your Section: A
# Your Student ID Number: 03230337
################################
# REFERENCES
#https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.com/python/ref_string_isdigit.asp
################################
# SOLUTION
# Your Solution Score: 491603
################################


def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines


def calculate_sum(file_name):
    lines = read_input(file_name)
    total_sum = 0

    for line in lines:
        first_digit = ''
        last_digit = ''
        
        for char in line:
            if char.isdigit():
                first_digit = char
                break
        
        for char in reversed(line):
            if char.isdigit():
                last_digit = char
                break

        if first_digit and last_digit:
            number = int(first_digit + last_digit)
            total_sum += number

    return total_sum

def print_solution(file_name):
    total_sum = calculate_sum(file_name)
    print(f"The total sum from the given input file {file_name} is {total_sum}")

if __name__ == "__main__":
    file_name = '337.txt'
    print_solution(file_name) 