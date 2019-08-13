import unittest;
from pythonDemo.UnitTest.myScore import StudentScore;
class testStdentScore(unittest.TestCase):
    def test_80_to_100(self):
        self.assertEqual(StudentScore('bart',80).get_grade(),'A');
        self.assertEqual(StudentScore('lisa',90).get_grade(),'A');

    def test_60_to_80(self):
        self.assertEqual(StudentScore("bart",60).get_grade(),'B');
        self.assertEqual(StudentScore("lisa",70).get_grade(),'B');

    def test_0_to_60(self):
        self.assertEqual(StudentScore("bart",35).get_grade(),"C");
        self.assertEqual(StudentScore("lisa",59).get_grade(),"C");
    def test_error(self):
        with self.assertRaises(ValueError):
            StudentScore("bart",-1).get_grade();
        with self.assertRaises(ValueError):
            StudentScore("bart", 'a').get_grade();
    if __name__== '__main__':
      unittest.main();