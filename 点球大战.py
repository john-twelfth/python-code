import random
import os, sys
import time

# Windows Hack to print colorful text at original cmd or powershell terminal
if os.name == 'nt': os.system("")   # Correct way is using colorama module, this is dirty
# Windows Terminal / Linux 没这个问题，不需要这行

ai_image = """\
        (\(\    
        (-.-)   
        o_(")(")
"""

class Anim(object):
    def __init__(self) -> None:
        self.goal = """\
        ┌─────────────────────┐
        │                     │ │
        │                     │  │
        │                     │   │
"""
        self.standpos = "\x1b[4;10H"
        self.keeper = "      ฅ(๑*д*๑)ฅ      "
        self.leftsave = "ﾍ(;´Д｀ﾍ)            "
        self.rightsave = "           Σ(°Д °;)っ"
        self.centersave = "      °(°ˊДˋ°) °     "
        self.lauthface = "      (๑•́ ₃•̀๑)      "
    
    def clear(self) -> None:
        sys.stdout.write('\x1bc')
        sys.stdout.flush()

    def print_goal(self) -> None:
        self.clear()
        sys.stdout.write(self.goal)
        sys.stdout.write(f"{self.standpos}{self.keeper}")
        sys.stdout.flush()
    
    def saveleft(self) -> None:
        sys.stdout.write(f"{self.standpos}{self.leftsave}")
        sys.stdout.flush()
    
    def saveright(self) -> None:
        sys.stdout.write(f"{self.standpos}{self.rightsave}")
        sys.stdout.flush()
    
    def savecenter(self) -> None:
        sys.stdout.write(f"{self.standpos}{self.centersave}")
        sys.stdout.flush()
    
    def laugh(self) -> None:
        sys.stdout.write(f"{self.standpos}{self.lauthface}")
        sys.stdout.flush()
    
    def printball(self, loc='c'):
        match loc:
            case 'c': sys.stdout.write(f"\x1b[3;20H⚽️")
            case 'l': sys.stdout.write(f"\x1b[3;10H⚽️")
            case 'r': sys.stdout.write(f"\x1b[3;28H⚽️")
            case _: pass
        sys.stdout.flush()
    
    def movetoend(self) -> None:
        sys.stdout.write("\x1b[6;0H")

    def showanim(self, protect: int, attack: int, isfail: bool) -> None:
        if isfail:
            self.print_goal()
            time.sleep(1)
            match protect:
                case 1: self.saveleft()
                case 2: self.savecenter()
                case 3: self.saveright()
            time.sleep(1)
            self.laugh()
            time.sleep(1)
            self.movetoend()
        else:
            self.print_goal()
            time.sleep(1)
            match attack:
                case 1: self.printball('l')
                case 2: self.printball('c')
                case 3: self.printball('r')
            time.sleep(1)
            match protect:
                case 1: self.saveleft()
                case 2: self.savecenter()
                case 3: self.saveright()
            if not attack == protect:
                match attack:
                    case 1: self.printball('l')
                    case 2: self.printball('c')
                    case 3: self.printball('r')
            time.sleep(1)
            self.movetoend()

        

def bunnysay(text: str) -> None:
    if len(text) == 0: return
    lchar = '─'*len(text.encode('gb2312'))
    sys.stdout.write(f"""\x1b[9{random.randint(1,6)}m\
        (\(\     ┌{lchar}┐
        (-.-)   < {text}│
        o_(")(") └{lchar}┘\x1b[0m
    """)

