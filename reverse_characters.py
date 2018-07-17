import unittest


def reverse(list_of_chars):

    # Reverse the input list of chars in place
   size = len(list_of_chars)
   if(size > 1):
       for i, item in enumerate(list_of_chars):
           if( i < size/2):
               temp = list_of_chars[size - i - 1]
               list_of_chars[size - i -1] = list_of_chars[i]
               list_of_chars[i] = temp
           else:
               break

   else:
       return list_of_chars


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