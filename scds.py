'''诗词大赛主程序'''
import time
import tkinter
import ckcs


class SayPoet(object):
    '''出口成诗游戏'''
    def __init__(self):
        self.time_limit = 60
        self.say_poet_interface = None
        self.say_poet = ckcs.PoetGame()
        self.exiting = 0
        self.answering_state = [0] * self.say_poet.question_amount
        self.answer = None

    def run(self):
        '''出口成诗运行函数'''
        global mode_select_interface
        mode_select_interface.destroy()
        self.say_poet.get_question()
        self.say_poet.get_poet_library()
        start_time = time.time()
        while not self.exiting:
            end_time = time.time()
            if end_time - start_time > self.time_limit:
                break
            self.say_poet_display()
            if self.exiting == 1:
                break
            if self.say_poet.unanswered == [0] * self.say_poet.question_amount:
                break
        if self.exiting == 0:
            self.show_grade()

    def say_poet_display(self):
        '''出口成诗界面'''
        background_color = ['skyblue', 'green', 'grey']
        self.say_poet_interface = tkinter.Tk()
        self.say_poet_interface.title("出口成诗")
        self.say_poet_interface.geometry("400x400+500+150")
        question_button1 = tkinter.Button(self.say_poet_interface,
                                          text=self.say_poet.questions[0],
                                          bg=background_color[self.answering_state[0]],
                                          font=('楷体', 18),
                                          activeforeground='green',
                                          command=self.button1_response)
        question_button1.place(relwidth=0.3, relheight=0.1, relx=0, rely=0.02)
        question_button2 = tkinter.Button(self.say_poet_interface,
                                          text=self.say_poet.questions[1],
                                          bg=background_color[self.answering_state[1]],
                                          font=('楷体', 18),
                                          activeforeground='green',
                                          command=self.button2_response)
        question_button2.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.02)
        question_button3 = tkinter.Button(self.say_poet_interface,
                                          text=self.say_poet.questions[2],
                                          bg=background_color[self.answering_state[2]],
                                          font=('楷体', 18),
                                          activeforeground='green',
                                          command=self.button3_response)
        question_button3.place(relwidth=0.3, relheight=0.1, relx=0.7, rely=0.02)
        question_button4 = tkinter.Button(self.say_poet_interface,
                                          text=self.say_poet.questions[3],
                                          bg=background_color[self.answering_state[3]],
                                          font=('楷体', 18),
                                          activeforeground='green',
                                          command=self.button4_response)
        question_button4.place(relwidth=0.3, relheight=0.1, relx=0, rely=0.14)
        question_button5 = tkinter.Button(self.say_poet_interface,
                                          text=self.say_poet.questions[4],
                                          bg=background_color[self.answering_state[4]],
                                          font=('楷体', 18),
                                          activeforeground='green',
                                          command=self.button5_response)
        question_button5.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.14)
        question_button6 = tkinter.Button(self.say_poet_interface,
                                          text=self.say_poet.questions[5],
                                          bg=background_color[self.answering_state[5]],
                                          font=('楷体', 18),
                                          activeforeground='green',
                                          command=self.button6_response)
        question_button6.place(relwidth=0.3, relheight=0.1, relx=0.7, rely=0.14)
        question_button7 = tkinter.Button(self.say_poet_interface,
                                          text=self.say_poet.questions[6],
                                          bg=background_color[self.answering_state[6]],
                                          font=('楷体', 18),
                                          activeforeground='green',
                                          command=self.button7_response)
        question_button7.place(relwidth=0.3, relheight=0.1, relx=0, rely=0.26)
        question_button8 = tkinter.Button(self.say_poet_interface,
                                          text=self.say_poet.questions[7],
                                          bg=background_color[self.answering_state[7]],
                                          font=('楷体', 18),
                                          activeforeground='green',
                                          command=self.button8_response)
        question_button8.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.26)
        question_button9 = tkinter.Button(self.say_poet_interface,
                                          text=self.say_poet.questions[8],
                                          bg=background_color[self.answering_state[8]],
                                          font=('楷体', 18),
                                          activeforeground='green',
                                          command=self.button9_response)
        question_button9.place(relwidth=0.3, relheight=0.1, relx=0.7, rely=0.26)
        question_button10 = tkinter.Button(self.say_poet_interface,
                                           text=self.say_poet.questions[9],
                                           bg=background_color[self.answering_state[9]],
                                           font=('楷体', 18),
                                           activeforeground='green',
                                           command=self.button10_response)
        question_button10.place(relwidth=0.3, relheight=0.1, relx=0, rely=0.38)
        question_button11 = tkinter.Button(self.say_poet_interface,
                                           text=self.say_poet.questions[10],
                                           bg=background_color[self.answering_state[10]],
                                           font=('楷体', 18),
                                           activeforeground='green',
                                           command=self.button11_response)
        question_button11.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.38)
        question_button12 = tkinter.Button(self.say_poet_interface,
                                           text=self.say_poet.questions[11],
                                           bg=background_color[self.answering_state[11]],
                                           font=('楷体', 18),
                                           activeforeground='green',
                                           command=self.button12_response)
        question_button12.place(relwidth=0.3, relheight=0.1, relx=0.7, rely=0.38)
        label = tkinter.Label(self.say_poet_interface, text="请输入答案：", font=("宋体", 18))
        label.place(relwidth=0.37, relheight=0.1, relx=0, rely=0.5)
        self.answer = tkinter.Entry(self.say_poet_interface, font=("宋体", 14))
        self.answer.place(relwidth=0.8, relheight=0.1, relx=0, rely=0.6)
        submit_button = tkinter.Button(self.say_poet_interface,
                                       text='提交',
                                       font=('楷体', 18),
                                       activeforeground='green',
                                       command=self.submit_response)
        submit_button.place(relwidth=0.18, relheight=0.1, relx=0.81, rely=0.6)
        exit0 = tkinter.Button(self.say_poet_interface, text="退出游戏", font=('楷体', 18),
                               activeforeground='red', command=self.exit_say_poet)
        exit0.place(relwidth=0.3, relheight=0.1, relx=0.7, rely=0.9)
        back0 = tkinter.Button(self.say_poet_interface, text="返回首页", font=('楷体', 18),
                               activeforeground='red', command=self.back_mode_selection)
        back0.place(relwidth=0.3, relheight=0.1, relx=0, rely=0.9)
        self.say_poet_interface.protocol("WM_DELETE_WINDOW", self.exit_say_poet)
        self.say_poet_interface.mainloop()

    def show_grade(self):
        '''显示回答情况和最终得分'''
        right_amounts = 0
        conclusion = ''
        for i in range(self.say_poet.question_amount):
            if self.say_poet.answers[i] != '':
                right_amounts += 1
                conclusion += '{0:>2}、回答正确：{1}\n'.format(i + 1, self.say_poet.answers[i])
            else:
                conclusion += '{0:>2}、回答错误/未回答。\n'.format(i + 1)
        self.say_poet.grade = right_amounts / self.say_poet.question_amount * 100
        score = '您的总得分为：{0:.1f}分'.format(self.say_poet.grade)
        self.say_poet_interface = tkinter.Tk()
        self.say_poet_interface.title("回答情况总结")
        self.say_poet_interface.geometry("400x400+500+150")
        label = tkinter.Label(self.say_poet_interface, text=conclusion,
                              font=("宋体", 12), anchor='w', justify='left')
        label.place(relwidth=1, relheight=0.55, relx=0, rely=0.05)
        label2 = tkinter.Label(self.say_poet_interface, text=score, font=("宋体", 18), anchor='w')
        label2.place(relwidth=1, relheight=0.1, relx=0, rely=0.65)
        exit0 = tkinter.Button(self.say_poet_interface, text="退出游戏", font=('楷体', 18),
                               activeforeground='red', command=self.exit_say_poet)
        exit0.place(relwidth=0.3, relheight=0.1, relx=0.7, rely=0.85)
        back0 = tkinter.Button(self.say_poet_interface, text="返回首页", font=('楷体', 18),
                               activeforeground='red', command=self.back_mode_selection)
        back0.place(relwidth=0.3, relheight=0.1, relx=0, rely=0.85)
        self.say_poet_interface.protocol("WM_DELETE_WINDOW", self.exit_say_poet)
        self.say_poet_interface.mainloop()

    def submit_response(self):
        '''提交回答并处理'''
        number = 0
        for i in range(self.say_poet.question_amount):
            if self.answering_state[i] == 1:
                number = i
        answers = self.answer.get()
        answer_right = self.say_poet.verification(number, answers)
        if answer_right:
            self.answering_state[number] = 2
        self.say_poet_interface.destroy()

    def exit_say_poet(self):
        '''出口成诗界面的退出游戏函数'''
        global is_running
        is_running = False
        self.say_poet_interface.destroy()
        self.exiting = 1

    def back_mode_selection(self):
        '''出口成诗界面返回游戏模式选择界面的函数'''
        self.say_poet_interface.destroy()
        self.exiting = 1

    def clear_select_state(self):
        '''清除选中的状态'''
        for i in range(self.say_poet.question_amount):
            if self.answering_state[i] == 1:
                self.answering_state[i] = 0
        self.say_poet_interface.destroy()

    def button1_response(self):
        '''点击第一个单词的响应'''
        if self.answering_state[0] == 0:
            self.clear_select_state()
            self.answering_state[0] = 1

    def button2_response(self):
        '''点击第二个单词的响应'''
        if self.answering_state[1] == 0:
            self.clear_select_state()
            self.answering_state[1] = 1

    def button3_response(self):
        '''点击第三个单词的响应'''
        if self.answering_state[2] == 0:
            self.clear_select_state()
            self.answering_state[2] = 1

    def button4_response(self):
        '''点击第四个单词的响应'''
        if self.answering_state[3] == 0:
            self.clear_select_state()
            self.answering_state[3] = 1

    def button5_response(self):
        '''点击第五个单词的响应'''
        if self.answering_state[4] == 0:
            self.clear_select_state()
            self.answering_state[4] = 1

    def button6_response(self):
        '''点击第六个单词的响应'''
        if self.answering_state[5] == 0:
            self.clear_select_state()
            self.answering_state[5] = 1

    def button7_response(self):
        '''点击第七个单词的响应'''
        if self.answering_state[6] == 0:
            self.clear_select_state()
            self.answering_state[6] = 1

    def button8_response(self):
        '''点击第八个单词的响应'''
        if self.answering_state[7] == 0:
            self.clear_select_state()
            self.answering_state[7] = 1

    def button9_response(self):
        '''点击第九个单词的响应'''
        if self.answering_state[8] == 0:
            self.clear_select_state()
            self.answering_state[8] = 1

    def button10_response(self):
        '''点击第十个单词的响应'''
        if self.answering_state[9] == 0:
            self.clear_select_state()
            self.answering_state[9] = 1

    def button11_response(self):
        '''点击第十一个单词的响应'''
        if self.answering_state[10] == 0:
            self.clear_select_state()
            self.answering_state[10] = 1

    def button12_response(self):
        '''点击第十二个单词的响应'''
        if self.answering_state[11] == 0:
            self.clear_select_state()
            self.answering_state[11] = 1


