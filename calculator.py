import math
import tkinter as tk

global variable
variable = ""


class Cal:
    def __init__(self, calculator):
        self.calculator = calculator
        self.calculator.title('简易计算器')  # 定义计算器名字
        self.calculator.resizable(width=True, height=True)  # 设置窗口可拉伸
        self.calculator = tk.Frame(root)
        self.calculator.pack()  # 设置计算器界面可以随着窗口的放缩而放缩，并且置于界面中间

        self.text_input = tk.StringVar()
        self.equation = tk.StringVar()  # 定义输入文本框和显示结果文本框
        self.text_input.set("0")
        self.equation.set(" ")  # 设置文本框初始显示的内容

        self.Input_box = tk.Entry(self.calculator, fg="black", bg='powderblue', bd=10, textvariable=self.text_input,
                                  insertwidth=2, justify='right').grid(columnspan=7)
        self.show_result_eq = tk.Entry(self.calculator, fg="black", bg='powderblue', bd=10, textvariable=self.equation,
                                       insertwidth=2, justify='right').grid(columnspan=7)

        # 第二行
        self.Buttonsin = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='sin',
                                   command=lambda: self.Click('sin')).grid(row=2, column=1)  # 计算sin
        self.Clear = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='AC',
                               command=lambda: self.ClearDisplay()).grid(row=2, column=2)  # 清空键
        self.backspace = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='←',
                                   command=lambda: self.BackSpace()).grid(row=2, column=3)  # 退格键
        self.Devision = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='/',
                                  command=lambda: self.Click("/")).grid(row=2, column=4)  # 除号键
        self.factorial = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='n!',
                                   command=lambda: self.Factorial()).grid(row=2, column=5)  # 阶乘键
        self.Buttonpi = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='π',
                                  command=lambda: self.Click('π')).grid(row=2, column=6)  # π键

        # 第三行
        self.Buttoncos = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='cos',
                                   command=lambda: self.Click('cos')).grid(row=3, column=1)  # 计算cos
        self.Button7 = tk.Button(self.calculator, bg='orange', fg="black", width=15, height=3, text='7',
                                 command=lambda: self.Click(7)).grid(row=3, column=2)  # 数字7
        self.Button8 = tk.Button(self.calculator, bg='orange', fg="black", width=15, height=3, text='8',
                                 command=lambda: self.Click(8)).grid(row=3, column=3)  # 数字8
        self.Button9 = tk.Button(self.calculator, bg='orange', fg="black", width=15, height=3, text='9',
                                 command=lambda: self.Click(9)).grid(row=3, column=4)  # 数字9
        self.Multiply = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='*',
                                  command=lambda: self.Click("*")).grid(row=3, column=5)  # 乘法键
        self.Delivery = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='%',
                                  command=lambda: self.Click("%")).grid(row=3, column=6)  # 取余键

        # 第四行
        self.Buttontan = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='tan',
                                   command=lambda: self.Click('tan')).grid(row=4, column=1)  # 计算tan
        self.Button4 = tk.Button(self.calculator, bg='orange', fg="black", width=15, height=3, text='4',
                                 command=lambda: self.Click(4)).grid(row=4, column=2)  # 数字4
        self.Button5 = tk.Button(self.calculator, bg='orange', fg="black", width=15, height=3, text='5',
                                 command=lambda: self.Click(5)).grid(row=4, column=3)  # 数字5
        self.Button6 = tk.Button(self.calculator, bg='orange', fg="black", width=15, height=3, text='6',
                                 command=lambda: self.Click(6)).grid(row=4, column=4)  # 数字6
        self.Subtraction = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='-',
                                     command=lambda: self.Click("-")).grid(row=4, column=5)  # 减号键
        self.Left_bracket = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='(',
                                      command=lambda: self.Click('(')).grid(row=4, column=6)  # (

        # 第五行
        self.comma = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text=',',
                               command=lambda: self.Click(',')).grid(row=5, column=1)  # 逗号
        self.Button1 = tk.Button(self.calculator, bg='orange', fg="black", width=15, height=3, text='1',
                                 command=lambda: self.Click(1)).grid(row=5, column=2)  # 数字1
        self.Button2 = tk.Button(self.calculator, bg='orange', fg="black", width=15, height=3, text='2',
                                 command=lambda: self.Click(2)).grid(row=5, column=3)  # 数字2
        self.Button3 = tk.Button(self.calculator, bg='orange', fg="black", width=15, height=3, text='3',
                                 command=lambda: self.Click(3)).grid(row=5, column=4)  # 数字3
        self.Addition = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='+',
                                  command=lambda: self.Click("+")).grid(row=5, column=5)  # 加号键
        self.Right_bracket = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text=')',
                                       command=lambda: self.Click(')')).grid(row=5, column=6)  # 数字7

        # 第六行
        self.log = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='log',
                             command=lambda: self.Click('log')).grid(row=6, column=1)  # 对数
        self.Button0 = tk.Button(self.calculator, bg='orange', fg="black", height=3, width=48, text='0',
                                 command=lambda: self.Click(0)).grid(row=6, columnspan=6)  # 数字0
        self.decimal_point = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='.',
                                       command=lambda: self.Click(".")).grid(row=6, column=5)  # 小数点
        self.Equals = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='=',
                                command=lambda: self.Run()).grid(row=6, column=6)  # 等号
        # 第七行

        self.Button_pow = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='pow',
                                    command=lambda: self.Click('pow')).grid(row=7, column=5)  # 计算乘方
        self.Button_up_ceil = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3,
                                        text='up_ceil',
                                        command=lambda: self.Click('up_ceil')).grid(row=7, column=4)  # 向上取整
        self.Button_down_floor = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3,
                                           text='down_floor', command=lambda: self.Click('down_floor')).grid(row=7,
                                                                                                             column=3)  # 向下取整
        self.Button_round = tk.Button(self.calculator, bg='powderblue', fg="black", width=15, height=3, text='round',
                                      command=lambda: self.Click('round')).grid(row=7, column=2)  # 四舍五入取整

    def Click(self, numbers):
        # 将按钮上显示的内容转变成字符串显示在输入文本框上
        global variable
        variable = variable + str(numbers)
        self.text_input.set(variable)

    def Run(self):
        global variable
        elements = self.text_input.get()
        if elements[0] == 'u':
            elements = elements.replace('up_ceil(', '')
            elements = elements.replace(')', '')  # 此时文本框元素没有了'up_ceil()'
            variable = '%.4f' % math.ceil(eval(elements))
            self.equation.set(str(variable))
        elif elements[0] == 'd':
            elements = elements.replace('down_floor(', '')
            elements = elements.replace(')', '')  # 此时文本框元素没有了'down_floor()'
            variable = '%.4f' % math.floor(eval(elements))
            self.equation.set(str(variable))
        elif elements[0] == 'r':
            elements = elements.replace('round(', '')
            elements = elements.replace(')', '')  # 此时文本框元素没有了'round()'
            variable = '%.4f' % round(eval(elements))
            self.equation.set(str(variable))
        elif elements[0] == 'p':
            try:
                elements = elements.replace('pow(', '')
                elements = elements.replace(')', '')  # 此时文本框元素没有了'pow()'
                arg = elements.split(',')
                variable = '%.4f' % pow(eval(arg[0]), eval(arg[1]))
                self.equation.set(str(variable))
            except TypeError:
                self.equation.set('Error!')
        elif elements[0] == 'l':
            try:
                elements = elements.replace('log(', '')
                elements = elements.replace(')', '')  # 此时文本框元素没有了'log()'
                arr = elements.split(',')
                variable = str('%.4f' % math.log(eval(arr[0]), eval(arr[1])))
                self.equation.set(variable)
            except ValueError:
                self.equation.set('Error!')
        elif elements[0] == 's':
            elements = elements.replace('sin(', '')
            elements = elements.replace(')', '')  # 此时文本框元素没有了'sin()'
            if 'π' in elements:
                rep = math.pi
                elements = elements.replace('π', str(rep))
                variable = '%.4f' % math.sin(eval(elements))
                self.equation.set(str(variable))
            else:
                variable = '%.4f' % math.sin(eval(elements) * math.pi / 180.0)
                self.equation.set(str(variable))
        elif elements[0] == 'c':
            elements = elements.replace('cos(', '')
            elements = elements.replace(')', '')  # 此时文本框元素没有了'cos()'
            if 'π' in elements:
                rep = math.pi
                elements = elements.replace('π', str(rep))
                variable = '%.4f' % math.cos(eval(elements))
                self.equation.set(str(variable))
            else:
                variable = '%.4f' % math.cos(eval(elements) * math.pi / 180.0)
                self.equation.set(str(variable))
        elif elements[0] == 't':
            elements = elements.replace('tan(', '')
            elements = elements.replace(')', '')  # 此时文本框元素没有了'tan()'
            if 'π' in elements:
                rep = math.pi
                elements = elements.replace('π', str(rep))
                variable = '%.4f' % math.tan(eval(elements))
                self.equation.set(str(variable))
            else:
                variable = '%.4f' % math.tan(eval(elements) * math.pi / 180.0)
                self.equation.set(str(variable))
        else:
            try:
                # self.equation.set(elements)
                answer = '%.4f' % eval(elements)  # 保留四位小数
                self.equation.set(str(answer))
            except (ZeroDivisionError, SyntaxError, ValueError):
                self.equation.set(str('Error!'))

    def ClearDisplay(self):
        global variable
        variable = ""
        self.text_input.set("0")
        self.equation.set("0")

    def BackSpace(self):
        global variable
        len_variable = len(str(variable))
        variable = str(variable)[:len_variable - 1]
        self.text_input.set(variable)

    def Factorial(self):
        global variable
        self.text_input.set('{}!'.format(variable))
        variable = str(math.factorial(eval(variable)))
        self.equation.set(variable)


# 程序的入口
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('800x600')  # 定义窗口初始大小
    my_cal = Cal(root)  # 实例化
    root.mainloop()  # 进入消息循环
