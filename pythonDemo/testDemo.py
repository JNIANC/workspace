from functools import reduce;
#将字符串转换成int或float
def str2float(s):
    digitis = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9};
    def char2float(s):
        return digitis[s];
    return reduce(lambda x,y:x * 10 + y,map(char2float,s.replace(".","")));
def mainStr2Float():
    s = input("please input your str to change float:")
    if s.find(".")!=-1:
        print('str2float(\'%s\') ='%s,str2float(s)/pow(10,(len(s)-s.find(".")-1)));
    else:
        print("str2float(\'%s\') ="%s,str2float(s));

#filter
def testFilter(n):
    s = str(n);
    return s == s[::-1];
print(list(filter(testFilter,range(0,1000))));
print(list(filter(lambda n:str(n) == str(n)[::-1],range(0,1000))));

#sorted
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
print(sorted(["Cred","able","cookie","drep"],key=str.lower));
#sorted 的反向排序
print(sorted(["Cred","able","cookie","drep"],key=str.lower,reverse=True));
L = [('Bob', 75,1), ('Adam', 92,2), ('Bart', 66,6), ('Lisa', 88,5)]
#列表分别按名字排序：
print(sorted(L,key=lambda t:t[0]))
#再按成绩从高到低排序：
print(sorted(L,key=lambda t:t[1],reverse=True))
with open("C:/Users/13995/Desktop/新建文本文档.txt","r",encoding="utf-8") as f:
    print(f.read())
#匿名函数
print(list(filter(lambda n:n%2 == 1,range(1,20))));
#装饰器
print(testFilter.__name__)
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time,functools;
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        startTime = time.time();
        result = func(*args,**kw);
        endTime = time.time();
        print("%s函数的执行结果为时间为%fms"%(func.__name__,(endTime-startTime)*1000));
        return result
    return wrapper;
@log
def f(x,y):
    time.sleep(0.0012)
    return x * y;
print(f(3,4));

#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
#begin call
import functools;
def beginlog(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("begin call %s"%func.__name__);
        fun = func(*args,**kw);
        print("end call %s" % func.__name__);
        return fun;
    return wrapper;
@beginlog
def testbeginlog():
    print("content...");
testbeginlog();

#又支持：@log('execute')
import functools;
def finallLog(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            if None!=text:
                print("input str is [%s] and begin call [%s]"%(text,func.__name__));
                fun = func(*args,**kwargs);
                print("input str is [%s] and end call [%s]" % (text, func.__name__));
            else:
                print("begin call [%s]" % (func.__name__));
                fun = func(*args, **kwargs);
                print("end call [%s]" % (func.__name__));
            return fun;
        return wrapper;
    if isinstance(text,str):
        return decorator; #首先如果有参数 就跟原来一样直接返回decorator即可
    else:   #如果没有参数 其实log(func)就是log里边其实直接传的参数就是func 返回的应该是wrapper
        strtmp = text;
        text = None;
        return decorator(strtmp); #所以这里的应该是直接decorator(func) 返回wrapper
@finallLog
def testfinallLog(x,y):
    return x * y;
testfinallLog(3,5)
#偏函数
def int2(s,base =2):
    return int(s,base);
print(int2("1010101",2));
#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()
import functools;
int22 =functools.partial(int,base=2);
print(int22("1010101"))

#OOP
class Student(object):
    def __init__(self,name,score):
        self.__name  = name;
        self.__score = score;

    def get_score(self):
        return self.__score;

    def set_score(self,score):
        self.__score = score;

    def get_grade(self):
        if self.__score>=90:
            return 'A';
        elif self.__score>=60:
            return 'B';
        else:
            return 'C';
print(Student("bor",89).get_grade());

class Student1(object):
    def __init__(self,name,gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender;
    def set_gender(self,gender):
        if gender in("male","female"):
            self.__gender = gender;
        else:
            raise ValueError("bad gender");
#dir()
print(dir(Student(56,56)));

class Student2(object):
    count =0;
    def __init__(self, name):
        self.name = name
        Student2.count+=1;
print(Student2("ba1").count);
print(Student2("ba2").count);

#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    @property
    def width(self):
        return self.__width;
    @width.setter
    def width(self,width):
        if not isinstance(width, int):
            raise ValueError("[%s] must be integer" %width);
        if width < 0:
            raise ValueError("[%s]\'s value must be bigger than 0" %width);
        self.__width = width;

    @property
    def height(self):
        return self.__height;
    @height.setter
    def height(self,height):
        if not isinstance(height, int):
            raise ValueError("[%s] must be integer" % height);
        if height < 0:
            raise ValueError("[%s]\'s value must be bigger than 0" % height);
        self.__height = height;
    @property
    def resolution(self):
        return self.__width * self.__height;
screen = Screen();
screen.height = 768
screen.width = 1024
print('resolution =%d'%screen.resolution);
if screen.resolution == 786432:
    print("测试通过!");
else:
    print("测试不通过!");

#把Student的gender属性改造为枚举类型，可以避免使用字符串
from enum import Enum,unique
@unique
class Gender(Enum):
    Male = 0
    Female = 1

class StudentEnum(object):
    def __init__(self, name, gender):
        self.name = name
        if isinstance(gender, Gender):
            self.gender = gender;
        else:
            raise TypeError("gender must be gender type");
print(StudentEnum('BAR',Gender.Male))
print(StudentEnum('bar',Gender['Male']));
print(StudentEnum('bar',Gender(0)))

#错误处理
import logging
try:
    print("try...");
    n = 10/0;
except ZeroDivisionError as e:
    print("except:",e)
except ValueError as e:
    print("except:",e);
finally:
    print("end...")
#运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce
def str2num(s):
    try:
        result = int(s);
    except:
        try:
            result = float(s);
        except:
            raise TypeError("type error");
    finally:
        return result;
def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)
main()