class ClickPoet(object):
    def __init__(self):
        self.click_poet = None

    def run(self):
        '''点字成诗运行函数'''
        global mode_select_interface
        mode_select_interface.destroy()

    def click_poet_display(self):
        '''点字成诗界面'''


class ModeSelection(object):
    '''诗词大赛游戏'''
    def start(self):
        '''开始游戏'''
        global is_running
        while is_running:
            self.selection()

    def selection(self):
        '''模式选择界面'''
        saying_poet = SayPoet()
        clicking_poet = ClickPoet()
        global is_running, mode_select_interface
        if is_running:
            mode_select_interface = tkinter.Tk()
            mode_select_interface.title("游戏模式选择")
            mode_select_interface.geometry("400x400+500+150")
            mode1 = tkinter.Button(mode_select_interface, text="出口成诗", font=('楷体', 18),
                                   activeforeground='blue', command=saying_poet.run)
            mode1.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.2)
            mode2 = tkinter.Button(mode_select_interface, text="点字成诗", font=('楷体', 18),
                                   activeforeground='blue', command=clicking_poet.run)
            mode2.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.4)
            exit0 = tkinter.Button(mode_select_interface, text="退出游戏", font=('楷体', 18),
                                   activeforeground='red', command=self.exit_mode_select)
            exit0.place(relwidth=0.3, relheight=0.1, relx=0.35, rely=0.6)
            mode_select_interface.protocol("WM_DELETE_WINDOW", self.exit_mode_select)
            mode_select_interface.mainloop()

    def exit_mode_select(self):
        '''模式选择界面的退出游戏函数'''
        global mode_select_interface, is_running
        is_running = False
        mode_select_interface.destroy()


if __name__ == '__main__':
    mode_select_interface = None
    is_running = True
    game = ModeSelection()
    game.start()
    print('游戏结束')
