
class CuteCat:
    def __init__(self,cat_name,cat_age,cat_ikun):
        self.name = cat_name
        self.age = cat_age
        self.ikun = cat_ikun
       
    def ikuning(self,doing):
        if self.ikun == True:
            print(f"hello Ikun {cat1.name}")
            print(f"{cat1.name} is dancing the {doing}")


cat1 = CuteCat("chicken",112,True)#喵喵参数

print(f"name:{cat1.name}  age:{cat1.age}")
cat1.ikuning("ikun")
