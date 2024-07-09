import unittest

from longest_ones_sequence_start import longest_ones_sequence_start


class Test_longest_ones_sequence_start(unittest.TestCase):

    def test_longest_ones_sequence_start_1(self):
        # Test case 1: Basic test - binary 10011100
        number = 156
        print(longest_ones_sequence_start(number))
        self.assertEqual(longest_ones_sequence_start(number) ,4)

    def test_longest_ones_sequence_start_2(self):
        # Test case 2: Basic test - binary 1011000
        number = 88
        self.assertEqual( longest_ones_sequence_start(number) , 3)

    def test_longest_ones_sequence_start_3(self):
        # Test case 3: binary single '1'
        number = 1
        self.assertEqual(longest_ones_sequence_start(number) ,1)

    def test_longest_ones_sequence_start_4(self):
        # Test case 4: Multiple continuous 1s of same length
        number = 11001110111
        self.assertEqual(longest_ones_sequence_start(number) ,7)

    def test_longest_ones_sequence_start_5(self):
        # Test case 5: negative integer
        number = -1
        with self.assertRaises(ValueError): 
            longest_ones_sequence_start(number)

    def test_longest_ones_sequence_start_6(self):
        # Test case 6: String
        number = "string"
        with self.assertRaises(ValueError): 
            longest_ones_sequence_start(number)        

    def test_longest_ones_sequence_start_7(self):
        # Test case 7: empty
        number = None
        with self.assertRaises(ValueError): 
            longest_ones_sequence_start(number)             

    def test_longest_ones_sequence_start_8(self):
        # Test case 8: Enter value 0
        number = 0
        with self.assertRaises(ValueError): 
            longest_ones_sequence_start(number)
        
        print("longest_ones_sequence_start test cases passed!")

if __name__ == '__main__':
    unittest.main()