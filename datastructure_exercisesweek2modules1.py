from collections import deque
#Câu 1
def max_sliding_window(num_list, k):
    if not num_list or k == 0:
        return []

    if k == 1:
        return num_list

    dq = deque()
    max_values = []

    for i in range(len(num_list)):
        # Remove elements not within the window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove elements smaller than the current element from the deque
        while dq and num_list[dq[-1]] < num_list[i]:
            dq.pop()

        # Add the current element index at the end of the deque
        dq.append(i)

        # If we have processed at least k elements, add to results
        if i >= k - 1:
            max_values.append(num_list[dq[0]])

    return max_values
# Example usage
assert max_sliding_window ([3 , 4 , 5 , 1 , -44] , 3) == [5 , 5 , 5]
num_list = [3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1]
k = 3
print(max_sliding_window(num_list, k))
#Câu 2
def count_chars_case_insensitive(string):
    # Convert the string to lower case to handle case insensitivity


    # Initialize an empty dictionary to store the character counts
    char_count = {}

    # Iterate over each character in the string
    for char in string:
        # Skip spaces
        if char == ' ':
            continue

        # Update the count for the character
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

# Example usage
assert count_chars_case_insensitive(" Baby ") == {'B': 1 , 'a': 1 , 'b': 1 , 'y': 1}
print(count_chars_case_insensitive('smiles'))  # Output: {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
#Bài 3
!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko

def count_word ( file_path ) :
  counter = {}
  with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Remove newline characters and convert to lowercase
            line = line.strip().lower()
            # Split the line into words
            words = line.split()
            # Count the occurrences of each word
            for word in words:
                if word in counter:
                    counter[word] += 1
                else:
                    counter[word] = 1


  return counter
file_path = '/content/P1_data.txt'
result = count_word ( file_path )
assert result ['who'] == 3
print ( result ['man'])
#Bài 4
def levenshtein_distance(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and first column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Compute the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,      # Deletion
                           dp[i][j - 1] + 1,      # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution

    return dp[m][n]

# Example usage
s = "hola"
t = "hello"
print(f"Levenshtein distance between '{s}' and '{t}' is {levenshtein_distance(s, t)}")
def divide_Sum (a,b):
    return a/b

