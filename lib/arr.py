def SecondGreatLow(arr):
    arr = sorted(set(arr))  # Remove duplicates and sort the array
    if len(arr) == 2:
        return f"{arr[1]} {arr[0]}"  # Special case for only 2 numbers
    return f"{arr[1]} {arr[-2]}"  # Return second lowest and second greatest

def final_output(arr, token):
    result = SecondGreatLow(arr) + token
    return ''.join('X' if (i+1) % 3 == 0 else c for i, c in enumerate(result))

# Example usage
input_arr = [1, 42, 42, 180]
challenge_token = "ni2ge5shj9c"
print(final_output(input_arr, challenge_token))  # Example final output