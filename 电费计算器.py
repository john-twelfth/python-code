
import tkinter as tk

root = tk.Tk()
root.title('电费计算器')
root.geometry("510x370")

tk.Label(root, text='电器').grid(row=0, column=0)
tk.Label(root, text='功率(千瓦)').grid(row=0, column=1)
tk.Label(root, text='每天用时(小时)').grid(row=0, column=2)
tk.Label(root, text='每月天数').grid(row=0, column=3)
tk.Label(root, text='电费(元)').grid(row=0, column=4)

class Item:
    count = 0

    def __init__(self):
        Item.count += 1
        self.name = tk.StringVar()
        self.power = tk.DoubleVar(value="")
        self.hours = tk.DoubleVar(value="")
        self.days = tk.IntVar(value="")
        self.charge = tk.DoubleVar(value="")
        r = Item.count
        tk.Entry(root, textvariable=self.name, width=15).grid(row=r, column=0)
        tk.Entry(root, textvariable=self.power, width=10).grid(row=r, column=1)
        tk.Entry(root, textvariable=self.hours, width=10).grid(row=r, column=2)
        tk.Entry(root, textvariable=self.days, width=10).grid(row=r, column=3)
        tk.Entry(root, textvariable=self.charge, width=20, state=tk.DISABLED).grid(row=r, column=4)

    def cal_charge(self):
        c = self.power.get() * self.hours.get() * self.days.get() * price.get()
        self.charge.set(c)
        return c

items = []
for i in range(10):
    items.append(Item())

tk.Label(root, text='', width=5).grid(row=11, column=0)

tk.Label(root, text='电价(元/度)').grid(row=12, column=0)
price = tk.DoubleVar(value=1)
tk.Entry(root, textvariable=price, width=10).grid(row=12, column=1)

def cal():
    total = 0
    for i in items:
        n = i.name.get()
        if n:
            total += i.cal_charge()
    total = round(total, 2)
    charge.set(total)

tk.Button(root, text='计算', command=cal, width=10).grid(row=12, column=2)

tk.Label(root, text='共计电费(元)').grid(row=12, column=3)
charge = tk.DoubleVar()
tk.Entry(root, textvariable=charge, width=20, state=tk.DISABLED).grid(row=12, column=4)

root.mainloop()