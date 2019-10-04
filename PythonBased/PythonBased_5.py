#面向过程
std1 = {'name':'aaa','score':90}
std2 = {'name':'bbb','score':80}
def print_score(std):
    print('%s: %s'%(std['name'],std['score']))
print_score(std1)
print_score(std2)

#面向对象
class student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s'%(self.name,self.score))

aaa = student('AAA',90)
bbb = student('BBB',80)
aaa.print_score()
bbb.print_score()