#对StudentScore类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：
class StudentScore(object):
    def __init__(self,name,score):
        self.__name = name;
        self.__score = score;

    def get_grade(self):
        if isinstance(self.__score,str) or (self.__score<0 or self.__score>100):
            raise ValueError("score must between 0 to 100");
        if self.__score>= 80:
            return 'A';
        if self.__score>=60:
            return 'B';
        else:
            return 'C';