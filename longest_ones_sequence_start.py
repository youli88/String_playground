"""longest_ones_sequence_start - coding using python 3.12.3
"""
        
"""Accept a number and returns the starting positon of the longest continuous sequences of the 1s in its binary format.
   The starting position is from 1.

INPUT:
number: int. Must be positive and cannot be empty

OUTPUT: 
starting_position: int. The starting position of the longest continous sequences of the 1s
"""     
def longest_ones_sequence_start(number):
     # Validate input: Ensure number is an integer
     if not isinstance(number, int):
         raise ValueError("Number must be a positive integer and cannot be empty.")

     # Validate input: Ensure number is positive
     if number <= 0 :
         raise ValueError("Number must be positive.")

     # Convert the number to binary representation
     binary_str = bin(number)[2:]  # Remove the '0b' prefix
     
     print ("Binary string of {} is = {}".format(number, binary_str))

     # Initialize variables to track the longest sequence
     max_length = 0
     start_position = 0 # Note the start position is from 1
     current_length = 0

     # Iterate through each digit in the binary string
     for i, digit in enumerate(binary_str):
         if digit == '1':
             # Increment the current sequence length
             current_length += 1
             if current_length > max_length:
                 # Update max_length and start_position if necessary
                 max_length = current_length
                 # Calculate the starting position of the longest continuous sequence of 1s
                 # We add 2 to the result:
                 #   - 1 to correct for the fact that 'i' starts from 0
                 #   - 1 to compensate for the start position of the max length
                 start_position = i - max_length + 2 
         else:
             # Reset the current sequence length
             current_length = 0

     # Return the starting position of the longest sequence of 1s
     return start_position

def main():

    # Ask the user for a number
    while True:
        try:
            decimal_number = int(input("Enter a positive integer: "))
            if decimal_number <= 0:
                print("Number must be a positive integer. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Calculate the longest ones sequence start
    try:
        start_position = longest_ones_sequence_start(decimal_number)
        print(f"The starting position of the longest continuous sequence of 1s in {decimal_number} (in binary) is: {start_position}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()