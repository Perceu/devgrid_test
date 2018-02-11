import unittest
from scoreboard import Scoreboard

class TestStringMethods(unittest.TestCase):

    def test_ScoreBoard(self):
        sample_input = '1 \n1 2 10 I \n3 1 11 C \n1 2 19 R \n1 2 21 C \n1 1 25 C '
        sample_output = '1 2 66 \n3 1 11 \n'
        print('### Input ###')
        print(sample_input)
        print('### Output ###')
        print(sample_output)
        self.assertEqual(Scoreboard(sample_input).get_output(), sample_output)

if __name__ == '__main__':
    unittest.main()