import unittest


def reverse_words(message):

     reversal(message, 0 , len(message) - 1)

     start = 0
     for i in range(len(message) + 1):
        if( i == len(message) or message[i] == ' '):
            reversal(message, start, i -1)
            start = i + 1


def reversal(message, first_index, last_index):
     # Decode the message by reversing the words

     while first_index < last_index :
         message[first_index],message[last_index] = message[last_index],message[first_index]
         first_index+=1
         last_index-=1



# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)


    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        #print(message)
        #print(expected)
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)

