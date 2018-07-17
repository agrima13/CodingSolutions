import unittest


def reverse(list_of_chars):

    # Reverse the input list of chars in place
   left_index = 0
   right_index = len(list_of_chars) - 1
   while left_index < right_index :
       list_of_chars[left_index], list_of_chars[right_index] = list_of_chars[right_index],list_of_chars[left_index]
       left_index+=1
       right_index-=1


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        print(list_of_chars)
        print(expected)
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        print(list_of_chars)
        print(expected)
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        reverse(list_of_chars)
        expected = ['G','F','E', 'D', 'C', 'B', 'A']
        print(list_of_chars)
        print(expected)
        self.assertEqual(list_of_chars, expected)


#unittest.main(verbosity=2)