import re
"""find_word_with_most_char - coding using python 3.12.3
"""

"""Given a long statement and an input letter, find the word which contains the most number of the given character. 
If more than one word has the exact same number of the given letter, it should return the word with the most number 
of total letters. If more than one words have equal number of given character and the total number of characters
retuen the word that appeared first in the given statement.

INPUT:
statemt: string. A long statement. Cannot be empty.
char: str. An input letter. Must be a single uppercase or lowercase letter.

OUTPUT: 
word: string. The word with most occurrences of the char. If no word is found with the char, None is return.
"""   
def find_word_with_most_char(statement, char):
    # Validate input: Ensure char is a single character
    if len(char) != 1 or not char.isalpha():
        raise ValueError("Input letter must be a single uppercase or lowercase letter.")
        
    # Validate input: Ensure statement is not empty
    if not statement.strip():
        raise ValueError("Statement cannot be empty.")            

    # Split the statement into individual words
    words = re.findall(r"[\w']+|[.,!?;]", statement)

    # Initialize variables to keep track of the maximum count and length
    max_count = 0
    max_length = 0
    result_word = None

    # Iterate through each word in the statement
    for word in words:
        # Count the occurrences of the specified character in the word
        char_count = word.count(char)
        
        #print("char count is {}".format(char_count))

        # Update the maximum count and length if necessary
        if char_count == 0:
            pass
        elif char_count > max_count:
            max_count = char_count
            max_length = len(word)
            result_word = word
        elif char_count == max_count and len(word) > max_length:
            max_length = len(word)
            result_word = word

    # Return the word that meets the specified criteria
    return result_word

        
def main():
    while True:
        # Get user input for the statement
        long_statement = input("Enter a statement: ")
        if len(long_statement) >= 1:
            break
        else:
            print("Please enter a statement.")        

    # Ask the user for a character
    while True:
        input_letter = input("Enter a single uppercase or lowercase letter: ")
        if len(input_letter) == 1 and input_letter.isalpha():
            break
        else:
            print("Please enter a single character.")

    # Calculate the word with the most occurrences of the specified character
    result_word = find_word_with_most_char(long_statement, input_letter)
    if result_word == None:
        print(f"No word with the letter '{input_letter}' characters is found!")
    else:
        print(f"The word with the most '{input_letter}' characters is: {result_word}")

if __name__ == "__main__":
    main()
