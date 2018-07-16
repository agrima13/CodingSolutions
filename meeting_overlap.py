import unittest

def merge_ranges(meetings):
    sorted_meetings = sorted(meetings)
    merged_range = [sorted_meetings[0]]

    for start,end in sorted_meetings[1:]:
        prev_start,prev_end = merged_range[-1]
        if prev_end >= start:
            merged_range[-1] = (prev_start,max(end,prev_end))
        else:
            merged_range.append((start,end))

    return merged_range

# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        print("Actual"+" ",actual)
        print("Expected"+" ",expected)
        self.assertEqual(actual, expected)


    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        print("Actual"+" ",actual)
        print("Expected"+" ",expected)
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        print("Actual"+" ",actual)
        print("Expected"+" ",expected)
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        print("Actual"+" ",actual)
        print("Expected"+" ",expected)
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        print("Actual"+" ",actual)
        print("Expected"+" ",expected)
        self.assertEqual(actual, expected)



    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]

        print("Actual"+" ",actual)
        print("Expected"+" ",expected)
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (10, 12),(4,8), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        print("Actual"+" ",actual)
        print("Expected"+" ",expected)
        self.assertEqual(actual, expected)

