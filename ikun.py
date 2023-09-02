import sys
from time import sleep


def clean():
    sys.stdout.write("\x1bc")  # 清空终端
    sys.stdout.flush()         # 清空终端缓存


class ikun:
    def __init__(self, kun_t_f, kun_name, kun_age, ikun_iage):
        self.name = kun_name
        self.t_f = kun_t_f
        self.age = kun_age
        self.iage = 0
        n = 0
        # if ("t" in self.t_f) or ("T" in self.t_f):
        if ("鸡" in self.t_f) or ("唱跳" in self.t_f):
            n += 1
            self.iage = ikun_iage
        if self.age < self.iage:
            n -= 1
        clean()
        if n == 1:
            print("正确,是ikun")
            self.t_f = True
        else:
            print("错误,不是ikun --你干嘛~哎呦")
            self.iage = " --"
            self.t_f = False

    def changtiao(self):
        print(f"欢迎来到唱跳\n我是练习两年半的个人练习生\n鸡你太美~\n你好:{self.name}")

    def kun_baby(self, doing1):

        print("哥哥正在为你 "+doing1)

    def kun_ball(self, y_n):
        if "y" in y_n:
            print("我的篮球在我手里，你怎么会有，你个小黑子藏得挺深哪")
            return 0
        else:
            print("你是我的真ikun")


clean()
kun1 = ikun(input("请输入暗号:"), str(input("姓名:")),
            float(input("年龄:")), float(input("kun龄:")))


# kun1 = ikun("t","kunkun",13,2.5)
clean()
print(
    f"ikun判定通知书:  \nikun判断:{kun1.t_f}  \n姓名:{kun1.name}  \n年龄:{kun1.age}  \nkun龄:{kun1.iage}")
if kun1.t_f:

    print("\n正在转接，请稍等...")
    sleep(3)
    clean()
    print("欢迎来到大本营，鸡你太美")
    while True:
        print("请选择：\n1.唱跳 \n2.帮助坤坤找篮球 \n3.坤坤宝贝 \n4.给作者点赞 \n5.退出")
        print("\n")
        c = int(input("请输入编号:"))
        if c > 5 or c < 1:
            print("你干嘛 哎哟~")
        else:
            if c == 1:
                kun1.changtiao()
            elif c == 2:
                x = kun1.kun_ball(input("你看见坤坤的篮球了吗(y/n)"))
                if x == 0:
                    break
            elif c == 3:
                while True:
                    clean()
                    doing = input("你想要坤坤宝贝做什么呢\n注:按“5”退出")
                    if doing != "5":
                        kun1.kun_baby(doing)
                    else:
                        break
                    
                    print("\n程序响应中")
                    sleep(3)
            elif c == 4:
                print('作者谢谢你')
            else:
                break
        
        print("\n程序响应中")
        sleep(3)
        clean()
    print("\n程序结束")
else:
    print("\n程序结束")
