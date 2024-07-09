import unittest

from find_word_with_most_char import find_word_with_most_char


class Test_find_word_with_most_char(unittest.TestCase):
    def setUp(self):
        #print('setUp')
        self.statement = "This is a long sentence and I want to educate everyone in this whole crazy world...."

    #def tearDown(self):
        #print('tearDown\n')

    def test_find_word_with_most_char_1(self):
        # Test case 1:basic test case
        input_letter = 'z'
        self.assertEqual(find_word_with_most_char(self.statement, input_letter),"crazy")

    def test_find_word_with_most_char_2(self):
        # Test case 2: test it is case sensitive
        input_letter = 'I'
        self.assertEqual(find_word_with_most_char(self.statement, input_letter) , "I")

    def test_find_word_with_most_char_3(self):
        # Test case 3: statement have words same number of most occurances of letters and same length, the first word in statement is returned
        input_letter = 'e'
        self.assertEqual(find_word_with_most_char(self.statement, input_letter) , 'sentence')

    def test_find_word_with_most_char_4(self):
        # Test case 4:  test the word with most occurances of letter returned
        statement_test = "Apples are amazing, and bananas are also awesome."
        input_letter = 'a'
        self.assertEqual(find_word_with_most_char(statement_test, input_letter) , "bananas")

    def test_find_word_with_most_char_5(self):
        # Test case 5:  The stament has the same most occurances and the longest length word is returned
        statement_test = "The elephant and the eagle both enjoy eating apples."
        input_letter = 'e'
        self.assertEqual(find_word_with_most_char(statement_test, input_letter) , "elephant")
 
    def test_find_word_with_most_char_6(self): 
        # Test case 6: Empty statement
        statement_test = ""
        input_letter = 'x'
        with self.assertRaises(ValueError): 
            find_word_with_most_char(statement_test, input_letter)
            
    def test_find_word_with_most_char_7(self): 
        # Test case 7: Empty letter
        statement_test = "This is a string"
        input_letter = ""
        with self.assertRaises(ValueError): 
            find_word_with_most_char(statement_test, input_letter)

    def test_find_word_with_most_char_8(self): 
        # Test case 8: More than 1 char in letter
        statement_test = "This is a string"
        input_letter = "is"
        with self.assertRaises(ValueError): 
            find_word_with_most_char(statement_test, input_letter)
            

    def test_find_word_with_most_char_9(self): 
        # Test case 9: Letter cannot be found in the statement
        statement_test = "This is a string"
        input_letter = "z"
        self.assertIsNone(find_word_with_most_char(statement_test, input_letter))
           
    def test_find_word_with_most_char_10(self): 
        # Test case 10: Letter is not A-Z and a-z
        statement_test = "This is a string"
        input_letter = "9"
        with self.assertRaises(ValueError): 
            find_word_with_most_char(statement_test, input_letter)         

        print("find_word_with_most_char test cases passed!")


if __name__ == '__main__':
    unittest.main()