class GAME(object):
    def __init__(self) -> None:
        self.direction = [1, 2, 3]
        self.round = 4
        self.playerwin = False
        self.computerwin = False
        self.playerpoint = 0
        self.computerpoint = 0
        self.failstatus = {
            0: "球员大力抽射踢中门框力（悲",
            1: "球员员用力过猛滑倒力（悲",
            2: "球员大力出奇迹把球踢爆力（恼",
            3: "球员踢得时候脱出来力，为了掩盖过去发出了很响的声音（悲",
        }
        self.failp = 10    # 踢不进去的可能性 10 / 100
        self.anim = Anim()

    def cls(self) -> None:
        sys.stdout.write("\x1bc")  # 清空终端
        sys.stdout.flush()         # 清空终端缓存

    def showstatus(self) -> None:
        sys.stdout.write(f"\x1b[96m当前得分\x1b[0m\n\t\t玩家：{self.playerpoint}\n\t\t电脑：{self.computerpoint}\n\t\t剩余回合数：{self.round}\n")

    def judge(self, pdirct, cdirct, mode) -> None:
        if mode == 0:
            prot = cdirct
            att = pdirct
        else:
            prot = pdirct
            att = cdirct
        if random.randint(0, 99) < self.failp:
            self.cls()
            self.anim.showanim(prot, att, True)
            bunnysay(self.failstatus[random.randint(0, len(self.failstatus)-1)])
            time.sleep(1)
        elif pdirct == cdirct:
            val = "电脑防守住了你的进攻 ！" if mode == 0 else "你防守住了电脑的进攻 ！"
            self.cls()
            self.anim.showanim(prot, att, False)
            bunnysay(val)
            time.sleep(0.5)
        else:
            emotion = "喜" if mode == 0 else "悲"
            self.cls()
            self.anim.showanim(prot, att, False)
            if mode == 0:
                self.playerpoint += 1
            else:
                self.computerpoint += 1
            bunnysay(f"球进力（{emotion}")
            time.sleep(0.5)

    def showfinall(self) -> None:
        self.cls()
        if self.playerwin:
            bunnysay("恭喜你赢得了比赛！")
        else:
            bunnysay("你输力（悲")
        sys.stdout.write(f"\t\t你的比分为   {self.playerpoint} : {self.computerpoint}\n")

    def faq(self):
        while not (self.playerwin or self.computerwin):
            self.cls()
            self.showstatus()
            bunnysay("输入你要进攻的方向  [1]左  [2]中  [3]右")
            cdirct = random.randint(1, 3)   # 设置电脑方向
            try:
                pdirct = int(input("输入结束后按Enter , 输入[0]终止游戏： "))
            except:
                self.cls()
                bunnysay("输入不合法，请重新输入")
                time.sleep(0.5)
                continue
            if pdirct == 0:
                break
            elif not pdirct in self.direction:
                self.cls()
                bunnysay("你干嘛~哈哈~哎呦~")
                time.sleep(0.5)
                continue
            
            # 判断进球环节
            self.judge(pdirct, cdirct, 0)
            
            # 防守环节
            self.cls()
            self.showstatus()
            bunnysay("输入你要防守的方向  [1]左  [2]中  [3]右")
            cdirct = random.randint(1, 3)   # 设置电脑方向
            try:
                pdirct = int(input("输入结束后按Enter , 输入[0]终止游戏： "))
            except:
                self.cls()
                bunnysay("输入不合法，请重新输入")
                time.sleep(0.5)
                continue
            if pdirct == 0:
                break
            elif not pdirct in self.direction:
                self.cls()
                bunnysay("你干嘛~哈哈~哎呦~")
                time.sleep(0.5)
                continue
            
            # 判断进球环节
            self.judge(pdirct, cdirct, 1)

            # 判断胜负环节
            if abs(self.playerpoint-self.computerpoint) > self.round:
                if self.playerpoint > self.computerpoint:
                    self.playerwin = True
                else:
                    self.computerwin = True
            
            # 减少回合数
            if not self.round == 0: 
                self.round -= 1
            else:
                self.cls()
                bunnysay("加时赛 ！！！")
                continue
        # 结尾展示
        self.showfinall()

if __name__ == '__main__':
    game = GAME()
    game.cls()
    says = [
        f"你好啊，{os.getenv('USERNAME')}",
        f"欢迎游玩下北泽精神病院网瘾治疗游戏",
        f"我是沼气天使李田所，今天由我来陪你游玩罢（喜",
    ]
    for i in says:
        bunnysay(i)
        sys.stdout.write('\n')
        time.sleep(0.5)
    time.sleep(2)
    game.faq()
