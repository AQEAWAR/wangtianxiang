import tkinter as tk


class APP():
    def __init__(self):
        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.title('公式计算器')
        self.window.geometry('500x350')
        self.label1 = tk.Label(text="当前公式", font=(msFont, fontSize))
        self.label1.place(x=0, y=0, width=300, height=50)
        self.fun_str = tk.StringVar()  # 公式变量
        self.label2 = tk.Label(textvariable=self.fun_str, bg="white", font=(msFont, fontSize))
        self.label2.place(x=0, y=50, width=500, height=50)
        self.button1 = tk.Button(text='切换公式', command=self.choose_fun, font=(msFont, fontSize))
        self.button1.place(x=300, y=0, width=200, height=50)
        self.click_count = 0  # 点击次数
        self.tv_init()
        self.frame_init()
        self.sens = tk.StringVar()
        self.insert_init()
        self.label3 = tk.Label(textvariable=self.sens, bg="#DCDCDC", font=(msFont, fontSize))
        self.label3.place(x=300, y=100, width=200, height=200)
        self.label4 = tk.Label(text='M输出', font=(msFont, fontSize))
        self.label4.place(x=0, y=300, width=150, height=50)
        self.value = tk.StringVar()
        self.label5 = tk.Label(textvariable=self.value, bg="white", font=(msFont, fontSize))
        self.label5.place(x=150, y=300, width=150, height=50)
        self.button2 = tk.Button(text='计算', command=self.show_result, font=(msFont, fontSize))
        self.button2.place(x=300, y=300, width=200, height=50)

    def tv_init(self):
        self.t1 = tk.StringVar()
        self.t2 = tk.StringVar()
        self.t3 = tk.StringVar()
        self.t4 = tk.StringVar()
        self.t5 = tk.StringVar()

    def frame_init(self):
        self.f1 = tk.Label(textvariable=self.t1, bg="#FFF8DC").place(x=0, y=100, width=150, height=40)
        self.f2 = tk.Label(textvariable=self.t2, bg="#FFF8DC").place(x=0, y=140, width=150, height=40)
        self.f3 = tk.Label(textvariable=self.t3, bg="#FFF8DC").place(x=0, y=180, width=150, height=40)
        self.f4 = tk.Label(textvariable=self.t4, bg="#FFF8DC").place(x=0, y=220, width=150, height=40)
        self.f5 = tk.Label(textvariable=self.t5, bg="#FFF8DC").place(x=0, y=260, width=150, height=40)

    def insert_init(self):
        self.e1 = tk.Entry(bg="#F5FFFA")
        self.e1.place(x=150, y=100, width=150, height=40)
        self.e2 = tk.Entry(bg="#F5FFFA")
        self.e2.place(x=150, y=140, width=150, height=40)
        self.e3 = tk.Entry(bg="#F5FFFA")
        self.e3.place(x=150, y=180, width=150, height=40)
        self.e4 = tk.Entry(bg="#F5FFFA")
        self.e4.place(x=150, y=220, width=150, height=40)
        self.e5 = tk.Entry(bg="#F5FFFA")
        self.e5.place(x=150, y=260, width=150, height=40)

    def choose_fun(self):
        self.fun_str.set(fun_all[self.click_count])
        self.show_words()
        self.set_values()
        self.click_count += 1
        if self.click_count > 3:
            self.click_count = 0

    def run(self):
        self.window.mainloop()

    def show_words(self):
        if self.click_count == 0:
            val = sens['W'] + '\n' + sens['Z'] + '\n' + sens['Q'] + '\n' + sens['S'] + '\n' + sens['V']
        elif self.click_count == 1:
            val = sens['W'] + '\n' + sens['Q'] + '\n' + sens['S'] + '\n' + sens['V']
        elif self.click_count == 2:
            val = sens['W'] + '\n' + sens['Q'] + '\n' + sens['m']
        else:
            val = sens['C'] + '\n' + sens['S']
        self.sens.set(val)

    def set_values(self):
        if self.click_count == 0:
            self.t1.set('W')
            self.t2.set('Z')
            self.t3.set('Q')
            self.t4.set('S')
            self.t5.set('V')
        elif self.click_count == 1:
            self.t1.set('W')
            self.t2.set('Q')
            self.t3.set('S')
            self.t4.set('V')
            self.t5.set('')
        elif self.click_count == 2:
            self.t1.set('W')
            self.t2.set('Q')
            self.t3.set('m')
            self.t4.set('')
            self.t5.set('')
        else:
            self.t1.set('C')
            self.t2.set('S')
            self.t3.set('')
            self.t4.set('')
            self.t5.set('')

    def get_input(self):
        data = []
        e = [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), self.e5.get()]
        for each in e:
            if each.strip() != '':
                data.append(float(each))
            else:
                data.append('')
        return data

    def cal(self):
        data = self.get_input()
        if self.click_count - 1 == 0:
            W, Z, Q, S, V = data[0], data[1], data[2], data[3], data[4]
            return (W - 6000 - Z - Q) * S - V
        elif self.click_count - 1 == 1:
            W, Q, S, V = data[0], data[1], data[2], data[3]
            return (W - Q) * S - V
        elif self.click_count - 1 == 2:
            W, Q, m = data[0], data[1], data[2]
            return W - Q - 5000 * m
        else:
            C, S = data[0], data[1]
            return C / (1 - S) * S

    def show_result(self):
        self.value.set(self.cal())


fun1 = "公式一：M=(W-6000-Z-Q)*S-V"
fun2 = "公式二：M=(W-Q)*S-V"
fun3 = "公式三：M=W-Q-5000*m"
fun4 = "公式四：M=C/(1-S)*S"
fun_all = [fun1, fun2, fun3, fun4]

sens = {'W': 'W：应纳税额', 'Z': 'Z：住房基金等', 'Q': 'Q：其它支出', 'S': 'S：税率',
        'm': 'm：经营月数', 'V': 'V：速算扣除数', 'C': 'C:成本支出额'}

msFont = '微软雅黑'  # 字体
fontSize = 12  # 字体大小
