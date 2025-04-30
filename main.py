from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]: 
    pass

# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    sum = 0
    for j in even_int_list:
        sum += j**2
    return sum

# Main function
def main():
    # Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

# Boilerplate code
if __name__ == "__main__":
    main()