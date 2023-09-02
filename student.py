class Student:
    def __init__(self,s_name,s_chinese,s_maths,s_english):
        self.name = s_name
        self.chinese = s_chinese
        self.maths = s_maths
        self.english = s_english
    def ch(self):
        print(f"语文是{self.chinese}分")
    def en(self):
        print(f"英语是{self.english}分") 
    def ma(self):
        print(f"数学是{self.maths}分")   

student1 = Student("张三",70,80,33)

print(f"{student1.name}的语文是{student1.chinese}分,英语是{student1.english}分,数学是{student1.maths}分")
student1.ch()