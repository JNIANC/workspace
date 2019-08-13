# with open("C:/Users/13995/Desktop/新建文本文档.txt","r",encoding="utf-8") as f:
#      print(f.read())

import os;
def printDir_file(path,s):
    for x in os.listdir(path):
        this_path = os.path.join(path,x);
        if os.path.isfile(this_path):
            if s in  x:
                print("路径："+this_path);
        else:
            printDir_file(path,s);
printDir_file(".",".py");
import pickle;
def testPickle():
    d = dict(name="bar",age = "20");
    with open('d:\\data.pkl', 'wb') as f:
        pickle.dump(d, f);
    with open("d:/data.pkl",'rb') as f:
        print(pickle.load(f));
testPickle();

import json;
def testPickleJson():
    d = {"name":"bar","age":23};
    print(json.dumps(d));
    a = '{"name":"bar","age":23}';
    print(json.loads(a))
testPickleJson();

# 对象转json
class Student(object):
    def __init__(self,name,age,sort):
        self.name = name;
        self.age = age;
        self.sort = sort;
print(json.dumps(Student("bar",20,80),default=lambda obj:obj.__dict__))

# json转成对象
import json;
d = '{"name":"bar","age":34,"sort":90}';
def dict2Object(o):
    return Student(o["name"],o["age"],o["sort"]);
print(json.loads(d,object_hook=dict2Object))
# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True);
print(s)

import re;
print(re.match(r'^\d{3}\-\d{3,8}$','123-12345'));